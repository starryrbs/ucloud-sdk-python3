import json
import time

from ucloud.client import Client
from ucloud.core import auth

with open('./config.json', 'r') as fp:
    client_config = json.load(fp)

client = Client(
    client_config
)


def get_signature():
    cred = auth.Credential(
        "xxx",
        "xxx",
    )
    d = {
        "TemplateId": "xxx",
        "PhoneNumbers.0": "xxx",
        "SigContent": "xxx",
        "ProjectId": "xxxx",
        "TemplateParams.0": "xxxx",
        "Action": "SendUSMSMessage"
    }
    print(cred.verify_ac(d))

def main():
    usms = client.usms()
    usms.config.region = None

    response = usms.send_usms_message(
        {
            "ProjectId": client_config["project_id"],
            "PhoneNumbers": [client_config["phone"]],
            "SigContent": "圆通速递",
            "TemplateId": client_config["template_id"],
            "TemplateParams": []
        })

    print(response.values())


def test_add_backfill():
    usms = client.usms()
    usms.config.region = None
    response = usms.add_backfill({
        "SendNo": "8a0899e3-0858-447c-c7a8-f30d2ff85ecd",
        "Target": "+2349037108662",
        "BackfillTime": int(time.time()),
        "Content": "test backfill",
        "SendTime": int(time.time()),
    })
    print(response.values())


if __name__ == "__main__":
    main()
