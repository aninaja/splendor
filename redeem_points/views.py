from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

from redeem_points.forms import RedeemPointsForm
from user_profile.models import UserProfile

User = get_user_model()


# Create your views here.
def redeem_points(request, pk):
    user = User.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user=user)
    form = RedeemPointsForm(request.POST or None)
    if form.is_valid():
        redeem = form.save(commit=False)
        redeem.user = user
        points = form.cleaned_data['redeemed_points']
        redeem.redeemed_points = points
        redeem.save()
        if user_profile.total_points >= points:
            user_profile.total_points -= points
            user_profile.save()
        else:
            messages.success(request, 'Insufficient amount of points.')
            return redirect('redeem_points:redeem_points', pk)
        messages.success(request, 'Points redeemed successfully.')
        return redirect('patients:patient_info', pk)
    template_name = 'redeem_points.html'
    context = {'form': form, 'users': user}
    return render(request, template_name, context)

