from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `restart_article` (
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `title` VARCHAR(100) NOT NULL  COMMENT '标题',
    `description` VARCHAR(150) NOT NULL  COMMENT '摘要',
    `content` LONGTEXT NOT NULL  COMMENT '内容',
    `is_top` INT NOT NULL  COMMENT '是否置顶 0否 1是' DEFAULT 0,
    `is_show` INT NOT NULL  COMMENT '是否显示 0否 1是' DEFAULT 0,
    `img_src` VARCHAR(255)   COMMENT '图片地址',
    `views` INT NOT NULL  COMMENT '浏览次数',
    `font_count` INT NOT NULL  COMMENT '字数统计'
) CHARACTER SET utf8mb4 COMMENT='文章表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
