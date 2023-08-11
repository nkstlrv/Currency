from celery import shared_task
import time


@shared_task
def demo_task():
    for i in range(10):
        print("TESTING WORKER")
        time.sleep(0.1)
