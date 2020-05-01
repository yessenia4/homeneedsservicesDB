import datetime
from datetime import date
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .models import *

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

    def checkOlder18(dob):
        today = date.today()
        userDOB = datetime.datetime.strptime(dob,"%m/%d/%Y")
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
        user.userid = Users.objects.count()+1
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        user.password = password
        user.dob = datetime.datetime.strptime(dob,"%m/%d/%Y").strftime("%Y-%m-%d")
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
        user.dob = datetime.datetime.strptime(dob,"%m/%d/%Y").strftime("%Y-%m-%d")
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
        appContractor.contractorid = Contractorapplications.objects.count()+1
        appContractor.name = name
        appContractor.ssn = ssn
        appContractor.address = address
        appContractor.aptnum = aptnum
        appContractor.city = city
        appContractor.state = state
        appContractor.zipcode = zipcode
        appContractor.willingtravel = willingtravel
        appContractor.phone = phone
        appContractor.dob = datetime.datetime.strptime(dob,"%m/%d/%Y").strftime("%Y-%m-%d")
        appContractor.email = email
        appContractor.password = password
        appContractor.dateapp = datetime.now()
        appContractor.save()

        return appContractor