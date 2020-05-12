from .models import Report
from django import forms


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'author', 'content', 'fullshot', 'detailshot', 'menushot',
                  'youtubelink', 'lat', 'lng', 'location', 'gukmool', 'gogi', 'kimchi', 'service', 'weesaeng']
