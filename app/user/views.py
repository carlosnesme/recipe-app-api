from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from user.serializers import UserSerializer, AuhTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuhTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.get_queryset.filter(user=self.request.user).order_by('-name')    
