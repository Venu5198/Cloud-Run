from fastapi import FastAPI

app = FastAPI(title="Demo FastAPI App")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Hello from FastAPI on VM!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
