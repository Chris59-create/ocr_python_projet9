from django.urls import path
from feed import views

app_name = "feed"

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path('ticket/create/', views.create_ticket, name="ticket-create"),
    path('tickets/<int:ticket_id>/detail/', views.display_ticket,
         name='ticket-detail'),
    path('flow', views.flow, name='my-flow')

]
