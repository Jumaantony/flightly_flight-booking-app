from django.urls import path
from rest_framework.documentation import include_docs_urls

from flightly.docs.views import Index

urlpatterns = [
    path('docs/', include_docs_urls(title='Flightly API')),
    path('', Index.as_view(), name='index' ),
]