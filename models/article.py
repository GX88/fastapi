from .Mixin import TimestampMixin, fields
from .tags import Tag


class Article(TimestampMixin):
    id = fields.IntField(pk=True, description="主键")
    title = fields.CharField(max_length=100, description="标题")
    description = fields.CharField(max_length=150, description="摘要")
    content = fields.TextField(description="内容")
    tags: fields.ManyToManyRelation[Tag] = fields.ManyToManyField(
        'base.Tag', related_name='articles', through='article_tag', description="文章标签中间表", on_delete="CASCADE"
    )
    is_top = fields.CharField(max_length=1, default=0, description="是否置顶 0否 1是")
    is_show = fields.CharField(max_length=1, default=1, description="是否显示 0否 1是")
    img_src = fields.CharField(max_length=255, null=True, description="图片地址")
    views = fields.IntField(description="浏览次数")
    font_count = fields.IntField(description="字数统计")

    class Meta:
        table = "restart_article"
        table_description = "文章表"
