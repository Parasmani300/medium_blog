from django import forms
from blog_app.models import Profile,Category,Post
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['topic',]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password','date_joined']
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','organisation','topic1','topic2','topic3']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','poster','content','status']

class UserUpdateInfoForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','first_name','last_name')