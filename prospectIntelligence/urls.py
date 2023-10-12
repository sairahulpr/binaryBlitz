from django.urls import path
from prospectIntelligence.views import Index

urlpatterns = [
    path(r'index', Index.as_view(), name='issues-tracker'),
]