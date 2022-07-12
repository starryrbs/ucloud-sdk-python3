""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.udisk.schemas import apis


class UDiskClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UDiskClient, self).__init__(config, transport, middleware, logger)

    def attach_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **UDiskId** (str) - (Required) 需要挂载的UDisk实例ID.
        - **HostId** (str) - Host实例ID
        - **MultiAttach** (str) - 是否允许多点挂载（Yes: 允许多点挂载， No: 不允许多点挂载， 不填默认Yes ）
        - **UHostId** (str) - UHost实例ID。【UHostId和HostId必须选填一个，本字段即将废弃，建议使用HostId】
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **DeviceName** (str) - 挂载的设备名称
        - **HostId** (str) - 挂载的Host实例ID
        - **UDiskId** (str) - 挂载的UDisk实例ID
        - **UHostId** (str) - 挂载的UHost实例ID。【即将废弃，建议使用HostId】

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.AttachUDiskRequestSchema().dumps(d)

        resp = self.invoke("AttachUDisk", d, **kwargs)
        return apis.AttachUDiskResponseSchema().loads(resp)

    def clone_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """CloneUDisk - 从UDisk创建UDisk克隆

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - (Required) 实例名称
        - **SourceId** (str) - (Required) 克隆父Disk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - Year , Month, Dynamic，Postpay，Trial 默认: Month
        - **Comment** (str) - Disk注释
        - **CouponId** (str) - 使用的代金券id
        - **HostId** (str) - Host实例ID。克隆出的云盘可直接挂载到该主机上。
        - **Quantity** (int) - 购买时长 默认: 1
        - **RdmaClusterId** (str) - RDMA集群id。指定RSSD云盘克隆到对应的RDMA集群。
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No
        - **Tag** (str) - 业务组 默认：Default
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No

        **Response**

        - **UDiskId** (list) - 创建UDisk Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CloneUDiskRequestSchema().dumps(d)

        resp = self.invoke("CloneUDisk", d, **kwargs)
        return apis.CloneUDiskResponseSchema().loads(resp)

    def clone_udisk_snapshot(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CloneUDiskSnapshot - 从快照创建UDisk克隆

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - (Required) 实例名称
        - **SourceId** (str) - (Required) 克隆父Snapshot的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - Year , Month, Dynamic，Postpay 默认: Dynamic
        - **Comment** (str) - Disk注释
        - **CouponId** (str) - 使用的代金券id
        - **HostId** (str) - Host实例ID。克隆出的云盘可直接挂载到该主机上。
        - **Quantity** (int) - 购买时长 默认: 1
        - **RdmaClusterId** (str) - RDMA集群id。指定RSSD云盘克隆到对应的RDMA集群。
        - **Size** (int) - 购买UDisk大小,单位:GB,范围[1~8000]。(UDisk大小设定对本地盘快照有效，对云盘快照无效)
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No
        - **Tag** (str) - 业务组 默认：Default
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No

        **Response**

        - **UDiskId** (list) - 创建UDisk Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CloneUDiskSnapshotRequestSchema().dumps(d)

        resp = self.invoke("CloneUDiskSnapshot", d, **kwargs)
        return apis.CloneUDiskSnapshotResponseSchema().loads(resp)

    def clone_udisk_udataark(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CloneUDiskUDataArk - 从数据方舟的备份创建UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - (Required) 实例名称
        - **SnapshotTime** (int) - (Required) 指定从方舟克隆的备份时间点
        - **UDiskId** (str) - (Required) 需要克隆的源盘id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - Year , Month, Dynamic，Postpay 默认: Dynamic
        - **Comment** (str) - Disk注释
        - **CouponId** (str) - 使用的代金券id
        - **HostId** (str) - Host实例ID。克隆出的云盘可直接挂载到该主机上。
        - **Quantity** (int) - 购买时长 默认: 1
        - **RdmaClusterId** (str) - RDMA集群id。指定RSSD云盘克隆到对应的RDMA集群。
        - **Size** (int) - 购买UDisk大小,单位:GB,范围[1~8000]。(UDisk大小设定对本地盘备份有效，对云盘备份无效)
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No
        - **Tag** (str) - 业务组 默认：Default
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No

        **Response**

        - **UDiskId** (list) - 创建UDisk Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CloneUDiskUDataArkRequestSchema().dumps(d)

        resp = self.invoke("CloneUDiskUDataArk", d, **kwargs)
        return apis.CloneUDiskUDataArkResponseSchema().loads(resp)

    def create_attach_udisk(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateAttachUDisk - 创建并挂载UDisk磁盘

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - (Required) 实例名称
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,普通数据盘：范围[1~8000]；SSD数据盘：范围[1~8000]；RSSD数据盘：范围[1~32000]；高效数据盘：范围[1~32000]。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - Year , Month, Dynamic, Postpay, Trial 。 Size小于等于2000时，默认为Dynamic；Size大于2000时，默认为Month。
        - **CmkId** (str) - 加密需要的cmk id，UKmsMode为Yes时，必填
        - **CouponId** (str) - 使用的代金券id
        - **DiskType** (str) - UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），RSSDDataDisk（RSSD数据盘），EfficiencyDataDisk（高效数据盘），默认值（DataDisk）
        - **HostId** (str) - Host实例ID。当创建云盘类型为RSSDDataDisk时，根据传入的HostId，创建与虚机在同一PodId下的云盘。
        - **MultiAttach** (str) - 是否允许多点挂载（Yes: 允许多点挂载， No: 不允许多点挂载， 不填默认Yes ）
        - **Quantity** (int) - 购买时长 默认: 1
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No
        - **Tag** (str) - 业务组 默认：Default
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No
        - **UHostId** (str) - UHost实例ID。当创建云盘类型为RSSDDataDisk时，根据传入的UHostId，创建与虚机在同一PodId下的云盘。【UHostId和HostId必须选填一个，本字段即将废弃，建议使用HostId】
        - **UKmsMode** (str) - 是否加密。Yes：加密，No：不加密，默认值（No）

        **Response**

        - **DeviceName** (str) - 挂载设备名称
        - **HostId** (str) - 挂载的Host实例ID
        - **UDiskId** (str) - 挂载的UDisk实例ID
        - **UHostId** (str) - 挂载的UHost实例ID。【即将废弃，建议使用HostId】

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateAttachUDiskRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateAttachUDisk", d, **kwargs)
        return apis.CreateAttachUDiskResponseSchema().loads(resp)

    def create_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """CreateUDisk - 创建UDisk磁盘

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - (Required) 实例名称
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,普通数据盘：范围[1~8000]；SSD数据盘：范围[1~8000]；RSSD数据盘：范围[1~32000]；高效数据盘：范围[1~32000]。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - Year , Month, Dynamic, Postpay, Trial 。默认为Dynamic。
        - **CmkId** (str) - 加密需要的cmk id，UKmsMode为Yes时，必填
        - **CouponId** (str) - 使用的代金券id
        - **DiskType** (str) - UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），RSSDDataDisk（RSSD数据盘），EfficiencyDataDisk（高效数据盘），默认值（DataDisk）
        - **Quantity** (int) - 购买时长 默认: 1
        - **RdmaClusterId** (str) - RDMA集群id。DiskType为RSSDDataDisk可填，指定云盘创建到对应的RDMA集群。
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No
        - **Tag** (str) - 业务组 默认：Default
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No
        - **UKmsMode** (str) - 是否加密。Yes：加密，No：不加密，默认值（No）

        **Response**

        - **UDiskId** (list) - UDisk实例Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUDiskRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDisk", d, **kwargs)
        return apis.CreateUDiskResponseSchema().loads(resp)

    def create_udisk_snapshot(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUDiskSnapshot - 创建snapshot快照

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Name** (str) - (Required) 快照名称
        - **UDiskId** (str) - (Required) 快照的UDisk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ChargeType** (str) - Year , Month, Dynamic 默认: Dynamic  (已废弃)
        - **Comment** (str) - 快照描述
        - **Quantity** (int) - 购买时长 默认: 1  (已废弃)

        **Response**

        - **SnapshotId** (list) - 快照Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUDiskSnapshotRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUDiskSnapshot", d, **kwargs)
        return apis.CreateUDiskSnapshotResponseSchema().loads(resp)

    def delete_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """DeleteUDisk - 删除UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **UDiskId** (str) - (Required) 要删除的UDisk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteUDiskRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDisk", d, **kwargs)
        return apis.DeleteUDiskResponseSchema().loads(resp)

    def delete_udisk_snapshot(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUDiskSnapshot - 删除Snapshot

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **SnapshotId** (str) - 快照Id(填写后不能填写UDisk Id)
        - **UDiskId** (str) - UDisk Id,删除该盘所创建出来的所有快照(填写后不能填写SnapshotId)

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteUDiskSnapshotRequestSchema().dumps(d)

        resp = self.invoke("DeleteUDiskSnapshot", d, **kwargs)
        return apis.DeleteUDiskSnapshotResponseSchema().loads(resp)

    def describe_recycle_udisk(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeRecycleUDisk - 拉取回收站中云硬盘列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Limit** (int) - 返回数据长度, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0

        **Response**

        - **DataSet** (list) - 见 **RecycleUDiskSet** 模型定义
        - **TotalCount** (int) - 磁盘数量

        **Response Model**

        **RecycleUDiskSet**
        - **CountdownTime** (int) - 销毁倒计时
        - **CreateTime** (int) - 创建时间
        - **ExpiredTime** (int) - 过期时间
        - **Name** (str) - 磁盘名称
        - **Size** (int) - 磁盘容量
        - **Tag** (str) - 业务组
        - **UDiskId** (str) - 磁盘id
        - **Zone** (str) - 可用区


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeRecycleUDiskRequestSchema().dumps(d)

        resp = self.invoke("DescribeRecycleUDisk", d, **kwargs)
        return apis.DescribeRecycleUDiskResponseSchema().loads(resp)

    def describe_udisk(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDisk - 获取UDisk实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskType** (str) - ProtocolVersion字段为1时，需结合IsBoot确定具体磁盘类型:普通数据盘：DiskType:"CLOUD_NORMAL",IsBoot:"False"；普通系统盘：DiskType:"CLOUD_NORMAL",IsBoot:"True"；SSD数据盘：DiskType:"CLOUD_SSD",IsBoot:"False"；SSD系统盘：DiskType:"CLOUD_SSD",IsBoot:"True"；RSSD数据盘：DiskType:"CLOUD_RSSD",IsBoot:"False"；RSSD系统盘：DiskType:"CLOUD_RSSD",IsBoot:"True"；高效数据盘：DiskType:"CLOUD_EFFICIENCY",IsBoot:"False"；高效系统盘：DiskType:"CLOUD_EFFICIENCY",IsBoot:"True"；为空拉取所有。ProtocolVersion字段为0或没有该字段时，可设为以下几个值:普通数据盘：DataDisk；普通系统盘：SystemDisk；SSD数据盘：SSDDataDisk；SSD系统盘：SSDSystemDisk；RSSD数据盘：RSSDDataDisk；RSSD系统盘：RSSDSystemDisk：高效数据盘：EfficiencyDataDisk；高效系统盘：EfficiencySystemDisk；为空拉取所有。
        - **HostId** (str) - 根据传入的HostId，返回与该主机关联的云盘信息。
        - **HostIdForAttachment** (str) - 根据传入的HostIdForAttachment，筛选出能被挂载在该主机上的云盘。目前主要针对RSSD云盘。
        - **HostProduct** (str) - 宿主产品类型，可筛选挂载在该类型宿主上的云盘。可选值：uhost, uphost。为空拉取所有。（当HostIdForAttachment字段不为空时，该字段可以不填，若HostIdForAttachment与该字段宿主类型冲突，则以HostIdForAttachment字段为准。）
        - **IgnoreBackupMode** (str) - 是否忽略快照服务信息。Yes：忽略，No：不忽略，默认值（No）。（如不关心快照服务信息，建议选填“Yes”，可降低请求延时）
        - **IgnoreUBillInfo** (str) - 是否忽略计费信息。Yes：忽略，No：不忽略，默认值（No）。（如不关心账单信息，建议选填“Yes”，可降低请求延时）
        - **IsBoot** (str) - ProtocolVersion字段为1且DiskType不为空时，必须设置，设置规则请参照DiskType；ProtocolVersion字段为1且DiskType为空时，该字段无效。ProtocolVersion字段为0或没有该字段时，该字段无效。
        - **Limit** (int) - 返回数据长度, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        - **ProtocolVersion** (int) - 请求协议版本，建议升级为1，为1时DiskType与UHost磁盘类型定义一致；默认为0
        - **Status** (str) - 云盘状态。All(所有状态)，Available(可用)，Attaching(挂载中)，InUse(已挂载)， Detaching(卸载中)， Initializating(分配中)，Failed(创建失败)，Cloning(克隆中)，Restoring(恢复中)，RestoreFailed(恢复失败)。默认值：All
        - **UDiskBasicInfo** (str) - 是否只返回云盘基础信息（只包含云盘及关联主机的资源信息）。Yes：是，No：否，默认值（No）。（如仅需要基础信息，建议选填“Yes”，可降低请求延时）
        - **UDiskId** (str) - UDisk Id(留空返回全部)
        - **UHostIdForAttachment** (str) - 根据传入的UHostIdForAttachment，筛选出能被挂载在该主机上的云盘【本字段即将废弃，建议使用HostIdForAttachment】
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **UDiskDataSet** 模型定义
        - **TotalCount** (int) - 根据过滤条件得到的总数

        **Response Model**

        **UDiskDataSet**
        - **ArkSwitchEnable** (int) - 是否支持开启方舟，1支持 ，0不支持
        - **BackupMode** (str) - 该盘的备份方式。快照服务："SnapshotService"；数据方舟："UDataArk"；无备份方式：""
        - **ChargeType** (str) - Year,Month,Dynamic,Trial,Postpay
        - **CloneEnable** (int) - 是否支持克隆，1支持 ，0不支持
        - **CmkId** (str) - 该盘的cmk id
        - **CmkIdAlias** (str) - cmk id 别名
        - **CmkIdStatus** (str) - 该盘cmk的状态, Enabled(正常)，Disabled(失效)，Deleted(删除)，NoCmkId(非加密盘)
        - **CreateTime** (int) - 创建时间
        - **DataKey** (str) - 该盘的密文密钥
        - **DeviceName** (str) - 挂载的设备名称
        - **DiskType** (str) - 请求中的ProtocolVersion字段为1时，需结合IsBoot确定具体磁盘类型:普通数据盘：DiskType:"CLOUD_NORMAL",IsBoot:"False"； 普通系统盘：DiskType:"CLOUD_NORMAL",IsBoot:"True"；SSD数据盘：DiskType:"CLOUD_SSD",IsBoot:"False"；SSD系统盘：DiskType:"CLOUD_SSD",IsBoot:"True"；RSSD数据盘：DiskType:"CLOUD_RSSD",IsBoot:"False"；RSSD系统盘：DiskType:"CLOUD_RSSD",IsBoot:"True"；高效数据盘：DiskType:"CLOUD_EFFICIENCY",IsBoot:"False"；高效系统盘：DiskType:"CLOUD_EFFICIENCY",IsBoot:"True"。请求中的ProtocolVersion字段为0或没有该字段时，云硬盘类型参照如下:普通数据盘：DataDisk；普通系统盘：SystemDisk；SSD数据盘：SSDDataDisk；SSD系统盘：SSDSystemDisk；RSSD数据盘：RSSDDataDisk；RSSD系统盘：RSSDSystemDisk；高效数据盘：EfficiencyDataDisk；高效系统盘：EfficiencySystemDisk。
        - **ExpiredTime** (int) - 过期时间
        - **HostIP** (str) - 挂载的Host的IP
        - **HostId** (str) - 挂载的Host的Id
        - **HostName** (str) - 挂载的Host的Name
        - **IsBoot** (str) - 是否是系统盘，是："True", 否："False"
        - **IsExpire** (str) - 资源是否过期，过期:"Yes", 未过期:"No"
        - **Name** (str) - 实例名称
        - **RdmaClusterId** (str) - RDMA集群id，仅RSSD返回该值；其他类型云盘返回""。当云盘的此值与快杰云主机的RdmaClusterId相同时，RSSD可以挂载到这台云主机。
        - **Size** (int) - 容量单位GB
        - **SnapEnable** (int) - 是否支持快照，1支持 ，0不支持
        - **SnapshotCount** (int) - 该盘快照个数
        - **SnapshotLimit** (int) - 该盘快照上限
        - **Status** (str) - 状态:Available(可用),Attaching(挂载中), InUse(已挂载), Detaching(卸载中), Initializating(分配中), Failed(创建失败),Cloning(克隆中),Restoring(恢复中),RestoreFailed(恢复失败)
        - **Tag** (str) - 业务组名称
        - **UDataArkMode** (str) - 是否开启数据方舟，开启:"Yes", 不支持:"No"
        - **UDiskId** (str) - UDisk实例Id
        - **UHostIP** (str) - 挂载的UHost的IP。【即将废弃，建议使用HostIP】
        - **UHostId** (str) - 挂载的UHost的Id。【即将废弃，建议使用HostId】
        - **UHostName** (str) - 挂载的UHost的Name。【即将废弃，建议使用HostName】
        - **UKmsMode** (str) - 是否是加密盘，是:"Yes", 否:"No"
        - **Version** (str) - 是否支持数据方舟，支持:"2.0", 不支持:"1.0"
        - **Zone** (str) - 可用区


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDiskRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDisk", d, **kwargs)
        return apis.DescribeUDiskResponseSchema().loads(resp)

    def describe_udisk_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDiskPrice - 获取UDisk实例价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,普通数据盘：范围[1~8000]；SSD数据盘：范围[1~8000]；普通系统盘：范围[1~8000]；SSD系统盘：范围[1~4000]；RSSD数据盘：范围[1~32000]；RSSD系统盘：范围[1~4000]；高效数据盘：范围[1~32000]；高效系统盘：范围[1~500]。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - Year , Month, Dynamic，Postpay，Trial 默认: Month
        - **DiskType** (str) - UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），RSSDDataDisk(RSSD数据盘)，EfficiencyDataDisk（高效数据盘），SystemDisk（普通系统盘），SSDSystemDisk（SSD系统盘），RSSDSystemDisk(RSSD系统盘)，EfficiencySystemDisk（高效系统盘），默认值（DataDisk）
        - **IsTotalPrice** (str) - 是否将快照服务(数据方舟)，云硬盘放入一张订单, 是："Yes",否："No"，默认是"No"
        - **MachineType** (str) - 云主机机型（V2.0），枚举值["N", "C", "G", "O", "OM"]。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。
        - **Quantity** (int) - 购买UDisk的时长，默认值为1
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No

        **Response**

        - **DataSet** (list) - 见 **UDiskPriceDataSet** 模型定义

        **Response Model**

        **UDiskPriceDataSet**
        - **ChargeName** (str) - "UDataArk","SnapshotService","UDisk","Total"
        - **ChargeType** (str) - Year， Month， Dynamic，Trial
        - **ListPrice** (int) - 原价(对应计费OriginalPrice)
        - **OriginalPrice** (int) - 用户折后价(对应计费CustomPrice)
        - **Price** (int) - 实际价格 (单位: 分)


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDiskPriceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDiskPrice", d, **kwargs)
        return apis.DescribeUDiskPriceResponseSchema().loads(resp)

    def describe_udisk_snapshot(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDiskSnapshot - 获取UDisk快照

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Limit** (int) - 返回数据长度, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        - **SnapshotId** (str) - 快照id，SnapshotId , UDiskId 同时传SnapshotId优先
        - **UDiskId** (str) - UDiskId,返回该盘所做快照.(必须同时传Zone)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **UDiskSnapshotSet** 模型定义
        - **TotalCount** (int) - 根据过滤条件得到的总数

        **Response Model**

        **UDiskSnapshotSet**
        - **CmkId** (str) - 该快照的cmk id
        - **CmkIdAlias** (str) - cmk id 别名
        - **CmkIdStatus** (str) - 该快照cmk的状态, Enabled(正常)，Disabled(失效)，Deleted(删除)，NoCmkId(非加密盘)
        - **Comment** (str) - 快照描述
        - **CreateTime** (int) - 创建时间
        - **DataKey** (str) - 该快照的密文密钥
        - **DiskType** (int) - 磁盘类型，0：普通数据盘；1：普通系统盘；2：SSD数据盘；3：SSD系统盘；4：RSSD数据盘；5：RSSD系统盘。
        - **ExpiredTime** (int) - 过期时间
        - **IsUDiskAvailable** (bool) - 对应磁盘是否处于可用状态
        - **Name** (str) - 快照名称
        - **Size** (int) - 容量单位GB
        - **SnapshotId** (str) - 快照Id
        - **Status** (str) - 快照状态，Normal:正常,Failed:失败,Creating:制作中
        - **UDiskId** (str) - 快照的源UDisk的Id
        - **UDiskName** (str) - 快照的源UDisk的Name
        - **UHostId** (str) - 对应磁盘制作快照时所挂载的主机
        - **UKmsMode** (str) - 是否是加密盘快照，是:"Yes", 否:"No"
        - **Version** (str) - 快照版本
        - **Zone** (str) - 可用区


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDiskSnapshotRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDiskSnapshot", d, **kwargs)
        return apis.DescribeUDiskSnapshotResponseSchema().loads(resp)

    def describe_udisk_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUDiskUpgradePrice - 获取UDisk升级价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,普通数据盘：范围[1~8000]；SSD数据盘：范围[1~8000]；普通系统盘：范围[1~8000]；SSD系统盘：范围[1~4000]；RSSD数据盘：范围[1~32000]；RSSD系统盘：范围[1~4000]；高效数据盘：范围[1~32000]；高效系统盘：范围[1~500]。
        - **SourceId** (str) - (Required) 升级目标UDisk ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskType** (str) - 【已废弃】UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），RSSDDataDisk(RSSD数据盘)，EfficiencyDataDisk（高效数据盘），SystemDisk（普通系统盘），SSDSystemDisk（SSD系统盘），RSSDSystemDisk(RSSD系统盘)，EfficiencySystemDisk（高效系统盘），默认值（DataDisk）
        - **MachineType** (str) - 【已废弃】云主机机型（V2.0），枚举值["N", "C", "G", "O", "OM"]。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。
        - **SnapshotService** (str) - 是否开启快照服务（开启快照服务，可免费开启数据方舟）。Yes：开启，No：不开启，默认值：No。仅支持查询开启快照服务的价格。
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No

        **Response**

        - **OriginalPrice** (int) - 用户折后价 (对应计费CustomPrice)
        - **Price** (int) - 价格

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeUDiskUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDiskUpgradePrice", d, **kwargs)
        return apis.DescribeUDiskUpgradePriceResponseSchema().loads(resp)

    def detach_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **UDiskId** (str) - (Required) 需要卸载的UDisk实例ID
        - **HostId** (str) - Host实例ID
        - **UHostId** (str) - UHost实例ID。【UHostId和HostId必须选填一个，本字段即将废弃，建议使用HostId】
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **HostId** (str) - 卸载的Host实例ID
        - **UDiskId** (str) - 卸载的UDisk实例ID
        - **UHostId** (str) - 卸载的UHost实例ID。【即将废弃，建议使用HostId】

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DetachUDiskRequestSchema().dumps(d)

        resp = self.invoke("DetachUDisk", d, **kwargs)
        return apis.DetachUDiskResponseSchema().loads(resp)

    def recover_udisk(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RecoverUDisk - 从回收站中恢复云硬盘

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **UDiskId** (str) - (Required) 云硬盘资源ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ChargeType** (str) - Year , Month, Dynamic 默认: Dynamic
        - **Quantity** (int) - 购买时长 默认: 1

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RecoverUDiskRequestSchema().dumps(d)

        resp = self.invoke("RecoverUDisk", d, **kwargs)
        return apis.RecoverUDiskResponseSchema().loads(resp)

    def rename_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """RenameUDisk - 重命名UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **UDiskId** (str) - (Required) 重命名的UDisk的Id
        - **UDiskName** (str) - (Required) 重命名UDisk的name
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RenameUDiskRequestSchema().dumps(d)

        resp = self.invoke("RenameUDisk", d, **kwargs)
        return apis.RenameUDiskResponseSchema().loads(resp)

    def resize_udisk(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ResizeUDisk - 调整UDisk容量

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Size** (int) - (Required) 调整后大小, 单位:GB,普通数据盘：范围[1~8000]；SSD数据盘：范围[1~8000]；RSSD数据盘：范围[1~32000]。
        - **UDiskId** (str) - (Required) UDisk Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CouponId** (str) - 使用的代金券id
        - **MachineType** (str) - 云主机机型（V2.0），枚举值["N", "C", "G", "O", "OM"]。参考 `云主机机型说明 <https://docs.ucloud.cn/api/uhost-api/uhost_type>`_ 。

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ResizeUDiskRequestSchema().dumps(d)

        resp = self.invoke("ResizeUDisk", d, **kwargs)
        return apis.ResizeUDiskResponseSchema().loads(resp)

    def restore_udisk(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RestoreUDisk - 从备份恢复数据至UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **UDiskId** (str) - (Required) 需要恢复的盘ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **SnapshotId** (str) - 从指定的快照恢复
        - **SnapshotTime** (int) - 指定从方舟恢复的备份时间点

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RestoreUDiskRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("RestoreUDisk", d, **kwargs)
        return apis.RestoreUDiskResponseSchema().loads(resp)

    def set_udisk_udataark_mode(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """SetUDiskUDataArkMode - 设置UDisk数据方舟的状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **UDiskId** (str) - (Required) 需要设置数据方舟的UDisk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **CouponId** (str) - 使用的代金券id
        - **UDataArkMode** (str) - 【开启数据方舟入口已关闭】是否开启数据方舟。Yes：开启，No：不开启，默认值：No

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.SetUDiskUDataArkModeRequestSchema().dumps(d)

        resp = self.invoke("SetUDiskUDataArkMode", d, **kwargs)
        return apis.SetUDiskUDataArkModeResponseSchema().loads(resp)
