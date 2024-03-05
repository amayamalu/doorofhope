"""door_of_hope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from door_of_hope_app import  views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin_index',views.admin_index),
    path('caretaker_index',views.caretaker_index),
    path('',views.loginform),
    path('login_view_post',views.login_view_post),
    path('admin_homepage_view',views.admin_homepage_view),
    path('caretaker_homepage_view',views.caretaker_homepage_view),
    path('user_homepage_view',views.user_homepage_view),
    path('add_caretaker_view',views.add_caretaker_view),
    path('add_caretaker_view_post',views.add_caretaker_view_post),
    path('view_caretaker',views.view_caretaker),
    path('update_caretaker_view/<id>',views.update_caretaker_view),
    path('update_caretaker_view_post/<id>',views.update_caretaker_view_post),
    path('delete_caretaker/<id>',views.delete_caretaker),
    path('view_user',views.view_user),
    path('need_donation_view',views.need_donation_view),
    path('need_donation_view_post',views.need_donation_view_post),
    path('view_donation',views.view_donation),
    path('update_needs_donation_view/<id>',views.update_needs_donation_view),
    path('update_needs_donation_view_post/<id>',views.update_needs_donation_view_post),
    path('delete_needs_donation/<id>',views.delete_needs_donation),
    path('view_suggestion',views.view_suggestion),
    path('add_photos_view',views.add_photos_view),
    path('add_photos_view_post',views.add_photos_view_post),
    path('view_photos',views.view_photos),
    path('update_photos_view/<id>',views.update_photos_view),
    path('update_photos_view_post/<id>',views.update_photos_view_post),
    path('delete_photos/<id>',views.delete_photos),
    path('add_sponsorship_view',views.add_sponsorship_view),
    path('add_sponsorship_view_post',views.add_sponsorship_view_post),
    path('view_sponsorship',views.view_sponsorship),
    path('update_sponsorship_view/<id>',views.update_sponsorship_view),
    path('update_sponsorship_view_post/<id>',views.update_sponsorship_view_post),
    path('delete_sponsorship/<id>',views.delete_sponsorship),
    path('view_sponsorship_request',views.view_sponsorship_request),
    path('approve_sponsorship/<id>',views.approve_sponsorship),
    path('reject_sponsorship/<id>',views.reject_sponsorship),
    path('view_donation_history',views.view_donation_history),
    path('view_medicine_request',views.view_medicine_request),
    path('approve_medicine_request/<id>',views.approve_medicine_request),
    path('reject_medicine_request/<id>',views.reject_medicine_request),
    path('view_request_for_caretaker',views.view_request_for_caretaker),
    path('approve_caretaker_view/<id>',views.approve_caretaker_view),
    path('approve_caretaker_view_post/<cid>/<rid>',views.approve_caretaker_view_post),
    path('reject_caretaker/<id>',views.reject_caretaker),
    path('view_request_for_volunteer', views.view_request_for_volunteer),
    path('approve_volunteer/<id>',views.approve_volunteer),
    path('approve_volunteer_post/<rid>/<vid>',views.approve_volunteer_post),
    path('reject_volunteer/<id>',views.reject_volunteer),
    path('view_requested_user_reports',views.view_requested_user_reports),
    path('view_report/<id>',views.view_report),
    path('change_admin_password_view',views.change_admin_password_view),
    path('change_admin_password_view_post',views.change_admin_password_view_post),

    #############################################################################

    path('change_caretaker_password_view',views.change_caretaker_password_view),
    path('change_caretaker_password_view_post',views.change_caretaker_password_view_post),
    path('patients_view',views.patients_view),
    path('add_daily_report_view/<uid>',views.add_daily_report_view),
    path('add_daily_report_view_post/<uid>',views.add_daily_report_view_post),
    path('view_daily_report/<uid>',views.view_daily_report),
    path('update_daily_report_view/<id>',views.update_daily_report_view),
    path('update_daily_report_view_post/<id>',views.update_daily_report_view_post),
    path('delete_daily_report/<id>',views.delete_daily_report),
    path('send_medicine_request_view',views.send_medicine_request_view),
    path('send_medicine_request_view_post',views.send_medicine_request_view_post),
    path('view_medicine_status',views.view_medicine_status),
    path('add_suggestion_view',views.add_suggestion_view),
    path('add_suggestion_view_post',views.add_suggestion_view_post),
    path('view_suggestions',views.view_suggestions),
    path('update_suggestion_view/<id>',views.update_suggestion_view),
    path('update_suggestion_post/<id>',views.update_suggestion_post),
    path('delete_suggestion/<id>',views.delete_suggestion),
    path('reminder_setting_view/<uid>',views.reminder_setting_view),
    path('reminder_setting_view_post/<uid>',views.reminder_setting_view_post),
    path('view_reminder/<uid>',views.view_reminder),
    path('update_reminder/<id>',views.update_reminder),
    path('update_reminder_post/<id>',views.update_reminder_post),
    path('delete_reminder/<id>',views.delete_reminder),
    path('logout',views.logout),


    #####################################################################################

    path('user_login',views.user_login),
    path('user_register',views.user_register),
    path('caretaker_request',views.caretaker_request),
    path('caretaker_request_status',views.caretaker_request_status),
    path('view_sponsorships',views.view_sponsorships),
    path('send_sponsorship_request',views.send_sponsorship_request),
    path('view_sponsorship_requests',views.view_sponsorship_requests),
    path('view_Donation',views.view_Donation),
    path('send_donation_requests',views.send_donation_requests),
    path('view_user_photos',views.view_user_photos),
    path('view_user_reports',views.view__user_reports),
    path('view_user_reminder',views.view_user_reminder),


    ##########################################################
    path('public_sponsorship',views.public_sponsorship),
    path('public_volunteer',views.public_volunteer),










]
