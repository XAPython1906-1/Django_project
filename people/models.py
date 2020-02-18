from django.db import models
from partner.models import TicketInfo


class User(models.Model):       # 用户表

    USER_CHOICES = [(1, '管理员'), (2, '用户')]

    user_id = models.AutoField(primary_key=True, auto_created=True)  # 用户id
    username = models.CharField(max_length=20)      # 使用者名称
    password = models.CharField(max_length=20)      # 密码
    status = models.IntegerField(choices=USER_CHOICES, default=2)   # 类型
    phone_number = models.CharField(max_length=11, null=True)       # 电话号码
    user_number = models.CharField(max_length=18, null=True)        # 身份证号码
    address = models.TextField(null=True, default="暂未填写")       # 地址

    class Meta:
        db_table = 'user'       # 数据库表名


class Order(models.Model):      # 订单表

    PAID_CHOICES = [(1, '未支付'), (2, '已支付'), (3, '已取消')]

    order_id = models.AutoField(primary_key=True, auto_created=True)        # 订单id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)      # 关联用户
    ticket_id = models.ForeignKey(TicketInfo, on_delete=models.CASCADE)     # 关联票务信息
    number = models.IntegerField(default=1)     # 购买数量
    status = models.IntegerField(choices=PAID_CHOICES, default=1)   # 订单状态
    create_time = models.DateTimeField(auto_now_add=True)     # 创建时间
    update_time = models.DateTimeField(auto_now=True)        # 更新时间

    class Meta:
        db_table = 'order'       # 数据库表名






