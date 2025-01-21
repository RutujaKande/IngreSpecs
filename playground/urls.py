from django.urls import path
from . import views


urlpatterns=[
    path('',views.sayHello),
    path('submit',views.submitform),
    path('submit-ingredient', views.submit_ingredient, name='submit-ingredient'),
    path('y/', views.y_view, name='y'),
    path('y/<str:output>/', views.y_view, name='y_with_output')
    #
]