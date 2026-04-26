from rest_framework import serializers, viewsets
from django.contrib.auth.models import User

# Vulnerability: Mass assignment - accepting all fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Dangerous: exposes all fields including is_staff, is_superuser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # No field filtering, allows privilege escalation
    def perform_update(self, serializer):
        serializer.save()
