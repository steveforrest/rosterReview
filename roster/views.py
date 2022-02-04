from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import RosterList
from .forms import RosterForm, Comment
from django.views.decorators.csrf import csrf_protect

from .models import FACTIONS

# Create your views here.
class ListRosters(generic.ListView):
    model = RosterList
    queryset = RosterList.objects.filter(status=1).order_by('-createdOn')
    template_name = 'index.html'
    paginate_by = 10
    context_object_name = 'rosters'
    extra_context = {'factions': FACTIONS }

@csrf_protect
def post_roster(request):

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

    return render(
        request,
         'postRoster.html',
          {
              'form': form,
              'comment_form': Comment()
            }
    )


def roster_detail(request, id):
    post = RosterList.objects.get(pk=id)
    return render(request, 'RosterDetail.html', { 'post': post, 'factions': FACTIONS })



# class PostRoster(View):
#     context_object_name = 'postRosters'
#     def get(self, request, id, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, id=id)
#         comments = post.comments.filter(approved=True).order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )


# class RosterDetail(View):
#     context_object_name = 'postRosters'
#     def get(self, request, id, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, id=id)
#         comments = post.comments.filter(approved=True).order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )



