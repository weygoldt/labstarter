import os
import re
from openai import OpenAI

client = OpenAI()


def translate_text(text: str) -> str:
    sysprompt = (
        "You are a professional translator for technical documentation from english to german."
        "Preserve the markdown formatting and technical terminology."
    )
    prompt = (
        "Please translate the following technical documentation from English to German. "
        "Technical terms that are natively english and not common in the German programmer-language, such as open-source, should not be translated to German."
        "While referring to the reader, use the informal language instead of formal language."
        "This means, translating you to du instead of Sie."
        "The translated text should feel friendly and open for readers."
        "It is intended to help new, often insecure bachelors and masters students to quickly get up and running in our lab."
        "Preserve the markdown formatting and technical terminology:\n\n" + text
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": sysprompt},
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return completion.choices[0].message.content


def update_links(text):
    # Replace links pointing to markdown files to include _DE suffix
    pattern = r"(\[.*?\])\((.*?\.md)\)"

    def repl(match):
        text_part, link = match.groups()
        new_link = re.sub(r"(\.md)$", r"_DE.md", link)
        return f"{text_part}({new_link})"

    return re.sub(pattern, repl, text)


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Translate the content
    translated = translate_text(content)

    # Update the markdown links
    translated = update_links(translated)
    print(translated)

    # Create new file name
    base, ext = os.path.splitext(file_path)
    new_file_path = f"{base}_DE{ext}"

    with open(new_file_path, "w", encoding="utf-8") as file:
        file.write(translated)
    print(f"Translated and saved: {new_file_path}")


def main(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md") and not filename.endswith("_DE.md"):
            print(f"Processing: {filename}")
            file_path = os.path.join(directory, filename)
            process_file(file_path)


if __name__ == "__main__":
    main(".")
