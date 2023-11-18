from django.db import models


class BookingStatus(models.IntegerChoices):
    SUBMITTED = 1  # подана
    CONSIDERED = 2  # рассматривается
    CONFIRMED = 3  # подтверждена
    REJECTED = 4  # отклонен
