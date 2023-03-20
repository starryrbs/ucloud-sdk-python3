""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.upgsql.schemas import apis


class UPgSQLClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UPgSQLClient, self).__init__(
            config, transport, middleware, logger
        )

    def backup_u_pg_sql_log(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """BackupUPgSQLLog - 备份日志包

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BackupFile** (str) - (Required) 备份查询结果文件名称
        - **BackupName** (str) - (Required) 备份导出文件名称
        - **InstanceID** (str) - (Required) 资源ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BeginTime** (int) - 日志开始时间
        - **EndTime** (int) - 日志结束时间
        - **LogType** (str) - 日志类型:slow(慢日志),error(错误日志)

        **Response**

        - **Message** (str) - 错误信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.BackupUPgSQLLogRequestSchema().dumps(d)

        resp = self.invoke("BackupUPgSQLLog", d, **kwargs)
        return apis.BackupUPgSQLLogResponseSchema().loads(resp)

    def create_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUPgSQLInstance - 创建PG云数据库

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **AdminPassword** (str) - (Required) 管理员密码
        - **DBVersion** (str) - (Required) PostgreSQL的版本，pg10.4:postgresql-10.4，pg13.4:postgresql-13.4
        - **DiskSpace** (str) - (Required) 磁盘空间(GB)
        - **MachineType** (str) - (Required) 机器配置类型，2核4G的机器:o.pgsql2m.medium
        - **Name** (str) - (Required) 实例名称，至少6位
        - **ParamGroupID** (int) - (Required) DB实例使用的配置参数组id
        - **Port** (int) - (Required) 端口默认为5432
        - **SubnetID** (str) - (Required) 子网ID
        - **VPCID** (str) - (Required) VPC的ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceMode** (str) - UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例 "HA": 高可用版UDB实例 默认是"Normal"

        **Response**

        - **InstanceID** (str) - 资源ID
        - **Message** (str) - 返回信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUPgSQLInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUPgSQLInstance", d, **kwargs)
        return apis.CreateUPgSQLInstanceResponseSchema().loads(resp)

    def create_u_pg_sql_param_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUPgSQLParamTemplate - 创建PG参数模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DBVersion** (str) - (Required) 什么版本,以及类型的DB
        - **GroupName** (str) - (Required) 模板名称
        - **SrcGroupID** (int) - (Required) 基准模板
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Description** (str) - 描述信息

        **Response**

        - **GroupID** (int) - 创建的模板ID
        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUPgSQLParamTemplateRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUPgSQLParamTemplate", d, **kwargs)
        return apis.CreateUPgSQLParamTemplateResponseSchema().loads(resp)

    def create_u_pg_sql_readonly(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUPgSQLReadonly - 创建PG从库

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskSpace** (int) - (Required) 磁盘空间
        - **MachineType** (str) - (Required) 机器配置类型，2核4G的机器:o.pgsql2m.medium
        - **Name** (str) - (Required) Db名称
        - **Port** (int) - (Required) DB端口
        - **SrcInstanceID** (str) - (Required) 同步的源库
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **SubnetID** (str) - 子网ID
        - **VPCID** (str) - VPCID

        **Response**

        - **InstanceID** (str) - 资源ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateUPgSQLReadonlyRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUPgSQLReadonly", d, **kwargs)
        return apis.CreateUPgSQLReadonlyResponseSchema().loads(resp)

    def delete_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUPgSQLInstance - 删除PG实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) 实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("DeleteUPgSQLInstance", d, **kwargs)
        return apis.DeleteUPgSQLInstanceResponseSchema().loads(resp)

    def delete_u_pg_sql_param_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUPgSQLParamTemplate - 删除参数模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **GroupID** (int) - (Required) 模板ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteUPgSQLParamTemplateRequestSchema().dumps(d)

        resp = self.invoke("DeleteUPgSQLParamTemplate", d, **kwargs)
        return apis.DeleteUPgSQLParamTemplateResponseSchema().loads(resp)

    def download_u_pg_sql_param_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DownloadUPgSQLParamTemplate - 下载参数模板信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **GroupID** (int) - (Required) 参数模板id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Content** (str) - base64编码过的
        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DownloadUPgSQLParamTemplateRequestSchema().dumps(d)

        resp = self.invoke("DownloadUPgSQLParamTemplate", d, **kwargs)
        return apis.DownloadUPgSQLParamTemplateResponseSchema().loads(resp)

    def get_u_pg_sql_backup_strategy(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLBackupStrategy - 获取备份策略

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) DB实例Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **BackupMethod** (str) - 默认的备份方式
        - **BackupTimeRange** (str) - 自动备份预计开始时间范围
        - **BackupWeek** (str) - 自动备份预期星期几(1~7)开始
        - **Message** (str) - 返回的详细信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLBackupStrategyRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLBackupStrategy", d, **kwargs)
        return apis.GetUPgSQLBackupStrategyResponseSchema().loads(resp)

    def get_u_pg_sql_backup_url(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLBackupURL - 获取备份下载地址

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BackupID** (str) - (Required) 备份Id
        - **InstanceID** (str) - (Required) DB实例Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **BackupPath** (str) - DB实例备份文件公网的地址
        - **InnerBackupPath** (str) - DB实例备份文件内网的地址
        - **Message** (str) - 返回的详细信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLBackupURLRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLBackupURL", d, **kwargs)
        return apis.GetUPgSQLBackupURLResponseSchema().loads(resp)

    def get_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLInstance - 获取PG云数据库实例描述

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) 资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (dict) - 见 **UDBInstance** 模型定义
        - **Message** (str) - 返回信息

        **Response Model**

        **UDBInstance**
        - **AdminUser** (str) - 管理员帐户名，默认root
        - **BackupBeginTime** (int) - 备份开始时间，单位小时计，默认3点
        - **BackupCount** (int) - 备份文件保留的数量，默认7次
        - **BackupDate** (str) - 用于设置备份策略的备份日期标记位。共7位,每一位为一周中一天的备份情况 0表示关闭当天备份,1表示打开当天备份。最右边的一位 为星期天的备份开关，其余从右到左依次为星期一到星期 六的备份配置开关，每周必须至少设置两天备份。 例如：1100000 表示打开星期六和星期五的自动备份功能
        - **BackupTimeRange** (int) - 备份的时间段，范围[0,23]
        - **BackupZone** (str) - 跨可用区高可用备库所在可用区
        - **CreateTime** (int) - DB实例创建时间，采用UTC计时时间戳
        - **DBVersion** (str) - DB 版本
        - **DataFileSize** (float) - DB实例数据文件大小，单位GB
        - **DiskSpace** (int) - 磁盘空间(GB), 默认根据配置机型
        - **DiskUsedSize** (float) - DB实例磁盘已使用空间，单位GB
        - **ExpiredTime** (int) - DB实例过期时间，采用UTC计时时间戳
        - **IP** (str) - DBip
        - **InstanceID** (str) - DB实例id
        - **InstanceMode** (str) - Normal/HA,普通/高可用
        - **LogFileSize** (float) - DB实例日志文件大小，单位GB
        - **MemoryLimit** (int) - 内存限制(MB)，默认根据配置机型
        - **ModifyTime** (int) - DB实例修改时间，采用UTC计时时间戳
        - **Name** (str) - 实例名称
        - **ParamGroupID** (int) - DB实例使用的配置参数组id
        - **Port** (int) - DB port
        - **Remark** (str) - 备注
        - **State** (str) - DB状态标记 Init：初始化中，Fail：安装失败，Starting：启动中，Running：运行，Shutdown：关闭中，Shutoff：已关闭，Delete：已删除，Upgrading：升级中，Promoting：提升为独库进行中，Recovering：恢复中，Recover fail：恢复失败
        - **SubnetID** (str) - 子网ID
        - **SystemFileSize** (float) - DB实例系统文件大小，单位GB
        - **VPCID** (str) - VPC的ID
        - **Zone** (str) - DB实例所在可用区


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLInstance", d, **kwargs)
        return apis.GetUPgSQLInstanceResponseSchema().loads(resp)

    def get_u_pg_sql_instance_log(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLInstanceLog - 可以查询DB的错误日志和满查询日志

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **AccountID** (int) - (Required)
        - **BeginTime** (int) - (Required) 起始时间，需使用时间戳
        - **CompanyID** (int) - (Required)
        - **DBId** (str) - (Required) 实例ClusterID
        - **EndTime** (int) - (Required) 结束时间，需使用时间戳，结束时间需大于起始时间
        - **LogType** (str) - (Required) 日志类型
        - **ZoneID** (int) - (Required) 可用区

        **Response**

        - **Log** (str) - 返回的日志信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLInstanceLogRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLInstanceLog", d, **kwargs)
        return apis.GetUPgSQLInstanceLogResponseSchema().loads(resp)

    def get_u_pg_sql_instance_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLInstancePrice - 获取创建PG云数据库价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskSpace** (int) - (Required) 磁盘空间(GB)
        - **InstanceMode** (str) - (Required) UDB实例模式类型, 可选值如下: "Normal": 普通版UDB实例 "HA": 高可用版UDB实例
        - **MachineType** (str) - (Required) 机器配置类型 参考2C4G机器：o.pgsql2m.medium
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ChargeType** (str) - 计费模式。枚举值为： Year，按年付费； Month，按月付费； Dynamic，按小时付费（需开启权限）。默认为月付
        - **Quantity** (int) - 购买时长。默认: 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末。

        **Response**

        - **PriceSet** (list) - 见 **UPgSQLInstancePriceSet** 模型定义

        **Response Model**

        **UPgSQLInstancePriceSet**
        - **ChargeType** (str) - 计费类型，Year，Month，Dynamic。
        - **OriginalPrice** (float) - 购买原价，单位：元。
        - **Price** (float) - 实际价格，单位：元，保留小数点后两位有效数字。


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLInstancePriceRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLInstancePrice", d, **kwargs)
        return apis.GetUPgSQLInstancePriceResponseSchema().loads(resp)

    def get_u_pg_sql_param_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLParamTemplate - 获取模板信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **GroupID** (int) - (Required) 模板ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Data** (list) - 见 **Param** 模型定义
        - **Message** (str) - 描述信息

        **Response Model**

        **Param**
        - **AllowedVal** (str) - 允许的值
        - **ApplyType** (int) - 允许类型
        - **FormatType** (int) - 参数格式类型
        - **Key** (str) - 参数Key
        - **Modifiable** (bool) - 是否可以修改
        - **Value** (str) - 参数值
        - **ValueType** (int) - 值类型


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLParamTemplateRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLParamTemplate", d, **kwargs)
        return apis.GetUPgSQLParamTemplateResponseSchema().loads(resp)

    def get_u_pg_sql_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUPgSQLUpgradePrice - 获取 PG 云数据库升降级价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskSpace** (int) - (Required) 磁盘空间(GB)
        - **InstanceID** (str) - (Required) 资源ID
        - **MachineType** (str) - (Required) 机器配置类型
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceMode** (str) - UDB实例模式类型, 可选值如下: "normal": 普通版UDB实例 "ha": 高可用版UDB实例 默认是"normal"

        **Response**

        - **OriginalPrice** (float) - 限时优惠的折前原价
        - **Price** (float) - 规格调整差价。精确到小数点后2位。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetUPgSQLUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetUPgSQLUpgradePrice", d, **kwargs)
        return apis.GetUPgSQLUpgradePriceResponseSchema().loads(resp)

    def list_u_pg_sql_backup(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUPgSQLBackup - 获取备份列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) DB实例Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BackupType** (int) - 备份类型,默认值是0(0:表示全部,1:自动备份,2:手动备份
        - **Limit** (int) - 返回数据长度，默认为20，最大100
        - **Offset** (int) - 列表起始位置偏移量，默认为0

        **Response**

        - **DataSet** (list) - 见 **UPgSQLBackup** 模型定义
        - **Message** (str) - 返回的详细信息
        - **TotalCount** (int) - 总个数

        **Response Model**

        **UPgSQLBackup**
        - **BackupEndTime** (int) - 备份完成时间(Unix时间戳)
        - **BackupID** (str) - 备份id
        - **BackupName** (str) - 备份名称
        - **BackupSize** (int) - 备份文件大小(字节)
        - **BackupStartTime** (int) - 备份时间(Unix时间戳)
        - **BackupType** (int) - 备份类型，手动或者自动
        - **InstanceID** (str) - DB实例Id
        - **Region** (str) - 备份所在地域
        - **State** (str) - 备份状态 (Backuping：备份中,Success:备份成功, Failed:备份失败, Expired:备份过期)


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUPgSQLBackupRequestSchema().dumps(d)

        resp = self.invoke("ListUPgSQLBackup", d, **kwargs)
        return apis.ListUPgSQLBackupResponseSchema().loads(resp)

    def list_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUPgSQLInstance - 获取PG云数据库列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **UDBInstanceSet** 模型定义
        - **Message** (str) - 错误信息

        **Response Model**

        **UDBInstanceSet**
        - **CreateTime** (int) - DB实例创建时间，采用UTC计时时间戳
        - **DBVersion** (str) - 实例的版本，包括postgresql-10.4,postgresql-13.4
        - **DataSet** (list) - 见 **UDBReadonlyInstance** 模型定义
        - **ExpiredTime** (int) - DB实例过期时间，采用UTC计时时间戳
        - **IP** (str) - DB实例ip
        - **InstanceID** (str) - 资源ID
        - **InstanceMode** (str) - normal/ha/readonly,普通/高可用/只读从库
        - **MachineType** (str) - 机器规格，格式为nCmG,n代表cpu核数，m代表内存大小(GB)
        - **Name** (str) - 实例名称
        - **Remark** (str) - 备注
        - **State** (str) - 实例状态标记 Initing：初始化中，InitFailed：安装失败，Starting：启动中， Running：运行，Stopping：关闭中，Stopped：已关闭,Deleted: 已删除，Upgrading: 升级中 ，Promoting：提升为主库进行中，Recovering：恢复中，RecoverFailed：恢复失败，StartFailed：启动失败，ShutdownFailed：关闭失败，Deleting：删除中，DeleteFailed：删除失败
        - **SubnetID** (str) - 子网ID
        - **VPCID** (str) - VPC的ID
        - **Zone** (str) - 可用区


        **UDBReadonlyInstance**
        - **CreateTime** (int) - DB实例创建时间，采用UTC计时时间戳
        - **DBVersion** (str) - 实例的版本，包括postgresql-10.4,postgresql-13.4
        - **ExpiredTime** (int) - DB实例过期时间，采用UTC计时时间戳
        - **IP** (str) - DB实例ip
        - **InstanceID** (str) - 资源ID
        - **InstanceMode** (str) - normal/ha/readonly,普通/高可用/只读从库
        - **MachineType** (str) - 机器规格，格式为nCmG,n代表cpu核数，m代表内存大小(GB)
        - **Name** (str) - 实例名称
        - **Remark** (str) - 备注
        - **State** (str) - 实例状态标记 Initing：初始化中，InitFailed：安装失败，Starting：启动中， Running：运行，Stopping：关闭中，Stopped：已关闭,Deleted: 已删除，Upgrading: 升级中 ，Promoting：提升为主库进行中，Recovering：恢复中，RecoverFailed：恢复失败，StartFailed：启动失败，ShutdownFailed：关闭失败，Deleting：删除中，DeleteFailed：删除失败
        - **SubnetID** (str) - 子网ID
        - **VPCID** (str) - VPC的ID
        - **Zone** (str) - 可用区


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("ListUPgSQLInstance", d, **kwargs)
        return apis.ListUPgSQLInstanceResponseSchema().loads(resp)

    def list_u_pg_sql_log(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUPgSQLLog - 获取数据库日志

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BeginTime** (int) - (Required) 查询的日志开始的时间戳
        - **EndTime** (int) - (Required) 查询日志的结束时间戳
        - **InstanceID** (str) - (Required) 资源ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **LogSet** 模型定义
        - **Message** (str) - 错误信息

        **Response Model**

        **LogSet**
        - **BeginTime** (int) -
        - **EndTime** (int) -
        - **Name** (str) -
        - **Size** (int) -


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUPgSQLLogRequestSchema().dumps(d)

        resp = self.invoke("ListUPgSQLLog", d, **kwargs)
        return apis.ListUPgSQLLogResponseSchema().loads(resp)

    def list_u_pg_sql_machine_type(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUPgSQLMachineType - 获取UPgSQL支持机器类型列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **PgSQLMachineType** 模型定义
        - **Message** (str) - 返回信息

        **Response Model**

        **PgSQLMachineType**
        - **Cpu** (int) - cpu核数
        - **Description** (str) - 格式为nCmG,n代表cpu核数，m代表内存大小(GB)
        - **ID** (str) - 机器类型ID
        - **Memory** (int) - 内存用量(GB)
        - **Os** (str) - 机器类型，N/O


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUPgSQLMachineTypeRequestSchema().dumps(d)

        resp = self.invoke("ListUPgSQLMachineType", d, **kwargs)
        return apis.ListUPgSQLMachineTypeResponseSchema().loads(resp)

    def list_u_pg_sql_version(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUPgSQLVersion - 获取UPgSQL支持版本列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **DataSet** (list) - 见 **PgSQLVersion** 模型定义
        - **Message** (str) - 返回信息

        **Response Model**

        **PgSQLVersion**
        - **Available** (str) - 2位二进制控制是否开放单点和高可用，前一位控制单点是否开放，后一位控制高可用，例如"01"代表只开放高可用，"10"代表只开放单点，"11"代表全开放
        - **DBVersion** (str) - PgSQL版本


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListUPgSQLVersionRequestSchema().dumps(d)

        resp = self.invoke("ListUPgSQLVersion", d, **kwargs)
        return apis.ListUPgSQLVersionResponseSchema().loads(resp)

    def restart_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RestartUPgSQLInstance - 重启PG实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) 实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ForceToRestart** (bool) - 是否强制重启
        - **RestartHost** (bool) - 是否一并重启主机

        **Response**

        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RestartUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("RestartUPgSQLInstance", d, **kwargs)
        return apis.RestartUPgSQLInstanceResponseSchema().loads(resp)

    def start_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StartUPgSQLInstance - 启动 PG实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) 实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - 返回信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StartUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("StartUPgSQLInstance", d, **kwargs)
        return apis.StartUPgSQLInstanceResponseSchema().loads(resp)

    def stop_u_pg_sql_creating_readonly(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StopUPgSQLCreatingReadonly - 停止创建从库

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) 停止创建从库
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StopUPgSQLCreatingReadonlyRequestSchema().dumps(d)

        resp = self.invoke("StopUPgSQLCreatingReadonly", d, **kwargs)
        return apis.StopUPgSQLCreatingReadonlyResponseSchema().loads(resp)

    def stop_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """StopUPgSQLInstance - 关闭PG实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) 实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **ForceToStop** (bool) - 是否强制关闭
        - **StopHost** (bool) - 是否将主机一并关闭

        **Response**

        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.StopUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("StopUPgSQLInstance", d, **kwargs)
        return apis.StopUPgSQLInstanceResponseSchema().loads(resp)

    def update_u_pg_sql_attribute(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateUPgSQLAttribute - 更新数据库属性

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) DB实例Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Name** (str) - 新的db名字(不能为空字符串)
        - **Remark** (str) - 新的备注信息

        **Response**

        - **Message** (str) - 返回的详细信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateUPgSQLAttributeRequestSchema().dumps(d)

        resp = self.invoke("UpdateUPgSQLAttribute", d, **kwargs)
        return apis.UpdateUPgSQLAttributeResponseSchema().loads(resp)

    def update_u_pg_sql_backup_strategy(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateUPgSQLBackupStrategy - 修改备份策略

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) DB实例Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **BackupMethod** (str) - 选择默认的备份方式
        - **BackupTimeRange** (str) - 自动备份预计开始时间范围(00:00~23:59)，例如:(3:00~4:00)
        - **BackupWeek** (str) - 自动备份预期星期几(1~7)开始。默认1,2,3,4,5,6,7(星期一到星期日)

        **Response**

        - **Message** (str) - 返回的详细信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateUPgSQLBackupStrategyRequestSchema().dumps(d)

        resp = self.invoke("UpdateUPgSQLBackupStrategy", d, **kwargs)
        return apis.UpdateUPgSQLBackupStrategyResponseSchema().loads(resp)

    def update_u_pg_sql_password(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateUPgSQLPassword - 更新数据库密码

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **InstanceID** (str) - (Required) DB实例Id
        - **Password** (str) - (Required) 新的db密码
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - 返回的详细信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateUPgSQLPasswordRequestSchema().dumps(d)

        resp = self.invoke("UpdateUPgSQLPassword", d, **kwargs)
        return apis.UpdateUPgSQLPasswordResponseSchema().loads(resp)

    def upgrade_u_pg_sql_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpgradeUPgSQLInstance - 硬件规格升降级

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **DiskSpace** (int) - (Required) 磁盘空间(GB)
        - **InstanceID** (str) - (Required) 资源ID
        - **MachineType** (str) - (Required) 机器配置类型
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - 错误信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpgradeUPgSQLInstanceRequestSchema().dumps(d)

        resp = self.invoke("UpgradeUPgSQLInstance", d, **kwargs)
        return apis.UpgradeUPgSQLInstanceResponseSchema().loads(resp)

    def upload_u_pg_sql_param_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UploadUPgSQLParamTemplate - 上传参数模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Content** (str) - (Required) base64编码过的
        - **DBVersion** (str) - (Required) 应用的DB版本
        - **GroupName** (str) - (Required) 模板名称
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Description** (str) - 模板描述
        - **ParamGroupType** (str) - 版本

        **Response**

        - **GroupID** (int) - 生成的模板ID
        - **Message** (str) - 描述信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UploadUPgSQLParamTemplateRequestSchema().dumps(d)

        resp = self.invoke("UploadUPgSQLParamTemplate", d, **kwargs)
        return apis.UploadUPgSQLParamTemplateResponseSchema().loads(resp)
