from django.shortcuts import render
from django.http import HttpResponse
from .serializers import    UserSerializer, GroupSerializer
# Create your views here.

from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User



def index(request):
    print(request.POST)
    return HttpResponse("a")


def ids(request, id):
    return HttpResponse(f"a      {id}")

def cated(request):
    return HttpResponse(f"haslkasdf <br>  lkjsdflk ")



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

