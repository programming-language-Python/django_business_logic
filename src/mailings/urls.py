from django.urls import path
from . import views

urlpatterns = [
    path('add_to_common_list/', views.add_email_to_common_mailchimp_list_view),
    path('add_to_case_list/', views.add_email_to_case_mailchimp_list_view)
]
