import re

def clean_srt(input_path: str, output_path: str) -> str:
    with open(input_path, 'r', encoding='utf-8') as file:
        srt_content = file.readlines()

    cleaned_text = []
    for line in srt_content:
        line = line.strip()

        if line.isdigit():
            continue
        if "-->" in line:
            continue
        line = re.sub(r'<.*?>', '', line)

        if line:
            cleaned_text.append(line)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(cleaned_text))

    return output_path  # مسیر فایل خروجی برای استفاده بعدی
