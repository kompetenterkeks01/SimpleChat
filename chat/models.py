from django.db import models

class Message(models.Model):
    user_name = models.CharField(max_length=20)
    msg = models.CharField(max_length=280)
    pub_date = models.DateTimeField('date published')
    def __str__(self):

        return f"{str(self.user_name)} [{str(self.pub_date).split(' ')[1].split('.')[0]}]: {str(self.msg)}"
