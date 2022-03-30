import csv
import logging
from .models import Player, Country, Club, TransferMarket, Skills
from pathlib import Path

for item in [Player, Country, Club, TransferMarket, Skills]:
    item.objects.all().delete()

print("Table dropped successfully")
BASE_DIR = Path(__file__).resolve().parent.parent
data_link = str(BASE_DIR) + '/statlist/data/data.csv'