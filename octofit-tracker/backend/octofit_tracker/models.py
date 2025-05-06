from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100, blank=True, null=True)
    is_coach = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    steps = models.IntegerField()
    date = models.DateField()
    duration_minutes = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.activity_type} - {self.date}"

class Workout(models.Model):
    user = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.workout_type} - {self.date}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    total_steps = models.IntegerField()
    week = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.team} - {self.week}"
