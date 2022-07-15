from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class our(models.Model):
    name = models.CharField('Name', max_length=200)
    logo = models.ImageField('logo', upload_to=f"YarnCole\Company\Company_Logo", null=True, blank=True)
    email_address = models.EmailField("Email Address", null=True, blank=True)
    phonenumber2 = models.CharField('Second Number', max_length=200)
    phonenumber = models.CharField('Phone Number', max_length=200)
    facebookaddress = models.URLField('Facebook Link', null=True, blank='True', max_length=250)
    instagramaddress = models.URLField('Instagram link', null=True, blank='True', max_length=250)
    twitteraddress = models.URLField('Twitter link', null=True, blank='True', max_length=250)
    location = models.CharField('Location', max_length=200, null=True, blank=True)
    about_the_company = models.TextField('About the Church', max_length=2000)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))

    class Meta:
        verbose_name_plural = 'System'


class membertype(models.Model):
    member_type = models.CharField('Type of member', unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_type

    class Meta:
        verbose_name_plural = 'Members Types'


# Create your models here.
class member(models.Model):
    name = models.CharField('Name of The Member', unique=True, max_length=200)
    picture = models.ImageField('Picture of the Member', upload_to=f"Members\Members_Images", null=True, blank=True)

    date_of_birth = models.DateField()
    mobile_number = models.CharField('Mobile Number', max_length=13)
    residential_address = models.CharField('Residential Address', max_length=200)

    membertype = models.ForeignKey(membertype, on_delete=models.CASCADE)
    date_started = models.DateField('Date That The Member Started Going To Our Church ')
    any_relative = models.CharField("Any Relative's Name", max_length=200)
    relative_phone = models.CharField("The Relative's Mobile Number", max_length=13)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Members'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % self.img.url)


class paymenttype(models.Model):
    name = models.CharField('Type of Payment', unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Payment Types'


class paymentmethod(models.Model):
    paymentmethod = models.CharField('Type of Payment Method', unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paymentmethod

    class Meta:
        verbose_name_plural = 'Payment Methods'


class payments(models.Model):
    payment_types = models.ForeignKey(paymenttype, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(member, on_delete=models.CASCADE)
    picture = models.ImageField('Picture of the payment made(Eg:Screenshots,Images,etc)',
                                upload_to=f"Payments\Payment_Images", null=True, blank=True)
    reference = models.TextField('What is the payment for', max_length=2000)
    amount_paid = models.FloatField('Amount Paid (GHC)', max_length=200)
    date_paid = models.DateTimeField('Date and time that payment was made', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_types.paymenttype

    class Meta:
        verbose_name_plural = 'Payments'


class purchase_type(models.Model):
    purchase_type = models.CharField('Type of Purchase', unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purchase_type

    class Meta:
        verbose_name_plural = 'Purchase Type'


class purchase(models.Model):
    purchase_types = models.ForeignKey(purchase_type, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(member, on_delete=models.CASCADE)
    reference = models.TextField('What did you purchase', max_length=2000)
    picture = models.ImageField('Picture of the Purchase made(Eg:Screenshots,Images,etc)',
                                upload_to=f"Purchase\Purchase_Images", null=True, blank=True)
    amount_paid = models.FloatField('Amount Paid (GHC)', max_length=200)
    date_paid = models.DateTimeField('Date and time that when the purchase was made', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purchase_types.purchase_type

    class Meta:
        verbose_name_plural = 'Purchases'

class documents(models.Model):
    name =  models.CharField('Type of Purchase', max_length=200)
    picture = models.ImageField('Any Picture of the document (Eg:Screenshots,Images,etc)',
                                upload_to=f"Payments\Payment_Images", null=True, blank=True)
    picture2 = models.ImageField('Another Picture of the document (Eg:Screenshots,Images,etc)',
                                upload_to=f"Payments\Payment_Images", null=True, blank=True)
    picture3 = models.ImageField('Another Picture of the document (Eg:Screenshots,Images,etc)',
                                upload_to=f"Payments\Payment_Images", null=True, blank=True)

    file = models.ImageField('The Document(Eg:PDF,or Docx only)',
                                upload_to=f"Payments\Payment_Images", null=True, blank=True)
    reference = models.TextField('What is the document about', max_length=2000)

    date_made = models.DateTimeField('Date and time when the document was made', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Documents'