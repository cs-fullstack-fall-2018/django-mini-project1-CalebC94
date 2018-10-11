from django.shortcuts import render

from .models import TimeSheet


def index(request):
    TimeCards = TimeSheet.objects.all
    context = {'TimeCards': TimeCards}
    return render(request, 'timecard_app/index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged