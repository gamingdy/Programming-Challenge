import json

with open("letter_frequencies.json", "r") as letter_frequencies:
    letter_frequencies = json.load(letter_frequencies)


def similarity_score(sentence):
    sum_sentence = 0
    for letter in letter_frequencies:
        sum_sentence += sentence.count(letter) * letter_frequencies[letter]
    return sum_sentence


def _caesar_encrypt(sentence, key):
    sentence = sentence.lower()
    new_sentence = ""
    for char in sentence:
        actual_pos = ord(char)
        new_pos_number = (
            (actual_pos + key) if (actual_pos + key) <= 122 else (actual_pos + key) - 26
        )
        new_sentence += chr(new_pos_number)
    return new_sentence


def sort_result(list_score):
    list_score = list_score
    for el in list_score:
        for b in range(len(list_score) - 1):
            if list_score[b][0] < list_score[b + 1][0]:
                list_score[b], list_score[b + 1] = list_score[b + 1], list_score[b]

    return list_score


def decrypt(sentence):
    highest_score = 0
    list_score = []

    for i in range(1, 26):
        new_sentence = _caesar_encrypt(sentence, i)
        score = similarity_score(new_sentence)
        list_score.append((score, i))

    list_score = sort_result(list_score)
    result = []
    for element in list_score:
        result.append(_caesar_encrypt(sentence, element[1]))

    return result


a = "mjqqt"
b = decrypt(a)
print(b)
