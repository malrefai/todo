from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from app.views import todos_view

# Create a router and register our viewsts with it.
router = DefaultRouter()
router.register(r"todos", todos_view.TodoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r"^", include(router.urls))
]
