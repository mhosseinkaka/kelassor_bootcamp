from celery import shared_task

@shared_task(bind=True, default_retry_delay= 60)
def send_sms_to_user(self, phone):
    try:
        message = "سلام ویلا شما به پروژه ما اضافه شد :))"
        ...
    except Exception as e:
        raise self.retry(exc=e, max_retries=10)