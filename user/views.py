from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import Account
from user.permissions import AccountPermission
from user.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    permission_classes = [AccountPermission]

    @action(methods=['get'], detail=False, url_path='me')
    def get_me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
