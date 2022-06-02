from django import forms

from .models import Product, Bowl,Desayuno,Almuerzo,Handroll,HandrollReady

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price',)

class BowlForm(forms.ModelForm):

    class Meta:
        model = Bowl
        fields = ('proteina', 'base','salsa1','salsa2','extra1','extra2','extra3',
        'extra4','extra5','extra6','extra7','extra8','extra9','extra10')


class DesayunoForm(forms.ModelForm):

    class Meta:
        model = Desayuno
        fields = ('queso', 'proteina','vegetal1','vegetal2')

class AlmuerzoForm(forms.ModelForm):

    class Meta:
        model = Almuerzo
        fields = ('proteina', 'agregado')

class HandrollForm(forms.ModelForm):

    class Meta:
        model = Handroll
        fields = ('proteina1','proteina2','proteina3','vegetal1','vegetal2','vegetal3')



# admin.site.register(models.Handroll)
# admin.site.register(models.ProteinaHandroll)
# admin.site.register(models.VegetalesHandroll)
# admin.site.register(models.HandrollReady)
# admin.site.register(models.Kai)
# admin.site.register(models.CorteKai)
# admin.site.register(models.ExtraKai)
# admin.site.register(models.Selladitas)
