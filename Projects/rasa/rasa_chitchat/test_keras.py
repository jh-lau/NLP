"""
  User: Liujianhan
 """
__author__ = 'liujianhan'
from keras.layers import *
from keras.models import Model


def build_model():
    sequence = Input(shape=(maxlen,), dtype='int32')
    embeded = Embedding(chars + 1, word_size, input_length=maxlen, mask_zero=True)(sequence)
    blstm = Bidirectional(LSTM(64, return_sequences=True), merge_mode='sum')(embeded)
    output = TimeDistributed(Dense(5, activation='softmax'))(blstm)
    model = Model(inputs=sequence, outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
