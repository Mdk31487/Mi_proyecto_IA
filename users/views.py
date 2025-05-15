# users/views.py
from rest_framework import viewsets
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'profile': request.user.profile})
