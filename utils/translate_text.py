from google import genai

# کلاینت Gemini - کلید رو فعلاً داخل تابع نگه می‌داریم، بعداً می‌فرستیم به .env
client = genai.Client(api_key="AIzaSyDeis5wRVMl1hjIb09TlRgmx3Bp1jgFN_o")
#model = genai.GenerativeModel("gemini-2.0-flash")

def translate_text_to_persian(input_path: str, output_path: str) -> str:
    # خواندن متن پاک‌شده
    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()

    # درخواست ترجمه به Gemini
    prompt = (
        "Translate the following text to Persian in a **meaningful and natural way**. "
        "Make sure the translation is smooth and easy to understand for Persian speakers:\n\n"
        + text
    )

    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = prompt
    )

    # ذخیره متن ترجمه‌شده
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(response.text)

    return output_path
