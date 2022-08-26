from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    rutpersona = forms.IntegerField()
    genero = forms.CharField(max_length=1)
    fecnacimiento = forms.CharField(max_length=40)

class HijoForm(forms.Form):
    rutperosna = forms.IntegerField()
    ruthijo = forms.IntegerField()

class PadreForm(forms.Form):
    rutperosna = forms.IntegerField()
    rutpadre = forms.IntegerField()

class BuscaPersona(forms.Form):
    rutpersona = forms.IntegerField()
