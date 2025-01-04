with open("romanian.txt", "r", encoding="utf-8") as romanian_file:
    text = romanian_file.read()

#removing punctuation signs
for ch in text:
    if ch in ['.',',','!','?','\n']:
        text = text.replace(ch, '')
words = text.split(' ')

#total num of words + avg word len
total_words = len(words)
avg_word_length = sum(len(word) for word in words) / total_words

#word length distribution
word_lengths = [len(word) for word in words]
length_distribution = {}
for word_len in word_lengths:
    if word_len not in length_distribution:
        length_distribution[word_len] = 1
    else:
        length_distribution[word_len] += 1
sorted_length_distribution = list(length_distribution.items())
sorted_length_distribution = sorted(sorted_length_distribution, key= lambda v : v)

#word freq
word_frequency = {}
for word in words:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1
sorted_word_frequency = list(word_frequency.items())
sorted_word_frequency = sorted(sorted_word_frequency, key= lambda v : v[1], reverse=True)
first_10_most_used = sorted_word_frequency[:10]

# vowels versus consonants
vowels = set("aeiouăâîAEIOUĂÂÎ")
vowel_count = sum(sum(1 for char in word if char in vowels) for word in words)
consonant_count = sum(sum(1 for char in word if char.isalpha() and char not in vowels) for word in words)

#letter freq
letter_frequency = {}
for word in words:
    for char in word:
        if char.isalpha():
            char = char.lower()
            if char not in letter_frequency:
                letter_frequency[char] = 0
            else:
                letter_frequency[char] += 1
sorted_letter_frequency = list(letter_frequency.items())
sorted_letter_frequency = sorted(sorted_letter_frequency, key= lambda v : v[0])


print(f"Nr total cuvinte: {total_words}")
print(f"Lungimea medie a cuvintelor: {avg_word_length:.2f}")
print(f"Distributia lungimii cuvintelor: {sorted_length_distribution}")
print(f"Top 10 cuvinte cu nr max de aparitii: {first_10_most_used}")
print(f"Nr vocale: {vowel_count}\nNr de consoane: {consonant_count}\nMedie: {(vowel_count / consonant_count)}")
print(f"Nr aparitii litere: {sorted_letter_frequency}")

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
lengths = list(length_distribution.keys())
counts = list(length_distribution.values())
plt.bar(lengths, counts, color="skyblue")
plt.title("Distribuția lungimii cuvintelor")
plt.xlabel("Lungimea cuvântului")
plt.ylabel("Număr de cuvinte")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.subplot(1, 2, 2)
letters = list(letter_frequency.keys())
frequencies = list(letter_frequency.values())
plt.bar(letters, frequencies, color="lightcoral")
plt.title("Frecvența literelor")
plt.xlabel("Litere")
plt.ylabel("Frecvență")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()