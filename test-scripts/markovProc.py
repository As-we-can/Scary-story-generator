import random


class Markov:

    def markov_two_tokenizer(self):
        word_list = str(self).split(' ')
        tokenize_dict = {}
        for i in range(len(word_list) - 2):
            temp_word = ' '.join([word_list[i], word_list[i + 1]])
            if temp_word not in tokenize_dict:
                tokenize_dict[temp_word] = [word_list[i + 2]]
            else:
                tokenize_dict[temp_word].append(word_list[i + 2])
        return tokenize_dict

    @staticmethod
    def text_generator(token_dict, length):
        start_word = random.choice(list(token_dict.keys()))
        text_list = start_word.split()
        for i in range(length):
            temp_word = ' '.join([text_list[i], text_list[i + 1]])
            text_list.append(random.choice(token_dict[temp_word]))
        output_text = ' '.join(text_list)
        return output_text
