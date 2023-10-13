from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


# {
#     "username":"namme",
#     "email": "hyjac4k@gmail.com",
#     "password":"13456k78"
# }