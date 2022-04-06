from django.urls import include, path
from . import views


urlpatterns = [
    
    path('pdf/', views.ConvertPdfView.as_view()),


  
]