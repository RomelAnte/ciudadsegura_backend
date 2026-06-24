from django.urls import path
from .views import ReportListCreateView, ReportDetailView

urlpatterns = [
    path('reportes/', ReportListCreateView.as_view(), name='report-list-create'),
    path('reportes/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
]