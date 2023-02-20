from .models import Swords
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SwordSerializer

# djangorestframework has classes for building out views called ViewSets. With these we can wire up all our CRUD routes pretty easily.
class SwordViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Swords.objects.all()
    # The serializer class for serializing output
    serializer_class = SwordSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]