from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import *
from .helper import *

# Create your views here.

def index(request):
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    context = {'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'home.html', context)

def logout(request):
    try:
        del request.session['user_id']
        del request.session['contractor_id']
        del request.session['admin_id']
    except KeyError:
        print("No key(s) to delete")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

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
            return HttpResponse("Error: User trying to be deleted does not exist!")
    else:
        try:
            administrator = Administrators.objects.get(pk=request.session['admin_id'])
            administrator.delete()
            del request.session['admin_id']
            return redirect(index)
        except Administrators.DoesNotExist:
            return HttpResponse("Error: User trying to be deleted does not exist!")
    
def services_list(request):
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    serviceCategories = Servicecategories.objects.all()
    context = {'serviceCategories':serviceCategories, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'servicesList.html', context)

def becomeContractor(request):
    if request.session.has_key('contractor_id'):
        redirect(contractorProfile)
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
                    request.session['contractor_id'] = contractor.contractorid    #store user id of new user
                    try:
                        #remove other ids
                        del request.session['user_id']
                        del request.session['admin_id']
                    except KeyError:
                        print("No keys to delete")

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
        '''
        if request.method == 'POST':
            form = NewContractorForm(request.POST)
            #verify address can be located
            if VerifyValues.checkLocation(request.POST['address'], request.POST['city'], request.POST['state'], request.POST['zipcode']):
                #do something
            else:
                messages.error(request, "Error: Address provided is incorrect.")
        '''

        service = Services.objects.get(pk=pk)
        form = ContractForm()
        have_user = request.session.has_key('user_id')
        have_contractor = request.session.has_key('contractor_id')
        have_admin = request.session.has_key('admin_id')
        if have_user:
            user = Users.objects.get(pk=request.session['user_id'])
            context = {'service':service, 'form':form, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin, 'user': user}
        else:
            context = {'service':service, 'form':form, 'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
        return render(request, 'booking/bookingInformation.html', context)
    except Services.DoesNotExist:
        return HttpResponse("Error: Service does not exist!")

def bookingStep2(request):
    have_user = request.session.has_key('user_id')
    have_contractor = request.session.has_key('contractor_id')
    have_admin = request.session.has_key('admin_id')
    #get list of available contractors
    context = {'have_user':have_user, 'have_contractor':have_contractor, 'have_admin':have_admin}
    return render(request, 'booking/availableContractors.html', context)

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
                try:
                    #remove other ids
                    del request.session['contractor_id']
                    del request.session['admin_id']
                except KeyError:
                    print("No keys to delete")
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
                    user = UserFunctions.createNewUser(request.POST['firstname'], request.POST['lastname'], 
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
                request.session['contractor_id'] = contractor.contractorid  #store contractor id
                #remove other ids
                del request.session['user_id']
                del request.session['admin_id']
                #next = request.POST.get('next', '/')
                return redirect(contractorProfile)
            except Contractors.DoesNotExist:
                messages.error(request, "Incorrect email or password.")
            except KeyError:
                print("No keys to delete")
    
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

def contractorServices(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        try:
            servicesMy = Contractorsservicerecords.objects.get(contractorid=request.session['contractor_id'])
            context = {'contractor': contractor, 'servicesMy': servicesMy, 'hasServices': True}
        except Contractorsservicerecords.DoesNotExist:
            paymentM = None
            context = {'contractor': contractor, 'servicesMy': servicesMy, 'hasServices': False}

            return render(request, 'contractor/contractorServices.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorRatings(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        try:
            ratingMy = Rating.objects.get(contractorid=request.session['contractor_id'])
            context = {'contractor': contractor, 'ratingMy': ratingMy, 'hasRatings': True}
        except Rating.DoesNotExist:
            paymentM = None
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
            paymentM = None
            context = {'contractor': contractor, 'contractsMy': contractsMy, 'hasContracts': False}
        
        return render(request, 'contractor/contractorContracts.html', context)
    else:
        return HttpResponse("Error: Not Logged-in!")

def contractorSchedule(request):
    if request.session.has_key('contractor_id'):
        contractor = Contractors.objects.get(pk=request.session['contractor_id'])
        context = {'contractor': contractor}

        return render(request, 'contractor/contractorContracts.html', context)
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
                administrator = Administrators.objects.get(email=email, password=password)
                request.session['admin_id'] = administrator.adminid     #store admin id
                #remove other ids
                del request.session['contractor_id']
                del request.session['user_id']
                #next = request.POST.get('next', '/')
                return redirect(adminProfile)
            except Administrators.DoesNotExist:
                messages.error(request, "Incorrect email or password.")
            except KeyError:
                print("No keys to delete")
    
        form = LoginUserForm()
        context = {'form':form}
        return render(request, 'adminLogin.html', context)

def adminProfile(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        context = {'administrator': administrator}
    else:
        messages.error(request, "Error: Not Signed-in.")
    
    return render(request, 'administrator/adminProfile.html', context)

def manageUsers(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        users = Users.objects.all()
        context = {'administrator': administrator, 'users':users}
    else:
        messages.error(request, "Error: Not Signed-in.")
    
    return render(request, 'administrator/manageUsers.html', context)

def manageContractors(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        contractors = Contractors.objects.all()
        context = {'administrator': administrator, 'contractors':contractors}
    else:
        messages.error(request, "Error: Not Signed-in.")
    
    return render(request, 'administrator/manageContractors.html', context)

def manageContractorApp(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        contractorApps = Contractorapplications.objects.all()
        context = {'administrator': administrator, 'contractorApps':contractorApps}
    else:
        messages.error(request, "Error: Not Signed-in.")
    
    return render(request, 'administrator/manageContractorApp.html', context)

def manageServiceApp(request):
    if request.session.has_key('admin_id'):
        administrator = Administrators.objects.get(pk=request.session['admin_id'])
        serviceApps = Serviceapplications.objects.all()
        context = {'administrator': administrator, 'serviceApps':serviceApps}
    else:
        messages.error(request, "Error: Not Signed-in.")
    
    return render(request, 'administrator/manageAddServiceApp.html', context)
