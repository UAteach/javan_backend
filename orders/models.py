from django.db import models
from django.db.models import Q
from django.conf import settings

from core.models import ExtendedUser
from items.models import Item

class Order(models.Model):
    # TODO: handle bin number mess
    bin_number = models.IntegerField(unique=True)

    STATUS = {
        ('ASSIGNED', 'ASSIGNED'),
        ('STARTED', 'STARTED'),
        ('PLACED', 'PLACED'),
        ('UPDATED', 'UPDATED'),
        ('FILLED', 'FILLED'),
        ('SELF-FILLED', 'SELF-FILLED'),
        ('OUT', 'OUT'),
        ('RETURNED', 'RETURNED'),
        ('EMPTIED', 'EMPTIED'),
        ('DONE', 'DONE')
    }
    status = models.CharField(max_length=11, choices=STATUS, default='ASSIGNED')

    master_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # TODO: see if can fix to be based on classification number
        # limit_choices_to=({CustomUser.classification == 2}),
        # limit_choices_to=Q(groups__name='Master Teacher'),
        related_name='master_teacher',
        null=True,
        blank=True,
    )

    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    # course = models.ForeignKey(
    #     Course,
    #     on_delete=models.CASCADE,
    #     null=True
    # )

    trello_id = models.CharField(max_length=50, blank=True)

    expected_pickup_datetime = models.DateTimeField(null=True, blank=True)
    actual_pickup_datetime = models.DateTimeField(null=True, blank=True)
    
    expected_return_datetime = models.DateTimeField(null=True, blank=True)
    actual_return_datetime = models.DateTimeField(null=True, blank=True)

    other_notes = models.TextField(null=True, blank=True)


class OrderContent(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True
    )

    # Not needed for unlisted item
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        null=True
    )

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    other_notes = models.TextField(null=True, blank=True)
    self_filled = models.BooleanField(default=False)


class OrderComplete:
    order = Order()
    status = ""
    members = []
    content = []
