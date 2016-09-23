from uuid import uuid4

from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"


def generate_app_token(sequencing_token):
    user = User(username='sequencing-{0}'.format(uuid4()), password=sequencing_token)
    user.save()
    token = Token.objects.create(user=user)
    return token.key
