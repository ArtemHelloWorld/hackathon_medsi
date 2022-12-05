from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from quizapi.views import QuizViewSet, QuizList
from userapi.views import *


patient_router = routers.SimpleRouter()
patient_router.register(r'patient', PatientViewSet)

doctor_router = routers.SimpleRouter()
doctor_router.register(r'doctor', DoctorViewSet)

patientDoctor_router = routers.SimpleRouter()
patientDoctor_router.register(r'patient-doctor', PatientDoctorViewSet)

quiz_router = routers.SimpleRouter()
quiz_router.register(r'quiz', QuizViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(patient_router.urls)),
    path('api/v1/', include(doctor_router.urls)),
    path('api/v1/', include(quiz_router.urls)),
    re_path('^api/v1/quiz-tag/(?P<tag>.+)/$', QuizList.as_view()),
    path('api/v1/', include(patientDoctor_router.urls)),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    # path('api/v1/patients/', PatientAPIList.as_view()),  # GET, POST
    # path('api/v1/patients/<int:pk>/', PatientAPIUpdate.as_view()),  # PUT
    #
    # path('api/v1/patient-detail/<int:pk>/', PatientAPIDetailView.as_view()),  # GET PUT DELETE







    # path('api/v1/meetuplist/', MeetUpAPIList.as_view()),
    # path('api/v1/meetuplist/<int:pk>/', MeetUpAPIList.as_view()),


]
