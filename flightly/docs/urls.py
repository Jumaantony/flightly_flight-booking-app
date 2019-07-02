from django.urls import path
from rest_framework.documentation import include_docs_urls, get_schema_view

from flightly.docs.views import Index

title = "Flightly"
description = "Flight Booking API"

urlpatterns = [
    path('docs/', include_docs_urls(title=title,
                                    description=description
                                    )),
    path('api/v1/', get_schema_view(title=title,
                                    description=description
                                    )),
    path('', Index.as_view(), name='index'),
]
