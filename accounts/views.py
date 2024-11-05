from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer



class LogoutAPIView(APIView):
    # TODO: Consider implementing throttle or rate limiting for this endpoint to prevent abuse.
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
            # FIXME: If your system supports multi-token authentication, review how tokens are handled here.
            if hasattr(request.user, 'auth_token'):
                request.user.auth_token.delete()

                # TODO: If the system supports multiple tokens per user, ensure only the current token is deleted.
                return Response(
                    data={'message': f'{request.user.username} logged out'},
                    status=status.HTTP_200_OK
                )
            else:
                # FIXME: Provide a more specific error message, e.g., if the token has already expired.
                return Response(
                    data={'error': 'Token not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            # TODO: Add logging here for better error tracking and debugging.
            return Response(
                data={'error': 'An error occurred while logging out.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
             
        
       
class UserRegistration(generics.CreateAPIView):
    """API view for user registration."""
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # TODO: Implement permission classes if user registration is restricted (e.g., AllowAny)
    # permission_classes = [permissions.AllowAny]  # Example permission class

    # TODO: Add throttle classes if you want to limit the number of registrations per IP
    # throttle_classes = [UserThrottle]  # Example throttle class

    # TODO: Consider adding custom logging for successful and failed registration attempts
    # def perform_create(self, serializer):
    #     # Custom logic before saving the user can go here
    #     user = serializer.save()
    #     # Example: Logging the registration
    #     logger.info(f'New user registered: {user.username}')