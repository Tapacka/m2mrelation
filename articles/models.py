from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering= ['name']

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tags, related_name = 'tags', through='TagsArticle')
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class TagsArticle(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.DO_NOTHING, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, related_name='scopes')
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering= ['-is_main']


