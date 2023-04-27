from .Mixin import TimestampMixin, fields


class Tag(TimestampMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from .article import Article
        articles: fields.ManyToManyRelation[Article]

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True, null=False, description="标签名")
    is_show = fields.IntField(default=1, description="是否显示 0否 1是")

    class Meta:
        table = "restart_tag"
        table_description = "标签表"
