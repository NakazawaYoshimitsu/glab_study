#-----------------------------------------------------------------------
#	bihin アプリケーションのform
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
from django.forms import ModelForm
from bihin.models import Bihin

# Create your views here.

#-----------------------------------------------------------------------
#	BihinForm：
#   備品登録/編集にて起動される.
#   Formを作成する.
#-----------------------------------------------------------------------
class BihinForm(ModelForm):
    """備品のフォーム"""
    class Meta:
        model = Bihin
        fields = (
            'bihin_no',
            'bihin_type',
            'bihin_manufct',
            'bihin_name',
            'bihin_shisan',
            'bihin_date',
            'bihin_sts',
            'bihin_text')
#class Bihin__(models.Model):
#    bihin_no = models.CharField(max_length=100)
#    bihin_name = models.CharField(max_length=100)
#    bihin_text = models.CharField(max_length=100)
#    bihin_date = models.DateField(blank=True, null=True)
#
#class BihinForm(ModelForm):
#    class Meta:
#        model = Bihin
#        fields = ('bihin_no', 'bihin_name', 'bihin_text', 'bihin_date')

