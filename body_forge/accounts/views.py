from datetime import date

from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView

from body_forge.accounts.forms import AppUserCreationForm, UserProfileEditForm

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class AppUserLoginView(LoginView):
    template_name = "accounts/login-page.html"


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # --- Dashboard Stats (Placeholders/Examples) ---
        # Assuming you have a Workout model linked to your user
        # total_workouts = Workout.objects.filter(user=user).count()
        # last_workout = Workout.objects.filter(user=user).order_by('-date').first()
        # last_workout_date = last_workout.date.strftime("%B %d, %Y") if last_workout else "N/A"

        context['total_workouts'] = 5  # Placeholder
        context['last_workout_date'] = date(2025, 5, 15).strftime("%B %d, %Y")  # Placeholder
        context['upcoming_plans'] = "None"  # Placeholder

        # --- Previous Workouts List ---
        # Example: Fetch user's workouts, annotate with exercise count
        # user_workouts = Workout.objects.filter(user=user).annotate(
        #     exercises_count=Count('exerciseinstance') # Assuming 'exerciseinstance' is related_name from ExerciseInstance to Workout
        # ).order_by('-date')[:5] # Show last 5 workouts

        context['user_workouts'] = [  # Placeholder data for demonstration
            {'name': 'Full Body Strength', 'date': date(2025, 5, 15), 'duration': '60 min', 'exercises_count': 5,
             'pk': 1},
            {'name': 'Cardio Blast', 'date': date(2025, 5, 12), 'duration': '45 min', 'exercises_count': 3, 'pk': 2},
            {'name': 'Leg Day', 'date': date(2025, 5, 10), 'duration': '75 min', 'exercises_count': 6, 'pk': 3},
        ]
        return context


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = "accounts/profile-details-page.html"


@login_required
def profile_edit_view(request):
    profile = request.user.profile  # Assuming you have a UserProfile model linked to User

    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile-details')  # Redirect to the profile details page
        else:
            messages.error(request, 'There was an error updating your profile.')
    else:
        form = UserProfileEditForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit-profile-page.html', context)
