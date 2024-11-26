from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    confirm_password=models.CharField(max_length=10)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Recipe(models.Model):
    Category_Choice = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    recipe_name=models.CharField(max_length=100)
    category=models.CharField(max_length=10,choices=Category_Choice)
    description=models.TextField()
    ingredients=models.TextField()
    instructions=models.TextField()
    registration=models.ForeignKey(Registration,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe_name} {self.category}'


class Rating(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.registration.first_name}, {self.recipe.recipe_name},{self.rating},{self.review}'