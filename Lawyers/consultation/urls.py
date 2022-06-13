from django.urls import path
from . import views

app_name = "consultation"

urlpatterns = [
    path("add_lawyer", views.add_lawyer, name="add_lawyer"),
    path("update_lawyer/<lawyer_id>/", views.list_lawyers, name="update_lawyer"),
    path("list_lawyers", views.list_lawyers, name="list_lawyers"),
    path("delete_lawyer/<lawyer_id>/", views.delete_lawyer, name="delete_lawyer"),
    path("add_user", views.add_user, name="add_user"),
    path("update_users/<users_id>/", views.list_users, name="update_users"),
    path("list_users", views.list_users, name="list_users"),
    path("delete_user/<users_id>/", views.delete_user, name="delete_user"),

    path("request_consultation/<lawyer_id>/", views.request_consultation, name="request_consultation"),
    path("replay_consultation/<consultation_request_id>/", views.replay_consultation, name="replay_consultation"),
    path("list_consultation", views.list_consultation, name="list_consultation"),
    path("delete_consultation_request/<consultation_request_id>/", views.delete_consultation_request,
         name="delete_consultation_request"),
    path("search_for_lawyers", views.search_for_lawyers, name="search_for_lawyers"),

]
