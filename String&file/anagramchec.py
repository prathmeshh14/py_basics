import os 
from collections import defaultdict

file_path="String&file/sample.txt"
if not os.path.exists(file_path):
    print(f"File '{file_path}' does not exist.")

else:
    anagram_dict = defaultdict(list)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word=line.strip()
            if not word:
                continue
            sorted_word="".join (sorted(word.lower()))
            anagram_dict[sorted_word].append(word)

    print("----------Found Anagrams----------")
    found=False
    for sorted_word,anagrams in anagram_dict.items():
        if len(anagrams)>1:
            print(f"Anagrams for '{sorted_word}': {', '.join(anagrams)}")
            found=True
    if not found:
        print("No anagrams found in the file.")
