from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Count, Sum
from datetime import timedelta


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'
    login_url = '/accounts/login/'  # Adjust to your login URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Get workout statistics
        workouts = user.workouts.all().order_by('-date')
        total_workouts = workouts.count()

        # Calculate workout duration statistics (assuming duration is stored as timedelta)
        total_duration = workouts.aggregate(
            total=Sum('duration')
        )['total'] or timedelta(0)

        # Format duration as hours:minutes
        total_hours = int(total_duration.total_seconds() // 3600)
        total_minutes = int((total_duration.total_seconds() % 3600) // 60)
        formatted_duration = f"{total_hours}h {total_minutes}m"

        # Get recent workouts (last 5)
        recent_workouts = workouts[:5]

        # Get workout frequency by day of week
        workout_frequency = (
            workouts.values('date__week_day')
            .annotate(count=Count('id'))
            .order_by('date__week_day')
        )

        # Add data to context
        context.update({
            'user': user,
            'total_workouts': total_workouts,
            'last_workout_date': workouts.first().date if workouts.exists() else None,
            'upcoming_plans': user.workouts.filter(date__gt=timezone.now()).count(),
            'total_duration': formatted_duration,
            'recent_workouts': recent_workouts,
            'workout_frequency': workout_frequency,
            'profile': user.profile  # Assuming you have a OneToOne profile
        })

        return context
