from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
class takePhoto(forms.Form):
    buttonPressed = forms.BooleanField(label='buttonPressed')
# class buttonPress(forms.Form):
#     buttonPress = forms.BooleanField()