from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, TagsArticle


class TagsArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        l=[]
        for form in self.forms:            
            if True in form.cleaned_data.values():                       
                l.append(form.cleaned_data['is_main'])           
        if True not in l:
            raise ValidationError('выберите главный тег')
        else:
            pass
        return super().clean()


class TagsArticleInline(admin.TabularInline):
    model = TagsArticle
    formset = TagsArticleInlineFormset
    


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsArticleInline]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
    