

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='fasting_blood_sugar',
            field=models.IntegerField(choices=[(1, '> 120 mg/dl'), (0, '< 120 mg/dl')], default=0),
        ),
    ]
