from imp import reload
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import RedirectResponse, StreamingResponse
from io import BytesIOapp = FastAPI()@app.get("/")
def read_root():
    return RedirectResponse(url='/docs')@app.post("/signatures/extraction")
async def create_upload_file(file: UploadFile):