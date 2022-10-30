from django.db import models

STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Arunachal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(choices= STATE_CHOICE,max_length=50)
    pin = models.PositiveIntegerField()
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile_img', blank=True)
    resume = models.FileField(upload_to='resume', blank=True)

    class Meta:
        ordering = ('-id',)
