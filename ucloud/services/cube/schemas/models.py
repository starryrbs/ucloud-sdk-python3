""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class EIPAddrSchema(schema.ResponseSchema):
    """EIPAddr -"""

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class EIPSetSchema(schema.ResponseSchema):
    """EIPSet -"""

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EIPAddr": fields.List(EIPAddrSchema()),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "PayMode": fields.Str(required=False, load_from="PayMode"),
        "Resource": fields.Str(required=False, load_from="Resource"),
        "Status": fields.Str(required=False, load_from="Status"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class CubeExtendInfoSchema(schema.ResponseSchema):
    """CubeExtendInfo -"""

    fields = {
        "CubeId": fields.Str(required=True, load_from="CubeId"),
        "Eip": fields.List(EIPSetSchema()),
        "Expiration": fields.Int(required=False, load_from="Expiration"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Tag": fields.Str(required=False, load_from="Tag"),
    }


class ValueSetSchema(schema.ResponseSchema):
    """ValueSet -"""

    fields = {
        "Timestamp": fields.Int(required=False, load_from="Timestamp"),
        "Value": fields.Float(required=True, load_from="Value"),
    }


class MetricDataSetSchema(schema.ResponseSchema):
    """MetricDataSet -"""

    fields = {
        "MetricName": fields.Str(required=False, load_from="MetricName"),
        "Values": fields.List(ValueSetSchema()),
    }
