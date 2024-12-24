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

