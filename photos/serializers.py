from rest_framework.serializers import ModelSerializer
from photos.models import Photo


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
