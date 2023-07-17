from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from img2pdf import convert
import os
from typing import List
from uuid import uuid4
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory to serve the HTML file
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    # Serve the index.html file
    with open("static/index.html", "r") as f:
        content = f.read()
    return HTMLResponse(content)

@app.post("/convert")
async def convert_images(images: List[UploadFile] = File(...)):
    image_files = []
    for image in images:
        if image.content_type.startswith('image/'):
            image_bytes = await image.read()
            image_files.append(image_bytes)

    if image_files:
        # Set the options for image resolution (dpi) and compression quality (0-100)
        dpi = 300  # Adjust the resolution (dpi) as needed (e.g., 300 dpi for higher quality)
        quality = 50  # Adjust compression quality (0-100; higher values mean less compression)

        # Perform the conversion with the specified options
        pdf_bytes = convert(image_files, dpi=dpi, quality=quality)

        pdf_filename = f"converted_{uuid4()}.pdf"
        pdf_path = os.path.join("static", pdf_filename)
        with open(pdf_path, "wb") as f:
            f.write(pdf_bytes)
        return {"success": True, "pdfUrl": pdf_path}
    else:
        return {"success": False, "message": "No valid image files found."}

@app.get("/download/{pdf_filename}")
async def download_pdf(pdf_filename: str):
    pdf_path = os.path.join("static", pdf_filename)
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path, filename=pdf_filename)
    else:
        return {"success": False, "message": "PDF file not found."}
