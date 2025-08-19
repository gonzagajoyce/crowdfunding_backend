from django.db import models
from django.contrib.auth import get_user_model

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def total_pledged(self):
        return self.pledges.aggregate(models.Sum('amount'))['amount__sum'] or 0

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        related_name='pledges',
        on_delete=models.CASCADE

    )
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges',
        on_delete=models.CASCADE
    
    )