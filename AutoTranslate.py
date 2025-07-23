# AutoTranslate.py

import sys
from googletrans import Translator

def translate_file(input_path, output_path, dest_lang='en'):
    translator = Translator()
    
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    print(f"Translating content from '{input_path}' to language '{dest_lang}'...")
    translation = translator.translate(text, dest=dest_lang)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translation.text)
        
    print(f"Translation saved to '{output_path}'")

def main():
    if len(sys.argv) < 3:
        print("Usage: python AutoTranslate.py <input_file> <output_file> [target_language]")
        print("Example: python AutoTranslate.py mytext.txt translated.txt es")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_language = sys.argv[3] if len(sys.argv) > 3 else 'en'

    translate_file(input_file, output_file, target_language)

if __name__ == "__main__":
    main()