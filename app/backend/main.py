from fastapi import FastAPI, Header, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sse_starlette.sse import EventSourceResponse
import ollama, json, time, os
from typing import Iterable

app = FastAPI(title="Gen-booking-Ukr")

PWD = os.getenv("ONLINE_PASSWORD", "qwerty123")

def check_pwd(x_password: str = Header(...)):
    if x_password != PWD: raise HTTPException(401, "Неправильний пароль")
    return x_password

def llama_stream(prompt: str) -> Iterable[str]:
    stream = ollama.chat(
        model="mamaylm-ukr",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    for chunk in stream:
        yield chunk["message"]["content"]

@app.post("/generate")
async def generate(req: dict, _: str = Depends(check_pwd)):
    return EventSourceResponse(llama_stream(req["prompt"]))
