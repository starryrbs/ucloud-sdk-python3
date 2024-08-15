""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.udns.schemas import models

""" UDNS API Schema
"""


"""
API: AssociateUDNSZoneVPC

绑定域名与VPC
"""


class AssociateUDNSZoneVPCRequestSchema(schema.RequestSchema):
    """AssociateUDNSZoneVPC - 绑定域名与VPC"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "VPCProjectId": fields.Str(required=True, dump_to="VPCProjectId"),
    }


class AssociateUDNSZoneVPCResponseSchema(schema.ResponseSchema):
    """AssociateUDNSZoneVPC - 绑定域名与VPC"""

    fields = {}


"""
API: CreateUDNSRecord

创建域名记录
"""


class CreateUDNSRecordRequestSchema(schema.RequestSchema):
    """CreateUDNSRecord - 创建域名记录"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "TTL": fields.Int(required=False, dump_to="TTL"),
        "Type": fields.Str(required=True, dump_to="Type"),
        "Value": fields.Str(required=True, dump_to="Value"),
        "ValueType": fields.Str(required=True, dump_to="ValueType"),
    }


class CreateUDNSRecordResponseSchema(schema.ResponseSchema):
    """CreateUDNSRecord - 创建域名记录"""

    fields = {
        "DNSRecordId": fields.Str(required=True, load_from="DNSRecordId"),
    }


"""
API: CreateUDNSZone

创建域名
"""


class CreateUDNSZoneRequestSchema(schema.RequestSchema):
    """CreateUDNSZone - 创建域名"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "DNSZoneName": fields.Str(required=True, dump_to="DNSZoneName"),
        "IsRecursionEnabled": fields.Str(
            required=False, dump_to="IsRecursionEnabled"
        ),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Type": fields.Str(required=True, dump_to="Type"),
    }


class CreateUDNSZoneResponseSchema(schema.ResponseSchema):
    """CreateUDNSZone - 创建域名"""

    fields = {
        "DNSZoneId": fields.Str(required=True, load_from="DNSZoneId"),
    }


"""
API: DeleteUDNSRecord

删除域名记录
"""


class DeleteUDNSRecordRequestSchema(schema.RequestSchema):
    """DeleteUDNSRecord - 删除域名记录"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "RecordIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DeleteUDNSRecordResponseSchema(schema.ResponseSchema):
    """DeleteUDNSRecord - 删除域名记录"""

    fields = {}


"""
API: DescribeUDNSDomain

zone下所有域名的rr记录
"""


class DescribeUDNSDomainRequestSchema(schema.RequestSchema):
    """DescribeUDNSDomain - zone下所有域名的rr记录"""

    fields = {
        "DNSZoneName": fields.Str(required=True, dump_to="DNSZoneName"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
    }


class DescribeUDNSDomainResponseSchema(schema.ResponseSchema):
    """DescribeUDNSDomain - zone下所有域名的rr记录"""

    fields = {
        "RecordInfos": fields.List(
            models.RecordInfoSchema(), required=True, load_from="RecordInfos"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeUDNSRecord

获取域名记录
"""


class DescribeUDNSRecordRequestSchema(schema.RequestSchema):
    """DescribeUDNSRecord - 获取域名记录"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "RecordIds": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeUDNSRecordResponseSchema(schema.ResponseSchema):
    """DescribeUDNSRecord - 获取域名记录"""

    fields = {
        "RecordInfos": fields.List(
            models.RecordInfoSchema(), required=False, load_from="RecordInfos"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DescribeUDNSZone

获取域名信息
"""


class DescribeUDNSZoneRequestSchema(schema.RequestSchema):
    """DescribeUDNSZone - 获取域名信息"""

    fields = {
        "DNSZoneIds": fields.List(fields.Str()),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class DescribeUDNSZoneResponseSchema(schema.ResponseSchema):
    """DescribeUDNSZone - 获取域名信息"""

    fields = {
        "DNSZoneInfos": fields.List(
            models.ZoneInfoSchema(), required=False, load_from="DNSZoneInfos"
        ),
        "TotalCount": fields.Int(required=True, load_from="TotalCount"),
    }


"""
API: DisassociateUDNSZoneVPC

解绑域名和VPC
"""


class DisassociateUDNSZoneVPCRequestSchema(schema.RequestSchema):
    """DisassociateUDNSZoneVPC - 解绑域名和VPC"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "VPCProjectId": fields.Str(required=True, dump_to="VPCProjectId"),
    }


class DisassociateUDNSZoneVPCResponseSchema(schema.ResponseSchema):
    """DisassociateUDNSZoneVPC - 解绑域名和VPC"""

    fields = {}


"""
API: ModifyUDNSRecord

修改域名记录
"""


class ModifyUDNSRecordRequestSchema(schema.RequestSchema):
    """ModifyUDNSRecord - 修改域名记录"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "RecordId": fields.Str(required=True, dump_to="RecordId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "TTL": fields.Int(required=False, dump_to="TTL"),
        "Value": fields.Str(required=False, dump_to="Value"),
        "ValueType": fields.Str(required=False, dump_to="ValueType"),
    }


class ModifyUDNSRecordResponseSchema(schema.ResponseSchema):
    """ModifyUDNSRecord - 修改域名记录"""

    fields = {}


"""
API: ModifyUDNSZone

修改域名备注/递归查询状态
"""


class ModifyUDNSZoneRequestSchema(schema.RequestSchema):
    """ModifyUDNSZone - 修改域名备注/递归查询状态"""

    fields = {
        "DNSZoneId": fields.Str(required=True, dump_to="DNSZoneId"),
        "IsRecursionEnabled": fields.Str(
            required=False, dump_to="IsRecursionEnabled"
        ),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class ModifyUDNSZoneResponseSchema(schema.ResponseSchema):
    """ModifyUDNSZone - 修改域名备注/递归查询状态"""

    fields = {}
