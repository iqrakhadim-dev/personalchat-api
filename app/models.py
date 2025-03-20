from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.IntegerChoices):
        CUSTOMER = 0, "Customer"
        ADMIN = 1, "Admin"
      

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.IntegerField(choices=Role.choices, default=Role.CUSTOMER)  # Default is Customer

    def save(self, *args, **kwargs):
        """Prevent non-staff users from setting Admin role"""
        if not self.is_staff and self.role == self.Role.ADMIN:
            self.role = self.Role.CUSTOMER  # Force back to Customer
        super().save(*args, **kwargs)

    # Fix ManyToManyField conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups"  # Avoids conflict
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions"  # Avoids conflict
    )

    
    def __str__(self):
        return self.username
#Categories
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField()
    def __str__(self):
        return self.name
class Personaldetail(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to="products/", default="default.jpg")
    link = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Review by {self.user.username} on {self.category.name}"
  
    
