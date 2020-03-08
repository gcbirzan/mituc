# Get raw text as string.
import re

import markovify
#
# with open("/home/gcbirzan/PycharmProjects/mituc/plugins/Mituc/corpus.txt") as f:
#     text = f.read()
#
# # Build the model.
# text_model = markovify.NewlineText(text, state_size=3)
#
# # Print five randomly-generated sentences
# for i in range(5):
#     sentence = text_model.make_sentence(tries=150)
#     sentence = re.sub('[^ ]*?:? *', '', sentence)
#     print(sentence)

from textgenrnn import textgenrnn
from textgenrnn.utils import textgenrnn_texts_from_file

textgen = textgenrnn()
file_path = r'C:\Users\gc\PycharmProjects\mituc\plugins\Mituc\corpus.txt'
# file_path = r'C:\Users\gc\PycharmProjects\mituc\plugins\Mituc\corpus_bigger.txt'
textgen.train_from_file(file_path, num_epochs=100, train_size=0.95, batch_size=1024 * 9)
# textgen.train_from_file(file_path, num_epochs=10, train_size=0.95, batch_size=2048, name='mituc', new_model=True, rnn_layers=3, rnn_size=128)
# textgen.train_from_file(r'C:\Users\gc\PycharmProjects\mituc\plugins\Mituc\corpus.txt', num_epochs=1, batch_size=2048 * 4)

textgen.generate()