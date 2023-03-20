""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.uphost.schemas import apis


class UPHostClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UPHostClient, self).__init__(
            config, transport, middleware, logger
        )

    def create_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """CreatePHost - 指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageId** (str) - (Required) ImageId，可以通过接口  `DescribePHostImage <https://docs.ucloud.cn/api/uphost-api/api/uphost-api/describe_phost_image.html>`_ 获取
        - **Password** (str) - (Required) 密码（密码需使用base64进行编码）
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - 计费模式，枚举值为：year, 按年付费； month,按月付费；默认为按月付费
        - **Cluster** (str) - 网络环境，可选千兆：1G ，万兆：10G， 默认1G。智能网卡可以选择25G。
        - **CouponId** (str) - 代金券
        - **Disks** (list) - 见 **CreatePHostParamDisks** 模型定义
        - **Name** (str) - 物理机名称，默认为phost
        - **Quantity** (str) - 购买时长，1-10个月或1-10年；默认值为1。月付时，此参数传0，代表购买至月末，1代表整月。
        - **Raid** (str) - Raid配置，默认Raid10  支持:Raid0、Raid1、Raid5、Raid10，NoRaid
        - **Remark** (str) - 物理机备注，默认为空
        - **SecurityGroupId** (str) - 防火墙ID，默认：Web推荐防火墙。如何查询SecurityGroupId请参见  `DescribeFirewall <https://docs.ucloud.cn/api/uphost-api/api/unet-api/describe_firewall.html>`_ 。
        - **SubnetId** (str) - 子网ID，不填为默认，VPC2.0下需要填写此字段。
        - **Tag** (str) - 业务组，默认为default
        - **Type** (str) - 物理机类型，默认为：db-2(基础型-SAS-V3)
        - **VPCId** (str) - VPC ID，不填为默认，VPC2.0下需要填写此字段。
        - **VpcIp** (str) - 指定内网ip创建

        **Response**

        - **PHostId** (list) - PHost的资源ID数组

        **Request Model**

        **CreatePHostParamDisks**
        - **CouponId** (str) - 裸金属机型参数->云盘代金券id。不适用于系统盘。请通过DescribeCoupon接口查询，或登录用户中心查看
        - **IsBoot** (str) - 裸金属机型参数->是否是系统盘。枚举值： True，是系统盘。 False，是数据盘（默认）。Disks数组中有且只能有一块盘是系统盘。
        - **Size** (int) - 裸金属机型参数->磁盘大小，单位GB，必须是10GB的整数倍。系统盘20-500GB，数据盘单块盘20-32000GB。
        - **Type** (str) - 裸金属机型参数->磁盘类型：枚举值：CLOUD_RSSD


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreatePHostRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreatePHost", d, **kwargs)
        return apis.CreatePHostResponseSchema().loads(resp)

    def create_phost_image(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreatePHostImage - 创建裸金属2.0用户自定义镜像

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageName** (str) - (Required) 镜像名称
        - **PHostId** (str) - (Required) UPHost实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageDescription** (str) - 镜像描述

        **Response**

        - **ImageId** (str) - 镜像ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreatePHostImageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreatePHostImage", d, **kwargs)
        return apis.CreatePHostImageResponseSchema().loads(resp)

    def describe_baremetal_machine_type(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeBaremetalMachineType - 获取裸金属机型的详细描述信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Type** (str) - 具体机型。若不填写，则返回全部机型

        **Response**

        - **MachineTypes** (list) - 见 **PHostCloudMachineTypeSet** 模型定义

        **Response Model**

        **PHostCloudMachineTypeSet**
        - **CPU** (dict) - 见 **PHostCPUSet** 模型定义
        - **Clusters** (list) - 见 **PHostClusterSet** 模型定义
        - **Components** (dict) - 见 **PHostComponentSet** 模型定义
        - **Memory** (int) - 内存大小，单位MB
        - **Type** (str) - 物理云主机机型别名，全网唯一。


        **PHostCPUSet**
        - **CoreCount** (int) - CPU核数
        - **Count** (int) - CPU个数
        - **Frequence** (float) - CPU主频
        - **Model** (str) - CPU型号


        **PHostClusterSet**
        - **Name** (str) - 集群名。枚举值：千兆网络集群：1G；万兆网络集群：10G；智能网卡网络：25G；
        - **StockStatus** (str) - 库存状态。枚举值：有库存：Available；无库存：SoldOut


        **PHostComponentSet**
        - **Count** (int) - 组件数量
        - **Name** (str) - 组件名称


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeBaremetalMachineTypeRequestSchema().dumps(d)

        resp = self.invoke("DescribeBaremetalMachineType", d, **kwargs)
        return apis.DescribeBaremetalMachineTypeResponseSchema().loads(resp)

    def describe_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHost - 获取物理机详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Limit** (int) - 返回数据长度，默认为20
        - **Offset** (int) - 数据偏移量，默认为0
        - **PHostId** (list) - PHost资源ID，若为空，则返回当前Region所有PHost。
        - **UDiskIdForAttachment** (str) - 要挂载的云盘id，过滤返回能被UDiskId挂载的云主机。目前主要针对rssd云盘使用
        - **VPCId** (str) - ULB使用参数，获取同VPC下机器信息。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **PHostSet** (list) - 见 **PHostSet** 模型定义
        - **TotalCount** (int) - 满足条件的PHost总数

        **Response Model**

        **PHostSet**
        - **AutoRenew** (str) - 自动续费
        - **BootDiskState** (str) - 裸金属机型字段。枚举值：Normal=>正常、ImageMaking=>镜像制作中。
        - **CPUSet** (dict) - 见 **PHostCPUSet** 模型定义
        - **ChargeType** (str) - 计费模式，枚举值为： Year，按年付费； Month，按月付费；默认为月付
        - **Cluster** (str) - 网络环境。枚举值：千兆：1G ，万兆：10G
        - **Components** (str) - 组件信息（暂不支持）
        - **CreateTime** (int) - 创建时间
        - **DiskSet** (list) - 见 **PHostDescDiskSet** 模型定义
        - **ExpireTime** (int) - 到期时间
        - **IPSet** (list) - 见 **PHostIPSet** 模型定义
        - **ImageName** (str) - 镜像名称
        - **IsSupportKVM** (str) - 是否支持紧急登录
        - **Memory** (int) - 内存大小，单位：MB
        - **Name** (str) - 物理机名称
        - **OSType** (str) - 操作系统类型
        - **OSname** (str) - 操作系统名称
        - **PHostId** (str) - PHost资源ID
        - **PHostType** (str) - 物理机类型，参见DescribePHostMachineType返回值
        - **PMStatus** (str) - 物理云主机状态。枚举值：\\ > 初始化:Initializing; \\ > 启动中：Starting； \\ > 运行中：Running；\\ > 关机中：Stopping； \\ > 安装失败：InstallFailed； \\ > 重启中：Rebooting；\\ > 关机：Stopped； \\ > 迁移中(裸金属云盘)：Migrating
        - **PhostClass** (str) - 物理云产品类型，枚举值：LocalDisk=>代表传统本地盘机型， CloudDisk=>云盘裸金属机型
        - **PowerState** (str) - 电源状态，on 或 off
        - **RaidSupported** (str) - 是否支持Raid。枚举值：Yes：支持；No：不支持。
        - **RdmaClusterId** (str) - RDMA集群id，仅云盘裸金属返回该值；其他类型物理云主机返回""。当物理机的此值与RSSD云盘的RdmaClusterId相同时，RSSD可以挂载到这台物理机。
        - **Remark** (str) - 物理机备注
        - **SN** (str) - 物理机序列号
        - **Tag** (str) - 业务组
        - **Zone** (str) - 可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_


        **PHostCPUSet**
        - **CoreCount** (int) - CPU核数
        - **Count** (int) - CPU个数
        - **Frequence** (float) - CPU主频
        - **Model** (str) - CPU型号


        **PHostDescDiskSet**
        - **Count** (int) - 磁盘数量
        - **DiskId** (str) - 裸金属机型参数：磁盘ID
        - **Drive** (str) - 裸金属机型参数：磁盘盘符
        - **IOCap** (int) - 磁盘IO性能，单位MB/s（待废弃）
        - **IsBoot** (str) - 裸金属机型参数：是否是启动盘。True/False
        - **Name** (str) - 磁盘名称，sys/data
        - **Space** (int) - 单盘大小，单位GB
        - **Type** (str) - 磁盘属性


        **PHostIPSet**
        - **Bandwidth** (int) - IP对应带宽，单位Mb，内网IP不显示带宽信息
        - **IPAddr** (str) - IP地址，
        - **IPId** (str) - IP资源ID(内网IP无资源ID)（待废弃）
        - **MACAddr** (str) - MAC地址
        - **OperatorName** (str) - 国际: Internation， BGP: BGP， 内网: Private
        - **SubnetId** (str) - 子网ID
        - **VPCId** (str) - VPC ID


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribePHostRequestSchema().dumps(d)

        resp = self.invoke("DescribePHost", d, **kwargs)
        return apis.DescribePHostResponseSchema().loads(resp)

    def describe_phost_image(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHostImage - 获取物理云主机镜像列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageId** (list) - 镜像ID
        - **ImageType** (str) - 镜像类别，枚举值，Base是基础镜像；Custom是自制镜像。
        - **Limit** (int) - 返回数据长度，默认为20
        - **MachineType** (str) - 机器型号，只支持当前zone的展示机型
        - **Offset** (int) - 数据偏移量，默认为0

        **Response**

        - **ImageSet** (list) - 见 **PHostImageSet** 模型定义
        - **TotalCount** (int) - 满足条件的镜像总数

        **Response Model**

        **PHostImageSet**
        - **CreateTime** (int) - 裸金属2.0参数。镜像创建时间。
        - **ImageDescription** (str) - 镜像描述
        - **ImageId** (str) - 镜像ID
        - **ImageName** (str) - 镜像名称
        - **ImageSize** (int) - 裸金属2.0参数。镜像大小。
        - **ImageType** (str) - 枚举值：Base=>基础镜像，Custom=>自制镜像。
        - **OsName** (str) - 操作系统名称
        - **OsType** (str) - 操作系统类型
        - **State** (str) - 裸金属2.0参数。镜像当前状态。
        - **Support** (list) - 支持的机型
        - **Version** (str) - 当前版本


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribePHostImageRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostImage", d, **kwargs)
        return apis.DescribePHostImageResponseSchema().loads(resp)

    def describe_phost_machine_type(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHostMachineType - 获取物理云机型的详细描述信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Type** (str) - 具体机型。若不填写，则返回全部机型

        **Response**

        - **MachineTypes** (list) - 见 **PHostMachineTypeSet** 模型定义

        **Response Model**

        **PHostMachineTypeSet**
        - **CPU** (dict) - 见 **PHostCPUSet** 模型定义
        - **Clusters** (list) - 见 **PHostClusterSet** 模型定义
        - **Components** (dict) - 见 **PHostComponentSet** 模型定义
        - **Disks** (list) - 见 **PHostDiskSet** 模型定义
        - **Memory** (int) - 内存大小，单位MB
        - **RaidSupported** (str) - 是否支持Raid。枚举值：支持：YES；不支持：NO
        - **Type** (str) - 物理云主机机型别名，全网唯一。


        **PHostCPUSet**
        - **CoreCount** (int) - CPU核数
        - **Count** (int) - CPU个数
        - **Frequence** (float) - CPU主频
        - **Model** (str) - CPU型号


        **PHostClusterSet**
        - **Name** (str) - 集群名。枚举值：千兆网络集群：1G；万兆网络集群：10G；智能网卡网络：25G；
        - **StockStatus** (str) - 库存状态。枚举值：有库存：Available；无库存：SoldOut


        **PHostComponentSet**
        - **Count** (int) - 组件数量
        - **Name** (str) - 组件名称


        **PHostDiskSet**
        - **Count** (int) - 磁盘数量
        - **IOCap** (int) - 磁盘IO性能，单位MB/s（待废弃）
        - **Name** (str) - 磁盘名称，sys/data
        - **Space** (int) - 单盘大小，单位GB
        - **Type** (str) - 磁盘属性


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribePHostMachineTypeRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostMachineType", d, **kwargs)
        return apis.DescribePHostMachineTypeResponseSchema().loads(resp)

    def describe_phost_tags(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHostTags - 获取物理机tag列表（业务组）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **TagSet** (list) - 见 **PHostTagSet** 模型定义
        - **TotalCount** (int) - Tag的个数

        **Response Model**

        **PHostTagSet**
        - **Tag** (str) - 业务组名称
        - **TotalCount** (int) - 该业务组中包含的主机个数


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribePHostTagsRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostTags", d, **kwargs)
        return apis.DescribePHostTagsResponseSchema().loads(resp)

    def get_phost_disk_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetPHostDiskUpgradePrice - 获取物理云裸金属挂载磁盘的升级价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **DiskSpace** (int) - (Required) 磁盘大小，单位GB，必须是10GB的整数倍。系统盘20-500GB，数据盘单块盘20-32000GB。
        - **PHostId** (str) - (Required) UPHost实例ID。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ReinstallTag** (bool) - 是否重装价格获取。复用此接口。扩容只能增加云盘大小。重装不限制。枚举值：true/false
        - **UDiskId** (str) - 磁盘 ID。获取扩容价格必填（只能扩不能减）；重装时候不需要填（根据所选盘大小决定）

        **Response**

        - **OriginalPrice** (float) - 升价差价原价。精度为小数点后2位。
        - **Price** (float) - 升级差价。精度为小数点后2位。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetPHostDiskUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetPHostDiskUpgradePrice", d, **kwargs)
        return apis.GetPHostDiskUpgradePriceResponseSchema().loads(resp)

    def get_phost_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetPHostPrice - 获取物理机价格列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - (Required) 计费模式，枚举值为： Year/Month
        - **Count** (int) - (Required) 购买数量，范围[1-5]
        - **Quantity** (int) - (Required) 购买时长，1-10个月或1-10年；默认值为1。月付时，此参数传0，代表购买至月末，1代表整月。
        - **Cluster** (str) - 网络环境，可选千兆：1G ；万兆：10G；25G网络：25G。
        - **Disks** (list) - 见 **GetPHostPriceParamDisks** 模型定义
        - **Type** (str) - 默认为：DB(数据库型)，可以通过接口  `DescribePHostMachineType <https://docs.ucloud.cn/api/uphost-api/api/uphost-api/describe_phost_machine_type.html>`_ 获取
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **PriceSet** (list) - 见 **PHostPriceSet** 模型定义

        **Request Model**

        **GetPHostPriceParamDisks**
        - **IsBoot** (str) - 裸金属机型参数->枚举值：\\ > True，是系统盘 \\ > False，是数据盘（默认）。Disks数组中有且只能有一块盘是系统盘。
        - **Size** (str) - 裸金属机型参数->磁盘大小，单位GB，必须是10GB的整数倍。系统盘20-500GB。数据盘是20-32000G。
        - **Type** (str) - 裸金属机型参数->磁盘类型：枚举值：CLOUD_RSSD


        **Response Model**

        **PHostPriceSet**
        - **ChargeType** (str) - Year/Month
        - **OriginalPrice** (float) - 原价格, 单位:元, 保留小数点后两位有效数字
        - **Price** (float) - 价格, 单位:元, 保留小数点后两位有效数字
        - **Product** (str) - 枚举值：phost=>为主机价格，如果是云盘包括了系统盘价格。cloudDisk=>所有数据盘价格，只是裸金属机型才返回此参数。


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetPHostPriceRequestSchema().dumps(d)

        resp = self.invoke("GetPHostPrice", d, **kwargs)
        return apis.GetPHostPriceResponseSchema().loads(resp)

    def get_phost_disk_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetPhostDiskUpgradePrice - 获取物理云裸金属挂载磁盘的升级价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **DiskId** (str) - (Required) 磁盘ID。
        - **DiskSpace** (int) - (Required) 裸金属机型参数->磁盘大小，单位GB，必须是10GB的整数倍。系统盘20-500GB，数据盘单块盘20-32000GB。
        - **PHostId** (str) - (Required) UPHost实例ID。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Price** (float) - 升级差价。精度为小数点后2位。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetPhostDiskUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetPhostDiskUpgradePrice", d, **kwargs)
        return apis.GetPhostDiskUpgradePriceResponseSchema().loads(resp)

    def modify_phost_image_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyPHostImageInfo - 修改自定义镜像名称和备注

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageId** (str) - (Required) 镜像ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - 镜像名称
        - **Remark** (str) - 备注

        **Response**

        - **ImageId** (str) - 镜像ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyPHostImageInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyPHostImageInfo", d, **kwargs)
        return apis.ModifyPHostImageInfoResponseSchema().loads(resp)

    def modify_phost_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyPHostInfo - 更改物理机信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) 物理机资源ID
        - **Name** (str) - 物理机名称，默认不更改
        - **Remark** (str) - 物理机备注，默认不更改
        - **Tag** (str) - 业务组，默认不更改
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyPHostInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyPHostInfo", d, **kwargs)
        return apis.ModifyPHostInfoResponseSchema().loads(resp)

    def poweroff_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """PoweroffPHost - 断电物理云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.PoweroffPHostRequestSchema().dumps(d)

        resp = self.invoke("PoweroffPHost", d, **kwargs)
        return apis.PoweroffPHostResponseSchema().loads(resp)

    def reboot_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """RebootPHost - 重启物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RebootPHostRequestSchema().dumps(d)

        resp = self.invoke("RebootPHost", d, **kwargs)
        return apis.RebootPHostResponseSchema().loads(resp)

    def reinstall_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ReinstallPHost - 重装物理机操作系统

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Password** (str) - (Required) 密码
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **BootDiskSpace** (int) - 裸金属机型参数->系统盘大小。 单位：GB， 范围[20,500]， 步长：10
        - **ImageId** (str) - 镜像Id，参考镜像列表，默认使用原镜像
        - **Name** (str) - 物理机名称，默认不更改
        - **Raid** (str) - 不保留数据盘重装，可选Raid
        - **Remark** (str) - 物理机备注，默认为不更改。
        - **ReserveDisk** (str) - 是否保留数据盘，保留：Yes，不报留：No， 默认：Yes
        - **Tag** (str) - 业务组，默认不更改。

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ReinstallPHostRequestSchema().dumps(d)

        resp = self.invoke("ReinstallPHost", d, **kwargs)
        return apis.ReinstallPHostResponseSchema().loads(resp)

    def reset_phost_password(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ResetPHostPassword - 重置裸金属实例的管理员密码

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) 裸金属实例ID
        - **Password** (str) - (Required) PHost新密码（密码格式使用BASE64编码）
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - 裸金属实例ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ResetPHostPasswordRequestSchema().dumps(d)

        resp = self.invoke("ResetPHostPassword", d, **kwargs)
        return apis.ResetPHostPasswordResponseSchema().loads(resp)

    def resize_phost_attached_disk(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ResizePHostAttachedDisk - 修改裸金属物理云已经挂载的云盘容量大小

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskSpace** (int) - 裸金属机型参数->磁盘大小，单位GB，必须是10GB的整数倍。系统盘20-500GB，数据盘单块盘20-32000GB。
        - **PHostId** (str) - UPHost实例ID。
        - **UDiskId** (str) - 磁盘ID。

        **Response**

        - **UDiskId** (str) - 改配成功的磁盘id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ResizePHostAttachedDiskRequestSchema().dumps(d)

        resp = self.invoke("ResizePHostAttachedDisk", d, **kwargs)
        return apis.ResizePHostAttachedDiskResponseSchema().loads(resp)

    def start_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """StartPHost - 启动物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StartPHostRequestSchema().dumps(d)

        resp = self.invoke("StartPHost", d, **kwargs)
        return apis.StartPHostResponseSchema().loads(resp)

    def stop_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """StopPHost - 关闭物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StopPHostRequestSchema().dumps(d)

        resp = self.invoke("StopPHost", d, **kwargs)
        return apis.StopPHostResponseSchema().loads(resp)

    def terminate_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """TerminatePHost - 删除物理云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **ReleaseEIP** (bool) - 是否释放绑定的EIP。true: 解绑EIP后，并释放；其他值或不填：解绑EIP。
        - **ReleaseUDisk** (bool) - 裸金属机型参数->删除主机时是否同时删除挂载的数据盘。默认为false。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.TerminatePHostRequestSchema().dumps(d)

        resp = self.invoke("TerminatePHost", d, **kwargs)
        return apis.TerminatePHostResponseSchema().loads(resp)

    def terminate_phost_image(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """TerminatePHostImage - 删除裸金属2.0用户自定义镜像

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ImageId** (str) - (Required) 自制镜像ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **ImageId** (str) - 自制镜像ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.TerminatePHostImageRequestSchema().dumps(d)

        resp = self.invoke("TerminatePHostImage", d, **kwargs)
        return apis.TerminatePHostImageResponseSchema().loads(resp)
