from datetime import datetime
from http import client
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from api.models import api

class Command(BaseCommand):
    help = 'Create client from JSON file'

    def handle(self, *args, **kwargs):
        # set the path to the datafile
        datafile = settings.BASE_DIR / 'data_api' / 'client.json'
        assert datafile.exists()

        # load the datafile
        with open(datafile, 'r') as f:
            data = json.load(f)
        
        # create tz-aware datetime object from the JSON string.
        DATE_FMT = "%Y-%m-%d %H:%M:%S"
        for api in data:
            client_date = datetime.strptime(client['last_play'], DATE_FMT)
            client['last_play'] = make_aware(client_date)

        # convert list of dictionaries to list of Track models, and bulk_create
        client = [client(**client) for api in data]

        client.objects.bulk_create(client)