from django.db import models

class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class caretaker(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class user(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    relation=models.CharField(max_length=200)
    patient_name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    medical_history=models.CharField(max_length=200)
    house=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class photos(models.Model):
    date=models.CharField(max_length=200)
    photo=models.CharField(max_length=200)
    program_name=models.CharField(max_length=200)

class suggestion(models.Model):
    date=models.CharField(max_length=200)
    suggestions=models.CharField(max_length=200)
    CARETAKER=models.ForeignKey(caretaker,default=1,on_delete=models.CASCADE)

class donation(models.Model):
    date=models.CharField(max_length=200)
    items=models.CharField(max_length=200)
    count=models.CharField(max_length=200)

class reports(models.Model):
    date=models.CharField(max_length=200)
    details=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class caretaker_reuqest(models.Model):
    date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    CARETAKER=models.ForeignKey(caretaker,default=1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class donation_request(models.Model):
    date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    DONATION=models.ForeignKey(donation,default=1,on_delete=models.CASCADE)

class medicine_request(models.Model):
    date=models.CharField(max_length=200)
    statuss=models.CharField(max_length=200)
    medicine=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    CARETAKER=models.ForeignKey(caretaker,default=1,on_delete=models.CASCADE)

class sponsorship(models.Model):
    patient=models.CharField(max_length=200)
    medical_history=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    need=models.CharField(max_length=200)
    house_name=models.CharField(max_length=200)
    postal=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)


class sponsorship_request(models.Model):
    date=models.CharField(max_length=200)
    statuss=models.CharField(max_length=200)
    detailss=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    SPONSORSHIP=models.ForeignKey(sponsorship,default=1,on_delete=models.CASCADE)

class reminder(models.Model):
    date=models.CharField(max_length=200)
    reminder=models.CharField(max_length=200)
    reminder_date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
