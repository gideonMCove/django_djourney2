from rest_framework import serializers
from .models import City,Attractions,Reviews

class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attractions_detail',
        read_only=True
    )
    attractions_id = serializers.PrimaryKeyRelatedField(
        queryset=Attractions.objects.all(),
        source='attractions'
    )
    class Meta:
        model = Reviews
        fields = ('all') 
        

class AttractionsSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='reviews_detail',
        many=True,
        read_only=True
    )
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='artist'
    )
    attractions_url = serializers.ModelSerializer.serializer_url_field(
        view_name='attractions_detail'
    )
    class Meta:
        model = Attractions
        fields = ('id','city','related_name','name','outdoors','photo_url','reviews','attractions_url','city_id',)


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = serializers.HyperlinkedRelatedField(
        view_name='attractions_detail',
        many=True,
        read_only=True
    )
    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'

    )
    class Meta: 
        model = City
        fields = ('id','name','country','photo_url', 'attractions','city_url')



