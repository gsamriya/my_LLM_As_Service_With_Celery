from fastapi import FastAPI
from pydantic import BaseModel
from app.tasks import generate_llm_response

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/generate")
def generate(data: PromptInput):
    task = generate_llm_response.delay(data.prompt)
    return {"task_id": task.id}

@app.get("/result/{task_id}")
def get_result(task_id: str):
    task = generate_llm_response.AsyncResult(task_id)
    if task.state == "PENDING":
        return {"status": "Pending"}
    elif task.state == "SUCCESS":
        return {"status": "Completed", "result": task.result}
    elif task.state == "FAILURE":
        return {"status": "Failed", "error": str(task.result)}
    else:
        return {"status": task.state}
