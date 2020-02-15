# -*- coding: utf-8 -*-
import numpy as np

symbols_quantity = 255

encoding_matrix = np.array([
    [1, 0, 0],
    [1, 3, 1],
    [1, 2, 0],
])

inverted_encoding_matrix = decoding_matrix = np.linalg.inv(encoding_matrix)

encoded_message = 'SŢÕVŝØOƙóMŢÏEŰá'
n = len(encoding_matrix)

encoded_message_chunked = [(encoded_message[i : i+n]) for i in range(0, len(encoded_message), n)] 

message_char_codes_chunked = [[ord(char) for char in chunk] for chunk in encoded_message_chunked]

decoded_char_codes_matrices = [np.dot(inverted_encoding_matrix, chunk).astype(int) for chunk in message_char_codes_chunked]

decoded_chars_matrices = [[chr(code%symbols_quantity) for code in matrix] for matrix in decoded_char_codes_matrices]

decoded_word_splitted = np.array(decoded_chars_matrices).flatten()

word = "".join(decoded_word_splitted)
print(word)