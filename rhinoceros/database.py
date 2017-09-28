#coding:utf-8

SQL_DATABASE="""

CREATE TABLE public.access_mo (
  mo_id CHARACTER VARYING(20) NOT NULL, -- 位置监控对象编号
  provider CHARACTER VARYING(10) NOT NULL, -- 接入类型
  create_time INTEGER NOT NULL, -- 创建时间
  data JSONB -- 外带附加数据,
  PRIMARY KEY (mo_id, provider)
);
CREATE UNIQUE INDEX access_mo_mo_id_uindex ON access_mo USING BTREE (mo_id);
CREATE INDEX access_mo_provider_index ON access_mo USING BTREE (provider);
CREATE INDEX access_mo_create_time_index ON access_mo USING BTREE (create_time);
COMMENT ON TABLE public.access_mo IS '移动对象列表';
COMMENT ON COLUMN public.access_mo.mo_id IS '位置监控对象编号';
COMMENT ON COLUMN public.access_mo.provider IS '接入类型';
COMMENT ON COLUMN public.access_mo.create_time IS '创建时间';
COMMENT ON COLUMN public.access_mo.data IS '外带附加数据';

"""