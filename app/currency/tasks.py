from celery import shared_task


@shared_task
def demo_test_task():
    print("TESTING WORKERS")
