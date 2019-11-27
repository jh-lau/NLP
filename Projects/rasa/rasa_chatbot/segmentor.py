"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import re

import numpy as np

np.set_printoptions(suppress=True)
import pandas as pd
from smart_open import open
from keras.layers import *
from keras.models import Model
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras.preprocessing import text, sequence

maxlen = 32


def clean(s):
    if '“/s' not in s:
        return s.replace('”/s', '')
    elif '”/s' not in s:
        return s.replace('“/s', '')
    elif '‘/s' not in s:
        return s.replace(' ’/s', '')
    elif '’/s' not in s:
        return s.replace('‘/s ', '')
    else:
        return s


s = open('msr_train.txt', 'r', encoding='gbk')
s = [line.strip() for line in s if line.strip()]
s = ''.join(map(clean, s))
s = re.split('[，。！？、]/[bems]', s)

data = []
label = []


def get_xy(s, data, label):
    for sentence in s:
        s = re.findall('(.)/(.)', sentence)
        if s:
            s = np.array(s)
            data.append(list(s[:, 0]))
            label.append(list(s[:, 1]))


get_xy(s, data, label)
d = pd.DataFrame(index=range(len(data)))
d['data'] = data
d['label'] = label
d = d[d.data.apply(len) <= maxlen]
d.index = range(len(d))

tag = pd.Series({'s': 0, 'b': 1, 'm': 2, 'e': 3, 'x': 4})

# 统计所有字，以及每个字编号
chars = []
for i in data:
    chars.extend(i)

chars = pd.Series(chars).value_counts()

chars[:] = range(1, len(chars) + 1)
tokenizer = text.Tokenizer(5200, lower=False)
tokenizer.fit_on_texts(data)
doc2seq = tokenizer.texts_to_sequences(d.data)
padding = sequence.pad_sequences(doc2seq, 32, padding='post')
train_data = padding
y_token = text.Tokenizer()
y_token.fit_on_texts(tag.index)
y_doc2seq = y_token.texts_to_sequences(d.label)
y_padding = sequence.pad_sequences(y_doc2seq, 32, padding='post')
y_padding = to_categorical(y_padding)
train_label = y_padding

word_size = 128
batch_size = 1024
input_dim = len(tokenizer.word_index)


def build_model():
    sequence = Input(shape=(maxlen,), dtype='int32')
    embeded = Embedding(len(chars) + 1, word_size, input_length=maxlen, mask_zero=True)(sequence)
    blstm = Bidirectional(LSTM(64, return_sequences=True), merge_mode='sum')(embeded)
    output = TimeDistributed(Dense(5, activation='softmax'))(blstm)
    model = Model(inputs=sequence, outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


if __name__ == '__main__':
    model = build_model()
    model.fit(train_data, train_label,
              batch_size=batch_size, epochs=10,
              callbacks=[ModelCheckpoint('model/weights.{epoch:02d}--{acc:.3f}.hdf5')])
