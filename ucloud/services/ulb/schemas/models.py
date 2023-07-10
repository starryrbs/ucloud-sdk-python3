""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class BackendSetSchema(schema.ResponseSchema):
    """BackendSet -"""

    fields = {
        "BackendId": fields.Str(required=True, load_from="BackendId"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
    }


class SSLBindedTargetSetSchema(schema.ResponseSchema):
    """SSLBindedTargetSet - DescribeSSL"""

    fields = {
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
    }


class ULBSSLSetSchema(schema.ResponseSchema):
    """ULBSSLSet - DescribeSSL"""

    fields = {
        "BindedTargetSet": fields.List(SSLBindedTargetSetSchema()),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Domains": fields.Str(required=False, load_from="Domains"),
        "HashValue": fields.Str(required=False, load_from="HashValue"),
        "SSLContent": fields.Str(required=False, load_from="SSLContent"),
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
        "SSLSource": fields.Int(required=False, load_from="SSLSource"),
        "SSLType": fields.Str(required=False, load_from="SSLType"),
        "USSLId": fields.Str(required=False, load_from="USSLId"),
    }


class BindVServerInfoSchema(schema.ResponseSchema):
    """BindVServerInfo - 绑定安全策略的VServer信息"""

    fields = {
        "Port": fields.Int(required=True, load_from="Port"),
        "ULBId": fields.Str(required=True, load_from="ULBId"),
        "VServerId": fields.Str(required=True, load_from="VServerId"),
        "VServerName": fields.Str(required=True, load_from="VServerName"),
    }


class SecurityPolicySchema(schema.ResponseSchema):
    """SecurityPolicy - 安全策略组"""

    fields = {
        "SSLCiphers": fields.List(fields.Str()),
        "SecurityPolicyId": fields.Str(
            required=True, load_from="SecurityPolicyId"
        ),
        "SecurityPolicyName": fields.Str(
            required=True, load_from="SecurityPolicyName"
        ),
        "SecurityPolicyType": fields.Int(
            required=True, load_from="SecurityPolicyType"
        ),
        "TLSVersion": fields.Str(required=True, load_from="TLSVersion"),
        "VServerSet": fields.List(BindVServerInfoSchema()),
    }


class TLSAndCiphersSchema(schema.ResponseSchema):
    """TLSAndCiphers -"""

    fields = {
        "SSLCiphers": fields.List(fields.Str()),
        "TLSVersion": fields.Str(required=False, load_from="TLSVersion"),
    }


class PolicyBackendSetSchema(schema.ResponseSchema):
    """PolicyBackendSet - 内容转发下rs详细信息"""

    fields = {
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ObjectId": fields.Str(required=False, load_from="ObjectId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=False, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),
    }


class ULBBackendSetSchema(schema.ResponseSchema):
    """ULBBackendSet - DescribeULB"""

    fields = {
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "IsBackup": fields.Int(required=False, load_from="IsBackup"),
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=False, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class BindSecurityPolicySchema(schema.ResponseSchema):
    """BindSecurityPolicy - VServer绑定的安全策略组信息"""

    fields = {
        "SSLCiphers": fields.List(fields.Str()),
        "SecurityPolicyId": fields.Str(
            required=False, load_from="SecurityPolicyId"
        ),
        "SecurityPolicyName": fields.Str(
            required=False, load_from="SecurityPolicyName"
        ),
        "SecurityPolicyType": fields.Int(
            required=False, load_from="SecurityPolicyType"
        ),
        "TLSVersion": fields.Str(required=False, load_from="TLSVersion"),
    }


class ULBPolicySetSchema(schema.ResponseSchema):
    """ULBPolicySet - 内容转发详细列表"""

    fields = {
        "BackendSet": fields.List(PolicyBackendSetSchema()),
        "DomainMatchMode": fields.Str(
            required=False, load_from="DomainMatchMode"
        ),
        "Match": fields.Str(required=False, load_from="Match"),
        "PolicyId": fields.Str(required=False, load_from="PolicyId"),
        "PolicyPriority": fields.Int(
            required=False, load_from="PolicyPriority"
        ),
        "PolicyType": fields.Str(required=False, load_from="PolicyType"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "Type": fields.Str(required=False, load_from="Type"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
    }


class LoggerSetSchema(schema.ResponseSchema):
    """LoggerSet - ulb日志信息"""

    fields = {
        "BucketName": fields.Str(required=False, load_from="BucketName"),
        "TokenID": fields.Str(required=False, load_from="TokenID"),
        "TokenName": fields.Str(required=False, load_from="TokenName"),
    }


class ULBVServerSetSchema(schema.ResponseSchema):
    """ULBVServerSet - DescribeULB"""

    fields = {
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "Domain": fields.Str(required=False, load_from="Domain"),
        "EnableCompression": fields.Int(
            required=False, load_from="EnableCompression"
        ),
        "EnableHTTP2": fields.Int(required=False, load_from="EnableHTTP2"),
        "ForwardPort": fields.Int(required=False, load_from="ForwardPort"),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "Method": fields.Str(required=False, load_from="Method"),
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "Path": fields.Str(required=False, load_from="Path"),
        "PersistenceInfo": fields.Str(
            required=False, load_from="PersistenceInfo"
        ),
        "PersistenceType": fields.Str(
            required=True, load_from="PersistenceType"
        ),
        "PolicySet": fields.List(ULBPolicySetSchema()),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "RequestMsg": fields.Str(required=False, load_from="RequestMsg"),
        "ResponseMsg": fields.Str(required=False, load_from="ResponseMsg"),
        "SSLSet": fields.List(ULBSSLSetSchema()),
        "SecurityPolicy": BindSecurityPolicySchema(),
        "Status": fields.Int(required=False, load_from="Status"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
    }


class ULBIPSetSchema(schema.ResponseSchema):
    """ULBIPSet - DescribeULB"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "EIP": fields.Str(required=False, load_from="EIP"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class FirewallSetSchema(schema.ResponseSchema):
    """FirewallSet - ulb防火墙信息"""

    fields = {
        "FirewallId": fields.Str(required=False, load_from="FirewallId"),
        "FirewallName": fields.Str(required=False, load_from="FirewallName"),
    }


class ULBSetSchema(schema.ResponseSchema):
    """ULBSet - DescribeULB"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EnableLog": fields.Int(required=False, load_from="EnableLog"),
        "ExpireTime": fields.Int(
            required=False, load_from="ExpireTime"
        ),  # Deprecated, will be removed at 1.0
        "FirewallSet": fields.List(FirewallSetSchema()),
        "IPSet": fields.List(ULBIPSetSchema()),
        "IPVersion": fields.Str(required=False, load_from="IPVersion"),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "LogSet": LoggerSetSchema(),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Resource": fields.List(
            fields.Str()
        ),  # Deprecated, will be removed at 1.0
        "SnatIps": fields.List(fields.Str()),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(
            required=False, load_from="ULBName"
        ),  # Deprecated, will be removed at 1.0
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VServerSet": fields.List(ULBVServerSetSchema()),
    }


class ULBSimpleSetSchema(schema.ResponseSchema):
    """ULBSimpleSet - ulb简明信息"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EnableLog": fields.Int(required=False, load_from="EnableLog"),
        "FirewallSet": fields.List(FirewallSetSchema()),
        "IPSet": fields.List(ULBIPSetSchema()),
        "IPVersion": fields.Str(required=True, load_from="IPVersion"),
        "ListenType": fields.Str(required=True, load_from="ListenType"),
        "LogSet": LoggerSetSchema(),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "SnatIps": fields.List(fields.Str()),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VServerCount": fields.Int(required=False, load_from="VServerCount"),
        "WAFMode": fields.Str(required=False, load_from="WAFMode"),
    }
