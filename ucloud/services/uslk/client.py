""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing




from ucloud.core.client import Client
from ucloud.services.uslk.schemas import apis









class USLKClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(USLKClient, self).__init__(config, transport, middleware, logger)

    
    
    
    
    
    
    
    def batch_create_uslk_short_link(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ BatchCreateUSLKShortLink - 批量创建短链接【免审】

        **Request**

        - **EndTime** (int) - (Required) 过期时间戳（秒级），传 3376656000 表示生成永久生效短链接
        - **LongLinks** (list) - (Required) 长链接数组，示例: "LongLinks.0": "http://ucloud.cn/0", "LongLinks.1": "http://ucloud.cn/1"
        - **Proto** (str) - (Required) 协议名称：http/https
        - **ScenarioID** (int) - (Required) 场景ID
        - **ShortLinkDomain** (str) - (Required) 短链接域名
        - **StartTime** (int) - (Required) 开始生效时间戳（秒级）, 传 3376656000 表示生成永久生效短链接
        
        **Response**

        - **Message** (str) - Message
        - **ShortLinks** (list) - 创建成功的短链接，根据传LongLinks顺序排列
        
        """
        # build request
        d = {
            
        }
        req and d.update(req)
        d = apis.BatchCreateUSLKShortLinkRequestSchema().dumps(d)
        
        # build options
        kwargs['max_retries'] = 0 # ignore retry when api is not idempotent
        
        resp = self.invoke("BatchCreateUSLKShortLink", d, **kwargs)
        return apis.BatchCreateUSLKShortLinkResponseSchema().loads(resp)
    
    
    
    
    
    
    
    def create_uslk_long_link(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateUSLKLongLink - 报备长链接

        **Request**

        - **LongLink** (str) - (Required) 要报备的长链接
        - **ScenarioID** (int) - (Required) 场景ID
        
        **Response**

        - **LongLinkID** (int) - 长链接ID
        - **Message** (str) - Message
        - **ReqUuid** (str) - ReqUuid
        
        """
        # build request
        d = {
            
        }
        req and d.update(req)
        d = apis.CreateUSLKLongLinkRequestSchema().dumps(d)
        
        # build options
        kwargs['max_retries'] = 0 # ignore retry when api is not idempotent
        
        resp = self.invoke("CreateUSLKLongLink", d, **kwargs)
        return apis.CreateUSLKLongLinkResponseSchema().loads(resp)
    
    
    
    
    
    
    
    def create_uslk_scenario(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateUSLKScenario - 长链接报备场景创建

        **Request**

        - **Scenario** (str) - (Required) 场景名称
        - **ScenarioDesc** (str) - (Required) 场景说明
        
        **Response**

        - **Message** (str) - Message
        - **ReqUuid** (str) - ReqUuid
        - **ScenarioID** (int) - 场景ID
        
        """
        # build request
        d = {
            
        }
        req and d.update(req)
        d = apis.CreateUSLKScenarioRequestSchema().dumps(d)
        
        # build options
        kwargs['max_retries'] = 0 # ignore retry when api is not idempotent
        
        resp = self.invoke("CreateUSLKScenario", d, **kwargs)
        return apis.CreateUSLKScenarioResponseSchema().loads(resp)
    
    
    
    
    
    
    
    def create_uslk_short_link(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateUSLKShortLink - 创建短链接

        **Request**

        - **EndTime** (int) - (Required) 过期时间戳，传 3376656000 表示生成永久生效短链接
        - **LongLinkID** (int) - (Required) 长链接ID，状态必须为审核通过
        - **Proto** (str) - (Required) 协议名称：http/https
        - **StartTime** (int) - (Required) 开始生效时间戳, 传 3376656000 表示生成永久生效短链接
        - **Type** (int) - (Required) 链接类型-预留：普通跳转、随机跳转，当前默认普通跳转 1: 普通跳转
        - **ShortLinkDomain** (str) - 短链接域名，默认：uslk.net
        
        **Response**

        - **Message** (str) - Message
        - **ShortLink** (str) - 生成的短链接内容
        
        """
        # build request
        d = {
            
        }
        req and d.update(req)
        d = apis.CreateUSLKShortLinkRequestSchema().dumps(d)
        
        # build options
        kwargs['max_retries'] = 0 # ignore retry when api is not idempotent
        
        resp = self.invoke("CreateUSLKShortLink", d, **kwargs)
        return apis.CreateUSLKShortLinkResponseSchema().loads(resp)
    
    
    
    
    
    
    
    def describe_uslk_redirect_records(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeUSLKRedirectRecords - 查询短链接访问明细列表

        **Request**

        - **EndTime** (int) - (Required) 查询周期结束时间戳(ms级别)
        - **ShortLink** (str) - (Required) 短链接
        - **StartTime** (int) - (Required) 查询周期开始时间戳(ms级别)
        - **FuzzySearch** (str) - 模糊查询字段值，支持根据生成短链接进行模糊查询。支持字段(ShortLink，场景名称)
        - **NumPerPage** (int) - 每页个数，用于分页查找，默认20
        - **OrderBy** (str) - 根据指定字段排序：默认按短链接访问时间：CreateTime 排序
        - **OrderType** (str) - 排序方式。asc-正序 desc-倒序
        - **Page** (int) - 页码，从0开始，用于分页查找
        
        **Response**

        - **Data** (list) - 见 **RedirectRecords** 模型定义
        - **Message** (str) - Message
        - **Total** (int) - 数据总量
        
        **Response Model**
        
        **RedirectRecords** 
        - **AccountID** (int) - 账户ID
        - **Browser** (str) - 访问设备
        - **ClientIP** (str) - 访问IP
        - **Os** (str) - 访问操作系统
        - **ProvinceCode** (str) - 访问省份信息
        - **RedirectTime** (int) - 重定向时间戳 (ms)
        - **RequestTime** (int) - 访问时间戳（ms）
        - **Scenario** (str) - 报备场景
        - **ScenarioID** (int) - 场景ID
        - **ShortLink** (str) - 短链接
        - **ShortLinkDomain** (str) - 短链接域名
        

        """
        # build request
        d = {
            
        }
        req and d.update(req)
        d = apis.DescribeUSLKRedirectRecordsRequestSchema().dumps(d)
        
        resp = self.invoke("DescribeUSLKRedirectRecords", d, **kwargs)
        return apis.DescribeUSLKRedirectRecordsResponseSchema().loads(resp)
    
    
    
    
    
    
    
    def describe_uslk_short_link_list(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeUSLKShortLinkList - 查询短链接列表

        **Request**

        - **EndTime** (int) - 查询周期结束时间戳
        - **FuzzySearch** (str) - 模糊查询字段值，支持根据生成短链接进行模糊查询。支持字段(LonkLink,场景名称)
        - **LongLinkID** (int) - 长链接ID
        - **NumPerPage** (int) - 每页个数，用于分页查找，默认20
        - **OrderBy** (str) - 根据指定字段排序：默认按创建时间：CreateTime 排序，支持值：CreateTime,StartTime,EndTime
        - **OrderType** (str) - 排序方式。asc-正序 desc-倒序
        - **Page** (int) - 页码，从0开始，用于分页查找
        - **ScenarioID** (int) - 场景ID
        - **ShortLink** (str) - 短链
        - **StartTime** (int) - 查询周期开始时间戳
        - **Status** (int) - 1: 待生效；2：已生效；3：已失效；4：已删除（预留）；5：已封禁
        
        **Response**

        - **Data** (list) - 见 **ShortLink** 模型定义
        - **Message** (str) - Message
        
        **Response Model**
        
        **ShortLink** 
        - **ClickCount** (int) - 累计访问量
        - **ClickCountToday** (int) - 当日访问量
        - **CreateTime** (int) - 短链接创建时间
        - **DeleteTime** (int) - 删除时间戳
        - **EndTime** (int) - 短链接过期时间戳
        - **ID** (int) - 短链接ID
        - **LongLinks** (list) - 关联长链接列表
        - **Operator** (str) - 操作人
        - **Remark** (str) - 操作说明(封禁原因)
        - **Scenario** (str) - 报备场景
        - **ScenarioDesc** (str) - 场景描述
        - **ScenarioID** (int) - 场景ID
        - **SecondaryLinks** (list) - 见 **SecondaryLinkForQuery** 模型定义
        - **ShortLink** (str) - 短链接
        - **ShortLinkDomain** (str) - 短链接域名
        - **StartTime** (int) - 短链接开始生效时间戳
        - **Status** (int) - 短链接状态：1: 待生效；2：已生效；3：已失效；4：已删除（预留）；5：已封禁
        - **Type** (int) - 链接类型-预留：1:普通跳转 3:智能跳转等
        - **UniqueClickCount** (int) - 累计独立访问量
        - **UniqueClickCountToday** (int) - 今日独立访问量
        - **UpdateTime** (int) - 更新时间戳
        

        **SecondaryLinkForQuery** 
        - **IsSecondary** (bool) - 是否是次链接
        - **LongLink** (str) - 长链接
        - **LongLinkID** (int) - 长链接ID
        - **Oses** (str) - 操作系统,例如: Windows,Android,多个以逗号分隔
        - **ProvinceCodes** (str) - 省份codes，例如: Hebei,Shandong,多个以逗号分隔
        - **Scenario** (str) - 场景名称
        - **ScenarioID** (int) - 场景ID
        - **ShortLongMapID** (int) - 长短链接映射ID
        

        """
        # build request
        d = {
            
        }
        req and d.update(req)
        d = apis.DescribeUSLKShortLinkListRequestSchema().dumps(d)
        
        resp = self.invoke("DescribeUSLKShortLinkList", d, **kwargs)
        return apis.DescribeUSLKShortLinkListResponseSchema().loads(resp)
    


