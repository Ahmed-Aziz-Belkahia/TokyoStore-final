# middleware.py

from django.utils import timezone
from .models import Product, RecentlyViewed
from django.urls import resolve

class RecentlyViewedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            resolved_url = resolve(request.path_info)
            if resolved_url.url_name == 'product_detail':  # Adjust to your product detail view name
                meta_title = resolved_url.kwargs.get('meta_title')
                if meta_title:
                    RecentlyViewed.objects.get_or_create(
                        user=request.user,
                        product=Product.objects.get(meta_title=meta_title),
                        defaults={'timestamp': timezone.now()}
                    )
        return response