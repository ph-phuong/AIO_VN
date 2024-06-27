import streamlit as st
import os


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


# Dùng đường dẫn tuyệt đối
file_path = "D:/Vi_Tinh/GIAO_TRINH/AIO/Ho_tro_Code/AIO_VN/Module_1/Tuan_4/data/vocab.txt"
vocabs = load_vocab(file_path)


def levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    iterate_distances(token1, token2, distances)

    return distances[len(token1)][len(token2)]


def iterate_distances(token1, token2, distances):
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            distances[i][j] = calculate_distance(
                token1[i - 1], token2[j - 1], distances[i - 1][j - 1], distances[i][j - 1], distances[i - 1][j])


def calculate_distance(char1, char2, prev_distance, left_distance, top_distance):
    if char1 == char2:
        return prev_distance
    else:
        return 1 + min(left_distance, top_distance, prev_distance)


def main():
    st.title('Word Correction using Levenshtein Distance')
    word = st.text_input('Word: ')

    if st.button('Compute'):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary: ')
        col1.write(vocabs)

        col2.write('Distances :')
        col2.write(sorted_distances)


if __name__ == '__main__':
    main()
