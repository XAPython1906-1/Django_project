from django.db import models

from partner.models import TicketInfo
from people.models import Order


class Evaluate(models.Model):       # 评价表

    evaluate_id = models.AutoField(primary_key=True, auto_created=True)     # 评价id
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)   # 关联订单
    text = models.TextField()   # 评价内容
    reply_peoplr = models.CharField(max_length=20, null=True)      # 回复人
    reply_text = models.TextField(null=True)     # 回复内容
    create_time = models.DateTimeField(auto_now_add=True)     # 创建时间
    update_time = models.DateTimeField(auto_now=True)        # 回复时间

    class Meta:
        db_table = 'evaluate'       # 数据库表名


class Complaint(models.Model):      # 投诉表
    complaint_id = models.AutoField(primary_key=True, auto_created=True)    # 投诉id
    comname = models.CharField(max_length=20, null=True, default='匿名')    # 投诉人
    ticket_id = models.ForeignKey(TicketInfo, on_delete=models.CASCADE)     # 关联票务信息
    text = models.TextField()   # 投诉内容
    reply_peoplr = models.CharField(max_length=20, null=True)      # 回复人
    reply_text = models.TextField(null=True)     # 回复内容
    create_time = models.DateTimeField(auto_now_add=True)     # 创建时间
    update_time = models.DateTimeField(auto_now=True)        # 回复时间

    class Meta:
        db_table = 'complaint'       # 数据库表名







