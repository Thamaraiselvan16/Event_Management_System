# ems_project/ams_app/management/commands/task.py

import pandas as pd
from django.core.management.base import BaseCommand
from ems_app.models import Event

class Command(BaseCommand):
    help = 'Import data from CSV to SQLite database'

    def handle(self, *args, **options):
        # Load CSV file
        csv_data = pd.read_csv('D:\\E_M_S\ems_project\\data.csv')   #please change your directory

        # Iterate through rows and save to database
        for index, row in csv_data.iterrows():
            Event.objects.create(
                event_name=row['event_name'],
                city_name=row['city_name'],
                date=row['date'],
                time=row['time'],
                latitude=row['latitude'],
                longitude=row['longitude']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))



# http://localhost:8000/events/find/?latitude=40.7128&longitude=-74.0060&date=2024-03-22