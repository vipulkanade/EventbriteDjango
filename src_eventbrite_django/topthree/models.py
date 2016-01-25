from __future__ import unicode_literals

from django.db import models

# Create your models here.
CATEGORIES = (
    ('music', 'Music'),
    ('business', 'Business & Professional'),
    ('food', 'Food & Drink'),
    ('community', 'Community & Culture'),
    ('performing','Performing & Visual Arts'),
    ('film', 'Film, Media & Entertainment'),
    ('sports','Sports & Fitness'),
    ('travel', 'Travel & Outdoor'),
    ('charity', 'Charity & Causes'),
    ('religion', 'Religion & Spirituality'),
    ('family', 'Family & Education'),
    ('seasonal', 'Seasonal & Holiday'),
    ('government', 'Government & Politics'),
    ('fashion', 'Fashion & Beauty'),
    ('home', 'Home & Lifestyle'),
    ('auto', 'Auto, Boat & Air'),
    ('hobbies', 'Hobbies & Special Interest'),
    ('other', 'Other'),
)

class Categories(models.Model):
    category_1 =  models.CharField(max_length = 20, choices = CATEGORIES)
    category_2 = models.CharField(max_length = 20, choices = CATEGORIES)
    category_3 = models.CharField(max_length = 20, choices = CATEGORIES)

    def __unicode__(self): #__str__ for python3
        return self.category_1