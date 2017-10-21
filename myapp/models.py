from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    student_id = models.IntegerField() 
    UNDERGRAD = 1
    MSC = 2
    PHD = 3
    LEVEL_CHOICES = (
        (UNDERGRAD, 'Undergrad'),
        (MSC, 'Masters'),
        (PHD, 'PhD')
    )
    level = models.IntegerField(default=UNDERGRAD, choices=LEVEL_CHOICES)
    def __str__(self):
        name=self.user.first_name+' '+self.user.last_name
        return "(%s)" % (name)


class Instructor(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    webpage=models.URLField()
    office=models.CharField(max_length=100,default='EH 120')
    def __str__(self):
        name=self.user.first_name+' '+self.user.last_name
        return "%s" % name


class Author(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=50)
    #age=models.IntegerField()
    birthdate=models.DateField()
    #city=models.CharField(max_length=50,default="windsor")
    country=models.CharField(max_length=50,default="Canada")
    def __str__(self):
        return "%s" % self.firstname
    
class Book(models.Model):
        title=models.CharField(max_length=100)
        author=models.ManyToManyField(Author)
        numpages=models.IntegerField(null=True)
        in_stock=models.BooleanField(default=True)
        pubyear=models.DateField(null=True)
        def __str__(self):
        #return self.title
            return "(%s, %s, %s)" % (self.title, str(self.author),str(self.numpages),)
        
        
class Course(models.Model):
    course_no=models.IntegerField(primary_key=True)
    title= models.CharField(max_length=100)
    textbook=models.ForeignKey(Book)
    instructor=models.ForeignKey(Instructor, null=True)
    students=models.ManyToManyField(Student)
    def __str__(self):
        return "%s" % self.title
class Topic(models.Model):
    subject = models.CharField(max_length=100, unique=True)   
    intro_course = models.BooleanField(default=True)
    NO_PREFERENCE = 0
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    TIME_CHOICES = (
        (0, 'No preference'),
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Evening')
    )
    time = models.IntegerField(default=0, choices=TIME_CHOICES)
    num_responses = models.IntegerField(default=0)
    avg_age =models.IntegerField(default=20)
    def __str__(self):
        return "(%s, %s, %s)" % (self.subject, str(self.intro_course),str(self.avg_age))
