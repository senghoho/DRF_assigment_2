from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    
    class Meta:
        model = Album
        fields = ['id','artist','title','year','description','created_at','updated_at','tracks','tag']
    
    tracks = serializers.SerializerMethodField(read_only=True)
    def get_tracks(self, instance):
        serializer = TrackSerializer(instance.tracks, many=True)
        return serializer.data
    
    # tag 실제 값으로 바꿔보자
    tag = serializers.SerializerMethodField()
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]


class TrackSerializer(serializers.ModelSerializer):
    #id = serializers.CharField(read_only=True)
    #created_at = serializers.CharField(read_only=True)
    #updated_at = serializers.CharField(read_only=True)

    album = serializers.SerializerMethodField()

    def get_album(self, instance):
        return instance.album.title

    class Meta:
        model = Track
        fields = ['album','number','title']
        read_only_fields = ['album']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__' # 직렬화 했을 때 보여주고 싶은 필드 (모든 필드)