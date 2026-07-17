class Vocabulary:
    def __init__(self):
        self.word_to_id = {
            "<PAD>": 0,
            "<EOS>": 1,
        }

        self.id_to_word = {
            0: "<PAD>",
            1: "<EOS>",
        }

        self.next_id = 2

    def add_word(self, word):
        if word not in self.word_to_id:
            self.word_to_id[word] = self.next_id
            self.id_to_word[self.next_id] = word
            self.next_id += 1

        return self.word_to_id[word]


    def encode(self, text):

        words = text.split()

        token_ids = []

        for word in words:
            token_id = self.add_word(word)
            token_ids.append(token_id)
        return token_ids




    def decode(self, ids):

        words = []

        for token_id in ids:
            words.append(self.id_to_word(token_id))
        return words

    

