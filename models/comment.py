from tortoise import models, fields


class Comment(models.Model):
    id = fields.IntField(pk=True, description="Comment ID")
    cid = fields.IntField(default=0, description="评论父组级")
    ArticleID = fields.IntField(null=False, description="文章ID")
    talkUser = fields.CharField(max_length=25, description="被评论用户")
    type = fields.CharField(max_length=50, null=False, description="评论类型")
    content = fields.TextField(null=False, description="评论内容")
    email = fields.CharField(max_length=50, null=False, description="邮箱")
    nickname = fields.CharField(max_length=25, null=False, description="用户名称")
    website = fields.CharField(max_length=50, null=False, description="网站")
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')

    class Meta:
        table = "comment"
        table_description = "评论表"

