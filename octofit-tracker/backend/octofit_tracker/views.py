from rest_framework import viewsets
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = getattr(settings, 'API_BASE_URL', 'http://localhost:8000/api/')
    return Response({
        'users': base_url + 'users/?format=api',
        'teams': base_url + 'teams/?format=api',
        'activities': base_url + 'activities/?format=api',
        'leaderboard': base_url + 'leaderboard/?format=api',
        'workouts': base_url + 'workouts/?format=api'
    })
