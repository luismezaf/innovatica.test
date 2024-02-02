
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=4)
    confirm_password = serializers.CharField(min_length=4)

    def validate_password(self, value: str):
        if value != self.initial_data.get('confirm_password'):
            raise ValidationError("Las contraseñas no coinciden")

    def validate_confirm_password(self, value: str):
        if value != self.initial_data.get('password'):
            raise ValidationError("Las contraseñas no coinciden")
