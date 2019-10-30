from django import forms

from presenca.models import Materia
    
class MateriaForm(ModelForm):
	class Meta:
		model = Materia
		fields = '__all__'
