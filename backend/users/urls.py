from django.urls import path

from users.views import AccountDetails, ContactView

app_name = 'backend'
urlpatterns = [
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
]
