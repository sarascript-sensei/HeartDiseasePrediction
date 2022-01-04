from django.db import models
from accounts.models import UserProfileInfo
from django.utils import timezone
from django.urls import reverse


sex_choices=((0, 'Женский'),(1, 'Мужской'))
cp_choice=((0,'Нет'),(1, 'Типичная стенокардия'),(2, 'Атипичная стенокардия'),(3, 'Отсутсвие стенокардии'),(4, 'Отсутсвие симптомов'))
fasting_blood_sugar_choices=((1,'> 120 мг/дл'),((0,'< 120 мг/дл')))
resting_ecg_choices=((0, 'Норма'),(1, 'Наличие аномалии зубца ST-T'),(2, 'Гипертрофия'))
exercise_induced_angina_choices=((0, 'Нет'),(1, 'Да'))
st_slope_choices=((1, 'Нарастающий'),(2, 'Ровный'),(3, 'Понижающий'))
number_of_vessels_choices=((0, 'Нет'),(1, 'Один'),(2, 'Два'),(3, 'Три'))
thallium_scan_results_choices=((3, 'Норма'),(6, 'Исправлен дефект'),(7, 'Обратимый дефект'))

class Predictions(models.Model):
    profile = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='predict')
    age = models.IntegerField()
    sex = models.IntegerField(choices=sex_choices, default=0)
    cp = models.IntegerField(choices=cp_choice,default=0)
    resting_bp = models.IntegerField()
    serum_cholesterol = models.IntegerField()
    fasting_blood_sugar = models.IntegerField(choices=fasting_blood_sugar_choices,default=0)
    resting_ecg = models.IntegerField(choices=resting_ecg_choices,default=0)
    max_heart_rate = models.IntegerField()
    exercise_induced_angina = models.IntegerField(choices=exercise_induced_angina_choices,default=0)
    st_depression = models.DecimalField(max_digits=4, decimal_places=2)
    st_slope = models.IntegerField(choices=st_slope_choices)
    number_of_vessels = models.IntegerField(choices=number_of_vessels_choices)
    thallium_scan_results = models.IntegerField(choices=thallium_scan_results_choices)
    predicted_on = models.DateTimeField(default=timezone.now)
    num=models.IntegerField()

    def get_absolute_url(self):
        return reverse('predict:predict', kwargs={'pk': self.profile.pk})
