from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db import models
from django.dispatch import receiver
class MyAppConfig(AppConfig):
    name='Rank'
    def ready(self):
        post_migrate.connect(self.handle_post_migrate)
    def handle_post_migrate(self, sender, **kwargs):
        from Rank.utils import load_csv_data
        load_csv_data()
        
