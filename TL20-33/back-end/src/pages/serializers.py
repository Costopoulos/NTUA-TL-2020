from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'card_id', 'wallet_id', 'points', 'user_id'] #'id' or 'user_id'
        extra_kwargs = {
            'password':{'write_only': True}
        }

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     #username = validated_data.pop('username', None)
    #     instance = self.Meta.model(**validated_data)
    #     print(instance)
    #     #str(instance) = username, if username = validated_data.pop('username', None)
    #     if password is not None:
    #         #instance.set_password(password)
    #         userpass = get_user_model().objects.raw("INSERT INTO pleasework_user VALUES (NULL, 0, NULL, NULL, 0, 0, NULL, 102,'"+str(instance)+"','"+password+"','eu.erat@sitametluctus.net',102,'201',123)")
    #     #instance.save()
    #     #print(User)
        
    #     #return instance
    #     return userpass
    #     # return Response({
    #     #     'message': 'success'
    #     # })
