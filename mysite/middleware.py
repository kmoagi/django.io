from django.http import HttpResponseRedirect
from django.urls import reverse

#class that will handle the authentication and authorization checks for accessing the admin page

# If the user is not a superuser, it redirects them to the admin login page.

class AdminRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:login'))
        return self.get_response(request)