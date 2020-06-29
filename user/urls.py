from django.urls import path
from user import views
urlpatterns=[
    path('userview/',views.UserView.as_view()),
    path('userAPIview/',views.UserAPIView.as_view()),
    path('userAPIview/<str:id>/',views.UserAPIView.as_view())
]