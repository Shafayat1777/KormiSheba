# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from app.models import Account, Services

class RegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2',)

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')
        
	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Credentials.")

                
class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('profile_pics','email', 'username','address', 'mobile_number', 'profile_pics' )

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

class AccountUpdateForm2(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username','address', 'mobile_number', 'profile_pics', 
                  'working_fields', 'experience',)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class ServicesForm(forms.ModelForm):
    
    class Meta:
        model = Services
        # fields = '__all__'
        fields = ('title', 'category', 'description', 'infoOfBuyer', 'images', 'price', 'deliveryTime')

    def __init__(self, *args, **kwargs):
            super(ServicesForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs = {'class': 'form-control'}
    
    def clean_title(self):
        title = self.cleaned_data['title'].lower()
        try:
             services = Services.objects.get(title=title)
        except Exception as e:
            return title
        raise forms.ValidationError(f"Title {title} is already in use.")  