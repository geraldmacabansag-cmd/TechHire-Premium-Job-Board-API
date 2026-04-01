from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobs/create/', JobCreateView.as_view(), name='job-create')
]