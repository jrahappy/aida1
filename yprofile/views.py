from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse

from accounts.models import CustomUser
from accounts.forms import CustomUserChangeForm


def YourProfile(request, user_id):
    custom_user = get_object_or_404(CustomUser, pk=user_id)
    # custom_user = CustomUser.objects.get(pk=user_id)
    # print(custom_user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=custom_user)
        if form.is_valid():
            form.save()
            return redirect('yprofile:your_profile', user_id=user_id)
    else:
        form = CustomUserChangeForm(instance=custom_user)

    print(form.is_bound)

    context = {
        'form': form
    }
    return render(request, 'yprofile/update.html', context)
