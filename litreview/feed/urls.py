from django.urls import path
from feed import views

app_name = "feed"

urlpatterns = [
    path('flow', views.flow, name='my-flow'),
    path('ticket/create/', views.create_ticket, name="ticket-create"),
    path('tickets/<int:ticket_id>/update/', views.update_ticket,
         name='ticket-update'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket,
         name='ticket-delete'),
    path('tickets/<int:ticket_id>/review/', views.create_review,
         name='review-create'),
    path('review/create_direct', views.create_review_directly,
         name='review-direct-create'),
    path('reviews/<int:review_id>/update/', views.update_review,
         name='review-update'),
    path('reviews/<int:review_id>/delete/', views.delete_review,
         name='review-delete'),
    path('posts', views.display_my_posts, name='my-posts')
]
