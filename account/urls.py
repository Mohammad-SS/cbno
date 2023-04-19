from django.urls import path
from .views import TwoSumAPIView , ContactCreateAPIView

urlpatterns = [
    path("two_sum", TwoSumAPIView.as_view(), name="two-sum"),
    path("contact", ContactCreateAPIView.as_view(), name="contact"),
]
