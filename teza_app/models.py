from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=255)
    band = models.TextField()
    year = models.IntegerField()
    generated_text = models.TextField(blank=True, null=True)
    generated_image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    capitalized_words_count = models.IntegerField(default=0,blank=True, null=True)
    words_followed_by_numbers = models.IntegerField(default=0,blank=True, null=True)
    def is_year_even(self):
        return self.year % 2 == 0

    def __str__(self):
        return f"{self.name} - {self.band} ({self.year})"
