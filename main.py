# https://github.com/detectlanguage/detectlanguage-python
# pip install detectlanguage

import detectlanguage
detectlanguage.configuration.api_key = "b2fe70f140a8259e68baca15692a306e"

with open("romanian.txt", "r", encoding="utf-8") as romanian_file:
    f = romanian_file.read()
    print(detectlanguage.detect(f))

with open("spanish.txt", "r", encoding="utf-8") as spanish_file:
    f = spanish_file.read()
    print(detectlanguage.detect(f))



# https://github.com/dumitrescustefan/RoWordNet?tab=readme-ov-file
# pip install rowordnet
import rowordnet as rwn

with open("romanian.txt", "r", encoding="utf-8") as romanian_file:
    text = romanian_file.read()

#removing punctuation signs
for ch in text:
    if ch in ['.',',','!','?','\n']:
        text = text.replace(ch, '')
words = text.split(' ')

wn = rwn.RoWordNet()
for word in words:
    synset_ids = wn.synsets(literal=word)
    for synset_id in synset_ids:
        if word in wn(synset_id).literals and len(wn(synset_id).literals) > 1:
            print(wn(synset_id).literals)