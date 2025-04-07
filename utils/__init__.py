# utils/__init__.py
def download_subtitle_from_server():
    import requests
    response = requests.get("http://127.0.0.1:8000/download-subtitle/")
    return response
