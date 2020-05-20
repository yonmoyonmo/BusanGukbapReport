from .models import Report2
from django import forms


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report2
        fields = ['thumbnail', 'title', 'author', 'content', 'fullshot', 'fullshot_caption', 'detailshot', 'detailshot_caption', 'menushot', 'menushot_caption',
                  'youtubelink', 'lat', 'lng', 'location', 'gukmool', 'gogi', 'kimchi', 'service', 'weesaeng']
