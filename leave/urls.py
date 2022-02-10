from django.urls import path

from leave import views

urlpatterns = [
    path("requestleave", views.request_leave),
    path("", views.show),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
]
