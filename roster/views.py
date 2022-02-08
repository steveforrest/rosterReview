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

    # def get(self, request, *args, **kwargs):
    #     queryset = RosterList.objects.filter(status=1)
    #     post = get_object_or_404(queryset, pk=id)
    #     comments = post.comments.filter(approved=True).order_by("-created_on")


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

    return render(request, 'postRoster.html', {'form': form, 'comment_form': CommentForm()})


def roster_detail(request, id):
    """
    View to render the roster details
    """
    post = RosterList.objects.get(pk=id)
    user = User.objects.get(username=request.user.username)

    form = CommentForm()
    
    if request.method == 'POST':
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

        return redirect(reverse('roster-detail', args=[id]))
    else:
        # Getting the comments stored on the database related to the id of the post above
        # filter the comments by the post filed on the Comment model
        comments = Comment.objects.filter(post=post)
        form = CommentForm()
   
   
    context = {
        'LikesForm': form,
        'comment_form': form,
        'factions': FACTIONS,
        'post': post,
        'comments': comments
    }
# use the post variable which gets the object needed to be acounted by its id and create a variable set it to count and call the method created to count the likes in the model
    number_of_likes = post.number_of_likes()
    number_of_dislikes = post.number_of_dislikes()
    number_of_comments = post.number_of_comments()

    context['number_of_likes'] = number_of_likes
    context['number_of_dislikes'] = number_of_dislikes
    context['number_of_comments'] = number_of_comments

    # return redirect(reverse('home'))
    return render(request, 'RosterDetail.html', context)


class PostLike(View):
    '''
    view for the likes on a list
    '''
    def Post(self, request, pk):
        post = get_object_or_404(Post, pk=id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request,user)
        else:
            post.likes.add(request,user)
        return HttpResponseRedirect(reverse('roster-detail', args=[id]))


class PostDislike(View):
    '''
    view for the likes on a list
    '''
    def PostDislike(self, request, pk):
        post = get_object_or_404(Post, pk=id)

        if post.dislike.filter(id=request.user.id).exists():
            post.dislike.remove(request,user)
        else:
            post.dislike.add(request,user)
        return HttpResponseRedirect(reverse('roster-detail', args=[id]))
 
