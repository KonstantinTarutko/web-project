from django import forms
from .models import Post, Category


# categories = [('Personal', 'Personal'),
#           ('Family', 'Family'),
#           ('Business', 'Business'),
#           ('Relationships', 'Relationships')]

categories = Category.objects.all().values_list('name', 'name')

category_list = []

for object in categories:
    category_list.append(object)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Create article name', 'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your text', 'class': 'form-control'}),
        }


class ProposePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Create article name', 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'form-control', 'id': 'propose'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your text', 'class': 'form-control'}),
        }
