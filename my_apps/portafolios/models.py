from django.db import models

# Create your models here.


class ProjectTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(ProjectTag, related_name='projects', blank=True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portafolios/images/', blank=True, null=True)
    url = models.URLField(blank=True)
    
    slug = models.SlugField(unique=True, blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
        

class ProjectContent(models.Model):
    
    class ContentType(models.TextChoices):
        TEXT = 'text'
        IMAGE = 'image'
        CODE = 'code'
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contents")
    content_type = models.CharField(max_length=50, choices=ContentType.choices, default=ContentType.TEXT)
    
    content = models.TextField()
    image = models.ImageField(upload_to='portafolios/content/images/')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.project.title} - {self.content_type}"
    
    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'
        ordering = ['order']