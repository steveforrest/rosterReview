from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import RosterList, Comment
from .forms import RosterForm, CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import FACTIONS

# Create your views here.
class ListRosters(generic.ListView):
    """
    View to post roster the index page
    """
    model = RosterList
    queryset = RosterList.objects.filter(status=1).order_by('-createdOn')
    template_name = 'index.html'
    paginate_by = 10
    context_object_name = 'rosters'
    extra_context = {'factions': FACTIONS }




@csrf_protect
def post_roster(request):

    """
    View to allow user to post a new roster 

    """

    # create an empty form  to post into the table
    form = RosterForm()
    
    if request.method == 'POST':
        # handle the post and save the form data
        form = RosterForm(request.POST)
        #if the form is valid
        if form.is_valid():

            new_form = form.save(commit=False)
            #check if user is authenticated if so use their username if not use guest as createdBy 
            if request.user.is_authenticated:
                new_form.createdBy = request.user
            else:
                new_form.createdBy = "guest"
            
            new_form.status = 1
            new_form.save()
        

        return redirect(reverse('home'))
        
    else:
        form = RosterForm()

    return render(request, 'postRoster.html', {'roster_form': form, 'comment_form': CommentForm()})


class RosterDetail(View):
    """
    view to render the roster details page
    """
    def get(self, request, id, *args, **kwargs):
        """
        used to get data from the db
        """
        queryset = RosterList.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=id)
        comments = Comment.objects.filter(post=post)
        liked = False
        disliked = False
        if post.Likes.filter(id=self.request.user.id).exists():
            liked = True
            disliked = False
        elif post.Dislikes.filter(id=self.request.user.id).exists():
            liked = False
            disliked = True
            
        
        return render(
            request,
            "RosterDetail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                'factions': FACTIONS,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, id, *args, **kwargs):
        """
        function to allow view to post to db
        """
        post = RosterList.objects.get(pk=id)
        roster = RosterList.objects.filter(post=post)
        user = User.objects.get(username=request.user.username)
        comments = Comment.objects.filter(post=post)
        # if post.Likes.filter(id=self.request.user.id).exists():
        #     liked = True
        #     disliked = False
        # elif post.Dislikes.filter(id=self.request.user.id).exists():
        #     liked = False
        #     disliked = True
        # handle the post and save the form data
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.user = user
            new_form.save()
            # add the user to the Comments field of the RosterList
            post.Comments.add(user)
            # save the RosterList
            post.save()
        context = {
            'LikesForm': form,
            'DisikesForm': form,
            'comment_form': form,
            'factions': FACTIONS,
            'post': post,
            'comments': comments,
            'roster': roster,
        }
        # use the post variable which gets the object needed to be acounted by its id and create a variable set it to count and call the method created to count the likes in the model
        number_of_likes = post.number_of_likes()
        number_of_dislikes = post.number_of_dislikes()
        number_of_comments = post.number_of_comments()

        context['number_of_likes'] = number_of_likes
        context['number_of_dislikes'] = number_of_dislikes
        context['number_of_comments'] = number_of_comments

        # return redirect(reverse('home'))
        return render(request, 'RosterDetail.html',{
            'roster_form': RosterForm(),
        },
        context)


    
class PostLike(View):
    '''
    view for the likes on a list
    '''
    def post(self, request, id, *args, **kwargs):
        post = get_object_or_404(RosterList, pk=id)

        if post.Likes.filter(id=request.user.id).exists():
            post.Likes.remove(request.user)
        else:
            post.Likes.add(request.user)
            post.Dislikes.remove(request.user)
        return HttpResponseRedirect(reverse('roster-detail', args=[id]))


class PostDislike(View):
    '''
    view for the likes on a list
    '''
    def post(self, request, id, *args, **kwargs):
        post = get_object_or_404(RosterList, pk=id)

        if post.Dislikes.filter(id=request.user.id).exists():
            post.Dislikes.remove(request.user)
        else:
            post.Dislikes.add(request.user)
            post.Likes.remove(request.user)
        return HttpResponseRedirect(reverse('roster-detail', args=[id]))
 
