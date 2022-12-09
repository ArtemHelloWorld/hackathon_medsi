from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from quizapi.models import Quiz
from quizapi.serializers import QuizSerializer
from userapi.permissions import IsOwnerOrReadOny


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsOwnerOrReadOny]


class QuizList(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):

        tag = f"#{self.kwargs['tag']}"
        return Quiz.objects.filter(tag=tag)



