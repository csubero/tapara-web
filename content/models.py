from django.db import models
from django.urls import reverse


class Service(models.Model):
    """Model for services offered by Tapara Dev"""
    name = models.CharField(max_length=100, verbose_name='Nombre del Servicio')
    description = models.TextField(verbose_name='Descripción')
    short_description = models.CharField(max_length=200, verbose_name='Descripción Corta', 
                                       help_text='Descripción breve para mostrar en tarjetas')
    icon = models.CharField(max_length=50, default='fas fa-code', verbose_name='Icono',
                          help_text='Clase CSS del icono (ej: fas fa-code)')
    is_featured = models.BooleanField(default=False, verbose_name='Destacado')
    order = models.IntegerField(default=0, verbose_name='Orden')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Model for portfolio projects"""
    STATUS_CHOICES = [
        ('completed', 'Completado'),
        ('in_progress', 'En Progreso'),
        ('planned', 'Planificado'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Nombre del Proyecto')
    description = models.TextField(verbose_name='Descripción')
    short_description = models.CharField(max_length=200, verbose_name='Descripción Corta')
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name='Imagen')
    url = models.URLField(blank=True, null=True, verbose_name='URL del Proyecto')
    github_url = models.URLField(blank=True, null=True, verbose_name='URL de GitHub')
    technologies = models.CharField(max_length=200, verbose_name='Tecnologías Utilizadas',
                                  help_text='Separadas por comas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed',
                            verbose_name='Estado')
    is_featured = models.BooleanField(default=False, verbose_name='Destacado')
    order = models.IntegerField(default=0, verbose_name='Orden')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.name


class TeamMember(models.Model):
    """Model for team members"""
    name = models.CharField(max_length=100, verbose_name='Nombre')
    position = models.CharField(max_length=100, verbose_name='Cargo')
    bio = models.TextField(verbose_name='Biografía')
    photo = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name='Foto')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    linkedin = models.URLField(blank=True, null=True, verbose_name='LinkedIn')
    github = models.URLField(blank=True, null=True, verbose_name='GitHub')
    twitter = models.URLField(blank=True, null=True, verbose_name='Twitter')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    order = models.IntegerField(default=0, verbose_name='Orden')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Miembro del Equipo'
        verbose_name_plural = 'Miembros del Equipo'
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class ContactMessage(models.Model):
    """Model for contact form messages"""
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Asunto')
    message = models.TextField(verbose_name='Mensaje')
    is_read = models.BooleanField(default=False, verbose_name='Leído')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class CompanyInfo(models.Model):
    """Model for company information (singleton)"""
    company_name = models.CharField(max_length=100, default='Tapara Dev', verbose_name='Nombre de la Empresa')
    tagline = models.CharField(max_length=200, verbose_name='Lema',
                              default='Desarrollo de aplicaciones web, móviles e integraciones')
    about_text = models.TextField(verbose_name='Texto de Acerca De')
    mission = models.TextField(blank=True, null=True, verbose_name='Misión')
    vision = models.TextField(blank=True, null=True, verbose_name='Visión')
    logo = models.ImageField(upload_to='company/', blank=True, null=True, verbose_name='Logo')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    address = models.TextField(blank=True, null=True, verbose_name='Dirección')
    
    class Meta:
        verbose_name = 'Información de la Empresa'
        verbose_name_plural = 'Información de la Empresa'
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass  # Prevent deletion
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def __str__(self):
        return self.company_name
