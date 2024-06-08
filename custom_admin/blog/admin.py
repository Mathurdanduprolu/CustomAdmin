# blog/admin.py

from django.contrib import admin
from django import forms
from .models import Post, Comment

# Define the custom form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

# Define the custom action first
@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')

# Define inline model admin
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

# Register PostAdmin with the custom action and form
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'created_at', 'updated_at', 'status')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'status')
    actions = [make_published]
    inlines = [CommentInline]

# Register CommentAdmin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author', 'text')
    list_filter = ('created_at',)

# Custom Admin Site
from django.urls import path
from django.shortcuts import render
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'My Custom Admin'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('my_view/', self.admin_view(self.my_view))
        ]
        return custom_urls + urls

    def my_view(self, request):
        context = dict(
            self.each_context(request),
            key="value",
        )
        return render(request, 'admin/my_view.html', context)

admin_site = MyAdminSite(name='myadmin')

admin_site.register(Post, PostAdmin)
admin_site.register(Comment, CommentAdmin)
