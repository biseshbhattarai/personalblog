from django.db import models 


class MessageForm(models.Model):
    first_name = models.CharField(max_length=400)
    email = models.CharField(max_length=20)
    message = models.CharField(max_length=800)


    def __str__(self):
        return self.first_name

class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

