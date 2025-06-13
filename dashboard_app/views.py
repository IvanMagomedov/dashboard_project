from django.shortcuts import render
from .models import SalesRecord
from django.db.models import Sum
from datetime import datetime

def dashboard_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    queryset = SalesRecord.objects.all()
    if start_date and end_date:
        queryset = queryset.filter(date__range=[start_date, end_date])

    # Подготовка данных для графика
    data = (
        queryset
        .values('date')
        .annotate(total_amount=Sum('amount'))
        .order_by('date')
    )

    labels = [entry['date'].strftime("%Y-%m-%d") for entry in data]
    values = [entry['total_amount'] for entry in data]

    return render(request, 'dashboard_app/dashboard.html', {
        'labels': labels,
        'values': values,
        'start_date': start_date,
        'end_date': end_date,
        'records': queryset.order_by('-date')[:100],
    })