from django.db import models


class Partner(models.Model):     # 合作商表

    partner_id = models.AutoField(primary_key=True, auto_created=True)  # 合作商id
    partname = models.CharField(max_length=20)      # 合作商名称
    password = models.CharField(max_length=20)      # 密码
    address = models.TextField(null=True, default="暂未填写")   # 地址

    class Meta:
        db_table = 'partner'       # 数据库表名


class TicketInfo(models.Model):     # 票务信息表

    TYPE_CHOICES = [(1, '演唱会'), (2, '话剧歌剧'),
                    (3, '音乐会'), (4, '展览休闲'),
                    (4, '舞蹈'), (6, '其他')]
    STAUTS_CHOICES = [(1, '在售中'), (2, '已售罄'), (3, '暂停销售')]

    ticket_id = models.AutoField(primary_key=True, auto_created=True)   # 票务信息id
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)   # 关联所属合作商
    infoname = models.TextField()       # 演出名称
    address = models.TextField()        # 演出地址
    tictype = models.IntegerField(choices=TYPE_CHOICES)     # 类型选择
    show_time = models.DateTimeField()  # 演出时间
    peice = models.FloatField()         # 单张价格
    status = models.IntegerField(choices=STAUTS_CHOICES, default=1)     # 销售状态
    total = models.IntegerField()       # 总量
    surplus = models.IntegerField()     # 剩余票数

    class Meta:
        db_table = 'ticket'       # 数据库表名



