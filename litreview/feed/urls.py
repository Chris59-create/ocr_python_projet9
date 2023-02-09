from django.urls import path
from feed import views

app_name = "feed"

urlpatterns = [
    path('flow', views.flow, name='my-flow'),
    path('ticket/create/', views.create_ticket, name="ticket-create"),
    path('tickets/<int:ticket_id>/update/', views.update_ticket,
         name='ticket-update'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket,
         name='ticket-delete')
]
