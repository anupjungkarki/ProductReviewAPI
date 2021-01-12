from .views import MyObtainTokenPairView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    # For Add Custom Claim Payload
    # Default payload includes the user_id. You can add any information you want, you just have to modify the claim.
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
