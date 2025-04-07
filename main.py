from fastapi import FastAPI, File, UploadFile
import os
import shutil
from utils.extract_audio import extract_audio  
from utils.transcribe import transcribe_audio
from utils.clean_text import clean_srt
from utils.translate_text import translate_text_to_persian
from utils.generate_srt import rebuild_srt_with_translations
from fastapi.responses import FileResponse
from utils import download_subtitle_from_server


app = FastAPI()

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    if not file.filename:
        return {"error": "No filename provided"}

    # ساخت مسیر امن برای ذخیره فایل
    safe_filename = os.path.basename(file.filename.replace(" ", "_"))
    file_path = os.path.join(TEMP_DIR, safe_filename)

    # ذخیره فایل در temp/
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # مرحله بعدی (استخراج صدا)
    audio_path = extract_audio(file_path)  # فایل صوتی ذخیره می‌شه

    #تبدیل صدا به متن
    transcribed_text = transcribe_audio(audio_path) 

     # مسیر فایل SRT و فایل پاک‌شده
    srt_path = os.path.join(TEMP_DIR, safe_filename + "output.srt")
    cleaned_text_path = os.path.join(TEMP_DIR, safe_filename + "cleaned_output.txt")

    # پاک‌سازی SRT
    clean_srt(srt_path, cleaned_text_path)

    # ترجمه متن پاک‌سازی‌شده
    translated_output_path = os.path.join(TEMP_DIR, safe_filename + "translated_output.txt")
    translate_text_to_persian(cleaned_text_path, translated_output_path)

    # ایجاد فایل SRT ترجمه‌شده
    filename_wo_ext = os.path.splitext(safe_filename)[0]  # حذف پسوند
    final_srt_path = os.path.join(TEMP_DIR, filename_wo_ext + "_translated_final.srt")
    rebuild_srt_with_translations(srt_path, translated_output_path, final_srt_path)
    

    return {
        "message": "file uploaded and vocal extracted successfully",
        "video_path": file_path,
        "audio_path": audio_path,
        "transcription": transcribed_text,
        "cleaned_text_file": cleaned_text_path,
        "translated_file": translated_output_path,
        "final_subtitle_file": final_srt_path
    }
    

@app.get("/download-subtitle/")
def download_subtitle():
    file_path = os.path.join(TEMP_DIR, "translated_final.srt")
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename="translated_subtitle.srt", media_type='application/octet-stream')
    else:
        return {"error": "Subtitle file not found"}
