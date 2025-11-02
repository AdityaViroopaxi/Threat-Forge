from celery import Celery

celery = Celery(__name__, broker=os.getenv("REDIS_URL"), backend=os.getenv("REDIS_URL"))
@celery.task
def fetch_and_update_iocs():
    # Pull IOC data, normalize, score, and update MongoDB
    pass
