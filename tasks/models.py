from django.db import models


class Task(models.Model):
    
    PRIORITY_CHOICES = [
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('high', 'High'),
    ]
    
    
   
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    owner = models.ForeignKey(
        "auth.User", related_name="tasks", on_delete=models.CASCADE
    )  
    
    



    
    class Meta:
        ordering = ['created']
    
        def __str__(self):
            return self.description
        
        
        