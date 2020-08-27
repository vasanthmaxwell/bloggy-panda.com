
from django import forms
from tinymce import TinyMCE
from .models import Blog,Comments


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Blog
        fields = '__all__'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','comment')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'comment': forms.Textarea(attrs={'class':'form-control','id':'message','cols':30,'rows':10})
        }