from django.core.management.base import BaseCommand
from dashboard_app.models import SalesRecord
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Загрузить тестовые данные продаж'

    def handle(self, *args, **kwargs):
        products = ['Хлеб', 'Молоко', 'Сыр', 'Яблоки', 'Чай']
        start_date = date(2024, 1, 1)

        records = []
        for i in range(100):
            record_date = start_date + timedelta(days=i)
            product = random.choice(products)
            amount = round(random.uniform(100, 5000), 2)

            records.append(SalesRecord(
                date=record_date,
                product=product,
                amount=amount
            ))

        SalesRecord.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('✅ Загружено 100 тестовых записей'))