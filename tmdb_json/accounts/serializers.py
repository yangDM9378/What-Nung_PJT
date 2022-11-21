from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    nick_name = serializers.CharField()
    def get_cleaned_data(self):
        data=super().get_cleaned_data()
        data['nick_name'] = self.validated_data.get('nick_name','')
        return data

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        extra_fields = []
        UserModel = get_user_model()
        if hasattr(UserModel, 'nick_name'):
            extra_fields.append('nick_name')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('nick_name',)