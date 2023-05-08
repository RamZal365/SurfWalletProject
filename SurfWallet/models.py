from django.contrib.auth.models import User
from django.db import models


# class Song(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tempo = models.IntegerField()
#     time_signature_top = models.IntegerField()
#     time_signature_bottom = models.IntegerField()
#     CLEF_OPTIONS = (
#         ('G_CLEF', 'G'),
#         ('C_CLEF', 'C'),
#         ('F_CLEF', 'F'),
#     )
#     clef = models.TextField(choices=CLEF_OPTIONS)
#     sharps = models.ManyToManyField('Note', through='SharpNote', related_name='songs')
#
#
# class Bar(models.Model):
#     song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='bars')
#     number = models.PositiveIntegerField()
#
#
# class Note(models.Model):
#     bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name='notes')
#     number = models.PositiveIntegerField()
#     name = models.CharField(max_length=10)
#     octave = models.PositiveIntegerField()
#     time = models.PositiveIntegerField()
#
#
# class SharpNote(models.Model):
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)
#     note = models.ForeignKey(Note, on_delete=models.CASCADE)
#     order = models.PositiveIntegerField()
#
#     class Meta:
#         ordering = ['order']