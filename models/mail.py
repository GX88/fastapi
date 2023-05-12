from .Mixin import TimestampMixin, fields


class EmailTemplate(TimestampMixin):
    id = fields.IntField(pk=True, description="主键")
    name = fields.CharField(max_length=255, null=False, description="模板名称")
    code = fields.TextField(null=False, description="模板代码")

    class Meta:
        table = "restart_email_template"
        table_description = "邮件模板表"
