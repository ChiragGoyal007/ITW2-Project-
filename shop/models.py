from django.db import models

class Song(models.Model):
    song_id = models.AutoField
    song_name = models.CharField(max_length= 50)
    artist  = models.CharField(max_length=50)
    price  = models.IntegerField(default=0)
    rating  = models.IntegerField()
    genre = models.CharField(max_length=10,default = "")
    image = models.ImageField(upload_to="shop/images",default = "")
    album  = models.CharField(max_length=30,default="")
    duration = models.CharField(max_length = 10, default = "0:00")

    def __str__(self):
        return self.song_name
    
class Library(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

