import datetime
from datetime import datetime
from datetime import date
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.db.models import Max
from .models import *

class OtherFunctions:
    def logout(request, key):
        try:
            del request.session[key]
        except KeyError:
            print("No " + key + " key to delete")

class VerifyValues:
    def checkLocation(address, city, state, zipcode):
        geolocator = Nominatim(user_agent="hns")
        try:
            location = geolocator.geocode(address + ", " + city + " " + zipcode)
        except Exception:
            return False
        if not location:
            return False
        else:
            return True

    def checkLocation2(address, zipcode):
        geolocator = Nominatim(user_agent="hns")
        try:
            location = geolocator.geocode(address + ", " + zipcode)
        except Exception:
            return False
        if not location:
            return False
        else:
            return True

    def checkOlder18(dob):
        today = date.today()
        userDOB = datetime.strptime(dob,"%Y-%m-%d")
        age = today.year - userDOB.year
        return(age >= 18)

    def checkWithinTravelDistance(willingTravel, c_address, c_city, c_state, c_zipcode, s_address, s_city, s_state, s_zipcode):
        geolocator = Nominatim(user_agent="hns")
        contractor_loc = geolocator.geocode(c_address + ", " + c_city + " " + c_zipcode)  #assume location was already verified
        service_loc = geolocator.geocode(s_address + ", " + s_city + " " + s_zipcode)  #assume location was already verified
        distance = geodesic(newport_ri, cleveland_oh).miles
        return(distance <= willingTravel)

class UserFunctions:
    def createNewUser(firstname, lastname, email, password, dob, phone, address, aptnum, city, state, zipcode):
        user = Users()  #create new user
        idnum = Users.objects.count()+1
        while Users.objects.filter(pk=userid).exists():
            idnum = idnum + 1
        user.userid = idnum
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        user.password = password
        user.dob = dob
        user.phone = phone
        user.address = address
        user.aptnum = aptnum
        user.city = city
        user.state = state
        user.zipcode = zipcode
        user.save()

        return user

    def editUser(id, firstname, lastname, password, dob, phone, address, aptnum, city, state, zipcode):
        user = Users.objects.get(pk=id)
        user.firstname = firstname
        user.lastname = lastname
        user.password = password
        user.dob = dob
        user.phone = phone
        user.address = address
        user.aptnum = aptnum
        user.city = city
        user.state = state
        user.zipcode = zipcode
        user.save()

class ContractorFunctions:
    def applyContractor(name, ssn, address, aptnum, city, state, willingtravel, zipcode, phone, dob, email, password):
        appContractor = Contractorapplications()
        idC = Contractorapplications.objects.count()+1
        while Contractorapplications.objects.filter(pk=idC).exists():
            idC = idC + 1
        appContractor.contractorid = idC
        appContractor.name = name
        appContractor.ssn = ssn
        appContractor.address = address
        appContractor.aptnum = aptnum
        appContractor.city = city
        appContractor.state = state
        appContractor.zipcode = zipcode
        appContractor.willingtravel = willingtravel
        appContractor.phone = phone
        appContractor.dob = dob
        appContractor.email = email
        appContractor.password = password
        appContractor.dateapp = datetime.now()
        appContractor.save()

        return appContractor

    def editContractor(id, name, address, aptnum, city, state, willingtravel, zipcode, phone, dob, password):
        contractor = Contractors.objects.get(pk=id)
        contractor.name = name
        contractor.address = address
        contractor.aptnum = aptnum
        contractor.city = city
        contractor.state = state
        contractor.willingtravel = willingtravel
        contractor.zipcode = zipcode
        contractor.phone = phone
        contractor.dob = dob
        contractor.password = password
        contractor.save()

    def applyService(contractor, serviceid, chargeservice, yearsexperience):
        appService = Serviceapplications()
        idS = Serviceapplications.objects.count()+1
        while Serviceapplications.objects.filter(pk=idS).exists():
            idS = idS + 1
        appService.serviceappid = idS
        appService.contractorid = contractor
        appService.serviceid = Services.objects.get(pk=serviceid)
        appService.chargeservice = chargeservice
        appService.yearsexperience = yearsexperience
        appService.dateapp = datetime.now()
        appService.save()

class AdminFunctions:
    def approveApp(app, adminid):
        app.adminid = Administrators.objects.get(pk=adminid)
        app.dateapproved = datetime.now()
        app.save(update_fields=['adminid', 'dateapproved'])

        return app

    def addContractor(approvedContractor):
        contractor = Contractors()
        contractor.contractorid = Contractorapplications.objects.get(pk=approvedContractor.contractorid)
        contractor.name = approvedContractor.name
        contractor.ssn = approvedContractor.ssn
        contractor.address = approvedContractor.address
        contractor.aptnum = approvedContractor.aptnum
        contractor.city = approvedContractor.city
        contractor.state = approvedContractor.state
        contractor.zipcode = approvedContractor.zipcode
        contractor.willingtravel = approvedContractor.willingtravel
        contractor.phone = approvedContractor.phone
        contractor.dob = approvedContractor.dob
        contractor.email = approvedContractor.email
        contractor.password = approvedContractor.password
        idS = Contractors.objects.count()+1
        while Contractors.objects.filter(pk=idS).exists():
            idS = idS + 1
        contractor.scheduleid = idS
        contractor.save()

    def addService(approvedService):
        serviceRecord = Contractorsservicerecords()
        serviceRecord.contractorid = approvedService.contractorid
        serviceRecord.serviceid = approvedService.serviceid
        serviceRecord.chargeservice = approvedService.chargeservice
        serviceRecord.yearsexperience = approvedService.yearsexperience
        serviceRecord.save()
