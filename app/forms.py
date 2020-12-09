"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length = 2, max_length = 50)
    auto = forms.CharField(label='Напишите марку вашего авто', min_length = 1, max_length = 100)
    service = forms.ChoiceField(label='Оцените качество работы сервиса',
                                choices=(('1','Отлично'),
                                         ('2','Хорошо'),
                                         ('3','Среднее'),
                                         ('4','Ужасно')), initial=1)
    feedback = forms.CharField(label='Ваш отзыв',
                              widget=forms.Textarea(attrs={'rows':12,'cols':20}))
    email = forms.EmailField(label='Ваш e-mail', min_length = 5)
    repeat = forms.ChoiceField(label='Обратитесь к нам еще раз?',
                               choices=(('1','Да'),
                                         ('2','Нет')), initial=1)
    consent = forms.BooleanField(label='Я согласен на отправку моего отзыва', required=True)

class CommentForm (forms.ModelForm):

    class Meta:

        model = Comment # используемая модель

        fields = ('text',) # требуется заполнить только поле text

        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','image')
        labels = {'title': "Заголовок",'description': "Краткое содержание",'content': "Полное содержание",'image': "Изображение"}