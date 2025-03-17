from django.urls import path
from .views import*

urlpatterns = [
    ##UI##
    path('home/', home, name='home'),
    ##COMMON##
    path('hello/', hello, name='hello'),
    ##AUTHENTICATION##
    ##DASHBOARD##
    ##ROOMS##
    ##BOOKINGS##
    ##PAYMENTS##
    ##PROFILE##
    ##COMMUNICATION##
    ##ADMIN##
    ##REPORTS##
    ##SETTINGS##
    ##HELP##
    ##ERRORS##
    ##TEST##
    ##DEBUG##
    ##EXTERNAL##
    ##DEVELOPER##
    ##DEMO##
    ##OTHER##
    ##EXPERIMENTAL##
    ##CUSTOM##

]