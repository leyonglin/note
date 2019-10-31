# Generated by Django 2.2.6 on 2019-10-25 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sale', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.TextField(verbose_name='汽车')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('oderNo', models.CharField(max_length=50, verbose_name='订单号')),
                ('status', models.IntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '取消订单'), (3, '订单失败'), (4, '交易成功'), (5, '交易完成')], default=0, verbose_name='订单状态')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('buser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buser', to=settings.AUTH_USER_MODEL)),
                ('suser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('buser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.CarInfo')),
            ],
        ),
    ]
