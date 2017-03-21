#--utf--
from django.db import models
from django.template.defaultfilters import slugify
class MathTheory(models.Model):
    title = models.CharField(max_length=200)
    task = models.TextField(blank=True)
    image = models.ImageField(upload_to='theory_images',blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MathTheory, self).save(*args, **kwargs)

    def __str__(self):
      return self.title

class TheoryHighterMath(models.Model):
    title = models.CharField(max_length=200)
    ask = models.TextField(blank=True)
    image = models.ImageField(blank=True)

class TheoryDiscretMath(models.Model):
    title = models.CharField(max_length=200)
    ask = models.TextField(blank=True)
    image = models.ImageField(blank=True)

class TheoryTheoryOfProbabilty(models.Model):
 title = models.CharField(max_length=200)
 ask = models.TextField(blank=True)
 image = models.ImageField(blank= True)