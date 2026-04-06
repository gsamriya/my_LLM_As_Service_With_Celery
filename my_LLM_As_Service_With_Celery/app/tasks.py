from celery import Celery
from .config import settings
import time
import random

celery_app = Celery(
    "llm_tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

@celery_app.task
def generate_llm_response(prompt: str) -> str:
    # Simulated LLM response (takes 3–5 seconds)
    time.sleep(random.randint(3, 5))
    return f"Generated response for: {prompt}"
