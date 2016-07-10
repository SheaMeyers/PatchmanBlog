from django import forms

from .models import Post, Reply

from nocaptcha_recaptcha.fields import NoReCaptchaField

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')


class ReplyForm(forms.ModelForm):
    captcha = NoReCaptchaField()

    class Meta:
        model = Reply
        fields = ('name', 'email', 'content')
