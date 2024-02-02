
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    # Write-only password
    password = serializers.CharField(write_only=True, label='Contraseña')

    def create(self, validated_data: dict):
        """
        Override create method to handle password hashing.
        """

        # Create instance
        instance: 'User' = super().create(validated_data)

        # Set new password
        password = validated_data.pop("password", None)
        if not password:
            raise ValidationError({"password": "This field is required"})
        instance.set_password(password)
        instance.save()

        # Return created instance
        return instance

    def update(self, instance: 'User', validated_data: dict):
        """
        Override update method to prevent password update.
        """

        validated_data.pop('password', None)
        return super().update(instance, validated_data)

    class Meta:
        fields = [
            'id',
            'username',
            'password',
            'email',
            'is_superuser',
            'first_name',
            'last_name',
            'is_active',
            'is_verified'
        ]
        model = User
