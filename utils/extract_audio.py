import os
import subprocess

def extract_audio(video_path: str) -> str:
    """
    Extracts audio from a given video file using ffmpeg and saves it in /temp as .mp3.
    Returns the path to the extracted audio file.
    """
    # مسیر خروجی صدا در همان پوشه temp
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_audio = os.path.join("temp", f"{base_name}.mp3")

    # اجرای دستور ffmpeg
    command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", output_audio]
    process = subprocess.run(command, capture_output=True, text=True)

    if process.returncode != 0:
        raise RuntimeError(f"vocal exttraction failure \n{process.stderr}")

    return output_audio
