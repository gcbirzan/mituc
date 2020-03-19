from pathlib import Path

import numpy
from textgenrnn.utils import textgenrnn_texts_from_file_context, textgenrnn_texts_from_file

# corpus_text = Path("plugins/Mituc/corpus_bigger.txt")
corpus_text = Path("plugins/Mituc/corups_small.txt")
# fp = "plugins/Mituc/corups_small.txt"

indices_list_path = Path(corpus_text.stem)

from textgenrnn import textgenrnn
textgen = textgenrnn()
# texts = textgenrnn_texts_from_file(fp)
# indices_list = textgen.generate_indices_list(texts)
if indices_list_path.exists():
    indices_list = numpy.load(indices_list_path)
else:
    texts = textgenrnn_texts_from_file(corpus_text)
    indices_list = textgen.generate_indices_list(texts)
    numpy.save(indices_list_path, indices_list)

# textgen.load('test_model')
textgen.train_from_file(corpus_text, num_epochs=10, train_size=0.8, validation=True, batch_size=1024, indices_list=indices_list, gen_epochs=1, new_model=True)

textgen.save('test_model')

pass
