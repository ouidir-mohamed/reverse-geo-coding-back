from django.urls import include, path
from . import views


urlpatterns = [
    
    path('xlsx/', views.ConvertXlsxView.as_view()),


  
]