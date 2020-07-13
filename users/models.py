from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    birth_date = models.DateField()
    banned = models.BooleanField()
    booked_books = models.ForeignKey('books.Book', related_name='users', on_delete=models.deletion.PROTECT)

    def __str__(self):
        ban_status = ''
        if self.banned:
            ban_status = 'BANNED '
        return f'{ban_status}{self.name}'
