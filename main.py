# https://github.com/detectlanguage/detectlanguage-python
# pip install detectlanguage
import random
# import detectlanguage
# detectlanguage.configuration.api_key = "b2fe70f140a8259e68baca15692a306e"
#
# with open("romanian.txt", "r", encoding="utf-8") as romanian_file:
#     f = romanian_file.read()
#     print(detectlanguage.detect(f))
#
# with open("spanish.txt", "r", encoding="utf-8") as spanish_file:
#     f = spanish_file.read()
#     print(detectlanguage.detect(f))
#


# https://github.com/dumitrescustefan/RoWordNet?tab=readme-ov-file
# pip install rowordnet
import rowordnet as rwn

with open("romanian.txt", "r", encoding="utf-8") as romanian_file:
    text = romanian_file.read()

copy_text = text
#removing punctuation signs
for ch in text:
    if ch in ['.',',','!','?','\n']:
        text = text.replace(ch, '')
words = text.split(' ')

wn = rwn.RoWordNet()
for word in words:
    synset_ids = wn.synsets(literal=word)
    candidates = []
    for synset_id in synset_ids:
        if word in wn(synset_id).literals and len(wn(synset_id).literals) > 1:
            candidates.append(wn(synset_id).literals)

    filtered_candidates = set(item for sublist in candidates for item in sublist if item != word)
    if len(filtered_candidates) > 0:
        friend = random.choice(list(filtered_candidates))
        print(f"Alegem pentru {word} -> {friend}")

        if random.random() < 0.50:
            copy_text = copy_text.replace(" " + word + " ", "{{ "+ friend + " }}")


import tkinter as tk
import re


def display_text(text_widget, text):

    parts = re.split(r"(\{\{.*?\}\})", text)

    for part in parts:
        if part.startswith("{{") and part.endswith("}}"):
            word = part[2:-2]
            text_widget.insert(tk.END, word, "highlight")
        else:
            text_widget.insert(tk.END, part)

root = tk.Tk()
root.title("Text modificat")

text_widget = tk.Text(root, wrap=tk.WORD, font=("Times New Roman", 14))
text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

text_widget.tag_configure("highlight", foreground="blue")

display_text(text_widget, copy_text)

text_widget.config(state=tk.DISABLED)

root.mainloop()

