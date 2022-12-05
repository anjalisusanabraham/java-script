from django.urls import path
from .import views

urlpatterns=[
    path('largest',views.js_largest),
    path('secondlargest',views.js_secondlargest),
    path('noofelements',views.js_noofelements),
    path('palindrom',views.js_palindrom),
    path('search',views.js_search)
]
