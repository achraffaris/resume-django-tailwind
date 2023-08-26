from django.db import models

class Experience(models.Model):
    company_name = models.CharField(max_length=50)
    starting_year = models.CharField(max_length=50)
    ending_year = models.CharField(max_length=50)
    position = models.CharField(max_length=150)
    description = models.TextField()
    def __str__(self):
        return self.company_name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Resume(models.Model):
    about = models.TextField()
    experience = models.ManyToManyField(Experience)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return str(self.pk)