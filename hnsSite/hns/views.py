from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.forms import formset_factory

from datetime import datetime, timedelta
import calendar
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

from .forms import *
from .helper import *
from .utils import EventCalendar

# Create your views here.

def index(request):
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    context = {'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'home.html', context)

def logout(request):
    OtherFunctions.logout(request, 'user_id')
    OtherFunctions.logout(request, 'contractor_id')
    OtherFunctions.logout(request, 'admin_id')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def logoutProfile(request):
    OtherFunctions.logout(request, 'user_id')
    OtherFunctions.logout(request, 'contractor_id')
    OtherFunctions.logout(request, 'admin_id')

    return redirect(index)

def deleteAccount(request):
    if request.session.has_key('user_id'):
        try:
            user = Users.objects.get(pk=request.session['user_id'])
            user.delete()
            del request.session['user_id']
            return redirect(index)
        except Users.DoesNotExist:
            return HttpResponse("Error: User trying to be deleted does not exist!")
    elif request.session.has_key('contractor_id'):
        try:
            contractor = Contractors.objects.get(pk=request.session['contractor_id'])
            contractor.delete()
            del request.session['contractor_id']
            return redirect(index)
        except Contractors.DoesNotExist:
            return HttpResponse("Error: Contractor trying to be deleted does not exist!")
    elif request.session.has_key('admin_id'):
        try:
            administrator = Administrators.objects.get(pk=request.session['admin_id'])
            administrator.delete()
            del request.session['admin_id']
            return redirect(index)
        except Administrators.DoesNotExist:
            return HttpResponse("Error: Administrator trying to be deleted does not exist!")
    else:
        return HttpResponse("Error: Not Logged-in!")
    
def services_list(request):
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    serviceCategories = Servicecategories.objects.all()
    context = {'serviceCategories':serviceCategories, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'servicesList.html', context)

def becomeContractor(request):
    if request.session.has_key('contractor_id'):
        return redirect(contractorProfile)
    else:
        if request.method == 'POST':
            form = NewContractorForm(request.POST)
            #verify age is over 18
            if VerifyValues.checkOlder18(request.POST['dob']):
                #verify address can be located
                if VerifyValues.checkLocation(request.POST['address'], request.POST['city'], request.POST['state'], request.POST['zipcode']):
                    contractor = ContractorFunctions.applyContractor(request.POST['name'], request.POST['ssn'], request.POST['address'],
                        request.POST['aptnum'], request.POST['city'], request.POST['state'], request.POST['willingtravel'], request.POST['zipcode'],
                        request.POST['phone'], request.POST['dob'], request.POST['email'], request.POST['password'])

                    return HttpResponse("Thank you! Your application has been submitted.")
                else:
                    messages.error(request, "Error: Address provided is incorrect.")
            else:
                messages.error(request, "Error: You need to be 18 or older.")

        form = NewContractorForm()
        have_user = request.session.has_key('user_id')
        have_contractor = request.session.has_key('contractor_id')
        have_admin = request.session.has_key('admin_id')
        context = {'form':form, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
        return render(request, 'becomeAContractor.html', context)

#booking views
def bookingStep1(request, pk):
    try:
        if request.method == 'POST':
            form = ContractForm(request.POST)
            description = request.POST['description']
            date = request.POST['dateservice']
            startTime = request.POST['starttime']
            zipcode = request.POST['servicezipcode']
            address = request.POST['serviceaddress']
            aptnum = request.POST['serviceaptnum']

            #verify address can be located
            if VerifyValues.checkLocation2(address, zipcode):
                if aptnum == "":
                    return redirect(bookingStep2, pk=pk, description=description, date=date, time=startTime, address=address, aptnum="none", zipcode=zipcode)
                else:
                    return redirect(bookingStep2, pk=pk, description=description, date=date, time=startTime, address=address, aptnum=aptnum, zipcode=zipcode)
            else:
                messages.error(request, "Error: Address provided is incorrect.")

        service = Services.objects.get(pk=pk)
        form = ContractForm()
        have_user = request.session.has_key('user_id')
        have_contractor = request.session.has_key('contractor_id')
        have_admin = request.session.has_key('admin_id')
        if have_user:
            user = Users.objects.get(pk=request.session['user_id'])
            context = {'service':service, 'form':form, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin, 'user': user}
            return render(request, 'booking/bookingInformation.html', context)
        else:
            context = {'service':service, 'form':form, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
        return render(request, 'booking/bookingInformation.html', context)
    except Services.DoesNotExist:
        return HttpResponse("Error: Service does not exist!")

def bookingStep2(request, pk, description, date, time, address, aptnum, zipcode):
    try:
        service = Services.objects.get(pk=pk)
        have_user = request.session.has_key('user_id')
        have_contractor = request.session.has_key('contractor_id')
        have_admin = request.session.has_key('admin_id')

        if have_user:
            user = Users.objects.get(pk=request.session['user_id'])
            #get list of available contractors
            contractors = Contractorsservicerecords.objects.filter(serviceid=service)
            context = {'service':service, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin, 'user': user, 'availableContractors':contractors}
            return render(request, 'booking/availableContractors.html', context)
        else:
            return HttpResponse("Error: Not Logged-in!")
    except Services.DoesNotExist:
        return HttpResponse("Error: Service does not exist!")

def bookingStep3(request):
    form = NewPaymentInfoForm()
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    context = {'form':form, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'booking/paymentContract.html', context)

def bookingConfirmation(request):
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    context = {'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'booking/contractConfirmation.html', context)

#user views
def login(request):
    if request.session.has_key('user_id'):
        return redirect(userProfile)
    else:
        if request.method == 'POST':
            form = form = LoginUserForm(request.POST)
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Users.objects.get(email=email, password=password)
                request.session['user_id'] = user.userid    #store user id
                #remove other ids
                OtherFunctions.logout(request, 'contractor_id')
                OtherFunctions.logout(request, 'admin_id')
                return HttpResponseRedirect(request.session['login_from'])
            except Users.DoesNotExist:
                messages.error(request, "Incorrect email or password.")

        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')

        form = LoginUserForm()
        context = {'form':form}
        return render(request, 'login.html', context)

def createUserAccount(request):
    if request.session.has_key('user_id'):
        return redirect(userProfile)
    else:
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            #verify age is over 18
            if VerifyValues.checkOlder18(request.POST['dob']):
                #verify address can be located
                if VerifyValues.checkLocation(request.POST['address'], request.POST['city'], request.POST['state'], request.POST['zipcode']):
                    user = UserFunctions.createNewUser(request.POST['firstname'], request.POST['lastname'], request.POST['email'], 
                        request.POST['password'], request.POST['dob'], request.POST['phone'], request.POST['address'],
                         request.POST['aptnum'], request.POST['city'], request.POST['state'], request.POST['zipcode'])
                    request.session['user_id'] = user.userid    #store user id of new user
                    try:
                        #remove other ids
                        del request.session['contractor_id']
                        del request.session['admin_id']
                    except KeyError:
                        print("No keys to delete")

                    return HttpResponseRedirect(request.session['create_user_from'])
                else:
                    messages.error(request, "Error: Address provided is incorrect.")
            else:
                messages.error(request, "Error: You need to be 18 or older.")
            
        request.session['create_user_from'] = request.META.get('HTTP_REFERER', '/')

        form = NewUserForm()
        context = {'form':form}
        return render(request, 'createNewUser.html', context)

def userProfile(request):
    if request.session.has_key('user_id'):
        user = Users.objects.get(pk=request.session['user_id'])
        context = {'user': user}

        return render(request, 'user/userProfile.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def userProfileEdit(request):
    if request.session.has_key('user_id'):
        user = Users.objects.get(pk=request.session['user_id'])

        if request.method == 'POST':
            form = NewUserForm(request.POST, instance=user)
            #verify age is over 18
            if VerifyValues.checkOlder18(request.POST['dob']):
                #verify address can be located
                if VerifyValues.checkLocation(request.POST['address'], request.POST['city'], request.POST['state'], request.POST['zipcode']):
                    user = UserFunctions.editUser(request.session['user_id'], request.POST['firstname'], request.POST['lastname'], 
                        request.POST['password'], request.POST['dob'], request.POST['phone'], request.POST['address'],
                        request.POST['aptnum'], request.POST['city'], request.POST['state'], request.POST['zipcode'])
                    return redirect(userProfile)
                else:
                    messages.error(request, "Error: Address provided is incorrect.")
            else:
                messages.error(request, "Error: You need to be 18 or older.")

        form = NewUserForm(instance=user)
        context = {'user': user, 'form':form}

        return render(request, 'user/editUserProfile.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def userPayment(request):
    if request.session.has_key('user_id'):
        user = Users.objects.get(pk=request.session['user_id'])
        try:
            paymentM = Paymentinfo.objects.get(userid=request.session['user_id'])
            context = {'user': user, 'paymentM': paymentM, 'hasPayment': True}
        except Paymentinfo.DoesNotExist:
            paymentM = None
            context = {'user': user, 'paymentM': paymentM, 'hasPayment': False}

        return render(request, 'user/userPaymentMethods.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def userBookingInfo(request):
    if request.session.has_key('user_id'):
        user = Users.objects.get(pk=request.session['user_id'])
        try:
            bookings = Contracts.objects.get(userid=request.session['user_id'])
            context = {'user': user, 'bookings': bookings, 'hasBooking': True}
        except Contracts.DoesNotExist:
            bookings = None
            context = {'user': user, 'bookings': bookings, 'hasBooking': False}
    
        return render(request, 'user/userBookingInformation.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

#contractor views
def contractorLogin(request):
    if request.session.has_key('contractor_id'):
        return redirect(contractorProfile)
    else:
        if request.method == 'POST':
            form = form = LoginUserForm(request.POST)
            email = request.POST['email']
            password = request.POST['password']
            try:
                contractor = Contractors.objects.get(email=email, password=password)
                request.session['contractor_id'] = contractor.contractorid.contractorid  #store contractor id
                #remove other ids
                OtherFunctions.logout(request, 'user_id')
                OtherFunctions.logout(request, 'admin_id')
                return redirect(contractorProfile)
            except Contractors.DoesNotExist:
                messages.error(request, "Incorrect email or password.")
    
        form = LoginUserForm()
        context = {'form':form}
        return render(request, 'contractorLogin.html', context)

def contractorProfile(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        context = {'contractor': contractor}

        return render(request, 'contractor/contractorProfile.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorProfileEdit(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])

        if request.method == 'POST':
            form = NewContractorForm(request.POST, instance=contractor)
            #verify age is over 18
            if VerifyValues.checkOlder18(request.POST['dob']):
                #verify address can be located
                if VerifyValues.checkLocation(request.POST['address'], request.POST['city'], request.POST['state'], request.POST['zipcode']):
                    contractor = ContractorFunctions.editContractor(request.session['contractor_id'], request.POST['name'], request.POST['address'],
                        request.POST['aptnum'], request.POST['city'], request.POST['state'], request.POST['willingtravel'], request.POST['zipcode'],
                        request.POST['phone'], request.POST['dob'], request.POST['password'])
                    return redirect(contractorProfile)
                else:
                    messages.error(request, "Error: Address provided is incorrect.")
            else:
                messages.error(request, "Error: You need to be 18 or older.")

        form = NewContractorForm(instance=contractor)
        context = {'contractor': contractor, 'form':form}

        return render(request, 'contractor/editContractorProfile.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorServices(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        servicesMy = contractor.contractorsservicerecords_set.all()
        context = {'contractor': contractor, 'servicesMy': servicesMy}
        
        return render(request, 'contractor/contractorServices.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorServiceApp(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        
        if request.method == 'POST':
            form = NewContractorForm(request.POST)
            service = request.POST['serviceid']
            charge = request.POST['chargeservice']
            experience = request.POST['yearsexperience']
            ContractorFunctions.applyService(contractor, service, charge, experience)
            return redirect(contractorServices)
        
        form = newServiceForm()
        context = {'contractor': contractor, 'form':form}
        
        return render(request, 'contractor/serviceApp.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def getdetails(request):
    category_id = request.GET.get('category')
    services = Services.objects.filter(categoryserviceid=category_id).order_by('title')
    return render(request, 'contractor/service_dropdown_list_options.html', {'services': services})

def contractorRatings(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        try:
            ratingMy = Rating.objects.get(contractorid=request.session['contractor_id'])
            context = {'contractor': contractor, 'ratingMy': ratingMy, 'hasRatings': True}
        except Rating.DoesNotExist:
            ratingMy = None
            context = {'contractor': contractor, 'ratingMy': ratingMy, 'hasRatings': False}
        
        return render(request, 'contractor/contractorRatings.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorContracts(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        try:
            contractsMy = Contracts.objects.get(contractorid=request.session['contractor_id'])
            context = {'contractor': contractor, 'contractsMy': contractsMy, 'hasContracts': True}
        except Contracts.DoesNotExist:
            contractsMy = None
            context = {'contractor': contractor, 'contractsMy': contractsMy, 'hasContracts': False}
        
        return render(request, 'contractor/contractorContracts.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorSchedule(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        
        d = date.today()

        previous_month = date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - timedelta(days=1)  # backs up a single day
        previous_month = date(year=previous_month.year, month=previous_month.month, day=1)  # find first day of previous month
 
        last_day = calendar.monthrange(d.year, d.month)
        next_month = date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + timedelta(days=1)  # forward a single day
        next_month = date(year=next_month.year, month=next_month.month, day=1)  # find first day of next month

        mySchedule = contractor.schedules_set.all()
        myTimeSlots = TimeSlots.objects.filter(pk__in=mySchedule.values('time_slot'))


        cal = EventCalendar(myTimeSlots)
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')

        context = {'contractor': contractor, 'calendar': mark_safe(html_calendar)}

        return render(request, 'contractor/contractorSchedule.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

#administrator views
def adminLogin(request):
    if request.session.has_key('admin_id'):
        return redirect(adminProfile)
    else:
        if request.method == 'POST':
            form = form = LoginUserForm(request.POST)
            email = request.POST['email']
            password = request.POST['password']
            try:
                administrator = Administrators.objects.get(adminemail=email, adminpassword=password)
                request.session['admin_id'] = administrator.adminid     #store admin id
                #remove other ids
                OtherFunctions.logout(request, 'user_id')
                OtherFunctions.logout(request, 'contractor_id')
                return redirect(adminProfile)
            except Administrators.DoesNotExist:
                messages.error(request, "Incorrect email or password.")
    
        form = LoginUserForm()
        context = {'form':form}
        return render(request, 'adminLogin.html', context)

def adminProfile(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        context = {'administrator': administrator}

        return render(request, 'administrator/adminWelcome.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def manageUsers(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        users = Users.objects.all()
        if not users:
            hasUsers = False
        else:
            hasUsers = True
        context = {'administrator': administrator, 'users':users, 'hasUsers':hasUsers}

        return render(request, 'administrator/manageUsers.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def adminEditUser(request, id):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        try:
            user = Users.objects.get(pk=id)

            if request.method == 'POST':
                form = NewUserForm(request.POST, instance=user)
                #verify age is over 18
                if VerifyValues.checkOlder18(request.POST['dob']):
                    #verify address can be located
                    if VerifyValues.checkLocation(request.POST['address'], request.POST['city'], request.POST['state'], request.POST['zipcode']):
                        user = UserFunctions.editUser(id, request.POST['firstname'], request.POST['lastname'], 
                            request.POST['password'], request.POST['dob'], request.POST['phone'], request.POST['address'],
                            request.POST['aptnum'], request.POST['city'], request.POST['state'], request.POST['zipcode'])
                        return redirect(manageUsers)
                    else:
                        messages.error(request, "Error: Address provided is incorrect.")
                else:
                    messages.error(request, "Error: You need to be 18 or older.")

            form = NewUserForm(instance=user)
            context = {'administrator': administrator, 'user': user, 'form':form}

            return render(request, 'administrator/editUser.html', context)
        except Users.DoesNotExist:
            return HttpResponse("Error: User trying to be deleted does not exist!")

    else:
        return HttpResponse("Error: Not Logged-in!")

def manageContractors(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        contractors = Contractors.objects.all()
        if not contractors:
            hasContractors = False
        else:
            hasContractors = True
        context = {'administrator': administrator, 'contractors':contractors, 'hasContractors':hasContractors}

        return render(request, 'administrator/manageContractors.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def manageContractorApp(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        contractorApps = Contractorapplications.objects.exclude(adminid__isnull=False)
        if not contractorApps:
            hasContractors = False
        else:
            hasContractors = True
        context = {'administrator': administrator, 'contractorApps':contractorApps, 'hasContractors':hasContractors}

        return render(request, 'administrator/manageContractorApp.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def manageServiceApp(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        serviceApps = Serviceapplications.objects.exclude(adminid__isnull=False)
        if not serviceApps:
            hasAppServices = False
        else:
            hasAppServices = True
        context = {'administrator': administrator, 'serviceApps':serviceApps, 'hasAppServices':hasAppServices}

        return render(request, 'administrator/manageAddServiceApp.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def adminApproveApp(request, id):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        try:
            contractorApp = Contractorapplications.objects.get(pk=id, dateapproved__isnull=True)
            email = contractorApp.email
            AdminFunctions.approveApp(contractorApp, administrator.adminid )
            AdminFunctions.addContractor(contractorApp)
            send_mail(
                'Contractor Application - Approved',
                'Congratulations,\nI am happy to inform you that your application to become a contractor has been approved. To login and provide further information to become an active contractor, please go to ec2-18-218-41-14.us-east-2.compute.amazonaws.com/contractor/contractor_login/.\nThank you,\nHomeNeedsServices Team',
                administrator.adminemail, [email], fail_silently=False,
            )

            return redirect(manageContractorApp)
        except Contractorapplications.DoesNotExist:
            return HttpResponse("Error: Contractor Application trying to be approved does not exist or has already been approved!")
    else:
        return HttpResponse("Error: Not Logged-in!")

def adminRejectApp(request, id):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        try:
            contractorApp = Contractorapplications.objects.get(pk=id, adminid__isnull=True)
            email = contractorApp.email
            contractorApp.delete()
            send_mail(
                'Contractor Application - Not Approved',
                'Hello,\nI regret to inform you that your application to become a contractor has been rejected. If you would like to know the reason, please contact us. The means to do so our provided at ec2-18-218-41-14.us-east-2.compute.amazonaws.com.\nThank you,\nHomeNeedsServices Team',
                administrator.adminemail, [email], fail_silently=False,
            )

            return redirect(manageContractorApp)
        except Contractorapplications.DoesNotExist:
            return HttpResponse("Error: Contractor Application trying to be approved does not exist or has already been approved!")
    else:
        return HttpResponse("Error: Not Logged-in!")

def adminApproveApp2(request, id):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        try:
            serviceApp = Serviceapplications.objects.get(pk=id, dateapproved__isnull=True)
            email = serviceApp.contractorid.email
            AdminFunctions.approveApp(serviceApp, administrator.adminid )
            AdminFunctions.addService(serviceApp)
            send_mail(
                'Add Service Application - Approved',
                'Congratulations,\nI am happy to inform you that your application to offer an additional service has been approved.\nThank you,\nHomeNeedsServices Team',
                administrator.adminemail, [email], fail_silently=False,
            )

            return redirect(manageServiceApp)
        except Contractorapplications.DoesNotExist:
            return HttpResponse("Error: Contractor Application trying to be approved does not exist or has already been rejected/approved!")
    else:
        return HttpResponse("Error: Not Logged-in!")

def adminRejectApp2(request, id):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        try:
            serviceApp = Serviceapplications.objects.get(pk=id, adminid__isnull=True)
            email = serviceApp.contractorid.email
            serviceApp.delete()
            send_mail(
                'Contractor Application - Not Approved',
                'Hello,\nI regret to inform you that your application to offer an additional service has been rejected. If you would like to know the reason, please contact us. The means to do so our provided at ec2-18-218-41-14.us-east-2.compute.amazonaws.com.\nThank you,\nHomeNeedsServices Team',
                administrator.adminemail, [email], fail_silently=False,
            )

            return redirect(manageServiceApp)
        except Contractorapplications.DoesNotExist:
            return HttpResponse("Error: Contractor Application trying to be rejected does not exist or has already been rejected/approved!")
    else:
        return HttpResponse("Error: Not Logged-in!")

def adminDeleteAccount(request, accountType, id):
    if accountType=='users':
        try:
            user = Users.objects.get(pk=id)
            user.delete()
            return redirect(manageUsers)
        except Users.DoesNotExist:
            return HttpResponse("Error: User trying to be deleted does not exist!")
    elif accountType=='contractors':
        try:
            contractor = Contractors.objects.get(pk=id)
            contractor.delete()
            return redirect(manageContractors)
        except Contractors.DoesNotExist:
            return HttpResponse("Error: Contractor trying to be deleted does not exist!")
    elif accountType=='administrators':
        try:
            administrator = Administrators.objects.get(pk=id)
            administrator.delete()
            return redirect(index)
        except Administrators.DoesNotExist:
            return HttpResponse("Error: Administrator trying to be deleted does not exist!")
    else:
        return HttpResponse("Error: Page Not Found!")
 