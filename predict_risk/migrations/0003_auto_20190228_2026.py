

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk', '0002_auto_20190228_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='cp',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Angina'), (4, 'Asymptomatic')], default=0),
        ),
    ]
