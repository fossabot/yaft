"""Contains models for tracking fitness.

Just weight and calories consumed for now.
"""

import datetime
from peewee import (
    DateField,
    Model,
    SmallIntegerField,
)


class DateData(Model):
    """Tracks weight and calories consumed for a given date."""
    date = DateField(
        unique=True,
        default=datetime.datetime.now,
        help_text="The date for the data",
    )
    calories = SmallIntegerField(
        null=True,
        help_text="Calories consumed in kcal",
    )
    weight = SmallIntegerField(
        null=True,
        help_text="Weight in kg",
    )
