from django.db import models


class Contact(models.Model):
    """
    A model to create a contact message which includes
    the user, their email & the message
    """
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(blank=False, null=False)

def __str__(self):
        return f'{self.first_name} {self.last_name}'
