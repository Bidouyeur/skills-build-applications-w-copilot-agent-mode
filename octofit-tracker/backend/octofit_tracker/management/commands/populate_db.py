from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Suppression des anciennes données
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Création des utilisateurs
        users = [
            User(email='thundergod@mhigh.edu', name='thundergod', team='Blue Team', is_coach=True),
            User(email='metalgeek@mhigh.edu', name='metalgeek', team='Blue Team', is_coach=False),
            User(email='zerocool@mhigh.edu', name='zerocool', team='Gold Team', is_coach=False),
            User(email='crashoverride@hmhigh.edu', name='crashoverride', team='Gold Team', is_coach=False),
            User(email='sleeptoken@mhigh.edu', name='sleeptoken', team='Gold Team', is_coach=False),
        ]
        User.objects.bulk_create(users)

        # Création des équipes
        blue_team = Team(name='Blue Team', members=[u.email for u in users if u.team == 'Blue Team'])
        blue_team.save()
        gold_team = Team(name='Gold Team', members=[u.email for u in users if u.team == 'Gold Team'])
        gold_team.save()

        # Création des activités
        from datetime import date
        activities = [
            Activity(user=users[0].email, activity_type='Cycling', steps=12000, date=date(2025, 5, 1), duration_minutes=60),
            Activity(user=users[1].email, activity_type='Crossfit', steps=9000, date=date(2025, 5, 2), duration_minutes=120),
            Activity(user=users[2].email, activity_type='Running', steps=15000, date=date(2025, 5, 3), duration_minutes=90),
            Activity(user=users[3].email, activity_type='Strength', steps=4000, date=date(2025, 5, 4), duration_minutes=30),
            Activity(user=users[4].email, activity_type='Swimming', steps=8000, date=date(2025, 5, 5), duration_minutes=75),
        ]
        Activity.objects.bulk_create(activities)

        # Création du leaderboard
        leaderboard_entries = [
            Leaderboard(team='Blue Team', total_steps=21000, week='2025-W18'),
            Leaderboard(team='Gold Team', total_steps=27000, week='2025-W18'),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Création des workouts
        workouts = [
            Workout(user=users[0].email, workout_type='Cycling', duration_minutes=60, calories_burned=500, date=date(2025, 5, 1)),
            Workout(user=users[1].email, workout_type='Crossfit', duration_minutes=120, calories_burned=900, date=date(2025, 5, 2)),
            Workout(user=users[2].email, workout_type='Running', duration_minutes=90, calories_burned=800, date=date(2025, 5, 3)),
            Workout(user=users[3].email, workout_type='Strength', duration_minutes=30, calories_burned=300, date=date(2025, 5, 4)),
            Workout(user=users[4].email, workout_type='Swimming', duration_minutes=75, calories_burned=600, date=date(2025, 5, 5)),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('La base de données octofit_db a été peuplée avec succès avec des données de test.'))
