"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import UserViewSet, QuestionViewSet, QuizViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'quiz', QuizViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserViewSet.as_view({'get':'list'}), name='user'),
    path('question/', QuestionViewSet.as_view({'get':'list'}), name='question'),
    path('quiz/', QuizViewSet.as_view({'get':'list'}), name='quiz'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),    # order matters, checks urls in order, makes sure request is processed so it doesn't just redirect to user first
]
