from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Report, ReportType
from .serializers import ReportSerializer, UserSerializer, TipoReporteSerializer, UserLoginSerializer


class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 
#     path('usuarios/<str:username>/<str:password>/', UserDetailView.as_view(), name='user-detail'),


class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

class ReportTypeListCreateView(generics.ListCreateAPIView):
    queryset = ReportType.objects.all()
    serializer_class = TipoReporteSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReportTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportType.objects.all()
    serializer_class = TipoReporteSerializer
    permission_classes = [permissions.IsAuthenticated]