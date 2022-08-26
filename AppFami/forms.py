from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    rutpersona = forms.CharField()
    genero = forms.CharField(max_length=1)
    fecnacimiento = forms.CharField(max_length=40)

class BuscaPersona(forms.Form):
    rutpersona = forms.IntegerField()
