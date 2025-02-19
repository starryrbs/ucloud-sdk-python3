import json

from ucloud.client import Client
from ucloud.core import auth

with open('./config.json', 'r') as fp:
    client_config = json.load(fp)

client = Client(
    client_config
)


def get_signature(data: dict):
    cred = auth.Credential(
        "4ZF9o0XPisb6zXaLguqDl18mG56XvnGDx",
        "1s6wQQ9yhuJ4MF2TwwGQlPAZpDzzilMrFYwHOOIT0jZ",
    )
    return cred.verify_ac(data)


def test_send_message():
    # 发送视频短信
    # response= client.uaccount().get_project_list()
    # print(response)
    iclient = client.isms()
    iclient.config.region = None
    response = iclient.send_isms_message({
        "TemplateId": "UVTG250218EEE310",
        "PhoneSet": ["15755407860"],
        "Zone": "",
        "Region": ""
    })
    print(response)


if __name__ == "__main__":
    main()
