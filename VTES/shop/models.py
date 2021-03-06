from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.template.defaultfilters import truncatechars
from django_jalali.db import models as jmodels
from authentication.models import Profile
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.html import format_html







#------------------------------------------------------------------------------
class Attributes(models.Model):
    name = models.CharField(max_length=60, verbose_name='ویژگی')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"





#------------------------------------------------------------------------------
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name = "نام")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='والد', verbose_name = "والد")

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return str(self.name)







#------------------------------------------------------------------------------
class Shop(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', verbose_name = "کاربر")
  name = models.CharField(max_length=70, verbose_name = "نام فروشگاه")
  logo = models.ImageField(default='logos/default.png', upload_to='logos', verbose_name = "لوگو فروشگاه")
  phone = models.CharField(max_length=50, null=True, blank=True, verbose_name = "شماره تماس")
  email = models.EmailField(max_length=50, null=True, blank=True, verbose_name = "ایمیل")
  address = models.CharField(max_length=200, null=True, blank=True, verbose_name = "آدرس")
  description = models.TextField(max_length=1000,null=True, blank=True, verbose_name = "توضیحات")
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='shop_category', verbose_name = "دسته بند")
  date_created = jmodels.jDateTimeField(auto_now_add=True, verbose_name = "تاریخ ایجاد")

  def __str__(self):
      return str(self.name)

  def logo_tag(self):
      return format_html("<img width=40 src='{}'>".format(self.logo.url))

  @property
  def short_description(self):
      return truncatechars(self.description, 50)

  def get_absolute_url(self):
      return reverse('shops_detail',args=[self.id])

  class Meta:
      verbose_name = "فروشگاه"
      verbose_name_plural = "فروشگاه ها"








#------------------------------------------------------------------------------
class Product(models.Model):
    approved = models.BooleanField(default=False, verbose_name = "تایید شده")
    available = models.BooleanField(default=True, verbose_name = "موجود")
    provider_shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop', verbose_name = "فروشگاه ارائه دهنده")
    code = models.CharField(max_length=50, verbose_name = "کد محصول")
    name = models.CharField(max_length=80, verbose_name = "نام محصول")
    image = models.ImageField(default='products/default.png', upload_to='products', verbose_name = "تصویر")
    price = models.IntegerField(verbose_name = "قیمت")
    qty = models.IntegerField(verbose_name = "تعداد")
    brand = models.CharField(max_length=50, verbose_name = "برند محصول")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name = "لینک محصول")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', verbose_name = "دسته بند")
    description = models.TextField(max_length=1000,null=True, blank=True, verbose_name = "توضیحات")
    datasheet = models.FileField(upload_to='datasheet', null=True, blank=True, max_length=254, verbose_name = "فایل و Datasheet")
    date_created = jmodels.jDateTimeField(auto_now_add=True, verbose_name = "تاریخ ایجاد")

    def __str__(self):
        return str(self.name)

    def img_tag(self):
        return format_html("<img width=40 src='{}'>".format(self.image.url))

    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id])

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"





#------------------------------------------------------------------------------
class Product_Attr(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attr',  verbose_name = "محصول مربوطه")
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE, verbose_name='ویژگی')

    class Meta:
        verbose_name = "ویژگی محول"
        verbose_name_plural = "ویژگی محصولات"

















#End
