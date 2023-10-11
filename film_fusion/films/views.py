from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics, permissions
from films.models import Movie, Director, Review, Cast

from films.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, CastSerializer
# Create your views here.

from users import authentication

class DirectorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.TokenAuthentication]

class DirectorDeleteAPIView(generics.DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.raw("SELECT * FROM films_movie")
    serializer_class = MovieSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class MovieNameDetailAPIView(generics.ListAPIView):

    lookup_field = 'title'
    def get_queryset(self):
        return Movie.objects.raw(f"SELECT * FROM films_movie WHERE title LIKE '%%{self.kwargs[self.lookup_field]}%%'")
    
    serializer_class = MovieSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class MovieDeleteAPIView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]



class MovieUpdateAPIView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class CastListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class MovieReviewsListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'movie_id'

    def get_queryset(self, *args, **kwargs):
        return Review.objects.filter(movie=self.kwargs[self.lookup_field])
    serializer_class = ReviewSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
