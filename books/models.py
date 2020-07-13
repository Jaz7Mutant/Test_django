from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    reserved = models.BooleanField()

    def __str__(self):
        return f'{self.author} {self.title} {self.release_date}'

    def reserve(self):
        self.reserved = True

    def release(self):
        self.reserved = False
