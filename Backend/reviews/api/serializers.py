from rest_framework.serializers import ModelSerializer

from reviews.models import Reviews


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = (
            'id', 'name', 'date', 'rating', 'comments', 'restaurantId')
