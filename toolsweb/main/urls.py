from django.urls import path
from .views import *

urlpatterns = [
    path('', index_pg),
    path('login/', login_pg),
    path('import/', import_pg),
]
