from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from feed.forms import EditTicket

from .models import Ticket



@login_required
def home_page(request):
    return render(request, "feed/home.html")


@login_required
def create_ticket(request):
    form = EditTicket()

    if request.method == 'POST':
        form = EditTicket(request.POST, request.FILES)

        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            return redirect('feed:ticket-detail', ticket.id)

    return render(request, 'feed/ticket_create.html', {'form': form})


@login_required
def display_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'feed/ticket_detail.html', {'ticket': ticket})


@login_required
def flow(request):
    tickets = Ticket.objects.all()

    return render(request, 'feed/flow.html', {'tickets': tickets})

