def load_the_word_list():
    with open("merged_list.txt", encoding="UTF-8") as f:
        return f.read().splitlines()


def wagner_fischer(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    current_row = range(len_s1 + 1)
    for i in range(1, len_s2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_s1
        for j in range(1, len_s1 + 1):
            add, delete, change = (
                previous_row[j] + 1,
                current_row[j - 1] + 1,
                previous_row[j - 1],
            )
            if s1[j - 1] != s2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[len_s1]


def spell_check(word, dictionary):
    suggestions = []

    if word in dictionary:
        return [(word, 0)]

    for correct_word in dictionary:
        distance = wagner_fischer(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]


if __name__ == "__main__":
    dictionary = load_the_word_list()
    while True:
        word = input("Enter a word: ")
        suggestions = spell_check(word, dictionary)
        for suggestion in suggestions:
            print(suggestion)
