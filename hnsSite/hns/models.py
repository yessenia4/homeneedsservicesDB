# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

class Administrators(models.Model):
    adminid = models.IntegerField(db_column='adminID', primary_key=True)  # Field name made lowercase.
    adminemail = models.CharField(db_column='adminEmail', max_length=100)  # Field name made lowercase.
    adminpassword = models.CharField(db_column='adminPassword', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrators'


class Contractpayment(models.Model):
    contractid = models.ForeignKey('Contracts', models.DO_NOTHING, db_column='contractID', primary_key=True, default=1)  # Field name made lowercase.
    time = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.IntegerField()
    refund = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contractPayment'


class Contractorapplications(models.Model):
    contractorid = models.IntegerField(db_column='contractorID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    ssn = models.IntegerField(unique=True)
    address = models.CharField(max_length=150)
    aptnum = models.CharField(db_column='aptNum', max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    willingtravel = models.IntegerField(db_column='willingTravel')  # Field name made lowercase.
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    dateapp = models.DateField(db_column='dateApp')  # Field name made lowercase.
    adminid = models.ForeignKey(Administrators, models.DO_NOTHING, db_column='adminID', default=None)  # Field name made lowercase.
    dateapproved = models.DateField(db_column='dateApproved', default=None)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'contractorApplications'


class Contractors(models.Model):
    contractorid = models.ForeignKey(Contractorapplications, models.DO_NOTHING, db_column='contractorID', primary_key=True, default=1)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    ssn = models.IntegerField(unique=True)
    scheduleid = models.IntegerField(db_column='scheduleID', unique=True)  # Field name made lowercase.
    address = models.CharField(max_length=150)
    aptnum = models.CharField(db_column='aptNum', max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(db_column='zipCode')  # Field name made lowercase.
    willingtravel = models.IntegerField(db_column='willingTravel')  # Field name made lowercase.
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'contractors'


class Contractorsservicerecords(models.Model):
    contractorid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='contractorID', primary_key=True, default=1)  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='serviceID')  # Field name made lowercase.
    chargeservice = models.DecimalField(db_column='chargeService', max_digits=10, decimal_places=2)  # Field name made lowercase.
    yearsexperience = models.IntegerField(db_column='yearsExperience')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contractorsServiceRecords'
        unique_together = (('contractorid', 'serviceid'),)


class ContractorsBackground(models.Model):
    contractorid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='contractorID', primary_key=True, default=1)  # Field name made lowercase.
    approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contractors_background'


class Contracts(models.Model):
    contractid = models.IntegerField(db_column='contractID', primary_key=True)  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='serviceID', default=1)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', default=1)  # Field name made lowercase.
    description = models.CharField(max_length=500)
    dateservice = models.DateField(db_column='dateService')  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    servicezipcode = models.IntegerField(db_column='serviceZipCode')  # Field name made lowercase.
    serviceaddress = models.CharField(db_column='serviceAddress', max_length=150)  # Field name made lowercase.
    serviceaptnum = models.CharField(db_column='serviceAptNum', max_length=10)  # Field name made lowercase.
    contractorid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='contractorID', default=1)  # Field name made lowercase.
    paymentid = models.ForeignKey('Paymentinfo', models.DO_NOTHING, db_column='paymentID', default=1)  # Field name made lowercase.
    datecontract = models.DateTimeField(db_column='dateContract')  # Field name made lowercase.
    cancelcontract = models.IntegerField(db_column='cancelContract')  # Field name made lowercase.

    def __str__(self):
        return self.description

    class Meta:
        managed = True
        db_table = 'contracts'


class Paymentinfo(models.Model):
    paymentid = models.IntegerField(db_column='paymentID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', default=1)  # Field name made lowercase.
    cardtype = models.CharField(db_column='cardType', max_length=20)  # Field name made lowercase.
    cardname = models.CharField(db_column='cardName', max_length=150)  # Field name made lowercase.
    cardnumber = models.IntegerField(db_column='cardNumber')  # Field name made lowercase.
    cvv = models.IntegerField()
    billingaddress = models.CharField(db_column='billingAddress', max_length=150)  # Field name made lowercase.
    expdate = models.DateField(db_column='expDate')  # Field name made lowercase.

    def __str__(self):
        return str(self.cardnumber)

    class Meta:
        managed = True
        db_table = 'paymentInfo'


class Rating(models.Model):
    contractorid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='contractorID', primary_key=True, default=1)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', default=1)  # Field name made lowercase.
    number_rating = models.IntegerField()
    title = models.CharField(max_length=50)
    comments = models.CharField(max_length=300)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'rating'
        unique_together = (('contractorid', 'userid'),)


class Schedules(models.Model):
    scheduleid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='scheduleID', primary_key=True, default=1)  # Field name made lowercase.
    time_slot = models.ForeignKey('TimeSlots', models.DO_NOTHING, db_column='time_slot_ID', default=1)  # Field name made lowercase.
    busy_available = models.IntegerField(db_column='busy/available')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'schedules'
        unique_together = (('scheduleid', 'time_slot'),)


class Serviceapplications(models.Model):
    serviceappid = models.IntegerField(db_column='serviceAppID', primary_key=True)  # Field name made lowercase.
    contractorid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='contractorID', default=1)  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='serviceID', default=1)  # Field name made lowercase.
    chargeservice = models.DecimalField(db_column='chargeService', max_digits=10, decimal_places=2, default=7.25)  # Field name made lowercase.
    yearsexperience = models.IntegerField(db_column='yearsExperience', default=0)  # Field name made lowercase.
    dateapp = models.DateField(db_column='dateApp')  # Field name made lowercase.
    adminid = models.ForeignKey(Administrators, models.DO_NOTHING, db_column='adminID', default=None)  # Field name made lowercase.
    dateapproved = models.DateField(db_column='dateApproved', default=None)  # Field name made lowercase.

    def __str__(self):
        return self.serviceappid

    class Meta:
        managed = True
        db_table = 'serviceApplications'
        unique_together = (('serviceappid', 'serviceid'),)


class Servicecategories(models.Model):
    categoryserviceid = models.IntegerField(db_column='categoryServiceID', primary_key=True)  # Field name made lowercase.
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_name

    class Meta:
        managed = False
        db_table = 'serviceCategories'


class Services(models.Model):
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    categoryserviceid = models.ForeignKey(Servicecategories, models.DO_NOTHING, db_column='categoryServiceID', default=1)  # Field name made lowercase.

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'services'


class TimeSlots(models.Model):
    time_slot_id = models.IntegerField(db_column='time_slot_ID', primary_key=True)  # Field name made lowercase.
    day = models.DateField()
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_slots'


class Users(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    aptnum = models.CharField(db_column='aptNum', max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(db_column='zipCode')  # Field name made lowercase.

    def __str__(self):
        return self.firstname

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    class Meta:
        managed = True
        db_table = 'users'