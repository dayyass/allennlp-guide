from allennlp.data.fields import TextField
from allennlp.data.token_indexers import SingleIdTokenIndexer, TokenCharactersIndexer
from allennlp.data.token_indexers import PosTagIndexer
from allennlp.data.tokenizers import WordTokenizer, CharacterTokenizer
from allennlp.data.tokenizers.word_splitter import SpacyWordSplitter
from allennlp.data import Vocabulary

# Splits text into words (instead of wordpieces or characters).
tokenizer = WordTokenizer()

# Represents each token with both an id from a vocabulary and a sequence of characters.
token_indexers = {'tokens': SingleIdTokenIndexer(namespace='token_vocab'),
                  'token_characters': TokenCharactersIndexer(namespace='character_vocab')}

vocab = Vocabulary()
vocab.add_tokens_to_namespace(['This', 'is', 'some', 'text', '.'],
                              namespace='token_vocab')
vocab.add_tokens_to_namespace(['T', 'h', 'i', 's', ' ', 'o', 'm', 'e', 't', 'x', '.'],
                              namespace='character_vocab')

text = "This is some text."
tokens = tokenizer.tokenize(text)
print(tokens)

text_field = TextField(tokens, token_indexers)

# In order to convert the token strings into integer ids, we need to tell the
# TextField what Vocabulary to use.
text_field.index(vocab)

# We typically batch things together when making tensors, which requires some
# padding computation.  Don't worry too much about the padding for now.
padding_lengths = text_field.get_padding_lengths()

tensor_dict = text_field.as_tensor(padding_lengths)
print(tensor_dict)
