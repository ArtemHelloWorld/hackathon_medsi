from rest_framework import serializers

from quizapi.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'  # list or __all__
