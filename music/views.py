from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializers
from .models import Song


@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET': 
        songs = Song.objects.all()
        serializer = SongSerializers(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializers = SongSerializers(song);
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = SongSerializers(song, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)