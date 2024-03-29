from django.db import models
from django.contrib.auth.models import User
import datetime

class City(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.name    

class Restaurant_Type(models.Model):
    title = models.CharField(max_length=150, unique=True, null=True) 
    title_fa = models.CharField(max_length=150, unique=True, null=True)
    def __str__(self):
        return self.title

class Food_Type(models.Model):
    title = models.CharField(max_length=150, unique=True, null=True)
    title_fa = models.CharField(max_length=150, unique=True, null=True)
    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    full_address = models.TextField(default="")
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200)
    long_description = models.TextField(default="")
    phone_number = models.CharField(max_length=20)
    type = models.ManyToManyField(Restaurant_Type)
    location_x = models.FloatField()
    location_y = models.FloatField()

    @property
    def average_score(self):
        reviews = Comment.objects.filter(restaurant = self.id)
        score = "ثبت نشده"
        if reviews:
            counter = 0
            score = 0
            for review in reviews:
                score += review.score
                counter += 1
            score = score/counter
        return score
    
    @property 
    def star(self):
        if self.average_score != "ثبت نشده":
            return range(int(self.average_score))
    
    @property
    def blank_star(self):
        if self.average_score != "ثبت نشده":
            return range(5- int(self.average_score))
    
    @property
    def half_star(self):
        if self.average_score != "ثبت نشده":
            if int(self.average_score) != self.average_score:
                return True
        return False
    
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ManyToManyField(Place)
    food_type = models.ForeignKey(Food_Type, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name   


class Comment(models.Model):
    score_choices = ((1,"خیلی بد"),(2,"بد"),(3,"متوسط"),(4,"خوب"),(5,"عالی"))
    score = models.IntegerField(choices=score_choices)
    body = models.TextField()
    restaurant = models.ForeignKey(Place, on_delete=models.CASCADE)
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(default= datetime.date.today)

    @property 
    def star(self):
        return range(self.score)
    
    @property
    def blank_star(self):
        return range(5- self.score)

    def __str__(self):
        return f"{self.score}-{self.restaurant}"