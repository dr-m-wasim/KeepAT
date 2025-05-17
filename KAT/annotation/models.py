# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Events(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    event_id = models.CharField(primary_key=True)
    event_name = models.CharField(blank=True, null=True)
    claim = models.CharField(blank=True, null=True)
    claim_url = models.CharField(blank=True, null=True)
    post_url = models.CharField(blank=True, null=True)
    label = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = "Events"
        managed = False
        db_table = 'events'


class Posts(models.Model):
    FEEDBACK_CHOICES = [
        ('0', 'Real'),
        ('1', 'Fake'),
    ]

    event_id = models.CharField(blank=True, null=True)
    post_id = models.AutoField(primary_key=True)
    post_url = models.CharField(blank=True, null=True)
    platform = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    student_label = models.CharField(blank=True, null=True)
    img_vid_none = models.IntegerField(blank=True, null=True)
    likes = models.CharField(blank=True, null=True)
    post_timestamp = models.CharField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    views = models.CharField(blank=True, null=True)
    shares = models.CharField(blank=True, null=True)
    reposts = models.CharField(blank=True, null=True)
    
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
        managed = False
        db_table = 'posts'


class PostsComments(models.Model):
    
    FEEDBACK_CHOICES = [
        ('Agree', 'Agree'),
        ('Disagree', 'Disagree'),
        ('Query', 'Query'),
        ('Comment', 'Comment'),
    ]

    comment_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField(blank=True, null=True)
    text = models.CharField(blank=True, null=True)
    user = models.CharField(blank=True, null=True)
    likes = models.CharField(blank=True, null=True)
    student_label = models.CharField(blank=True, null=True)
    
    annotator1 = models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )
    annotator2 = models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )
    annotator3 = models.CharField(
        max_length=10,
        choices=FEEDBACK_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural = "Post Comments"
        managed = False
        db_table = 'posts_comments'


class PostsUsers(models.Model):
    post_id = models.AutoField(primary_key=True)
    username = models.CharField(blank=True, null=True)
    followers = models.CharField(blank=True, null=True)
    followings = models.CharField(blank=True, null=True)
    verified_unverfied = models.IntegerField(blank=True, null=True)
    dp_url = models.CharField(blank=True, null=True)
    posts_count = models.CharField(blank=True, null=True)
    joining_date = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Posts Users"
        managed = False
        db_table = 'posts_users'


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Students"
        managed = False
        db_table = 'students'
