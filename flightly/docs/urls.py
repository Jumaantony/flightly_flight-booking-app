from django.urls import path
from rest_framework.documentation import include_docs_urls, get_schema_view

from flightly.docs.views import Index

urlpatterns = [
    path('docs/', include_docs_urls(title='Flightly API')),
    path('schema/', get_schema_view(title='Flightly API')),
    path('', Index.as_view(), name='index'),
]
