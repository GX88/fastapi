from tortoise import models, fields


class Log(models.Model):
    id = fields.IntField(pk=True, description="主键")
    ip = fields.CharField(max_length=50, description="ip地址")
    method = fields.CharField(max_length=10, description="请求方式")
    path = fields.CharField(max_length=255, description="请求路径")
    status = fields.IntField(description="状态码")
    device = fields.CharField(max_length=50, description="设备信息")
    system = fields.CharField(max_length=50, description="系统信息")
    browser = fields.CharField(max_length=50, description="浏览器信息")
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')

    class Meta:
        table = "restart_log"
        table_description = "日志表"
