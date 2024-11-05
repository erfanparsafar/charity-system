from rest_framework import serializers

from .models import Benefactor
from .models import Charity, Task


class BenefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = ['experience', 'free_time_per_week']

    def create(self, validated_data):
        # TODO: Ensure that the 'user' is always provided in the context in the calling code.
        user = self.context.get('user')  # Use get() to avoid KeyError if 'user' is missing

        # If 'user' is not provided in the context, raise a validation error.
        if user is None:
            raise serializers.ValidationError("User must be provided in context.")

        # Create the Benefactor instance with the validated data and user.
        benefactor = Benefactor.objects.create(
            user=user,
            experience=validated_data['experience'],
            free_time_per_week=validated_data['free_time_per_week']
        )

        return benefactor

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = [ 'name' , 'reg_number']
    def create(self , validated_data):
        
        user = self.context.get('user')
        
        if user is None:
            raise serializers.ValidationError('user must provided in context. ')
        
        charity = Charity.objects.create(
            user = user,
            name = validated_data['name'],
            reg_number = validated_data['reg_number']
            
        )
        
        return charity


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'state' , 'charity' , 'description' 
                 , 'assigned_benefactor' , 'date' ,'age_limit_from'
                 ,'age_limit_to','gender_limit' ]
        
    def create(self, data):
        task = Task.objects.create(**data)
        return task