import urllib.request
import os

url = "https://raw.githubusercontent.com/hingston/russian/master/10000-russian-words.txt"
req = urllib.request.urlopen(url)
words = req.read().decode('utf-8').splitlines()

mapping = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'",
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`'
}

output_path = "jcuken.dict.yaml"

with open(output_path, "w", encoding="utf-8") as f:
    f.write("---\nname: jcuken\nversion: \"1.0\"\nsort: by_weight\nuse_preset_vocabulary: false\n...\n")
    weight = 1000000
    
    # Add single letters for fallback
    for ru, qwerty in mapping.items():
        f.write(f"{ru}\t{qwerty}\t{weight}\n")
    
    weight = 100000
    for line in words:
        parts = line.strip().split()
        if not parts: continue
        if len(parts) >= 2:
            word = parts[1].lower()
        else:
            word = parts[0].lower()
        
        spelling = ""
        valid = True
        for char in word:
            if char in mapping:
                spelling += mapping[char] + ""
            else:
                valid = False
                break
        
        if valid:
            f.write(f"{word}\t{spelling.strip()}\t{weight}\n")
            weight -= 1

print(f"Generated dictionary.")