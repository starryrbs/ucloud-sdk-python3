""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.isms.schemas import apis


class ISMSClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(ISMSClient, self).__init__(config, transport, middleware, logger)

    def create_isms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateISMSSignature - 调用接口CreateISMSSignature申请视频短信签名

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **CertificateType** (int) - (Required) 签名的资质证明文件类型，需与签名类型保持一致，说明如下：0-三证合一/企业营业执照/组织机构代码证书/社会信用代码证书；1-应用商店后台开发者管理截图；2-备案服务商的备案成功截图(含域名，网站名称，备案号)；3-公众号或小程序的管理界面截图；4-商标注册证书；5-组织机构代码证书、社会信用代码证书；
        - **Description** (str) - (Required) 短信签名申请原因
        - **File** (str) - (Required) 短信签名的资质证明文件，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB
        - **SigContent** (str) - (Required) 短信签名内容；长度为2-12个字符, 可包含中文、数字和符号；无需填写【】或[]，系统会自动添加
        - **SigPurpose** (int) - (Required) 签名用途，0-自用，1-他用；
        - **SigType** (int) - (Required) 签名类型，说明如下：0-公司或企业的全称或简称；1-App应用的全称或简称；2-工信部备案网站的全称或简称；3-公众号或小程序的全称或简称；4-商标名的全称或简称；5-政府/机关事业单位/其他单位的全称或简称；
        - **ProxyFile** (str) - 短信签名授权委托文件，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB；当您是代理并使用第三方的签名时（也即SigPurpose为1-他用），该项为必填项；

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空
        - **SigId** (str) - 短信签名ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreateISMSSignatureRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateISMSSignature", d, **kwargs)
        return apis.CreateISMSSignatureResponseSchema().loads(resp)

    def create_isms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateISMSTemplate - 申请视频短信模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **Content** (str) - (Required) 视频短信模板内容。json数组的字符串格式。如：[{name:"0.txt",type:"txt",content:"北京是一座美丽的城市，我爱北京！",index:0},{name:"1.jpg",type:"jpg",content:"jpg文件字节的base64编码字符串",index:1},{name:”2.mp4”,type:"mp4",content:"mp4文件字节的base64编码字符串",index:2}]。name: 文件名，name中不能出现中文，必须要带上和type相同的后缀；type:文件类型，不能为空，文本为txt，图片为jpg、gif或png，音频为mp3，视频为mp4；content：文件内容，由文本、图片、音频、视频组成，文本使用txt文件，图片使用 jpg、gif、png 格式，音频使用 mp3 格式，视频使用mp4（视频只允许一个），文本、图片、音频、视频文件合计大小不可超过2M；index: 在视频短信中的位置。从0开始。
        - **MsgSignature** (str) - (Required) 视频短信签名
        - **MsgTitle** (str) - (Required) 视频短信标题
        - **Remark** (str) - (Required) 备注
        - **TemplateName** (str) - (Required) 视频短信模板名称
        - **UnsubscribeInfo** (str) - (Required) 退订信息，如：“回T退订”
        - **NetworkOperator** (str) - 需要报备的运营商。json数组的字符串格式。true-需要报备，false-不需要报备。如：{"telecom":true, "mobile":false, "unicom":true }
        - **Purpose** (int) - 模板用途类型：1-验证码类短信模板；2-系统通知类短信模板；3-会员推广类短信模板；
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - API接口调用出错时表示错误信息
        - **ReqUuid** (str) - 本次接口调用请求Id，用于问题排查。
        - **TemplateId** (str) - 申请的模板Id。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateISMSTemplateRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateISMSTemplate", d, **kwargs)
        return apis.CreateISMSTemplateResponseSchema().loads(resp)

    def delete_isms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteISMSSignature - 调用接口DeleteISMSSignature删除视频短信签名

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **SigIds** (list) - (Required) 签名ID，支持以数组的方式，举例，以SigIds.0、SigIds.1...SigIds.N方式传入

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DeleteISMSSignatureRequestSchema().dumps(d)

        resp = self.invoke("DeleteISMSSignature", d, **kwargs)
        return apis.DeleteISMSSignatureResponseSchema().loads(resp)

    def delete_isms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteISMSTemplate - 调用接口DeleteISMSTemplate删除视频短信模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **TemplateIds** (list) - (Required) 模板ID，支持以数组的方式，举例，以TemplateIds.0、TemplateIds.1...TemplateIds.N方式传入

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteISMSTemplateRequestSchema().dumps(d)

        resp = self.invoke("DeleteISMSTemplate", d, **kwargs)
        return apis.DeleteISMSTemplateResponseSchema().loads(resp)

    def get_isms_send_receipt(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetISMSSendReceipt - 获取视频短信发送记录的状态回执

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **TaskIdSet** (list) - (Required) 发送记录TaskId集合。调用SendUSMSVideoMessage时返回的TaskId的集合。以TaskIdSet.0、TaskIdSet.1...TaskIdSet.N的形式传入。每次请求最多支持100个
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Data** (list) - 见 **ReceiptPerTask** 模型定义
        - **Message** (str) - 错误信息
        - **ReqUuid** (str) - 本次请求uuid

        **Response Model**

        **ReceiptPerPhone**
        - **Phone** (str) - 手机号码
        - **ReceiptCode** (str) - 回执码
        - **ReceiptDesc** (str) - 回执结果描述
        - **ReceiptResult** (str) - 回执结果(发送成功、发送失败、状态未知)
        - **ReceiptTime** (int) - 回执返回时间
        - **SessionId** (str) - SessionId


        **ReceiptPerTask**
        - **ReceiptSet** (list) - 见 **ReceiptPerPhone** 模型定义
        - **TaskId** (str) - 发送短信时返回的TaskId


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetISMSSendReceiptRequestSchema().dumps(d)

        resp = self.invoke("GetISMSSendReceipt", d, **kwargs)
        return apis.GetISMSSendReceiptResponseSchema().loads(resp)

    def query_isms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """QueryISMSSignature - 调用接口QueryISMSSignature查询视频短信签名申请状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **SigId** (str) - (Required) 已申请的短信签名ID（短信签名申请时的工单ID）；签名ID和签名至少需填写1项；
        - **SigContent** (str) - 签名内容；签名ID和签名至少需填写1项；

        **Response**

        - **Data** (dict) - 见 **OutSignature** 模型定义
        - **Message** (str) - 发生错误时，表示具体错误描述

        **Response Model**

        **OutSignature**
        - **ErrDesc** (str) - 短信签名未通过审核原因
        - **SigContent** (str) - 短信签名内容
        - **SigId** (str) - 短信签名ID
        - **Status** (int) - 签名状态，0-待审核 1-审核中 2-审核通过 3-审核未通过 4-被禁用


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.QueryISMSSignatureRequestSchema().dumps(d)

        resp = self.invoke("QueryISMSSignature", d, **kwargs)
        return apis.QueryISMSSignatureResponseSchema().loads(resp)

    def query_isms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """QueryISMSTemplate - 查询模板状态信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **TemplateId** (str) - (Required) 模板Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Data** (dict) - 见 **OutTemplate** 模型定义
        - **Message** (str) - 错误信息
        - **ReqUuid** (str) - 本次请求uuid

        **Response Model**

        **OutTemplate**
        - **CreateTime** (int) - 创建时间，时间戳格式1629357838
        - **ExpireTime** (int) - 截止有效时间，时间戳格式1629357838
        - **Purpose** (int) - 视频短信类型（3-会员营销）
        - **Remark** (str) - 备注信息
        - **StatusDesc** (str) - 状态描述。json格式，给出运营商维度的审核状态信息，示例：{"telecom_status":2,"telecom_desc":"审核通过","unicom_status":2,"unicom_desc":"审核通过","mobile_status":2,"mobile_desc":"审核通过"}
        - **TemplateId** (str) - 模板ID
        - **TemplateName** (str) - 模板名称


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.QueryISMSTemplateRequestSchema().dumps(d)

        resp = self.invoke("QueryISMSTemplate", d, **kwargs)
        return apis.QueryISMSTemplateResponseSchema().loads(resp)

    def send_isms_message(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """SendISMSMessage - 发送视频短信

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_
        - **PhoneSet** (list) - (Required) 手机号码列表。暂时只支持中国大陆号码。若号码中带区号，需要将区号使用小括号包含，放在号码前面。如: (86)1851623xxxx
        - **TemplateId** (str) - (Required) 视频短信模板Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist>`_

        **Response**

        - **Message** (str) - 错误信息
        - **ReqUuid** (str) - 本次请求uuid
        - **TaskId** (str) - 本次调用TaskId，使用该字段查询回执信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.SendISMSMessageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("SendISMSMessage", d, **kwargs)
        return apis.SendISMSMessageResponseSchema().loads(resp)

    def update_isms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateISMSSignature - 调用接口UpdateISMSSignature修改未通过审核的视频短信签名，并重新提交审核

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **SigContent** (str) - (Required) 新的短信签名内容；长度为2-12个字符, 可包含中文、数字和符号；无需填写【】或[]，系统会自动添加
        - **SigId** (str) - (Required) 签名ID，支持以数组的方式，举例，以SigIds.0、SigIds.1...SigIds.N方式传入
        - **SigPurpose** (int) - (Required) 签名用途，0-自用，1-他用；
        - **SigType** (int) - (Required) 签名类型，说明如下：0-公司或企业的全称或简称；1-App应用的全称或简称；2-工信部备案网站的全称或简称；3-公众号或小程序的全称或简称；4-商标名的全称或简称；5-政府/机关事业单位/其他单位的全称或简称；
        - **CertificateType** (int) - 签名的资质证明文件类型，需与签名类型保持一致，说明如下：0-三证合一/企业营业执照/组织机构代码证书/社会信用代码证书；1-应用商店后台开发者管理截图；2-备案服务商的备案成功截图(含域名，网站名称，备案号)；3-公众号或小程序的管理界面截图；4-商标注册证书；5-组织机构代码证书、社会信用代码证书；
        - **Document** (str) - 短信签名的资质证明文件URL，若未更改审核材料，则该处使用已上传审核材料的URL链接，否则使用File参数
        - **File** (str) - 短信签名的资质证明文件内容，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB。内容格式如下: [file type];[code type],[base64]  如：image/jpeg;base64,5YaF5a65
        - **ProxyDoc** (str) - 短信签名授权委托文件URL，若未更改授权委托文件，则该处填写已上传的授权委托文件的URL链接，否则使用ProxyFile参数
        - **ProxyFile** (str) - 短信签名授权委托文件内容，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB；当您是代理并使用第三方的签名时（也即SigPurpose为1-他用），该项为必填项；格式和File类似。

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.UpdateISMSSignatureRequestSchema().dumps(d)

        resp = self.invoke("UpdateISMSSignature", d, **kwargs)
        return apis.UpdateISMSSignatureResponseSchema().loads(resp)
