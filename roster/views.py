from django.shortcuts import render
from django.views import generic
from .models import RosterList

# Create your views here.
class ListRosters(generic.ListView):
    model = RosterList
    queryset = RosterList.objects.filter(status=1).order_by('-createdOn')
    template_name = 'index.html'
    paginate_by = 10
    

# def Home(request):
#     return render(request, 'index.html')