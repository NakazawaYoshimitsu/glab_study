#-----------------------------------------------------------------------
#	bihin アプリケーションのmodels
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
from django.db import models

# Create your models here.

PCTYPE_CHOICES = (
    (0, 'ノートパソコン'),
    (1, 'デスクトップパソコン' )
)
SHISAN_CHOICES = (
    (0, '購入品'),
    (1, 'リース' )
)
STATUS_CHOICES = (
    (0, '保管棚'),
    (1, '貸出中'),
    (2, '廃棄'),
)

#-----------------------------------------------------------------------
#	Bihin：
#   Bihin DB のモデルを定義する.
#-----------------------------------------------------------------------
class Bihin(models.Model):
    """備品"""
    bihin_no = models.CharField('管理No', max_length=255)
    bihin_type = models.IntegerField('種別', choices=PCTYPE_CHOICES)
    bihin_manufct = models.CharField('メーカー', max_length=255)
    bihin_name = models.CharField('名称', max_length=255)
    bihin_shisan = models.IntegerField('資産', choices=SHISAN_CHOICES)
    bihin_date = models.DateField('登録日')
    bihin_sts = models.IntegerField('状態', choices=STATUS_CHOICES)
    bihin_text = models.TextField('備考', null=True)

