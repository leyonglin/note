from django.db import models
from userinfo.models import UserInfo

CAR_STATUS = (
    (0,'审核中'),
    (1,'已审核'),
    (2,'待审核'),
    (3,'未通过'),
)



# Create your models here.
class Brand(models.Model):
    title = models.CharField('名称',max_length=50)
    logo = models.ImageField(verbose_name='logo',upload_to='img/logo',default='')
    newprice = models.DecimalField(verbose_name='新车价格',max_digits=8,decimal_places=2)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.title


class CarInfo(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    regiset_data = models.DateField(verbose_name='上牌日期')
    engineNo = models.CharField('发动机号',max_length=50,null=True)
    mileage = models.IntegerField(verbose_name='公里数')
    record = models.CharField('维修记录',max_length=200)
    price = models.DecimalField(max_length=8,max_digits=7,decimal_places=2)
    picture = models.ImageField(verbose_name='汽车图片',upload_to='img/car')
    formalities = models.BooleanField(verbose_name='手续是否齐全',default=False)
    debt = models.BooleanField(verbose_name='是否有债务',default=False)
    promise =models.TextField(verbose_name='卖家承诺',default=False)
    status = models.IntegerField('审核状态',choices=CAR_STATUS,default=2)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.user.username