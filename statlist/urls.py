from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('profile/<int:id>/', views.details, name="details"),
    path('country', views.country, name="country"),
    path('club', views.club, name="club"),
    path('compare', views.compare, name="compare"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
