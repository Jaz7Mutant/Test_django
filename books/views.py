from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Book
from .serializers import BookSerializer, AvailableBookSerializer


class AvailableBooksView(generics.ListAPIView):
    serializer_class = AvailableBookSerializer

    def get_queryset(self):
        ordering_field = self.request.GET.get('ordering_field', 'author')
        return Book.objects.all().filter(reserved=False).order_by(ordering_field)


class AllBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        ordering_field = self.request.GET.get('ordering_field', 'author')
        return Book.objects.all().order_by(ordering_field)


class EditBookView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAdminUser, )


class CreateBookView(generics.CreateAPIView):
    serializer_class = BookSerializer
