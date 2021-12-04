from rest_framework import serializers
from codeInOne_API.quickstart.models import Challenge
from django.utils import timezone

class ChallengeSerializer(serializers.ModelSerializer):
    challengeName = serializers.CharField(max_length=200, default='')
    challengeDesc = serializers.CharField()
    release_date = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = Challenge
        fields = ('__all__')