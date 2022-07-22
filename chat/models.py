from django.db import models

class Message(models.Model):
    user_name = models.CharField(max_length=20)
    msg = models.CharField(max_length=280)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        timestamp = str(self.pub_date).split('.')[0]
        timestamp_time = timestamp.split(' ')[1]
        timestamp = timestamp.split(' ')[0]
        timestamp = f"{timestamp.split('-')[2]}.{timestamp.split('-')[1]}.{timestamp.split('-')[0]} {timestamp_time}"

        name = str(self.user_name)
        message = str(self.msg)
        return f"[{timestamp}] {name}: {message}"
