from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProfileForm
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'profile.html'



# two views: profile to display the user's profile and 
# edit_profile to handle the profile editing. Both views require 
# the user to be logged in (@login_required


@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'profiles/profile.html', {'profile': profile})

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