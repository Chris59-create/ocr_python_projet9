from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Ticket
from .forms import EditTicketForm



@login_required
def home_page(request):
    return render(request, "feed/home.html")


@login_required
def flow(request):
    tickets = Ticket.objects.all()

    return render(request, 'feed/flow.html', {'tickets': tickets})


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




