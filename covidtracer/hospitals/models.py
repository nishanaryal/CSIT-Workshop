from django.db import models

# Create your models here.
class RequestBed(models.Model):

    Gender_Options = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    BedType_Options = [
        ('ICU', 'ICU'),
        ('Normal', 'Normal'),
        ('Isolation', 'Isolation'),
        ('Ventilator','Ventilator'),
        ('Unspecified','Unspecified')
    ]

    Urgency_Options = [
        ('Urgent', 'Urgent'),
        ('Moderate', 'Moderate'),
        ('Not Urgent', 'Not Urgent')
    ]

    Aus_States = [
        ('Province 1', 'Province 1'),
        ('Province 2', 'Province 2'),
        ('Bagmati Province', 'Bagmati Province'),
        ('Gndaki Province', 'Tasmania'),
        ('Province 5', 'Province 5'),
        ('Province 6', 'Province 6'),
        ('Province 7', 'Province 7')
    ]

    Action_Status = [
        ('Solved', 'Solved'),
        ('Request Received', 'Request Received'),
        ('Waiting', 'Waiting'),
        ('Under Approval', 'Under Approval'),
        ('Cancelled', 'Cancelled'),
        ('Approved', 'Approved'),
        ('Patient Expired', 'Patient Expired'),
        ('Not available', 'Not available'),
        ('Still Finding', 'Still Finding')
    ]

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, verbose_name='Full Name')
    age = models.IntegerField()
    gender = models.CharField(choices=Gender_Options, default='Other', max_length=10, verbose_name='Gender')
    email = models.CharField(max_length=128, verbose_name='Email', null=True)
    contactNo = models.CharField(max_length=25, verbose_name='Contact No')
    streetAddress = models.CharField(max_length=200, verbose_name='Street Address')
    city = models.CharField(max_length=200, verbose_name='City')
    state = models.CharField( choices=Aus_States, default='', max_length=150, verbose_name='State')
    bedsQty = models.IntegerField(verbose_name='No of Beds')
    urgency = models.CharField(choices=Urgency_Options,default='Not Urgent', max_length=40, verbose_name='Urgency') 
    bedType = models.CharField(choices=BedType_Options,default='Normal', max_length=30, verbose_name='Bed Type')
    additionalInfo = models.TextField(verbose_name='Additional Information', blank=True, null=True)
    o_name = models.CharField(max_length=200, blank=True, null=True)
    o_contactNo = models.CharField(max_length=30, blank=True, null=True)
    o_address = models.CharField(max_length=200, blank=True, null=True)
    o_relation = models.CharField(max_length=100, blank=True, null=True)

    requestOn = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Request Date")
    seenStatus = models.BooleanField(default=False, verbose_name='Seen Status')
    action_status = models.CharField(choices=Action_Status,default='Receive', max_length=200, verbose_name='Plasma Donate')


class DonatePlasma(models.Model):
    Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    Donate_Options = [
        ('Receive', 'I am Looking for Plasma Donor'),
        ('Donate', 'I want to donate Plasma')
    ]

    States = [
        ('Province 1', 'Province 1'),
        ('Province 2', 'Province 2'),
        ('Bagmati Province', 'Bagmati Province'),
        ('Gndaki Province', 'Tasmania'),
        ('Province 5', 'Province 5'),
        ('Province 6', 'Province 6'),
        ('Province 7', 'Province 7')
    ]

    Action_Status = [
        ('', 'Please Select'),
        ('Request Received', 'Request Received'),
        ('Waiting', 'Waiting'),
        ('Looking for Donor', 'Looking for Donor'),
        ('Under Approval', 'Under Approval'),
        ('Transfer in Progress', 'Transfer in Progress'),
        ('Cancelled', 'Cancelled'),
        ('Approved', 'Approved'),
        ('Patient Expired', 'Patient Expired'),
        ('Donor Does not Fit', 'Donor Does not Fit'),
        ('Request More', 'Request More')
    ]

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, verbose_name='Full Name')
    age = models.IntegerField()
    gender = models.CharField(choices=Gender, default='Other', max_length=10, verbose_name='Gender')
    email = models.CharField(max_length=128, verbose_name='Email', null=True)
    contactNo = models.CharField(max_length=20, verbose_name='Contact No')
    streetAddress = models.CharField(max_length=200, verbose_name='Street Address')
    city = models.CharField(max_length=300, verbose_name='City')
    state = models.CharField( choices=States, default='', max_length=50, verbose_name='State')
    donor_option = models.CharField(choices=Donate_Options,default='Receive', max_length=100, verbose_name='Plasma Donate') 
    
    additionalInfo = models.TextField(verbose_name='Additional Information', blank=True, null=True)
    requestOn = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Request Date")
    seenStatus = models.BooleanField(default=False, verbose_name='Seen Status')
    action_status = models.CharField(choices=Action_Status,default='Receive', blank=True, max_length=200, verbose_name='Plasma Donate')


class OtherRequest(models.Model):
    Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    Urgency_Options = [
        ('Urgent', 'Urgent'),
        ('Moderate', 'Moderate'),
        ('Not Urgent', 'Not Urgent')
    ]
    RequestType = [
        ('Oxygen', 'Oxygen'),
        ('Food', 'Food'),
        ('Cremation', 'Cremation'),
        ('Quarantine Space', 'Quarantine Space'),
        ('Other','Other')
    ]

    States = [
         ('Province 1', 'Province 1'),
        ('Province 2', 'Province 2'),
        ('Bagmati Province', 'Bagmati Province'),
        ('Gndaki Province', 'Tasmania'),
        ('Province 5', 'Province 5'),
        ('Province 6', 'Province 6'),
        ('Province 7', 'Province 7')
    ]

    Action_Status = [
        ('Request Received', 'Request Received'),
        ('Waiting', 'Waiting'),
        ('Under Approval', 'Under Approval'),
        ('Cancelled', 'Cancelled'),
        ('Approved', 'Approved'),
        ('Unspecified', 'Unspecified')
    ]

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, verbose_name='Full Name')
    age = models.IntegerField()
    gender = models.CharField(choices=Gender, default='Other', max_length=10, verbose_name='Gender')
    email = models.CharField(max_length=128, verbose_name='Email', null=True)
    contactNo = models.CharField(max_length=30, verbose_name='Contact No')
    streetAddress = models.CharField(max_length=200, verbose_name='Street Address')
    city = models.CharField(max_length=300, verbose_name='City')
    state = models.CharField( choices=States, default='', max_length=50, verbose_name='State')
    requestType = models.CharField(choices=RequestType,default='Oxygen', max_length=100, verbose_name='Plasma Donate') 
    urgency = models.CharField(choices=Urgency_Options,default='Not Urgent', max_length=40, verbose_name='Urgency') 
    additionalInfo = models.TextField(verbose_name='Additional Information', blank=True, null=True)

    requestOn = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Request Date")
    seenStatus = models.BooleanField(default=False, verbose_name='Seen Status')

    action_status = models.CharField(choices=Action_Status,default='Receive', blank=True, max_length=200, verbose_name='Plasma Donate')