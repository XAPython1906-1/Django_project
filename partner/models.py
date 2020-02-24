from django.db import models


class Partner(models.Model):     # 合作商表

    partner_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='合作商id')
    partname = models.CharField(max_length=20, verbose_name='合作商名称')
    password = models.CharField(max_length=100, verbose_name='密码')
    address = models.TextField(null=True, default="暂未填写", verbose_name='地址')

    class Meta:
        db_table = 'partner'       # 数据库表名
        managed = False
        verbose_name_plural = verbose_name = '合作商管理'


class TicketInfo(models.Model):     # 票务信息表

    TYPE_CHOICES = [(1, '演唱会'), (2, '话剧歌剧'),
                    (3, '音乐会'), (4, '展览休闲'),
                    (4, '舞蹈'), (6, '其他')]
    STAUTS_CHOICES = [(1, '在售中'), (2, '已售罄'), (3, '暂停销售')]

    ticket_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='票务信息id')
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='关联所属合作商')
    infoname = models.TextField(verbose_name='演出名称')
    address = models.TextField(verbose_name='演出地址')
    tictype = models.IntegerField(choices=TYPE_CHOICES, verbose_name='类型选择')
    show_time = models.DateTimeField(verbose_name='演出时间')
    peice = models.FloatField(verbose_name='单张价格')
    status = models.IntegerField(choices=STAUTS_CHOICES, default=1, verbose_name='销售状态')
    total = models.IntegerField(verbose_name='总票数')
    surplus = models.IntegerField(verbose_name='剩余票数')

    class Meta:
        db_table = 'ticket'       # 数据库表名
        managed = False
        verbose_name_plural = verbose_name = '票务信息管理'


