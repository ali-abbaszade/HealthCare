from django.urls import path
from .views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("newsletter/", newsletter_view, name="newsletter"),
    path("department/", department_view, name="department"),
    path("department/<int:pid>/", department_single_view, name="department-single"),
]
