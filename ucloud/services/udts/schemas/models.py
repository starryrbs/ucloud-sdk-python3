""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class CheckResultItemSchema(schema.ResponseSchema):
    """CheckResultItem - 预检查结果项"""

    fields = {
        "ErrMessage": fields.Str(required=True, load_from="ErrMessage"),
        "State": fields.Str(required=True, load_from="State"),
    }


class CheckResultSchema(schema.ResponseSchema):
    """CheckResult - 预检查结果"""

    fields = {
        "Config": CheckResultItemSchema(),
        "Connection": CheckResultItemSchema(),
        "Privileges": CheckResultItemSchema(),
    }


class CheckUDTSTaskResultSchema(schema.ResponseSchema):
    """CheckUDTSTaskResult - 预检查返回的结果"""

    fields = {
        "Source": CheckResultSchema(),
        "Target": CheckResultSchema(),
    }


class TaskHistoryItemSchema(schema.ResponseSchema):
    """TaskHistoryItem - 任务历史记录中一条数据对应的 Model"""

    fields = {
        "AntID": fields.Str(required=False, load_from="AntID"),
        "AntState": fields.Str(required=False, load_from="AntState"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "CreateTimeH": fields.Str(required=False, load_from="CreateTimeH"),
    }


class SyncDataSchema(schema.ResponseSchema):
    """SyncData - 增量同步数据"""

    fields = {
        "BinlogGTID": fields.Str(required=False, load_from="BinlogGTID"),
        "BinlogName": fields.Str(required=True, load_from="BinlogName"),
        "BinlogPos": fields.Int(required=True, load_from="BinlogPos"),
        "ServerId": fields.Int(required=True, load_from="ServerId"),
    }


class ProgressSchema(schema.ResponseSchema):
    """Progress - 进度信息"""

    fields = {
        "CurCount": fields.Int(required=False, load_from="CurCount"),
        "CurDuration": fields.Int(required=False, load_from="CurDuration"),
        "Percentage": fields.Float(required=False, load_from="Percentage"),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "TotalDuration": fields.Int(required=False, load_from="TotalDuration"),
    }


class StatusDataSchema(schema.ResponseSchema):
    """StatusData - 动态状态信息"""

    fields = {
        "CurRetryCount": fields.Int(required=False, load_from="CurRetryCount"),
        "FailedMessage": fields.Str(required=False, load_from="FailedMessage"),
        "MaxRetryCount": fields.Int(required=False, load_from="MaxRetryCount"),
        "Progress": ProgressSchema(),
        "Status": fields.Str(required=False, load_from="Status"),
        "Sync": SyncDataSchema(),
    }


class ListDataItemSchema(schema.ResponseSchema):
    """ListDataItem - 返回列表的一个 Task 的信息"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "CurRetryCount": fields.Int(required=False, load_from="CurRetryCount"),
        "MaxRetryCount": fields.Int(required=False, load_from="MaxRetryCount"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Progress": ProgressSchema(),
        "Status": fields.Str(required=False, load_from="Status"),
        "TaskId": fields.Str(required=False, load_from="TaskId"),
        "Type": fields.Str(required=False, load_from="Type"),
    }
