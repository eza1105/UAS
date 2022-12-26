from django.forms import ModelForm
from django import forms
from MSY.models import *
 
class Fromdataikan(ModelForm,forms.Form):
    class Meta : 
        model = dataikan
        fields = '__all__'
        widgets ={
            'jenis_usaha'     :forms.TextInput({'class':'border  w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4','required':'required'}),
            'provinsi'        :forms.TextInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4','required':'required'}),
            'jenis_ikan'      : forms.TextInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4l','required':'required'}),
            'tahun'           : forms.NumberInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4l','required':'required'}),
            'trip'            : forms.NumberInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4l','required':'required'}),
            'ton'             : forms.NumberInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4l','required':'required'}),
        }

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['name', 'file']
        widgets = {
             'name' :  forms.TextInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4','required':'required'}),
        }


#         widgets ={
#             'nama' : forms.TextInput({
#                 'class':'border border-white block mb-4 rounded-lg text-gray/30 py-2 px-4', 'placeholder' : 'Nama Universitas', 'type' : 'text'
#                 }),
#             'lokasi' : forms.TextInput({
#                 'class':'border border-white block mb-4 rounded-lg text-gray/30 py-2 px-4', 'placeholder' : 'Lokasi Universitas', 'type' : 'text'
#                 }),
#             'prodi' : forms.TextInput({
#                 'class':'border border-white block mb-4 rounded-lg text-gray/30 py-2 px-4', 'placeholder' : 'Jumlah Prodi', 'type' : 'text'
#                 }),
#             'jenjang' : forms.TextInput({
#                 'class':'border border-white block mb-4 rounded-lg text-gray/30 py-2 px-4', 'placeholder' : 'Jenjang Universitas', 'type' : 'text'
#                 }),
#             'gambar' : forms.TextInput({
#                 'class':'border border-white block mb-4 rounded-lg text-gray/30 py-2 px-4', 'placeholder' : 'Logo Universitas', 'type' : 'text'
#                 }),
#         }