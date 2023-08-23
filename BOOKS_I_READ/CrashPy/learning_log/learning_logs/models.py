from django.db import models

# Create your models here.

class Topic(models.Model):   #Model is a parent class of django
    '''a topic the user is learning about'''
    # adding two attributes
    text = models.CharField(max_length = 200) #space to be reserved in db
    date_added = models.DateTimeField(auto_now_add=True) #current time taken default


class Entry(models.Model):
    '''something specific learned about a topic'''
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self): # __str__ returns string stored in text
        '''return a string representation of the model'''
        return f"{self.text[:50]}..."
