import os
import stable_whisper

def transcribe_audio(audio_path: str) -> str:
    # بارگذاری مدل
    model = stable_whisper.load_model('base')
    
    # transcribe کردن
    result = model.transcribe(audio_path)

    # ذخیره به صورت فایل txt
    txt_path = os.path.join("output", "transcription.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result.text)

    # ذخیره به صورت srt
    srt_path = os.path.join("output", "transcription.srt")
    result.to_srt_vtt(srt_path, word_level=False)

    return result.text
