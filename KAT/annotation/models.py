# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        verbose_name_plural = "Students"
        managed = True
        db_table = 'students'
class Events(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    event_id = models.CharField(primary_key=True, max_length=20)
    event_name = models.CharField(blank=True, null=True, max_length=100)
    claim = models.CharField(blank=True, null=True, max_length=2000)
    claim_url = models.CharField(blank=True, null=True,max_length=200)
    post_url = models.CharField(blank=True, null=True, max_length=20)
    label = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = "Events"
        managed = True
        db_table = 'events'


class Posts(models.Model):
    FEEDBACK_CHOICES = [
        ('0', 'Real'),
        ('1', 'Fake'),
    ]

    event_id = models.CharField(blank=True, null=True, max_length=20)
    post_id = models.AutoField(primary_key=True)
    post_url = models.CharField(blank=True, null=True, max_length=200)
    platform = models.CharField(blank=True, null=True, max_length=50)
    title = models.CharField(blank=True, null=True , max_length=2000)
    student_label = models.CharField(blank=True, null=True, max_length=20)
    img_vid_none = models.CharField(blank=True, null=True, max_length=200)
    likes = models.CharField(blank=True, null=True, max_length=20)
    post_timestamp = models.CharField(blank=True, null=True, max_length=200)
    comments = models.CharField(blank=True, null=True, max_length=200)
    views = models.CharField(blank=True, null=True, max_length=20)
    shares = models.CharField(blank=True, null=True, max_length=20)
    reposts = models.CharField(blank=True, null=True, max_length=20)
    
    annotator1 =  models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )
    annotator2 =  models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )
    annotator3 =  models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        managed = True
        db_table = 'posts'


class PostsComments(models.Model):
    
    FEEDBACK_CHOICES = [
        ('Agree', 'Agree'),
        ('Disagree', 'Disagree'),
        ('Query', 'Query'),
        ('Comment', 'Comment'),
        ('Irrelevent', 'Irrelevent'),
    ]

    comment_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField(blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=2000)
    user = models.CharField(blank=True, null=True, max_length=20)
    likes = models.CharField(blank=True, null=True, max_length=20)
    student_label = models.CharField(blank=True, null=True, max_length=20)
    
    annotator1 = models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )
    # annotator2 = models.CharField(
    #     max_length=10,
    #     choices=FEEDBACK_CHOICES,
    #     blank=True,
    #     null=True,
    # )
    # annotator3 = models.CharField(
    #     max_length=10,
    #     choices=FEEDBACK_CHOICES,
    #     blank=True,
    #     null=True,
    # )

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural = "Post Comments"
        managed = True
        db_table = 'posts_comments'


class PostsUsers(models.Model):
    post_id = models.AutoField(primary_key=True)
    username = models.CharField(blank=True, null=True, max_length=200)
    followers = models.CharField(blank=True, null=True, max_length=20)
    followings = models.CharField(blank=True, null=True, max_length=20)
    verified_unverfied = models.CharField(blank=True, null=True, max_length=10)
    dp_url = models.CharField(blank=True, null=True, max_length=200)
    posts_count = models.CharField(blank=True, null=True, max_length=20)
    joining_date = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Posts Users"
        managed = True
        db_table = 'posts_users'

