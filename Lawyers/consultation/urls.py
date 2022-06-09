from django.urls import path
from . import views

app_name = "consultation"

urlpatterns = [
    path("add_lawyer", views.add_lawyer, name="add_lawyer"),
    path("update_lawyer", views.list_lawyers, name="update_lawyer"),
    path("list_lawyers", views.list_lawyers, name="list_lawyers"),
    path("delete_lawyer", views.delete_lawyer, name="delete_lawyer"),
    path("add_consultation", views.add_consultation, name="add_consultation"),
    path("list_consultation", views.list_consultation, name="list_consultation"),
    path("delete_consultation/<consultation_id>/", views.delete_consultation, name="delete_consultation"),
    path("search_for_lawyers", views.search_for_lawyers, name="search_for_lawyers"),
    path("payment", views.payment, name="payment"),
]
