from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from photos.models import Photo
from photos.serializers import PhotoSerializer


# Create your views here.

class PhotoViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   mixins.ListModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user).order_by('-datetime')

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super(PhotoViewSet, self).create(request, *args, **kwargs)
