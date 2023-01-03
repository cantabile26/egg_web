# Generated by Django 3.2.8 on 2023-01-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('farm_code', models.IntegerField(verbose_name='농장 번호')),
                ('barn_code', models.CharField(max_length=10, unique=True, verbose_name='사업자 등록번호')),
                ('회계코드', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='회계코드')),
                ('계좌번호', models.IntegerField(unique=True, verbose_name='계좌번호')),
                ('출납일', models.DateTimeField(verbose_name='출납일')),
                ('발의일', models.DateTimeField(verbose_name='발의일')),
                ('결제일', models.DateTimeField(verbose_name='결제일')),
                ('등기일', models.DateTimeField(verbose_name='등기일')),
                ('결의구분', models.BooleanField(max_length=1, verbose_name='결의구분')),
                ('계정과목', models.CharField(max_length=256, verbose_name='계정과목')),
                ('적요', models.CharField(max_length=256, verbose_name='적요')),
                ('수입', models.IntegerField(verbose_name='수입')),
                ('지출', models.IntegerField(verbose_name='지출')),
                ('자금원천', models.CharField(max_length=256, verbose_name='자금원천')),
                ('정렬', models.CharField(max_length=256, verbose_name='정렬')),
                ('비고', models.CharField(max_length=256, verbose_name='비고')),
            ],
        ),
    ]
