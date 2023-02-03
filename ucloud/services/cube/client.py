""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.cube.schemas import apis


class CubeClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(CubeClient, self).__init__(config, transport, middleware, logger)

    def create_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateCubeDeployment - 创建Cube的Deployment

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Deployment** (str) - (Required) base64编码的Deployment的yaml。大小不超过16KB
        - **SubnetId** (str) - (Required) 子网Id
        - **VPCId** (str) - (Required) VPCId
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Postpay， \\ 后付费；默认为后付费
        - **CpuPlatform** (str) - Cpu平台（V6：Intel、A2：AMD），默认V6。支持的地域（北京2B、北京2E、上海2A、广东、香港 、东京）目前北京2E仅有A2，其余地域仅有V6
        - **KubeConfig** (str) - base64编码的kubeconfig。大小不超过16KB
        - **Name** (str) - Deployment名称
        - **Quantity** (int) - 购买时长。默认:值 1。 月付时，此参数传0，代表购买至月末。
        - **Tag** (str) - 业务组。默认：Default（Default即为未分组）

        **Response**

        - **Deployment** (str) - 经过base64编码的Deployment的yaml
        - **DeploymentId** (str) - 控制器ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateCubeDeploymentRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateCubeDeployment", d, **kwargs)
        return apis.CreateCubeDeploymentResponseSchema().loads(resp)

    def create_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateCubePod - 创建Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Pod** (str) - (Required) base64编码的Pod的yaml。大小不超过16KB
        - **SubnetId** (str) - (Required) 子网Id
        - **VPCId** (str) - (Required) VPCId
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Postpay， \\ 后付费；默认为后付费
        - **CouponId** (str) - 代金券ID。请通过DescribeCoupon接口查询，或登录用户中心查看
        - **CpuPlatform** (str) - Cpu平台（V6：Intel、A2：AMD、Auto），默认Auto。支持的地域（北京2B、北京2E、上海2A、广东、香港 、东京）目前北京2E仅有A2，其余地域仅有V6
        - **Group** (str) - pod所在组
        - **KubeConfig** (str) - base64编码的kubeconfig。大小不超过16KB
        - **Name** (str) - pod的名字
        - **Quantity** (int) - 购买时长。默认:值 1。 月付时，此参数传0，代表购买至月末。
        - **Tag** (str) - 业务组。默认：Default（Default即为未分组）

        **Response**

        - **CubeId** (str) - cube的资源Id
        - **Pod** (str) - base64编码的yaml

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateCubePod", d, **kwargs)
        return apis.CreateCubePodResponseSchema().loads(resp)

    def delete_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteCubeDeployment - 删除Cube的Deployment

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DeploymentId** (str) - (Required) 控制器Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteCubeDeploymentRequestSchema().dumps(d)

        resp = self.invoke("DeleteCubeDeployment", d, **kwargs)
        return apis.DeleteCubeDeploymentResponseSchema().loads(resp)

    def delete_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteCubePod - 删除Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - cubeid和uid任意一个（必须）
        - **ReleaseEIP** (bool) - 删除cube时是否释放绑定的EIP。默认为false。
        - **Uid** (str) - cubeid和uid任意一个（必须）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteCubePodRequestSchema().dumps(d)

        resp = self.invoke("DeleteCubePod", d, **kwargs)
        return apis.DeleteCubePodResponseSchema().loads(resp)

    def get_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeDeployment - 获取Deployment的详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DeploymentId** (str) - (Required) Deployment的Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Deployment** (str) - 经过base64编码的Deployment的yaml

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeDeploymentRequestSchema().dumps(d)

        resp = self.invoke("GetCubeDeployment", d, **kwargs)
        return apis.GetCubeDeploymentResponseSchema().loads(resp)

    def get_cube_exec_token(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeExecToken - 获取登录容器的token

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ContainerName** (str) - (Required) 容器名称
        - **CubeId** (str) - CubeId 和 Uid 中必须填写任意一个。CubeId 是所有 Cube 资源的唯一 ID，如非在 UK8S 通过 Virtual Kubelet 插件创建的 Cube， 则必填 CubeId
        - **Uid** (str) - CubeId 和 Uid 中必须填写任意一个。Uid 是在 UK8S 中通过 Virtual Kubelet 插件创建出的 Cube 的唯一标识
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **TerminalUrl** (str) - terminal的登录连接地址，限单点登录，有效时间5min
        - **Token** (str) - 有效时间5min

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeExecTokenRequestSchema().dumps(d)

        resp = self.invoke("GetCubeExecToken", d, **kwargs)
        return apis.GetCubeExecTokenResponseSchema().loads(resp)

    def get_cube_extend_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeExtendInfo - 获取Cube的额外信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeIds** (str) - (Required) id列表以逗号(,)分割
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **ExtendInfo** (list) - 见 **CubeExtendInfo** 模型定义

        **Response Model**

        **CubeExtendInfo**
        - **CubeId** (str) - Cube的Id
        - **Eip** (list) - 见 **EIPSet** 模型定义
        - **Expiration** (int) - 资源有效期
        - **Name** (str) - Cube的名称
        - **Tag** (str) - 业务组名称


        **EIPSet**
        - **Bandwidth** (int) - EIP带宽值
        - **BandwidthType** (int) - 带宽类型0标准普通带宽，1表示共享带宽
        - **CreateTime** (int) - EIP创建时间
        - **EIPAddr** (list) - 见 **EIPAddr** 模型定义
        - **EIPId** (str) - EIPId
        - **PayMode** (str) - 付费模式，带宽付费或者流量付费
        - **Resource** (str) - EIP绑定对象的资源Id
        - **Status** (str) - EIP状态，表示使用中或者空闲
        - **Weight** (int) - EIP权重


        **EIPAddr**
        - **IP** (str) - IP地址
        - **OperatorName** (str) - 线路名称BGP或者internalation


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeExtendInfoRequestSchema().dumps(d)

        resp = self.invoke("GetCubeExtendInfo", d, **kwargs)
        return apis.GetCubeExtendInfoResponseSchema().loads(resp)

    def get_cube_metrics(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeMetrics - 获取Cube实例（Pod，PodX，Deploy等）监控数据时间序列

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BeginTime** (int) - (Required) 开始时间
        - **ContainerName** (str) - (Required) Pod内容器名称
        - **EndTime** (int) - (Required) 结束时间，必须大于开始时间
        - **MetricName** (list) - (Required) 监控指标名称
        - **ResourceId** (str) - (Required) Cube实例资源ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSets** (list) - 见 **MetricDataSet** 模型定义
        - **Message** (str) - 错误信息

        **Response Model**

        **MetricDataSet**
        - **MetricName** (str) -
        - **Values** (list) - 见 **ValueSet** 模型定义


        **ValueSet**
        - **Timestamp** (int) -
        - **Value** (float) -


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeMetricsRequestSchema().dumps(d)

        resp = self.invoke("GetCubeMetrics", d, **kwargs)
        return apis.GetCubeMetricsResponseSchema().loads(resp)

    def get_cube_pod(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """GetCubePod - 获取Pod的详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - CubeId和Uid任意一个
        - **Uid** (str) - CubeId和Uid任意一个
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Pod** (str) - base64编码的pod的yaml

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubePodRequestSchema().dumps(d)

        resp = self.invoke("GetCubePod", d, **kwargs)
        return apis.GetCubePodResponseSchema().loads(resp)

    def get_cube_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubePrice - 获取cube的价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - (Required) 计费模式。枚举值为： \\ > Year，按年付费； \\ > Month，按月付费；\\ > Dynamic，按小时预付费 \\ > Postpay，按秒后付费，默认为月付
        - **Count** (str) - (Required) 购买数量
        - **Cpu** (str) - (Required) CPU 配置，单位为毫核，例如如 1 核则须输入 1000
        - **Mem** (str) - (Required) 内存配置，单位为 Mi，例如 1Gi 须输入 1024
        - **Quantity** (int) - (Required) 购买时长。默认:值 1。按小时购买（Dynamic/Postpay）时无需此参数。 月付时，此参数传0，代表购买至月末。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **OriginalPrice** (int) - 列表价格，单位为分
        - **Price** (int) - 折扣后价格，单位为分

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubePriceRequestSchema().dumps(d)

        resp = self.invoke("GetCubePrice", d, **kwargs)
        return apis.GetCubePriceResponseSchema().loads(resp)

    def get_cube_token(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeToken - 获取Cube的token，可用于terminal登录、log获取

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ContainerName** (str) - (Required) 容器名称
        - **CubeId** (str) - CubeId 和 Uid 中必须填写任意一个。CubeId 是所有 Cube 资源的唯一 ID，如非在 UK8S 通过 Virtual Kubelet 插件创建的 Cube， 则必填 CubeId
        - **Uid** (str) - CubeId 和 Uid 中必须填写任意一个。Uid 是在 UK8S 中通过 Virtual Kubelet 插件创建出的 Cube 的唯一标识
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Token** (str) - 有效时间5min

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeTokenRequestSchema().dumps(d)

        resp = self.invoke("GetCubeToken", d, **kwargs)
        return apis.GetCubeTokenResponseSchema().loads(resp)

    def list_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListCubeDeployment - 获取Cube的Deployment列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Limit** (int) - (Required) 默认20
        - **Offset** (int) - (Required) 默认0
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Deployments** (list) - DeploymentInfo
        - **TotalCount** (int) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListCubeDeploymentRequestSchema().dumps(d)

        resp = self.invoke("ListCubeDeployment", d, **kwargs)
        return apis.ListCubeDeploymentResponseSchema().loads(resp)

    def list_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListCubePod - 获取Pods列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DeploymentId** (str) - Deployment的Id
        - **Group** (str) - 组名称
        - **Limit** (int) - 默认20
        - **Offset** (int) - 默认0
        - **SubnetId** (str) - 子网Id
        - **VPCId** (str) - VPC的Id
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Pods** (list) - Pod列表，每条数据都做了base64编码
        - **TotalCount** (int) - Cube的总数

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListCubePodRequestSchema().dumps(d)

        resp = self.invoke("ListCubePod", d, **kwargs)
        return apis.ListCubePodResponseSchema().loads(resp)

    def modify_cube_extend_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyCubeExtendInfo - 修改Cube额外信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - (Required) cube的id
        - **Name** (str) - 修改的名字，规则（^[a-zA-Z0-9-_.\u4e00-\u9fa5]{1,32}）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyCubeExtendInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyCubeExtendInfo", d, **kwargs)
        return apis.ModifyCubeExtendInfoResponseSchema().loads(resp)

    def modify_cube_tag(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyCubeTag - 修改业务组名字

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **CubeId** (str) - (Required) CubeId
        - **Tag** (str) - (Required) 业务组名称
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **CubeId** (str) - CubeId

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyCubeTagRequestSchema().dumps(d)

        resp = self.invoke("ModifyCubeTag", d, **kwargs)
        return apis.ModifyCubeTagResponseSchema().loads(resp)

    def reboot_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RebootCubePod - 重启Cube Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **CubeId** (str) - (Required) cube资源id（cube-xxxxxx）
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RebootCubePodRequestSchema().dumps(d)

        resp = self.invoke("RebootCubePod", d, **kwargs)
        return apis.RebootCubePodResponseSchema().loads(resp)

    def renew_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RenewCubePod - 更新Pod

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **CubeId** (str) - (Required) 容器Id
        - **Pod** (str) - (Required) base64编码的Pod的yaml
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Pod** (str) - base64编码过的yaml，需要解码获取信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RenewCubePodRequestSchema().dumps(d)

        resp = self.invoke("RenewCubePod", d, **kwargs)
        return apis.RenewCubePodResponseSchema().loads(resp)

    def update_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateCubeDeployment - 更新Deployment

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Deployment** (str) - (Required) base64编码的Deployment的yaml。大小不超过16KB
        - **DeploymentId** (str) - (Required) Deployment的Id
        - **Name** (str) - Deployment的name
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Deployment** (str) - 经过base64编码的Deployment的yaml

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateCubeDeploymentRequestSchema().dumps(d)

        resp = self.invoke("UpdateCubeDeployment", d, **kwargs)
        return apis.UpdateCubeDeploymentResponseSchema().loads(resp)
