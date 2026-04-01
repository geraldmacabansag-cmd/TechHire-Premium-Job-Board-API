from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import JobPosting
from .serializers import JobPostingSerializer
from rest_framework.permissions import IsAdminUser 


class JobListView(generics.ListAPIView):
    """
    GET /api/jobs/
    List all job postings.

    Query params:
      ?search=<term>    — search title & description
      ?location=<city>  — filter by exact location
      ?ordering=created_at | -created_at
      ?page=<n>         — pagination (10 per page)
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['location']
    ordering_fields = ['created_at']
    ordering = ['-created_at']      # default: newest first


class JobDetailView(generics.RetrieveAPIView):
    """
    GET /api/jobs/<id>/
    Retrieve a single job posting.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobCreateView(generics.CreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [IsAdminUser]

@api_view(['GET'])
def home(request):
    return Response({
        "message": "Welcome to TechHire API 🚀",
        "endpoints": {
            "jobs_list":   "/api/jobs/",
            "job_detail":  "/api/jobs/<id>/",
            "get_token":   "/api/token/",
            "refresh_token": "/api/token/refresh/",
        },
    })