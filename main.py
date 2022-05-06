from imp import reload
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import RedirectResponse, StreamingResponse
from io import BytesIO

from extractor.signature_extractor import signature_extractor


app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url='/docs')@app.post("/signatures/extraction")
async def create_upload_file(file: UploadFile):if __name__ == "__main__":
if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)