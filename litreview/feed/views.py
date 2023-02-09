from itertools import chain

from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value

from .models import Ticket, Review
from .forms import EditTicketForm


def get_users_viewable_tickets(user):
    viewable_tickets = Ticket.objects.filter(user=user)

    return viewable_tickets


def get_users_viewable_reviews(user):
    viewable_reviews = Review.objects.filter(user=user)

    return viewable_reviews


@login_required
def flow(request):

    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed/flow.html', context={'posts': posts})


@login_required
def create_ticket(request):
    form = EditTicketForm()

    if request.method == 'POST':
        form = EditTicketForm(request.POST, request.FILES)

        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            return redirect('feed:my-flow')

    return render(request, 'feed/ticket_create.html', {'form': form})


@login_required
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = EditTicketForm(instance=ticket)

    if request.method == 'POST':
        form = EditTicketForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            form.save()

            return redirect('feed:my-flow')

    return render(request, 'feed/ticket_update.html', {'form': form})


@login_required
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        ticket.delete()

        return redirect('feed:my-flow')

    return render(request, 'feed/ticket_delete.html', {'ticket': ticket})




