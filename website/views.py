from django.views.generic import ListView, DetailView

from website.models import Event


class AllEventsView(ListView):
    model = Event
    template_name = 'website/home.html'
    paginate_by = 100
    context_object_name = 'all_events'


class SportsView(ListView):
    model = Event
    template_name = 'website/sports.html'
    paginate_by = 100
    context_object_name = 'all_events'


class EconomicsView(ListView):
    model = Event
    template_name = 'website/economics.html'
    paginate_by = 100
    context_object_name = 'all_events'


class PoliticsView(ListView):
    model = Event
    template_name = 'website/politics.html'
    paginate_by = 100
    context_object_name = 'all_events'


class CryptoView(ListView):
    model = Event
    template_name = 'website/crypto.html'
    paginate_by = 100
    context_object_name = 'all_events'


class OtherView(ListView):
    model = Event
    template_name = 'website/other.html'
    paginate_by = 100
    context_object_name = 'all_events'


class EventView(DetailView):
    model = Event
    template_name = 'website/event.html'
