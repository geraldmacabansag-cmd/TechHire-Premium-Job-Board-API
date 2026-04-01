from rest_framework import serializers
from .models import JobPosting

LOCKED = "🔒 Premium Feature"


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = [
            'id',
            'title',
            'description',
            'location',
            'company_name',
            'salary_range',
            'application_link',
            'created_at',
        ]

    def _is_premium(self, request) -> bool:
        """Return True only if the request carries a valid JWT for a Premium user."""
        if request is None:
            return False
        user = request.user
        if not user or not user.is_authenticated:
            return False
        profile = getattr(user, 'userprofile', None)
        return profile is not None and profile.is_premium

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')

        if not self._is_premium(request):
            data['company_name'] = LOCKED
            data['salary_range'] = LOCKED
            data['application_link'] = LOCKED

        return data