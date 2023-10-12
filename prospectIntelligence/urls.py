from django.urls import path
from prospectIntelligence.views import Index, UsecaseMappedAccount

urlpatterns = [
    path(r'index', Index.as_view(), name='index'),
    path(r'usecase-mapped-account', UsecaseMappedAccount.as_view(), name='usecase-mapped-account'),
]