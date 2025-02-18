import time

from ucloud.client import Client
from ucloud.core import auth

"""
ProjectId=org-0umfhx&Signature=194024aa96bb2d4f308187940537243f9f10824d&ShortLinkDomain=x.6a1.cn&Action=BatchCreateUSLKShortLink&ScenarioID=53&PublicKey=CAH1meOA4uCAmi5HPC46NgE5fYnImeHlwadOFvJ2H&Proto=http&StartTime=1661875200&EndTime=1664467200&LongLinks.0%3Dhttps%3A%2F%2Fmst.vip.com%2F94F7w_vcN0uEYmAu013BAQ.php%3Fwq%3D1%26wapid%3Dmst_100035863%26_src%3Dmst%26extra_banner%3D115035863%26nova%3D1%26nova_platform%3D1%26mst_page_type%3Dguide%26extra_channel%3Daim
"""


client = Client(
    {
        "project_id": "org-ixs3fl",
        "public_key": "4JEWwze9AhdIPIfFk4ENIk78x5Pfk",
        "private_key": "GOfhdGsaG1CIWt9O5JtduQHgktIN3azZ0EcRk7sXGca3",
    }
)

def get_signature():
    cred = auth.Credential(
        "4ZF9o0XPisb6zXaLguqDl18mG56XvnGDx",
        "1s6wQQ9yhuJ4MF2TwwGQlPAZpDzzilMrFYwHOOIT0jZ",
    )
    d = {
        "TemplateId": "UTA220908DJFCSD",
        "PhoneNumbers.0": "18323348282",
        "SigContent": "狮桥",
        "ProjectId": "org-l11ua0",
        "TemplateParams.0": "您预约的[遗迹探险套装金属币&指南针]即将开始预售，请打开[新物集]支持喜欢的项目。",
        "Action": "SendUSMSMessage"
    }
    print(cred.verify_ac(d))


"""

https://api.ucloud.cn/?Action=SendBatchUSMSMessage&ProjectId=org-1funf0&TaskContent=W3siVGVtcGxhdGVJZCI6ICJVVE4yMzA4MjRUNlFUSVAiLCAiU2lnQ29udGVudCI6ICJVQ2xvdWTkvJjliLvlvpciLCAiVGFyZ2V0IjogW3siVGVtcGxhdGVQYXJhbXMiOiBbIuadjuS9s+ixqiIsIjIwMjPlubQ45pyIMjTml6UiLCLkuIrmtbfluIIiXSwgIlBob25lIjogIjE4MDA1MjE4NTY5IiwgIlVzZXJJZCI6ICJ5b3UgbWFuIGMgZGVmaW5lIHRoZSBjb250ZW50In0gXSB9IF0=&PublicKey=6ItlMaO0t988dUfnvjKAOfH5lLPsNnnaV1Y5tbUaU
"""


# 'f50ff18bc2f71abc88d31d7152a71dc78bf0beef'
def main():


    usms = client.usms()
    usms.config.region = None

    # task_content = [{"TemplateId": "UTN230824T6QTIP", "SigContent": "UCloud优刻得", "Target": [{"TemplateParams": ["李佳豪","2023年8月24日","上海市"], "Phone": "18005218569", "UserId": "you man c define the content"} ] } ]
    #
    # task_content_str = base64.b64encode(json.dumps(task_content).encode()).decode()
    # task_content_str = "W3siVGVtcGxhdGVJZCI6ICJVVE4yMzA4MjRUNlFUSVAiLCAiU2lnQ29udGVudCI6ICJVQ2xvdWTkvJjliLvlvpciLCAiVGFyZ2V0IjogW3siVGVtcGxhdGVQYXJhbXMiOiBbIuadjuS9s+ixqiIsIjIwMjPlubQ45pyIMjTml6UiLCLkuIrmtbfluIIiXSwgIlBob25lIjogIjE4MDA1MjE4NTY5IiwgIlVzZXJJZCI6ICJ5b3UgbWFuIGMgZGVmaW5lIHRoZSBjb250ZW50In0gXSB9IF0"
    # response = usms.send_batch_usms_message({
    #     "ProjectId": "org-1funf0",
    #     "TaskContent": task_content_str,
    # })

    response = usms.send_usms_message(
        {
            "ProjectId": "org-ixs3fl",
            "PhoneNumbers": ["18570351804"],
            "SigContent": "圆通速递",
            "TemplateId": "UTN240522FQHEAL",
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
