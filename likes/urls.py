from django.urls import path
from . import views

# http://127.0.0.1:8000/blog/
# http://127.0.0.1:8000/blog/1
# http://127.0.0.1:8000/type/1
# http://127.0.0.1:8000/blog/date/2020/2

urlpatterns = [  
    path('like_change', views.like_change, name='like_change'),   
]
