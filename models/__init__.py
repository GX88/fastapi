from tortoise.contrib.pydantic import pydantic_model_creator

from .config import Config
from .mail import EmailTemplate
from .article import Article
from .comment import Comment
from .log import Log
from .tags import Tag

ConfigAll = pydantic_model_creator(Config)
EmailAll = pydantic_model_creator(EmailTemplate)
