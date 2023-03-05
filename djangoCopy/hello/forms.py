from django import forms
# from django import models

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class takePhoto(forms.Form):
    buttonPressed = forms.BooleanField(label='buttonPressed')

class UserDistanceValue(forms.Form):
    distance = forms.IntegerField(label='distance')

# class saveImage(forms.Form):
#     image = models.ImageField(upload_to= )

# class buttonPress(forms.Form):
#     buttonPress = forms.BooleanField()




# ACTION_CHOICES= (

# )

# class Upload(models.Model):
#     image = models.ImageField(upload_to='images')
#     action = models.CharField(max_length=50, choices=ACTION_CHOICES)

#     def save(self, *args, **kwargs)