from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    nick_name = serializers.CharField()
    def get_cleaned_data(self):
        data=super().get_cleaned_data()
        data['nick_name'] = self.validated_data.get('nick_name','')
        return data
