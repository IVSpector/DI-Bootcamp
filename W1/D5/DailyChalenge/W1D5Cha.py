# Challenge 1: Sorting
# def input_words():
#     user_words = input("Input several words separated by commas (word1,word2,...) or 'q' for quit: ")
#     if user_words == "q":
#         return "quit"
#     elif len(user_words) == 0:
#         print("You have not entered any data! Goodbye")
#         return "quit"
#     else:
#         return user_words
#
#
# def transform_to_list(words):
#     return words.split(",")
#
#
# def sert_list(list):
#     return sorted(list)
#
#
# def join_result(sorted_list):
#     return ','.join(sorted_list)
#
#
# a = input_words()
# while a != "quit":
#     print(join_result(sert_list(transform_to_list(a))))
#     a = input_words()


# Challenge 2: Longest Word
# def input_sentence():
#     while True:
#         user_sentence = input("Input a sentence or 'q' for quite: ")
#         if len(user_sentence) == 0:
#             print("Please, insert somthing!")
#             continue
#         else:
#             return user_sentence  # Here can be "q" for quit.
#
#
# def split_by_words(sentence):
#     return sentence.split()
#
#
# def long_word(list_words):
#     # max_length = max(len(each_list) for each_list in list_words)
#     longest_list = max(list_words, key=len)
#     return longest_list
#
#
# a = input_sentence()
# while a != "q":
#     print(long_word(split_by_words(a)))
#     a = input_sentence()
