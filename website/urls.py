from django.urls import path

from website.views import AllEventsView, EventView, SportsView, EconomicsView, PoliticsView, NewView, OtherView

urlpatterns = [
    path('', AllEventsView.as_view(), name='home'),
    path('sports/', SportsView.as_view(), name='sports'),
    path('economics/', EconomicsView.as_view(), name='economics'),
    path('politics/', PoliticsView.as_view(), name='politics'),
    path('new/', NewView.as_view(), name='new'),
    path('other', OtherView.as_view(), name='other'),
    path('event/<int:pk>', EventView.as_view(), name='event'),
]
