

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(0, 'Female'), (1, 'Male')], default=0)),
                ('cp', models.IntegerField(choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Angina'), (4, 'Asymptomatic')], default=1)),
                ('resting_bp', models.IntegerField()),
                ('serum_cholesterol', models.IntegerField()),
                ('fasting_blood_sugar', models.IntegerField(choices=[(1, 'true'), (2, 'false')], default=0)),
                ('resting_ecg', models.IntegerField(choices=[(0, 'Normal'), (1, 'Having ST-T wave abnormality'), (2, 'hypertrophy')], default=0)),
                ('max_heart_rate', models.IntegerField()),
                ('exercise_induced_angina', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('st_depression', models.DecimalField(decimal_places=2, max_digits=4)),
                ('st_slope', models.IntegerField(choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Down Sloping')])),
                ('number_of_vessels', models.IntegerField(choices=[(0, 'None'), (1, 'One'), (2, 'Two'), (3, 'Three')])),
                ('thallium_scan_results', models.IntegerField(choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')])),
                ('predicted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('num', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predict', to='accounts.UserProfileInfo')),
            ],
        ),
    ]
