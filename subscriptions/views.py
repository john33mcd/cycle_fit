from django.shortcuts import render, get_object_or_404
from .models import Subscription


def all_subscriptions(request):
    """ view to show all subscriptions, filtering and search results """

    subscriptions = Subscription.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/subscriptions.html', context)


def subscription_detail(request, subscriptions_id):
    """ view to show individual subscription details """

    subscription = get_object_or_404(Subscription, pk=subscription_id)

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/subscription_detail.html', context)