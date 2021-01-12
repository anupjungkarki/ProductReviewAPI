
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# For Add Custom Claim Payload
# Default payload includes the user_id. You can add any information you want, you just have to modify the claim.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
