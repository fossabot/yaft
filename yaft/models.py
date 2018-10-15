"""Contains database related functionality."""

import datetime
from peewee import (
    DateField,
    Model,
    Proxy,
    SmallIntegerField,
)


# We'll replace this with a proper Database object once we've
# initialized one
database_proxy = Proxy()


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta: # pylint: disable=missing-docstring
        database = database_proxy


class DateData(BaseModel):
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
