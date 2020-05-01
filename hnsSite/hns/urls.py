from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout', views.logout, name='logout'),
    path('deleteAccount', views.deleteAccount, name='deleteAccount'),
    path('services/', views.services_list, name='services_list'),
    path('booking/booking_information/<str:pk>', views.bookingStep1, name='booking1'),
    path('becomeContractor/', views.becomeContractor, name='becomeContractor'),
    path('login/', views.login, name='login'),
    path('create_account/', views.createUserAccount, name="createUserAccount"),
    path('account/user_profile/', views.userProfile, name='userProfile'),
    path('account/user_profile/edit', views.userProfileEdit, name='userProfile_edit'),
    path('account/payment_methods/', views.userPayment, name='userPayment'),
    path('account/booking_history/', views.userBookingInfo, name='userBooking'),
    path('contractor/contractor_login/', views.contractorLogin, name='loginContractor'),
    path('contractor/contractor_profile/', views.contractorProfile, name='contractorProfile'),
    path('administrator/admin_login/', views.adminLogin, name='loginAdministrator'),
    path('administrator/admin_profile/', views.contractorProfile, name='administratorProfile'),
]