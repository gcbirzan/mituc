# Get raw text as string.
import re

import markovify

with open("/home/gcbirzan/PycharmProjects/mituc/plugins/Mituc/corpus.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text, state_size=3)

# Print five randomly-generated sentences
for i in range(5):
    sentence = text_model.make_sentence(tries=150)
    sentence = re.sub('[^ ]*?:? *', '', sentence)
    print(sentence)
