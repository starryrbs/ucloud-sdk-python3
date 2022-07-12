""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.ucdn.schemas import models

""" UCDN API Schema
"""


"""
API: AddCertificate

添加证书
"""


class AddCertificateRequestSchema(schema.RequestSchema):
    """AddCertificate - 添加证书"""

    fields = {
        "CaCert": fields.Str(required=False, dump_to="CaCert"),
        "CertName": fields.Str(required=True, dump_to="CertName"),
        "PrivateKey": fields.Str(required=True, dump_to="PrivateKey"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UserCert": fields.Str(required=True, dump_to="UserCert"),
    }


class AddCertificateResponseSchema(schema.ResponseSchema):
    """AddCertificate - 添加证书"""

    fields = {}


"""
API: BatchDescribeNewUcdnDomain

批量获取加速域名配置
"""


class BatchDescribeNewUcdnDomainRequestSchema(schema.RequestSchema):
    """BatchDescribeNewUcdnDomain - 批量获取加速域名配置"""

    fields = {
        "ChannelType": fields.Str(required=False, dump_to="ChannelType"),
        "DomainId": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class BatchDescribeNewUcdnDomainResponseSchema(schema.ResponseSchema):
    """BatchDescribeNewUcdnDomain - 批量获取加速域名配置"""

    fields = {
        "Arrearage": fields.List(
            fields.Str(), required=False, load_from="Arrearage"
        ),
        "ChargeType": fields.Int(required=False, load_from="ChargeType"),
        "DomainSet": fields.List(
            models.DomainInfoSchema(), required=False, load_from="DomainSet"
        ),
        "LastChargeType": fields.Int(
            required=False, load_from="LastChargeType"
        ),
        "MaxDomainNum": fields.Int(required=False, load_from="MaxDomainNum"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "Vip": fields.Str(required=False, load_from="Vip"),
    }


"""
API: BatchRefreshNewUcdnDomainCache

批量刷新缓存
"""


class BatchRefreshNewUcdnDomainCacheRequestSchema(schema.RequestSchema):
    """BatchRefreshNewUcdnDomainCache - 批量刷新缓存"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "UrlList": fields.Str(required=True, dump_to="UrlList"),
    }


class BatchRefreshNewUcdnDomainCacheResponseSchema(schema.ResponseSchema):
    """BatchRefreshNewUcdnDomainCache - 批量刷新缓存"""

    fields = {
        "TaskId": fields.Str(required=False, load_from="TaskId"),
    }


"""
API: ControlUcdnDomainCacheAccess

封禁解封缓存访问
"""


class ControlUcdnDomainCacheAccessRequestSchema(schema.RequestSchema):
    """ControlUcdnDomainCacheAccess - 封禁解封缓存访问"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "UrlList": fields.List(fields.Str()),
    }


class ControlUcdnDomainCacheAccessResponseSchema(schema.ResponseSchema):
    """ControlUcdnDomainCacheAccess - 封禁解封缓存访问"""

    fields = {}


"""
API: DeleteCertificate

删除证书
"""


class DeleteCertificateRequestSchema(schema.RequestSchema):
    """DeleteCertificate - 删除证书"""

    fields = {
        "CertName": fields.Str(required=True, dump_to="CertName"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class DeleteCertificateResponseSchema(schema.ResponseSchema):
    """DeleteCertificate - 删除证书"""

    fields = {}


"""
API: DescribeNewUcdnPrefetchCacheTask

获取预取任务状态
"""


class DescribeNewUcdnPrefetchCacheTaskRequestSchema(schema.RequestSchema):
    """DescribeNewUcdnPrefetchCacheTask - 获取预取任务状态"""

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Status": fields.Str(required=False, dump_to="Status"),
        "TaskId": fields.List(fields.Str()),
    }


class DescribeNewUcdnPrefetchCacheTaskResponseSchema(schema.ResponseSchema):
    """DescribeNewUcdnPrefetchCacheTask - 获取预取任务状态"""

    fields = {
        "TaskList": fields.List(
            models.TaskInfoSchema(), required=False, load_from="TaskList"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeNewUcdnRefreshCacheTask

获取域名刷新任务状态
"""


class DescribeNewUcdnRefreshCacheTaskRequestSchema(schema.RequestSchema):
    """DescribeNewUcdnRefreshCacheTask - 获取域名刷新任务状态"""

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Status": fields.Str(required=False, dump_to="Status"),
        "TaskId": fields.List(fields.Str()),
    }


class DescribeNewUcdnRefreshCacheTaskResponseSchema(schema.ResponseSchema):
    """DescribeNewUcdnRefreshCacheTask - 获取域名刷新任务状态"""

    fields = {
        "TaskList": fields.List(
            models.TaskInfoSchema(), required=False, load_from="TaskList"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetCertificateV2

获取证书列表(新)
"""


class GetCertificateV2RequestSchema(schema.RequestSchema):
    """GetCertificateV2 - 获取证书列表(新)"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetCertificateV2ResponseSchema(schema.ResponseSchema):
    """GetCertificateV2 - 获取证书列表(新)"""

    fields = {
        "CertList": fields.List(
            models.CertListSchema(), required=True, load_from="CertList"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: GetNewUcdnDomainBandwidth

获取域名带宽数据
"""


class GetNewUcdnDomainBandwidthRequestSchema(schema.RequestSchema):
    """GetNewUcdnDomainBandwidth - 获取域名带宽数据"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainBandwidthResponseSchema(schema.ResponseSchema):
    """GetNewUcdnDomainBandwidth - 获取域名带宽数据"""

    fields = {
        "BandwidthList": fields.List(
            models.BandwidthInfoSchema(),
            required=False,
            load_from="BandwidthList",
        ),
        "Traffic": fields.Float(required=False, load_from="Traffic"),
    }


"""
API: GetNewUcdnDomainHitRate

获取域名命中率
"""


class GetNewUcdnDomainHitRateRequestSchema(schema.RequestSchema):
    """GetNewUcdnDomainHitRate - 获取域名命中率"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class GetNewUcdnDomainHitRateResponseSchema(schema.ResponseSchema):
    """GetNewUcdnDomainHitRate - 获取域名命中率"""

    fields = {
        "HitRateList": fields.List(
            models.HitRateInfoSchema(), required=False, load_from="HitRateList"
        ),
    }


"""
API: GetNewUcdnDomainHttpCode

获取域名状态码监控
"""


class GetNewUcdnDomainHttpCodeRequestSchema(schema.RequestSchema):
    """GetNewUcdnDomainHttpCode - 获取域名状态码监控"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainHttpCodeResponseSchema(schema.ResponseSchema):
    """GetNewUcdnDomainHttpCode - 获取域名状态码监控"""

    fields = {
        "HttpCodeDetail": fields.List(
            models.HttpCodeInfoSchema(),
            required=False,
            load_from="HttpCodeDetail",
        ),
    }


"""
API: GetNewUcdnDomainHttpCodeV2

获取域名详细状态码监控
"""


class GetNewUcdnDomainHttpCodeV2RequestSchema(schema.RequestSchema):
    """GetNewUcdnDomainHttpCodeV2 - 获取域名详细状态码监控"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainHttpCodeV2ResponseSchema(schema.ResponseSchema):
    """GetNewUcdnDomainHttpCodeV2 - 获取域名详细状态码监控"""

    fields = {
        "HttpCodeV2Detail": fields.List(
            models.HttpCodeV2DetailSchema(),
            required=False,
            load_from="HttpCodeV2Detail",
        ),
    }


"""
API: GetNewUcdnDomainRequestNum

获取域名请求数
"""


class GetNewUcdnDomainRequestNumRequestSchema(schema.RequestSchema):
    """GetNewUcdnDomainRequestNum - 获取域名请求数"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetNewUcdnDomainRequestNumResponseSchema(schema.ResponseSchema):
    """GetNewUcdnDomainRequestNum - 获取域名请求数"""

    fields = {
        "RequestList": fields.List(
            models.RequestInfoSchema(), required=False, load_from="RequestList"
        ),
    }


"""
API: GetNewUcdnLogRefererStatistics

获取热点referer统计
"""


class GetNewUcdnLogRefererStatisticsRequestSchema(schema.RequestSchema):
    """GetNewUcdnLogRefererStatistics - 获取热点referer统计"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.Str(required=False, dump_to="DomainId"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "OrderBy": fields.Int(required=False, dump_to="OrderBy"),
    }


class GetNewUcdnLogRefererStatisticsResponseSchema(schema.ResponseSchema):
    """GetNewUcdnLogRefererStatistics - 获取热点referer统计"""

    fields = {
        "RefererStatistics": fields.List(
            models.RefererStatisticsSchema(),
            required=False,
            load_from="RefererStatistics",
        ),
    }


"""
API: GetNewUcdnLogUrlStatistics

获取日志url统计
"""


class GetNewUcdnLogUrlStatisticsRequestSchema(schema.RequestSchema):
    """GetNewUcdnLogUrlStatistics - 获取日志url统计"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.Str(required=True, dump_to="DomainId"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "OrderBy": fields.Int(required=False, dump_to="OrderBy"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetNewUcdnLogUrlStatisticsResponseSchema(schema.ResponseSchema):
    """GetNewUcdnLogUrlStatistics - 获取日志url统计"""

    fields = {
        "UrlStatisticsList": fields.List(
            models.UrlStatisticsSchema(),
            required=False,
            load_from="UrlStatisticsList",
        ),
    }


"""
API: GetUcdnDomain95BandwidthV2

获取域名九五峰值带宽数据
"""


class GetUcdnDomain95BandwidthV2RequestSchema(schema.RequestSchema):
    """GetUcdnDomain95BandwidthV2 - 获取域名九五峰值带宽数据"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomain95BandwidthV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnDomain95BandwidthV2 - 获取域名九五峰值带宽数据"""

    fields = {
        "CdnBandwidth": fields.Float(required=False, load_from="CdnBandwidth"),
        "Time": fields.Int(required=True, load_from="Time"),
    }


"""
API: GetUcdnDomainBandwidthV2

获取域名带宽数据(新)
"""


class GetUcdnDomainBandwidthV2RequestSchema(schema.RequestSchema):
    """GetUcdnDomainBandwidthV2 - 获取域名带宽数据(新)"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Primeval": fields.Int(required=False, dump_to="Primeval"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class GetUcdnDomainBandwidthV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainBandwidthV2 - 获取域名带宽数据(新)"""

    fields = {
        "BandwidthTrafficList": fields.List(
            models.BandwidthTrafficInfoSchema(),
            required=False,
            load_from="BandwidthTrafficList",
        ),
    }


"""
API: GetUcdnDomainConfig

批量获取加速域名配置
"""


class GetUcdnDomainConfigRequestSchema(schema.RequestSchema):
    """GetUcdnDomainConfig - 批量获取加速域名配置"""

    fields = {
        "ChannelType": fields.Str(required=False, dump_to="ChannelType"),
        "DomainId": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainConfigResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainConfig - 批量获取加速域名配置"""

    fields = {
        "DomainList": fields.List(
            models.DomainConfigInfoSchema(),
            required=True,
            load_from="DomainList",
        ),
    }


"""
API: GetUcdnDomainHitRate

获取域名命中率
"""


class GetUcdnDomainHitRateRequestSchema(schema.RequestSchema):
    """GetUcdnDomainHitRate - 获取域名命中率"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "HitType": fields.Int(required=False, dump_to="HitType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainHitRateResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainHitRate - 获取域名命中率"""

    fields = {
        "HitRateList": fields.List(
            models.HitRateInfoV2Schema(),
            required=False,
            load_from="HitRateList",
        ),
    }


"""
API: GetUcdnDomainHttpCodeV2

获取域名状态码信息
"""


class GetUcdnDomainHttpCodeV2RequestSchema(schema.RequestSchema):
    """GetUcdnDomainHttpCodeV2 - 获取域名状态码信息"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "Layer": fields.Str(required=False, dump_to="Layer"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainHttpCodeV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainHttpCodeV2 - 获取域名状态码信息"""

    fields = {
        "HttpCodeDetail": fields.List(
            models.HttpCodeInfoV2Schema(),
            required=False,
            load_from="HttpCodeDetail",
        ),
    }


"""
API: GetUcdnDomainInfoList

获取域名基本信息
"""


class GetUcdnDomainInfoListRequestSchema(schema.RequestSchema):
    """GetUcdnDomainInfoList - 获取域名基本信息"""

    fields = {
        "PageIndex": fields.Int(required=False, dump_to="PageIndex"),
        "PageSize": fields.Int(required=False, dump_to="PageSize"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainInfoListResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainInfoList - 获取域名基本信息"""

    fields = {
        "DomainInfoList": fields.List(
            models.DomainBaseInfoSchema(),
            required=True,
            load_from="DomainInfoList",
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: GetUcdnDomainLog

获取加速域名原始日志
"""


class GetUcdnDomainLogRequestSchema(schema.RequestSchema):
    """GetUcdnDomainLog - 获取加速域名原始日志"""

    fields = {
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class GetUcdnDomainLogResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainLog - 获取加速域名原始日志"""

    fields = {
        "LogSet": fields.List(
            models.LogSetListSchema(), required=False, load_from="LogSet"
        ),
    }


"""
API: GetUcdnDomainLogV2

获取域名5分钟日志
"""


class GetUcdnDomainLogV2RequestSchema(schema.RequestSchema):
    """GetUcdnDomainLogV2 - 获取域名5分钟日志"""

    fields = {
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainLogV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainLogV2 - 获取域名5分钟日志"""

    fields = {
        "DomainLogSet": fields.List(
            models.DomanLogListSchema(), required=True, load_from="DomainLogSet"
        ),
    }


"""
API: GetUcdnDomainOriginHttpCode

获取域名源站状态码监控
"""


class GetUcdnDomainOriginHttpCodeRequestSchema(schema.RequestSchema):
    """GetUcdnDomainOriginHttpCode - 获取域名源站状态码监控"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainOriginHttpCodeResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainOriginHttpCode - 获取域名源站状态码监控"""

    fields = {
        "HttpCodeDetail": fields.List(
            models.HttpCodeInfoSchema(),
            required=False,
            load_from="HttpCodeDetail",
        ),
    }


"""
API: GetUcdnDomainOriginHttpCodeDetail

获取域名源站详细状态码监控
"""


class GetUcdnDomainOriginHttpCodeDetailRequestSchema(schema.RequestSchema):
    """GetUcdnDomainOriginHttpCodeDetail - 获取域名源站详细状态码监控"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainOriginHttpCodeDetailResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainOriginHttpCodeDetail - 获取域名源站详细状态码监控"""

    fields = {
        "HttpCodeV2Detail": fields.List(
            models.HttpCodeV2DetailSchema(),
            required=False,
            load_from="HttpCodeV2Detail",
        ),
    }


"""
API: GetUcdnDomainOriginRequestNum

获取域名回源请求数
"""


class GetUcdnDomainOriginRequestNumRequestSchema(schema.RequestSchema):
    """GetUcdnDomainOriginRequestNum - 获取域名回源请求数"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainOriginRequestNumResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainOriginRequestNum - 获取域名回源请求数"""

    fields = {
        "RequestList": fields.List(
            models.RequestInfoV2Schema(),
            required=False,
            load_from="RequestList",
        ),
    }


"""
API: GetUcdnDomainPrefetchEnable

获取域名预取开启状态
"""


class GetUcdnDomainPrefetchEnableRequestSchema(schema.RequestSchema):
    """GetUcdnDomainPrefetchEnable - 获取域名预取开启状态"""

    fields = {
        "DomainId": fields.Str(required=True, dump_to="DomainId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainPrefetchEnableResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainPrefetchEnable - 获取域名预取开启状态"""

    fields = {
        "Enable": fields.Int(required=False, load_from="Enable"),
    }


"""
API: GetUcdnDomainRequestNumV2

获取域名请求数
"""


class GetUcdnDomainRequestNumV2RequestSchema(schema.RequestSchema):
    """GetUcdnDomainRequestNumV2 - 获取域名请求数"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainRequestNumV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainRequestNumV2 - 获取域名请求数"""

    fields = {
        "RequestList": fields.List(
            models.RequestInfoSchema(), required=False, load_from="RequestList"
        ),
    }


"""
API: GetUcdnDomainRequestNumV3

获取域名请求数
"""


class GetUcdnDomainRequestNumV3RequestSchema(schema.RequestSchema):
    """GetUcdnDomainRequestNumV3 - 获取域名请求数"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Protocol": fields.Str(required=False, dump_to="Protocol"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnDomainRequestNumV3ResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainRequestNumV3 - 获取域名请求数"""

    fields = {
        "RequestList": fields.List(
            models.RequestInfoV2Schema(),
            required=False,
            load_from="RequestList",
        ),
    }


"""
API: GetUcdnDomainTraffic

获取加速域名流量使用信息
"""


class GetUcdnDomainTrafficRequestSchema(schema.RequestSchema):
    """GetUcdnDomainTraffic - 获取加速域名流量使用信息"""

    fields = {
        "AccountType": fields.Str(required=False, dump_to="AccountType"),
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnDomainTrafficResponseSchema(schema.ResponseSchema):
    """GetUcdnDomainTraffic - 获取加速域名流量使用信息"""

    fields = {
        "TrafficSet": fields.List(
            models.UcdnDomainTrafficSetSchema(),
            required=False,
            load_from="TrafficSet",
        ),
    }


"""
API: GetUcdnPassBandwidth

获取回源带宽数据（cdn回客户源站部分）
"""


class GetUcdnPassBandwidthRequestSchema(schema.RequestSchema):
    """GetUcdnPassBandwidth - 获取回源带宽数据（cdn回客户源站部分）"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnPassBandwidthResponseSchema(schema.ResponseSchema):
    """GetUcdnPassBandwidth - 获取回源带宽数据（cdn回客户源站部分）"""

    fields = {
        "BandwidthDetail": fields.List(
            models.BandwidthInfoDetailSchema(),
            required=False,
            load_from="BandwidthDetail",
        ),
    }


"""
API: GetUcdnPassBandwidthV2

获取回源带宽数据（cdn回客户源站部分）
"""


class GetUcdnPassBandwidthV2RequestSchema(schema.RequestSchema):
    """GetUcdnPassBandwidthV2 - 获取回源带宽数据（cdn回客户源站部分）"""

    fields = {
        "Areacode": fields.Str(required=False, dump_to="Areacode"),
        "BeginTime": fields.Int(required=False, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnPassBandwidthV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnPassBandwidthV2 - 获取回源带宽数据（cdn回客户源站部分）"""

    fields = {
        "BandwidthList": fields.List(
            models.BandwidthInfoDetailSchema(),
            required=False,
            load_from="BandwidthList",
        ),
    }


"""
API: GetUcdnProIspBandwidthV2

按省份运营商获取域名带宽数据
"""


class GetUcdnProIspBandwidthV2RequestSchema(schema.RequestSchema):
    """GetUcdnProIspBandwidthV2 - 按省份运营商获取域名带宽数据"""

    fields = {
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "Isp": fields.Str(required=False, dump_to="Isp"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Province": fields.List(fields.Str()),
        "Type": fields.Int(required=True, dump_to="Type"),
    }


class GetUcdnProIspBandwidthV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnProIspBandwidthV2 - 按省份运营商获取域名带宽数据"""

    fields = {
        "BandwidthSet": fields.List(
            models.ProIspBandwidthSetSchema(),
            required=True,
            load_from="BandwidthSet",
        ),
    }


"""
API: GetUcdnProIspRequestNumV2

按省份运营商获取域名请求数
"""


class GetUcdnProIspRequestNumV2RequestSchema(schema.RequestSchema):
    """GetUcdnProIspRequestNumV2 - 按省份运营商获取域名请求数"""

    fields = {
        "BeginTime": fields.Int(required=True, dump_to="BeginTime"),
        "DomainId": fields.List(fields.Str()),
        "EndTime": fields.Int(required=True, dump_to="EndTime"),
        "Isp": fields.Str(required=False, dump_to="Isp"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Province": fields.List(fields.Str()),
        "Type": fields.Int(required=False, dump_to="Type"),
    }


class GetUcdnProIspRequestNumV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnProIspRequestNumV2 - 按省份运营商获取域名请求数"""

    fields = {
        "RequestNumSet": fields.List(
            models.ProIspRequestNumSetV2Schema(),
            required=True,
            load_from="RequestNumSet",
        ),
    }


"""
API: GetUcdnTraffic

获取流量信息
"""


class GetUcdnTrafficRequestSchema(schema.RequestSchema):
    """GetUcdnTraffic - 获取流量信息"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnTrafficResponseSchema(schema.ResponseSchema):
    """GetUcdnTraffic - 获取流量信息"""

    fields = {
        "TrafficSet": fields.List(
            models.TrafficSetSchema(), required=False, load_from="TrafficSet"
        ),
    }


"""
API: GetUcdnTrafficV2

获取流量信息
"""


class GetUcdnTrafficV2RequestSchema(schema.RequestSchema):
    """GetUcdnTrafficV2 - 获取流量信息"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetUcdnTrafficV2ResponseSchema(schema.ResponseSchema):
    """GetUcdnTrafficV2 - 获取流量信息"""

    fields = {
        "TrafficSet": fields.List(
            models.TrafficSetSchema(), required=False, load_from="TrafficSet"
        ),
    }


"""
API: PrefetchNewUcdnDomainCache

提交预取任务
"""


class PrefetchNewUcdnDomainCacheRequestSchema(schema.RequestSchema):
    """PrefetchNewUcdnDomainCache - 提交预取任务"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "UrlList": fields.List(fields.Str()),
    }


class PrefetchNewUcdnDomainCacheResponseSchema(schema.ResponseSchema):
    """PrefetchNewUcdnDomainCache - 提交预取任务"""

    fields = {
        "TaskId": fields.Str(required=False, load_from="TaskId"),
    }


"""
API: QueryIpLocation

查询IP信息
"""


class QueryIpLocationRequestSchema(schema.RequestSchema):
    """QueryIpLocation - 查询IP信息"""

    fields = {
        "Ip": fields.List(fields.Str()),
    }


class QueryIpLocationResponseSchema(schema.ResponseSchema):
    """QueryIpLocation - 查询IP信息"""

    fields = {
        "Data": fields.List(
            models.IpLocationInfoSchema(), required=True, load_from="Data"
        ),
    }


"""
API: RefreshNewUcdnDomainCache

刷新缓存
"""


class RefreshNewUcdnDomainCacheRequestSchema(schema.RequestSchema):
    """RefreshNewUcdnDomainCache - 刷新缓存"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "UrlList": fields.List(fields.Str()),
    }


class RefreshNewUcdnDomainCacheResponseSchema(schema.ResponseSchema):
    """RefreshNewUcdnDomainCache - 刷新缓存"""

    fields = {
        "TaskId": fields.Str(required=False, load_from="TaskId"),
    }


"""
API: SwitchUcdnChargeType

切换账号计费方式
"""


class SwitchUcdnChargeTypeRequestSchema(schema.RequestSchema):
    """SwitchUcdnChargeType - 切换账号计费方式"""

    fields = {
        "ChargeType": fields.Str(required=True, dump_to="ChargeType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class SwitchUcdnChargeTypeResponseSchema(schema.ResponseSchema):
    """SwitchUcdnChargeType - 切换账号计费方式"""

    fields = {}


"""
API: UpdateUcdnDomainStatus

更新加速域名状态
"""


class UpdateUcdnDomainStatusRequestSchema(schema.RequestSchema):
    """UpdateUcdnDomainStatus - 更新加速域名状态"""

    fields = {
        "DomainId": fields.Str(required=True, dump_to="DomainId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Status": fields.Str(required=True, dump_to="Status"),
    }


class UpdateUcdnDomainStatusResponseSchema(schema.ResponseSchema):
    """UpdateUcdnDomainStatus - 更新加速域名状态"""

    fields = {}
