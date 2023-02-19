from django.core.management.base import BaseCommand
import factory
from decimal import Decimal
from core.models import Item
import random
from core import Currencies


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker('name')
    description = factory.Faker('text')
    price = factory.LazyAttribute(lambda _: Decimal(str(random.randint(10000, 1000000) / 100)))


class Command(BaseCommand):
    help = 'Creates currencies in the database'

    def handle(self, *args, **options):
        for i in range(100):
            ItemFactory.create(currency=random.choice(Currencies.CHOICE)[0])

        self.stdout.write(self.style.SUCCESS('Currencies created successfully'))
