from django.core.management.base import BaseCommand
from core.models import Product
from random import randint
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help_text = "Populate products"

    def handle(self, *args, **options):
        products = [
            'Tony Tv',
            'Ramsung Tv',
            'Red Cherry 44',
            'xyz 001',
            'Dp Washing Machine'
        ]

        for product in products:
            Product.objects.create(
                name=product,
                description=lorem_ipsum.sentence(),
                price=randint(5000, 30000)
            )
        