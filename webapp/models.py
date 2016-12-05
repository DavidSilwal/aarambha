from django.db import models

# Create your models here.

class Blog(models.Model):
     title = models.CharField(max_length=200)
     text = models.TextField()
     image = models.ImageField(blank = True)
     pub_date = models.DateTimeField('Published Date')
     author = models.CharField(max_length=200)
     author_email = models.EmailField(blank = True)
     def __str__(self):
        return self.title;

class Work(models.Model):
     title = models.CharField(max_length=200)
     text = models.TextField()
     image = models.ImageField(blank = True)
     pub_date = models.DateTimeField('Published Date')
     
     def __str__(self):
        return self.title
     
EVENT_STATUS = (
        ('a','Approved'),
        ('s','Submitted'),
        ('r','Rejected'),
)
 
class Event(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField(blank = True)
     event_date = models.DateTimeField()
     event_venue = models.CharField(max_length=200)
     status = models.CharField(max_length=1,choices = EVENT_STATUS)
     pub_date = models.DateTimeField('Published Date')
     image = models.ImageField(blank = True)
     
     def __char__(self):
        return self.title
        
class Member(models.Model):
     first_name =models.CharField(max_length=20)
     last_name =models.CharField(max_length=20)
     contact_no = models.CharField(max_length=20,blank = True)
     email = models.EmailField(blank = True)
     facebook = models.URLField(max_length=200,blank = True)
     image = models.ImageField(blank = True)
     designation = models.CharField(max_length=50)
     
     def __str__(self):
        return self.first_name

    