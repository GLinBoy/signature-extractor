from imp import reload
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import RedirectResponse, StreamingResponse
from io import BytesIOapp = FastAPI()