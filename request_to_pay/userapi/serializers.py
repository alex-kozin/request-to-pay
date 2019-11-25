from rest_framework import serializers

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "first_name", "last_name", "user_type",
         "last_login", "date_joined")

    def to_representation(self, instance):
        """
        Show additional field 'admin' if the user has admin rights
        and field 'active' is the user is inactive.

        Show address information if the user is a customer
        """
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        if not instance.is_active:
            representation['active'] = False
        if instance.user_type == 'C':
            representation['address'] = instance.address
        return representation
