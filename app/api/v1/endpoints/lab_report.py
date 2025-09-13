from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil

from app.config import TEMP_FOLDER_NAME
from app.services.lab_report.ocr.ocr import OCR


router = APIRouter()

def get_ocr():
    return OCR()



@router.post("/lab_report_analysis")
async def lab_report(file : UploadFile = File(...), ocr : OCR = Depends(get_ocr)):
    
    allowed_file_types = ["image/jpeg","image/png","image/bmp", "application/pdf"]
    
    if file.content_type not in allowed_file_types:
        raise HTTPException(status_code=400, detail="Only Image and PDF file are acceptable.")
    
    # make temp folder 
    os.makedirs(TEMP_FOLDER_NAME, exist_ok=True)
    temp_file_path = os.path.join(TEMP_FOLDER_NAME, file.filename)
    
    with open(temp_file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
        
    ### Classify File
    if file.content_type == "application/pdf":
        print("PDF calling..........")
        
        pdf_data = ocr.pdf_to_text(pdf_file=temp_file_path)
        
        return JSONResponse({
            "file_name" : file.filename,
            "pdf_to_text" : pdf_data
        })
    elif file.content_type.startswith("image/"):
        print("Image calling.........")
        
        img_data = ocr.img_to_text(img_file=temp_file_path)
        
        return JSONResponse({
            "file_name" : file.filename,
            "img_to_text" : img_data
        })
    else:
        return JSONResponse({
            "Error" : "Something Went Wrong!!!!"
        })
        