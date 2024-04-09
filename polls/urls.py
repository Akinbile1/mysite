from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('student_signup', views.student_signup, name="student_signup"),
    path('tutor_signup/', views.tutor_signup, name='tutor_signup'),
    path('signin/', views.login_view, name="signin"),
    path('forgotPass', views.forgotPass, name="forgotPass"),
    path('signout', views.logout_view, name="signout"),
    path('tutor_dashboard/', views.tutor_dashboard, name='tutor_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]