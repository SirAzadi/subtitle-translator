def rebuild_srt_with_translations(original_srt_path: str, translated_txt_path: str, output_srt_path: str) -> str:
    # خواندن فایل ترجمه‌شده
    with open(translated_txt_path, "r", encoding="utf-8") as f:
        translated_lines = [line.strip() for line in f if line.strip()]

    # خواندن فایل SRT اصلی
    with open(original_srt_path, "r", encoding="utf-8") as f:
        srt_lines = f.readlines()

    new_srt_lines = []
    translation_index = 0
    i = 0

    while i < len(srt_lines):
        # شماره
        new_srt_lines.append(srt_lines[i])
        i += 1

        # زمان
        if i < len(srt_lines):
            new_srt_lines.append(srt_lines[i])
            i += 1

        # پرش از متن‌های قبلی
        while i < len(srt_lines) and srt_lines[i].strip() != "":
            i += 1

        # افزودن متن ترجمه‌شده
        if translation_index < len(translated_lines):
            new_srt_lines.append(translated_lines[translation_index] + "\n")
            translation_index += 1

        # افزودن خط خالی
        new_srt_lines.append("\n")
        i += 1

    # ذخیره SRT نهایی
    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.writelines(new_srt_lines)

    return output_srt_path
