import json
import django_filters

from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q

from .models import DepreciationClass
from .serializers import DepreciationClass

from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.viewsets import ModelViewSet
from base.rest_extensions import CheckIfSuperUser;


class DepreciationClassFilter(django_filters.FilterSet):
    class Meta:
        model = DepreciationClass
        fields = ['title']

class DepreciationClassViewSet(viewsets.ModelViewSet, CheckIfSuperUser):

    queryset = DepreciationClass.objects.all()
    serializer_class = DepreciationClassFilter
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = DepreciationClassFilter
    search_fields = ('title')

    def create(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(DepreciationClassViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(DepreciationClassViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(DepreciationClassViewSet, self).destroy(request, *args, **kwargs)


