from itertools import chain

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value, Q

from .models import Ticket, Review
from .forms import EditTicketForm, EditReviewForm


def get_users_viewable_tickets(user):
    """
    Called by flow().
    :param user: the request user.
    :return: list of the tickets created by the  user and the members he
    follows.
    """
    viewable_tickets = Ticket.objects.filter(
        Q(user=user) | Q(user__in=user.followed_members.all())
    )

    return viewable_tickets


def get_users_viewable_reviews(user):
    """
    Called by flow().
    :param user: the request user.
    :return: List of te reviews created by the user and the members he follows.
    """
    viewable_reviews = Review.objects.filter(
        Q(user=user) | Q(user__in=user.followed_members.all())
    )

    return viewable_reviews


@login_required
def flow(request):
    """
    Render the page flow.html with the tickets and reviews viewable by the
    request user. From the newest to the oldest.
    """

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
    """
    Render the EditTicketForm to create a ticket
    """
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
    """
    Render the EditTicketForm with a ticket instance to create a ticket
    """
    ticket = Ticket.objects.get(id=ticket_id)
    form = EditTicketForm(instance=ticket)

    if request.method == 'POST':
        form = EditTicketForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():

            form.save()

            return redirect('feed:my-posts')

    return render(request, 'feed/ticket_update.html', {'form': form})


@login_required
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        ticket.delete()

        return redirect('feed:my-posts')

    return render(request, 'feed/ticket_delete.html', {'ticket': ticket})


@login_required
def create_review(request, ticket_id):
    """
    Render the EditReviewForm to create a review.
    :param ticket_id: id of the ticket source of the review to create
    """
    ticket = Ticket.objects.get(id=ticket_id)
    
    form = EditReviewForm()

    if request.method == 'POST':
        form = EditReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('feed:my-flow')

    context = {'form': form, 'ticket': ticket}

    return render(request, 'feed/review_create.html', context=context)


@login_required
def create_review_directly(request):
    """
    Render the EditTicketForm and The EditReviewForm to create directly a
    ticket (without previous ticket).
    """
    edit_ticket_form = EditTicketForm()
    edit_review_form = EditReviewForm()

    if request.method == 'POST':

        edit_ticket_form = EditTicketForm(
            request.POST, request.FILES
        )
        edit_review_form = EditReviewForm(request.POST)

        if edit_review_form.is_valid() and edit_ticket_form.is_valid():

            ticket = edit_ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = edit_review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect('feed:my-flow')

    context = {
        'edit_ticket_form': edit_ticket_form,
        'edit_review_form': edit_review_form
    }

    return render(request, 'feed/review_direct_create.html', context=context)


@login_required
def display_review(request, review_id):
    review = Review.objects.get(id=review_id)

    return render(request, 'feed/review_display.html', {'review': review})


@login_required
def update_review(request, review_id):
    """
    Render the EditReviewForm with a review instance to update it.
    :param review_id: id of the review to update
    """
    review = Review.objects.get(id=review_id)
    ticket = review.ticket

    review_rating = review.rating
    
    form = EditReviewForm(instance=review)

    if request.method == 'POST':
        form = EditReviewForm(request.POST, instance=review)

        if form.is_valid():

            form.save()

        return redirect('feed:my-posts')

    context = {'review_rating': review_rating, 'form': form, 'ticket': ticket}

    return render(request, 'feed/review_update.html', context=context)

        
@login_required
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)

    if request.method == 'POST':
        review.delete()

        return redirect('feed:my-posts')

    return render(request, 'feed/review_delete.html', {'review': review})
    

@login_required
def display_my_posts(request):
    """
    Render the page posts.html with the tickets and reviews created by the
    request user. From the newest to the oldest.
    """
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed/posts.html', context={'posts': posts})
