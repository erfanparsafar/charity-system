from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model with registration functionality."""
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'password', 'phone', 'address', 'gender', 
            'age', 'description', 'first_name', 'last_name', 'email'
        ]
        # TODO: Consider adding additional fields if needed, like profile_picture or is_active

    def create(self, validated_data):
        """Create a new user with hashed password and additional fields."""
        
        # TODO: Validate email to ensure it is unique
        # TODO: Check if phone number is required or optional based on business logic
        # TODO: Implement any additional logic for creating related objects (e.g., Profile, Settings)

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
            address=validated_data.get('address', ''),
            gender=validated_data.get('gender', User.Gender.UNSET),
            age=validated_data.get('age'),
            description=validated_data.get('description', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
        )
        
        # TODO: Send a welcome email to the user
        # TODO: Log the creation of a new user for audit purposes
        
        return user

    # TODO: Implement update method if user details need to be updated in the future
    # TODO: Implement additional validation methods if necessary (e.g., validate_phone, validate_email)