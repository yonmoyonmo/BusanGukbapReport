from .models import *
from django import forms


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report3
        fields = [
            'title', 'author', 'content',
            'open_close', 'phone', 'youtubelink', 'address']


class ImageForm(forms.ModelForm):
    class Meta:
        model = ReportImages
        fields = ['image', ]


class GukmoolForm(forms.ModelForm):
    class Meta:
        model = Gukmool
        fields = [
            'yuksu', 'yeomdo', 'hexColor',
            'saewoo', 'salt', 'blackPepper',
            'toRyeom', 'yangNyeomJang', 'ddaroGukbap',
            'NETgukbap',
        ]


class GoguiForm(forms.ModelForm):
    class Meta:
        model = Gogui
        fields = [
            'meatPart', 'texture', 'thickness',
            'smell', 'dippingSource', ]


class KimchiForm(forms.ModelForm):
    class Meta:
        model = Kimchi
        fields = [
            'spicy', 'banchan',
        ]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'banchanTime', 'gukbaptime', 'kindness',
            'banchanRefill', 'selfServing', 'gukmulRefill', 'dessert', ]


class WeesaengForm(forms.ModelForm):
    class Meta:
        model = Weesaeng
        fields = [
            'floor', 'table', 'spoons',
            'cups', 'kitchen', 'tissue', 'toilets', ]


class LatlngForm(forms.ModelForm):
    class Meta:
        model = Latlng
        fields = ['lat', 'lng']
