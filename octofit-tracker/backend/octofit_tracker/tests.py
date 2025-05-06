from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="test@example.com", activity_type="run", steps=1000, date="2023-01-01", duration_minutes=30)
        self.assertEqual(activity.steps, 1000)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user="test@example.com", workout_type="cardio", duration_minutes=45, calories_burned=300, date="2023-01-01")
        self.assertEqual(workout.calories_burned, 300)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team="Team A", total_steps=5000, week="2023-W01")
        self.assertEqual(leaderboard.total_steps, 5000)
