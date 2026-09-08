from django.urls import path
from .views import ReportListCreateView, ReportDetailView, UserListCreateView, UserDetailView

urlpatterns = [
    path('reportes/', ReportListCreateView.as_view(), name='report-list-create'),
    path('reportes/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('usuarios/', UserListCreateView.as_view(), name='user-list-create'),
    path('usuarios/<int:pk>/', UserDetailView.as_view(), name='user-detail'),   
]