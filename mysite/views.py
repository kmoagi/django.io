from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProfileForm
from django.views.generic import TemplateView

#created a new views file to render the map page

from django.contrib.auth.models import User
from django.shortcuts import render


# we retrieve all registered users who have a non-null location and
#  include the associated profile using select_related. 
# We pass the users queryset to the map.html template.

def user_locations(request):
    users = User.objects.exclude(profile__location__isnull=True).select_related('profile')
    return render(request, 'map.html', {'users': users})


class ProfileView(TemplateView):
    template_name = 'profile.html'



# two views: profile to display the user's profile and 
# edit_profile to handle the profile editing. Both views require 
# the user to be logged in (@login_required


#login_required decorator is used to ensure that only authenticated
#  users can access the profile page

@login_required
def profile(request):
    user = request.user
    return render(request, 'profiles/profile.html', {'user': user})

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})