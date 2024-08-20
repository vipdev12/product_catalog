from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewGroupedByRateView(APIView):
    def get(self, request, product_id):
        reviews = Review.objects.filter(product_id=product_id)
        grouped_reviews = {}

        for review in reviews:
            rate = review.rate
            if rate not in grouped_reviews:
                grouped_reviews[rate] = []
            grouped_reviews[rate].append(ReviewSerializer(review).data)

        result = [{'rate': rate, 'items': items} for rate, items in grouped_reviews.items()]
        return Response(result)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
