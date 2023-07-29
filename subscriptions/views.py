from django.shortcuts import render, get_object_or_404
from .models import Subscription
from django.contrib import messages
from django.db.models import Q


def all_subscriptions(request):
    """ view to show all subscriptions, filtering and search results """

    subscriptions = Subscription.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('subscriptions'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        subscriptions = subscriptions.filter(queries)

    context = {
        'subscriptions': subscriptions,
        'search_term': query,
    }

    return render(request, 'subscriptions/subscriptions.html', context)


def subscription_detail(request, subscription_id):
    """ view to show individual product details """

    subscription = get_object_or_404(Subscription, pk=subscription_id)

    context = {
        'subscription': subscription,
    }

    return render(request, 'subscriptions/subscription_detail.html', context)