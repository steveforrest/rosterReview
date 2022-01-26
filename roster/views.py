from django.shortcuts import render
from django.views import generic, View
from .models import RosterList


# Create your views here.
class ListRosters(generic.ListView):
    model = RosterList
    queryset = RosterList.objects.filter(status=1).order_by('-createdOn')
    template_name = 'index.html'
    paginate_by = 10
    context_object_name = 'rosters'
    

# class rosterDetails(view):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
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

# def Home(request):
#     return render(request, 'index.html')