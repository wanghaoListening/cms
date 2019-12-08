CREATE TABLE `cms_category` (
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `c_name` VARCHAR(64) NOT NULL DEFAULT '' COMMENT '文章类目名称',
  `c_desc` VARCHAR(256) NOT NULL DEFAULT '' COMMENT '文章类目描述',
  `gmt_create` TIMESTAMP NOT NULL DEFAULT '1971-01-01 00:00:00' COMMENT '记录生成时间',
  `gmt_Modify` TIMESTAMP NOT NULL DEFAULT '1971-01-01 00:00:00' COMMENT '记录修改时间',
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文章类目表';


CREATE TABLE `cms_item` (
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `i_content` VARCHAR(512) NOT NULL DEFAULT '' COMMENT '文章内容',
  `c_id` BIGINT(20) NOT NULL COMMENT '所属类目id',
  `gmt_create` TIMESTAMP NOT NULL DEFAULT '1971-01-01 00:00:00' COMMENT '记录生成时间',
  `gmt_Modify` TIMESTAMP NOT NULL DEFAULT '1971-01-01 00:00:00' COMMENT '记录修改时间',
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文章表';


insert into cms_category (id,c_name,c_desc,gmt_create,gmt_Modify) values(null,'科学技术','专 注中外前沿科技',curdate(),curdate());
insert into cms_category (id,c_name,c_desc,gmt_create,gmt_Modify) values(null,'电影鉴赏','中 外经典电影评价文章',curdate(),curdate());