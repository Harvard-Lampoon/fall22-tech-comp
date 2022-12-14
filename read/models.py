from operator import mod
from pyexpat import model
from django.db import models
from django.conf import settings
from read.managers import WorkManager
from tinymce.models import HTMLField

class Work(models.Model):
    title = models.CharField(max_length=200)
    art_work = models.ForeignKey("ArtWork", related_name="works", on_delete=models.CASCADE, null=True)
    magazine = models.ForeignKey("Magazine", related_name="works", on_delete=models.SET_NULL, null=True, blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True, help_text="Written as YYYY-MM-DD")
    voice_file = models.FileField(upload_to="voices/", null=True, blank=True)
    active = models.BooleanField(default=True)
    classic = models.BooleanField(default=False)
    custom_display_name = models.CharField(max_length=200, null=True, blank=True, help_text="Leave blank if you want your name to show up")
    featured = models.BooleanField(default=False)
    laugh_score = models.PositiveBigIntegerField(default=0)
    original_work = models.BooleanField(default=True)

    objects = WorkManager()

    def __str__(self) -> str:
        return self.title

    def get_display_name(self):
        if self.custom_display_name:
            return self.custom_display_name
        return self.writer.display_name
    
    def get_preview_image(self):
        return self.art_work


class ArtWork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="art/")
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
    custom_display_name = models.CharField(max_length=200, null=True, blank=True)
    original_work = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_display_name(self):
        if self.custom_display_name:
            return self.custom_display_name
        return self.artist.display_name
        
    class Meta:
        ordering = ["-created_at"]

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    description = HTMLField(null=True, blank=True)
    special_link = models.URLField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    cover_image = models.ForeignKey(ArtWork, null=True, blank=True, on_delete=models.SET_NULL)

    issue_editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="issue_editor")
    custom_issue_editor = models.CharField(max_length=200, null=True, blank=True)
    art_editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="art_editor")
    custom_art_editor = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True, help_text="Written as YYYY-MM-DD")

    def __str__(self) -> str:
        return self.title

    def get_total_laughs(self):
        total = 0
        for work in self.works.all():
            total+=work.laugh_score
        return total
    
    def get_random_pieces(self):
        return self.works.filter(active=True).order_by("?")[:7]
        

class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.CharField(max_length=4)
    seller_link = models.URLField()
    active = models.BooleanField(default=True)
    description = HTMLField()
    cover_image = models.ForeignKey(ArtWork, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateField(null=True, blank=True, help_text="Written as YYYY-MM-DD")

    def __str__(self) -> str:
        return self.title

class View(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="views")
    created_at = models.DateTimeField(auto_now_add=True)
    cookie = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f"{self.work.title} view at {self.created_at}"
