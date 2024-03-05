import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from door_of_hope_app.models import *


def admin_index(request):
    return render(request,"ADMIN/admin_index.html")
def caretaker_index(request):
    return render(request,"CARETAKER/caretaker_index.html")


def loginform(request):
    return render(request,"index.html")

def login_view_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']

    credential=login.objects.filter(username=username,password=password)
    if credential.exists():
        request.session['log'] = "lo"  # logout
        request.session['lid'] = credential[0].id
        if credential[0].usertype=="admin":
            return HttpResponse("<script>alert('login');window.location='/admin_index'</script>")
        elif credential[0].usertype=="caretaker":
            return HttpResponse("<script>alert('login');window.location='/caretaker_index'</script>")
        elif credential[0].usertype=="volunteer":
            return HttpResponse("<script>alert('login');window.location='/caretaker_index'</script>")
        elif credential[0].usertype=="user":
            return HttpResponse("<script>alert('login');window.location='/user_homepage_view'</script>")
        else:
            return HttpResponse("<script>alert('invalid credentail');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('no such user');window.location='/'</script>")


def change_admin_password_view(request):
    return render(request,"ADMIN/change_password_admin.html")
def change_admin_password_view_post(request):
    current=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']
    p=login.objects.filter(id=1)
    if current==p[0].password:
        if new==confirm:
            login.objects.filter(id=1).update(password=new)
            return HttpResponse("<script>alert('changed');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('mismatch password');window.location='/change_admin_password_view"+"#aa'</script>")
    else:
        return HttpResponse("<script>alert('not found');window.location='/change_admin_password_view"+"#aa'</script>")


def admin_homepage_view(request):
    return render(request,"ADMIN/admin_homepage.html")

def caretaker_homepage_view(request):
    return render(request,"CARETAKER/caretaker_homepage.html")

def user_homepage_view(request):
    return render(request,"USER/user_homepage.html")


def add_caretaker_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"ADMIN/add_caretaker.html")

def add_caretaker_view_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    plac=request.POST['textfield4']
    password=request.POST['textfield5']
    type=request.POST['textfield6']
    image=request.FILES['fileField']
    d=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\door_of_hope\door_of_hope_app\static\photos\\"+d+'.jpg',image)
    path="/static/photos/"+d+'.jpg'
    i=caretaker.objects.filter(name=name,type=type)
    if i.exists():
        return HttpResponse("<script>alert('already registered');window.location='/add_caretaker_view" + "#aa'</script>")
    else:
        obj = login()
        obj.username = email
        obj.password = password
        obj.usertype = type
        obj.save()

        obj1 = caretaker()
        obj1.name = name
        obj1.email = email
        obj1.phone = phone
        obj1.place = plac
        obj1.image = path
        obj1.type = type
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('Registered');window.location='/view_caretaker" + "#aa'</script>")


def view_caretaker(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker.objects.all()
    return render(request,"ADMIN/view_caretaker.html",{"data":res})


def update_caretaker_view(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker.objects.get(id=id)
    return render(request,"ADMIN/update_caretaker.html",{"data":res,"id":id})

def update_caretaker_view_post(request,id):
    try:
        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        name1 = request.POST['textfield']
        email1 = request.POST['textfield2']
        phone1 = request.POST['textfield3']
        place1 = request.POST['textfield4']
        type1 = request.POST['textfield6']
        image1 = request.FILES['fileField']
        fs = FileSystemStorage()
        fs.save(r"C:\Users\amaya\PycharmProjects\door_of_hope\door_of_hope_app\static\photos\\" + d + '.jpg', image1)
        path1 = "/static/photos//" + d + '.jpg'
        caretaker.objects.filter(id=id).update(name=name1, place=place1, email=email1, phone=phone1, image=path1,type=type1)
        return HttpResponse("<script>alert('updated');window.location='/view_caretaker"+"#aa'</script>")
    except Exception as e:
        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        name1 = request.POST['textfield']
        email1 = request.POST['textfield2']
        phone1 = request.POST['textfield3']
        place1 = request.POST['fileField']
        type1 = request.POST['textfield6']
        caretaker.objects.filter(id=id).update(name=name1, place=place1, email=email1, phone=phone1,type=type1)
        return HttpResponse("<script>alert('updated');window.location='/view_caretaker"+"#aa'</script>")

def delete_caretaker(request,id):
    caretaker.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_caretaker"+"#aa'</script>")


def view_user(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=user.objects.all()
    return render(request,"ADMIN/view_user.html",{"data":res})

def need_donation_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"ADMIN/needs_donation.html")

def need_donation_view_post(request):
    items=request.POST['textfield']
    count=request.POST['textfield2']
    d=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    i=donation.objects.filter(items=items)
    if i.exists():
        return HttpResponse("<script>alert('alredy in donation');window.location='/need_donation_view#aa'</script>")
    else:
        obj = donation()
        obj.items = items
        obj.count = count
        obj.date=d
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_donation'</script>")


def view_donation(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=donation.objects.all()
    return render(request,"ADMIN/view_donation.html",{"data":res})

def update_needs_donation_view(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=donation.objects.get(id=id)
    return render(request,"ADMIN/update_donation.html",{"data":res})

def update_needs_donation_view_post(request,id):
    item1=request.POST['textfield']
    count=request.POST['textfield2']
    donation.objects.filter(id=id).update(items=item1,count=count)
    return HttpResponse("<script>alert('updated');window.location='/view_donation"+"#aa'</script>")

def delete_needs_donation(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    donation.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_donation"+"#aa'</script>")


def view_donation_history(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=donation_request.objects.all()
    return render(request,"ADMIN/view_donation_history.html",{"data":res})



def view_suggestion(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=suggestion.objects.all()
    return render(request,"ADMIN/view_suggestion.html",{"data":res})

def add_photos_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"ADMIN/add_prgrm_photo.html")

def add_photos_view_post(request):
    program_name=request.POST['textfield']
    photo=request.FILES['fileField']
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\door_of_hope\door_of_hope_app\static\photos\\"+d+'.jpg',photo)
    path="/static/photos//"+d+'.jpg'
    i=photos.objects.filter(program_name=program_name,photo=path)
    if i.exists():
        return HttpResponse("<script>alert('already in photos');window.location='/add_photos_view" + "#aa'</script>")
    else:
        obj = photos()
        obj.program_name = program_name
        obj.photo = path
        obj.date = d
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_photos" + "#aa'</script>")

def view_photos(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=photos.objects.all()
    return render(request,"ADMIN/view_photos.html",{"data":res})

def update_photos_view(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=photos.objects.get(id=id)
    return render(request,"ADMIN/update_photos.html",{"data":res})

def update_photos_view_post(request,id):
   try:
       program_name = request.POST['textfield']
       photo = request.FILES['fileField']
       d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
       fs = FileSystemStorage()
       fs.save(r"C:\Users\amaya\PycharmProjects\door_of_hope\door_of_hope_app\static\photos\\" + d + '.jpg', photo)
       path = "/static/photos//" + d + '.jpg'
       photos.objects.filter(id=id).update(program_name=program_name, photo=path)
       return HttpResponse("<script>alert('updated');window.location='/view_photos"+"#aa'</script>")

   except Exception as e:
       program_name = request.POST['textfield']
       photos.objects.filter(id=id).update(program_name=program_name)
       return HttpResponse("<script>alert('updated');window.location='/view_photos"+"#aa'</script>")


def delete_photos(request,id):
    photos.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted);window.location='/view_photos"+"#aa'</script>")







def add_sponsorship_view(request):
    return render(request,"ADMIN/add_sponsorship.html")

def add_sponsorship_view_post(request):
    patient=request.POST['textfield']
    medical_history=request.POST['textarea']
    house_name=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    needs=request.POST['textfield6']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    i=sponsorship.objects.filter(patient=patient,need=needs)
    if i.exists():
        return HttpResponse("<script>alert('alredy in sponsorship');window.location='/add_sponsorship_view" + "#aa'</script>")
    else:
        obj = sponsorship()
        obj.date = d
        obj.medical_history = medical_history
        obj.patient = patient
        obj.house_name = house_name
        obj.postal = post
        obj.pin = pin
        obj.need = needs
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_sponsorship" + "#aa'</script>")



def view_sponsorship(request):
    res=sponsorship.objects.all()
    return render(request,"ADMIN/view_sponsorship.html",{"data":res})

def update_sponsorship_view(request,id):
    res=sponsorship.objects.get(id=id)
    return render(request,"ADMIN/update_sponsership.html",{"data":res})

def update_sponsorship_view_post(request,id):
    patient = request.POST['textfield']
    medical_history = request.POST['textarea']
    house_name = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    needs = request.POST['textfield6']
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    sponsorship.objects.filter(id=id).update(date=d,medical_history=medical_history,patient=patient,house_name=house_name,postal=post,pin=pin,need=needs)
    return HttpResponse("<script>alert('updated');window.location='/view_sponsorship"+"#aa'</script>")


def delete_sponsorship(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    sponsorship.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_sponsorship"+"#aa'</script>")



def view_sponsorship_request(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=sponsorship_request.objects.all()
    return render(request,"ADMIN/view_sponsorship_request.html",{"data":res})

def approve_sponsorship(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    sponsorship_request.objects.filter(id=id).update(statuss="approved")
    return HttpResponse("<script>alert('approved');window.location='/view_sponsorship_request"+"#aa'</script>")

def reject_sponsorship(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    sponsorship_request.objects.filter(id=id).update(statuss="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_sponsorship_request"+"#aa'</script>")


def view_medicine_request(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=medicine_request.objects.all()
    return render(request,"ADMIN/view_medicine_request.html",{"data":res})


def approve_medicine_request(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    medicine_request.objects.filter(id=id).update(statuss="approved")
    return HttpResponse("<script>alert('approved');window.location='/view_medicine_request"+"#aa'</script>")

def reject_medicine_request(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    medicine_request.objects.filter(id=id).update(statuss="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_medicine_request"+"#aa'</script>")





def view_request_for_caretaker(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker_reuqest.objects.filter(type="caretaker")
    return render(request,"ADMIN/view_request_for_caretaker.html",{"data":res})

def approve_caretaker_view(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker.objects.filter(type="caretaker")
    return render(request,"ADMIN/list_caretaker.html",{"data":res, 'id':id})

def approve_caretaker_view_post(request,cid,rid):
    caretaker_reuqest.objects.filter(id=rid).update(CARETAKER_id=cid,status="approved")
    return HttpResponse("<script>alert('approve');window.location='/view_request_for_caretaker"+"#aa'</script>")


def reject_caretaker(request,id):
    caretaker_reuqest.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_request_for_caretaker"+"#aa'</script>")


def view_request_for_volunteer(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker_reuqest.objects.filter(type="volunteer")
    return render(request,"ADMIN/view_volunteer_request.html",{"data":res})

def approve_volunteer(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker.objects.filter(type="volunteer")
    return render(request,"ADMIN/list_volunteer.html",{"data":res,"id":id})

def approve_volunteer_post(request,rid,vid):
    caretaker_reuqest.objects.filter(id=rid).update(CARETAKER_id=vid,status="approved")
    return HttpResponse("<script>alert('Approve');window.location='/view_request_for_volunteer"+"#aa'</script>")


def reject_volunteer(request,id):
    caretaker_reuqest.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('Rejected');window.location='/view_request_for_volunteer"+"#aa'</script>")



def view_requested_user_reports(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker_reuqest.objects.filter(status="approved")
    return render(request,"ADMIN/view_requested_user_and_reports.html",{"data":res})

def view_report(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=reports.objects.filter(USER=id)
    return render(request,"ADMIN/view_reports.html",{"data":res})



#######################################################################################################

def change_caretaker_password_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"CARETAKER/change_password_caretaker.html")

def change_caretaker_password_view_post(request):
    current=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']
    p=login.objects.filter(id=request.session['lid'])
    if current==p[0].password:
        if new==confirm:
            login.objects.filter(id=request.session['lid']).update(password=new)
            return HttpResponse("<script>alert('changed');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('mismatch password');window.location='/change_caretaker_password_view"+"#cc'</script>")
    else:
        return HttpResponse("<script>alert('not found');window.location='/change_caretaker_password_view"+"#cc'</script>")


def patients_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=caretaker_reuqest.objects.filter(CARETAKER__LOGIN=request.session['lid'])
    return render(request,"CARETAKER/view_patients.html",{"data":res})

def add_daily_report_view(request,uid):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    uid=uid
    return render(request,"CARETAKER/add_daily_reports.html",{"uid":uid})

def add_daily_report_view_post(request,uid):
    details=request.POST['textfield']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    i=reports.objects.filter(details=details,USER=user.objects.get(id=uid))
    if i.exists():
        return HttpResponse("<script>alert('added');window.location='/patients_view" + "#cc'</script>")
    else:
        obj = reports()
        obj.details = details
        obj.date = d
        obj.USER = user.objects.get(id=uid)
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/patients_view" + "#cc'</script>")

def view_daily_report(request,uid):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=reports.objects.filter(USER=uid)
    return render(request,"CARETAKER/view_daily_reports.html",{"data":res})

def update_daily_report_view(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=reports.objects.get(id=id)
    return render(request,"CARETAKER/update_daily_report.html",{"data":res})

def update_daily_report_view_post(request,id):
    details=request.POST['textfield']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    reports.objects.filter(id=id).update(details=details)
    return HttpResponse("<script>alert('updated');window.location='/patients_view'</script>")


def delete_daily_report(request,id):
    reports.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/patients_view'</script>")





def send_medicine_request_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"CARETAKER/send_medicine_request.html")

def send_medicine_request_view_post(request):
    medicine=request.POST['textfield2']
    quantity=request.POST['textfield']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    obj=medicine_request()
    obj.CARETAKER = caretaker.objects.get(LOGIN=request.session['lid'])
    obj.medicine=medicine
    obj.quantity=quantity
    obj.statuss="pending"
    obj.date=d
    obj.save()
    return HttpResponse("<script>alert('requested');window.location='/view_medicine_status"+"#cc'</script>")

def view_medicine_status(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=medicine_request.objects.filter(CARETAKER__LOGIN=request.session["lid"])
    return render(request,"CARETAKER/view_medicine_status.html",{"data":res})


def add_suggestion_view(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"CARETAKER/add_suggestion.html")

def add_suggestion_view_post(request):
    suggestion1=request.POST['textfield']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    i=suggestion.objects.filter(suggestions=suggestion1)
    if i.exists():
        return HttpResponse("<script>alert('alredy added');window.location='/add_suggestion_view" + "#cc'</script>")
    else:
        obj = suggestion()
        obj.suggestions = suggestion1
        obj.date = d
        obj.CARETAKER = caretaker.objects.get(LOGIN=request.session["lid"])
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_suggestions" + "#cc'</script>")


def view_suggestions(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=suggestion.objects.filter(CARETAKER__LOGIN=request.session['lid'])
    return render(request,"CARETAKER/view_suggestions.html",{"data":res})

def update_suggestion_view(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=suggestion.objects.get(id=id)
    return render(request,"CARETAKER/update_suggestion.html",{"data":res})


def update_suggestion_post(request,id):
    sugg=request.POST['textfield']
    suggestion.objects.filter(id=id).update(suggestions=sugg)
    return HttpResponse("<script>alert('updated');window.location='/view_suggestions"+"#cc'</script>")


def delete_suggestion(request,id):
    suggestion.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_suggestions"+"#cc'</script>")


def reminder_setting_view(request,uid):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    uid=uid
    return render(request,"CARETAKER/reminder_setting.html",{"uid":uid})

def reminder_setting_view_post(request,uid):

    reminder1=request.POST['textfield']
    reminder_date=request.POST['textfield2']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    i=reminder.objects.filter(reminder=reminder1)
    if i.exists():
        return HttpResponse("<script>alert('already added');window.location='/patients_view" + "#cc'</script>")
    else:
        obj = reminder()
        obj.reminder = reminder1
        obj.reminder_date = reminder_date
        obj.date = d
        obj.USER = user.objects.get(id=uid)
        print(obj.USER)
        obj.save()
        return HttpResponse("<script>alert('reminder added');window.location='/patients_view" + "#cc'</script>")



def view_reminder(request,uid):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=reminder.objects.filter(USER=uid)
    return render(request,"CARETAKER/view_reminder.html",{"data":res})

def update_reminder(request,id):
    res=reminder.objects.get(id=id)
    return render(request,"CARETAKER/update_reminder.html",{"data":res})

def update_reminder_post(request,id):
    reminders=request.POST['textfield']
    reminders_date=request.POST['textfield2']
    # d=datetime.datetime.now().strftime("%Y-%m-%d")
    reminder.objects.filter(id=id).update(reminder=reminders,reminder_date=reminders_date)
    return HttpResponse("<script>alert('updated');window.location='/patients_view" + "#cc'</script>")


def delete_reminder(request,id):
    reminder.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/patients_view" + "#cc'</script>")

def logout(request):
    request.session['log']=""
    request.session.clear()
    return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")


###############################################################0###################################################################################

def user_login(request):
    unme=request.POST['username']
    pswd=request.POST['password']
    data=login.objects.filter(username=unme,password=pswd,usertype="user")
    if data.exists():
        return JsonResponse({"status":"ok","id":data[0].id})

    return JsonResponse({"status":"no"})

def user_register(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    patient_name=request.POST['Patient_name']
    relation=request.POST['relation']
    age=request.POST['age']
    medical=request.POST['medical']
    post=request.POST['post']
    pin=request.POST['pin']
    place=request.POST['place']
    passw=request.POST['password']

    i=user.objects.filter(name=name,email=email)
    if i.exists():
        return JsonResponse({"status": "no"})
    else:
        obj=login()
        obj.username=email
        obj.password=passw
        obj.usertype="user"
        obj.save()

        obj1=user()
        obj1.name=name
        obj1.email=email
        obj1.phone=contact
        obj1.patient_name=patient_name
        obj1.relation=relation
        obj1.age=age
        obj1.medical_history=medical
        obj1.post=post
        obj1.pincode=pin
        obj1.house=place
        obj1.LOGIN=obj
        obj1.save()
        return JsonResponse({"status":"ok"})

def caretaker_request(request):
    type=request.POST['type']
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN=lid)
    i=caretaker_reuqest.objects.filter(type=type,USER=uid)
    if i.exists():
        return JsonResponse({"status": "no"})
    else:
        obj=caretaker_reuqest()
        obj.date=datetime.datetime.now().strftime("%Y/%m/%d")
        obj.status="pending"
        obj.type=type
        obj.USER=uid
        obj.save()
        return JsonResponse({"status":"ok"})

def caretaker_request_status(request):
    lid=request.POST['lid']
    res=caretaker_reuqest.objects.filter(USER=user.objects.get(LOGIN=lid))
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "status":i.status,
                "type":i.type,
                "caretaker":i.CARETAKER.name,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def view_sponsorships(request):
    res=sponsorship.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "patient":i.patient,
                "medical_history":i.medical_history,
                "date":i.date,
                "need":i.need,
                "house_name":i.house_name,
                "postal":i.postal,
                "pin":i.pin,
            }
        )

    return JsonResponse({"status":"ok","data":data})

def send_sponsorship_request(request):
    lid=request.POST['lid']
    details=request.POST['details']
    sid=request.POST['sid']
    uid=user.objects.get(LOGIN=lid)
    i=sponsorship_request.objects.filter(USER=uid,detailss=details,SPONSORSHIP_id=sid)
    if i.exists():
        return JsonResponse({"status": "no"})
    else:
        obj=sponsorship_request()
        obj.date=datetime.datetime.now().strftime("%Y/%m/%d")
        obj.USER=uid
        obj.detailss=details
        obj.statuss="pending"
        obj.SPONSORSHIP_id=sid
        obj.save()
        return JsonResponse({"status":"ok"})

def view_sponsorship_requests(request):
    lid=request.POST['lid']
    res=sponsorship_request.objects.filter(USER__LOGIN=lid)
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "status":i.statuss,
                "detailss":i.detailss,
                "need":i.SPONSORSHIP.need,


            }
        )


    return JsonResponse({"status":"ok","data":data})

def view_Donation(request):
    res=donation.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "items":i.items,
                "count":i.count,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def send_donation_requests(request):
    lid = request.POST['lid']
    did = request.POST['did']
    uid = user.objects.get(LOGIN=lid)
    obj=donation_request()
    obj.date=datetime.datetime.now().strftime("%Y/%m/%d")
    obj.USER=uid
    obj.DONATION_id=did
    obj.save()
    return JsonResponse({"status":"ok"})

def view_user_photos(request):
    res=photos.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "program_name":i.program_name,
                "photo":i.photo,
            }
        )

    return JsonResponse({"status":"ok","data":data})

def view__user_reports(request):
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN=lid)
    res=reports.objects.filter(USER=uid)
    data=[]
    for i in res:
        data.append({
            "date":i.date,
            "details":i.details

        })
    return JsonResponse({"status":"ok","data":data})

def view_user_reminder(request):
    lid = request.POST['lid']
    uid = user.objects.get(LOGIN=lid)
    res=reminder.objects.filter(USER=uid)
    data=[]
    for i in res:
        data.append({
            "date":i.date,
            "reminder":i.reminder,
            "reminder_date":i.reminder_date
        })
    return JsonResponse({"status":"ok","data":data})


###############################################################################################################################

def public_sponsorship(request):
    res=sponsorship.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "date": i.date,
                "patient":i.patient,
                "medical_history":i.medical_history,
                "need":i.need,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def public_volunteer(request):
    res=caretaker.objects.filter(type="volunteer")
    data=[]
    for i in res:
        data.append(
            {
                "image":i.image,
                "name":i.name,
            }
        )

    return JsonResponse({"status":"ok","data":data})