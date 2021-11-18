""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core import client


class Client(client.Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        self._config = config
        super(Client, self).__init__(
            self._auto_config(), transport, middleware, logger
        )

    def pathx(self):
        from ucloud.services.pathx.client import PathXClient

        return PathXClient(
            self._auto_config("pathx"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def cube(self):
        from ucloud.services.cube.client import CubeClient

        return CubeClient(
            self._auto_config("cube"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def ipsecvpn(self):
        from ucloud.services.ipsecvpn.client import IPSecVPNClient

        return IPSecVPNClient(
            self._auto_config("ipsecvpn"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def isms(self):
        from ucloud.services.isms.client import ISMSClient

        return ISMSClient(
            self._auto_config("isms"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def stepflow(self):
        from ucloud.services.stepflow.client import StepFlowClient

        return StepFlowClient(
            self._auto_config("stepflow"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uaccount(self):
        from ucloud.services.uaccount.client import UAccountClient

        return UAccountClient(
            self._auto_config("uaccount"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def ubill(self):
        from ucloud.services.ubill.client import UBillClient

        return UBillClient(
            self._auto_config("ubill"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def ucdn(self):
        from ucloud.services.ucdn.client import UCDNClient

        return UCDNClient(
            self._auto_config("ucdn"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def udb(self):
        from ucloud.services.udb.client import UDBClient

        return UDBClient(
            self._auto_config("udb"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uddb(self):
        from ucloud.services.uddb.client import UDDBClient

        return UDDBClient(
            self._auto_config("uddb"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def udpn(self):
        from ucloud.services.udpn.client import UDPNClient

        return UDPNClient(
            self._auto_config("udpn"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def udts(self):
        from ucloud.services.udts.client import UDTSClient

        return UDTSClient(
            self._auto_config("udts"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def udisk(self):
        from ucloud.services.udisk.client import UDiskClient

        return UDiskClient(
            self._auto_config("udisk"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uec(self):
        from ucloud.services.uec.client import UECClient

        return UECClient(
            self._auto_config("uec"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def ufs(self):
        from ucloud.services.ufs.client import UFSClient

        return UFSClient(
            self._auto_config("ufs"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def ufile(self):
        from ucloud.services.ufile.client import UFileClient

        return UFileClient(
            self._auto_config("ufile"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uhost(self):
        from ucloud.services.uhost.client import UHostClient

        return UHostClient(
            self._auto_config("uhost"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uhub(self):
        from ucloud.services.uhub.client import UHubClient

        return UHubClient(
            self._auto_config("uhub"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uk8s(self):
        from ucloud.services.uk8s.client import UK8SClient

        return UK8SClient(
            self._auto_config("uk8s"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def ulb(self):
        from ucloud.services.ulb.client import ULBClient

        return ULBClient(
            self._auto_config("ulb"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def umem(self):
        from ucloud.services.umem.client import UMemClient

        return UMemClient(
            self._auto_config("umem"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def unvs(self):
        from ucloud.services.unvs.client import UNVSClient

        return UNVSClient(
            self._auto_config("unvs"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def unet(self):
        from ucloud.services.unet.client import UNetClient

        return UNetClient(
            self._auto_config("unet"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def uphost(self):
        from ucloud.services.uphost.client import UPHostClient

        return UPHostClient(
            self._auto_config("uphost"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def usms(self):
        from ucloud.services.usms.client import USMSClient

        return USMSClient(
            self._auto_config("usms"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def vpc(self):
        from ucloud.services.vpc.client import VPCClient

        return VPCClient(
            self._auto_config("vpc"),
            self.transport,
            self.middleware,
            self.logger,
        )

    def _auto_config(self, package="generic"):
        user_agent = "Package/{} {}".format(
            package, self._config.get("user_agent") or ""
        )
        return dict(user_agent=user_agent.rstrip(), **self._config)
