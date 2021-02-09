from celery import Celery

import config
from app.utils.helpers import fetch_flight_check, save_flight

celery_app = Celery(
    __name__,
    broker=config.CELERY_BROKER,
    backend=config.CELERY_BACKEND,
)


@celery_app.task
def check_flight_periodically(flight):
    INTERVAL_IN_SECONDS = 30

    check = fetch_flight_check(flight)

    if not check['checked'] and not check['invalid']:
        check_flight_periodically.apply_async(
            [flight],
            countdown=INTERVAL_IN_SECONDS,
        )
    elif check['checked']:
        save_flight(flight)
