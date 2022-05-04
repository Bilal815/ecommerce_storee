from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Tag, Newsletter
from django.contrib.auth.models import User
from .serializers import TagSerializer, NewsletterSerializer, UserSerializer, TagSerializer
from .permissions import IsOwner
from .utils import Util
from rest_framework.generics import ListAPIView

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def newsletters(self, req, pk=None):
        tag = self.get_object()
        if req.method == 'GET':
            serializer = TagSerializer(tag.newsletters, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)


class NewslettersViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.action in ['list', 'target_votar', 'suscriptions']:
            permission_classes = (IsAuthenticated,)
        elif self.action in ['create']:
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (IsOwner,)

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item in ['tags']:
                query[item + '__name'] = self.request.query_params[item]
                continue
            query[item + '__icontains'] = self.request.query_params[item]

        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data['owner'])
        if user.has_perm('newsletter.IsAdmin'):
            newsletter = NewsletterSerializer(data=request.data)
            if newsletter.is_valid():
                newsletter.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=newsletter.errors)
        else:
            return Response({"mensaje": "Owner no es administrador"}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def owner(self, req, pk=None):
        newsletter = self.get_object()
        serializer = UserSerializer(newsletter.owner)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['GET'], detail=True)
    def guests(self, req, pk=None):
        newsletter = self.get_object()
        for guest in newsletter.guests.all():
            serializer = UserSerializer(guest)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def tags(self, req, pk=None):
        newsletter = self.get_object()

        if req.method == 'GET':
            serializer = TagSerializer(newsletter.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if req.method in ['POST', 'DELETE']:
            tags_id = req.data['tags']
            for tag_id in tags_id:
                tag = Tag.objects.get(id=int(tag_id))
                if req.method == 'POST':
                    newsletter.tags.add(tag)
                    return Response(status=status.HTTP_201_CREATED)
                if req.method == 'DELETE':
                    try:
                        newsletter.tags.remove(tag)
                        return Response(status=status.HTTP_204_NO_CONTENT)
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def guest_admin(self, req, pk=None):
        admin_id = req.data['users']
        newsletter = self.get_object()

        for admin in admin_id:
            user_admin = User.objects.get(id=int(admin))
            if user_admin.has_perm('newsletter.IsAdmin'):
                newsletter.guests.add(user_admin)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def suscriptions(self, req, pk=None):
        """ As a user I want to be able to subscribe to a newsletter to receive related news in my email """
        newsletter = self.get_object()

        if req.method == 'GET':
            serializer = UserSerializer(newsletter.subscribers, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if req.method in ['POST', 'DELETE']:
            users_id = req.data['users']
            for id in users_id:
                user = User.objects.get(id=id)
                if req.method == 'POST':
                    newsletter.subscribers.add(user)
                    # suscription send email
                    email_body = 'Hola ' + user.username + ' gracias por suscribirte al boletin \n' + newsletter.name
                    data = {'email_body': email_body,
                            'to_email': user.email,
                            'email_subject': 'Suscripción'}

                    Util.send_email(data)
                    serializer = UserSerializer(newsletter.subscribers, many=True)
                    return Response(status=status.HTTP_201_CREATED, data=serializer.data)
                elif req.method == 'DELETE':
                    newsletter.subscribers.remove(user)
                    serializer = UserSerializer(newsletter.subscribers, many=True)
                    return Response(status=status.HTTP_204_NO_CONTENT, data=serializer.data)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def target_votar(self, req, pk=None):
        newsletter = self.get_object()
        target = newsletter.target.count()
        if req.method == 'GET':
            serializer = UserSerializer(newsletter.target, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if req.method in ['POST', 'DELETE']:

            """ As a user I want to be able to vote for a bulletin so that it can be launched
                of this newsletter and As a user I want to be able to unsubscribe from the newsletters
                to stop receiving news
            """

            users_id = req.data['users']
            for id in users_id:
                user = User.objects.get(id=int(id))
                if req.method == 'POST':
                    newsletter.target.add(user)

                    serializer = UserSerializer(newsletter.target, many=True)
                    return Response(status=status.HTTP_201_CREATED, data=serializer.data)
                elif req.method == 'DELETE':
                    newsletter.target.remove(user)
                    serializer = UserSerializer(newsletter.target, many=True)
                    return Response(status=status.HTTP_204_NO_CONTENT, data=serializer.data)


class NewsletterListUser(ListAPIView):
    # As a user I want to log in to be able to
    # see the newsletters to which I am subscribed
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        my_subscriptions = Newsletter.objects.filter(subscribers=self.request.user.id)
        return my_subscriptions
