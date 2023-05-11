from .Mixin import TimestampMixin, fields


class Config(TimestampMixin):
    id = fields.IntField(pk=True, description="主键")
    name = fields.CharField(max_length=50, null=False, description="配置名称")
    value = fields.JSONField(null=False, description="配置值")

    class Meta:
        table = "restart_config"
        table_description = "配置表"
