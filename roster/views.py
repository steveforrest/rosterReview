from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import RosterList, Comment
from .forms import RosterForm, CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .models import FACTIONS
from django.contrib import messages


# Create your views here.
class ListRosters(generic.ListView):
    """
    View to post roster the index page
    """
    model = RosterList
    queryset = RosterList.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 10
    context_object_name = 'rosters'
    extra_context = {'factions': FACTIONS}


@csrf_protect
@login_required
def post_roster(request):

    """
    View to allow user to post a new roster

    """

    # create an empty form  to post into the table
    form = RosterForm()

    if request.method == 'POST':
        # handle the post and save the form data
        form = RosterForm(request.POST)
        # if the form is valid
        if form.is_valid():

            new_form = form.save(commit=False)
            # check if user is authenticated if so use their
            # username if not use guest as created_by
            if request.user.is_authenticated:
                new_form.created_by = request.user
            else:
                new_form.created_by = "guest"

            new_form.status = 1
            new_form.save()

        return redirect(reverse('home'))

    else:
        form = RosterForm()

    return render(request, 'postRoster.html', {
        'roster_form': form, 'comment_form': CommentForm()
        })

@login_required
def update_roster(request, updated_id):
    # update = RosterList.objects.get(id=updated_id)
    roster = get_object_or_404(RosterList, id=updated_id)
    logged_in_user = request.user.id
    author = roster.created_by.id
    if logged_in_user is not author:
        messages.WARNING(request, f'You do not have permission to update this roster')
    if request.method == 'POST':
        form = RosterForm(request.POST, instance=roster)
        if form.is_valid():
            form.save()
            return redirect(reverse('roster-detail', args=[roster.id]))
    form = RosterForm(instance=roster)
    context = {
        'roster': roster, 'form': form,
    }
    return render(request, 'update_roster.html', context)

   
@login_required
def delete_roster(request, updated_id):
    roster = get_object_or_404(RosterList, id=updated_id)
    roster.delete()
    return redirect(reverse('home'))


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
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            disliked = False
        elif post.dislikes.filter(id=self.request.user.id).exists():
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
                "comment_form": CommentForm(),
            },
        )


    @method_decorator(login_required)
    def post(self, request, id, *args, **kwargs):
        """
        function to allow view to post to db
        """
        post = RosterList.objects.get(pk=id)
        user = User.objects.get(username=request.user.username)
        comments = Comment.objects.filter(post=post)
        # handle the post and save the form data
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.commenter = user
            new_form.save()
            # add the user to the Comments field of the RosterList
            post.list_comments.add(user)
            # save the RosterList
            post.save()
        context = {
            'LikesForm': form,
            'DisikesForm': form,
            'comment_form': form,
            'factions': FACTIONS,
            'post': post,
            'comments': comments,
        }
        # use the post variable which gets the object needed to
        # be acounted by it's id and create a variable set it to
        # count and call the method created to count the likes in the model
        number_of_likes = post.number_of_likes()
        number_of_dislikes = post.number_of_dislikes()
        number_of_comments = post.number_of_comments()

        context['number_of_likes'] = number_of_likes
        context['number_of_dislikes'] = number_of_dislikes
        context['number_of_comments'] = number_of_comments
        context['roster_form'] = RosterForm()

        return HttpResponseRedirect(reverse('roster-detail', args=[id]))


class PostLike(View):
    '''
    view for the likes on a list
    '''
    def post(self, request, id, *args, **kwargs):
        post = get_object_or_404(RosterList, pk=id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            post.dislikes.remove(request.user)
        return HttpResponseRedirect(reverse('roster-detail', args=[id]))


class PostDislike(View):
    '''
    view for the dislikes on a list
    '''
    def post(self, request, id, *args, **kwargs):
        post = get_object_or_404(RosterList, pk=id)

        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
            post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('roster-detail', args=[id]))
