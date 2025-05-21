import os
import string
import re


class Text:
    def __init__(self, text):
        self.text = text

    @property
    def split(self):
        return self.text.lower().split()

    def word_frequency(self, word):
        count = self.split.count(word.lower())
        return count if count != 0 else None

    def most_common_word(self):
        count_word_dict = {}
        for each_word in set(self.split):
            count_word_dict.update({each_word: self.word_frequency(each_word)})
        return max(count_word_dict, key=count_word_dict.get)

    def unique_words(self):
        return set(self.split)

    @classmethod
    def from_file(cls, file_path):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/{file_path}", "r", encoding="utf-8") as work_file:
            return cls(work_file.read())


class TextModification(Text):

    def remove_punctuation(self):
        cleaned_text = ''.join(ch for ch in self.text if ch not in string.punctuation)
        return cleaned_text

    def remove_stop_words(self):
        split_words = self.split
        return ' '.join(words for words in split_words if words not in ["and", "is", "a"])

    def remove_special_characters(self, character):
        pattern = re.escape(character)
        return re.sub(pattern, '', self.text)


text1 = Text("One two free one two two one one two")
print(text1.word_frequency("One"))
print(text1.most_common_word())

text2 = TextModification.from_file("workFile.txt")
print(text2.remove_punctuation())
print(text2.remove_stop_words())
print(text2.remove_special_characters("4"))
