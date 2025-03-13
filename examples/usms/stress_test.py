# 压力测试 通过调用ucloud sms网关发送http请求进行压力测试
import json
import threading
import time
from queue import Queue

from ucloud.client import Client


class StressTestConcurrentConfig:
    TotalRequests = 1
    RequestsPerSecond = 1


with open('./config.json', 'r') as fp:
    client_config = json.load(fp)

client = Client(
    client_config
)


def send_sms():
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


# 工作线程函数，控制每秒请求数
def worker(queue):
    while True:
        try:
            # 从队列中获取任务，非阻塞
            queue.get_nowait()
            send_sms()
            queue.task_done()
        except:
            break


if __name__ == '__main__':
    q = Queue()

    # 填充队列
    for _ in range(StressTestConcurrentConfig.TotalRequests):
        q.put(None)

    while not q.empty():
        # 每秒启动 REQUESTS_PER_SECOND 个线程
        threads = []
        for _ in range(min(StressTestConcurrentConfig.RequestsPerSecond, q.qsize())):
            t = threading.Thread(target=worker, args=(q,))
            threads.append(t)
            t.start()

        # 等待当前批次线程完成
        for t in threads:
            t.join()

        # 每秒休眠，确保速率控制
        time.sleep(1)

    print("所有请求已发送完成")
