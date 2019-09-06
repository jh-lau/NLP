"""
  User: Liujianhan
  Time: 12:39
 """
__author__ = 'liujianhan'
import os
from datetime import datetime

import numpy as np
import tensorflow as tf
from six.moves import cPickle as pickle
from sklearn.preprocessing import OneHotEncoder


def reset_graph(seed=42):
    tf.compat.v1.reset_default_graph()
    tf.compat.v1.set_random_seed(seed)
    np.random.seed(seed)


def log_dir(prefix=''):
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    root_logdir = 'tf_logs'
    if prefix:
        prefix += '-'
    name = prefix + 'run_' + now
    return os.path.join(root_logdir, name)


logdir = log_dir('high_level_API')

with open('assignments/allMNIST.pickle', 'rb') as f:
    save = pickle.load(f)
    train_dataset = save['train_dataset']
    train_labels = save['train_labels']
    test_dataset = save['test_dataset']
    test_labels = save['test_labels']
    del save


def shuffle(dataset, labels):
    permutation = np.random.permutation(labels.shape[0])
    shuffled_dataset = dataset[permutation, :, :]
    shuffled_labels = labels[permutation]
    return shuffled_dataset, shuffled_labels


train_dataset, train_labels = shuffle(train_dataset, train_labels)
test_dataset, test_labels = shuffle(test_dataset, test_labels)
encoder = OneHotEncoder(categories='auto')
train_labels_1hot = encoder.fit_transform(train_labels.reshape(-1,1)).toarray()
test_labels_1hot = encoder.fit_transform(test_labels.reshape(-1,1)).toarray()
train_flatten = train_dataset.reshape(-1, 784)
test_flatten = test_dataset.reshape(-1, 784)


def train():
    reset_graph()
    checkpoint_path = 'tmp/high_level_API_complicate_CNN'
    units = 28 * 28
    initial_learning_rate = .1
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate,
                                                                 decay_steps=10000,
                                                                 decay_rate=.96,
                                                                 staircase=True)

    cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                     monitor='val_acc',
                                                     verbose=1,
                                                     save_best_only=True,
                                                     load_weights_on_restart=True)
    stop_callback = tf.keras.callbacks.EarlyStopping(monitor='val_acc',
                                                     mode='max',
                                                     patience=10)
    csv_logger = tf.keras.callbacks.CSVLogger('csv_logger')
    tensorboard = tf.keras.callbacks.TensorBoard(logdir)

    model = tf.keras.models.Sequential([
        # tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation=tf.nn.relu,
        #                        input_shape=(28, 28, 1)),
        # tf.keras.layers.MaxPooling2D((2, 2), strides=2),
        # tf.keras.layers.Dropout(.25),
        # tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation=tf.nn.relu),
        # tf.keras.layers.MaxPooling2D((2, 2), strides=2),
        # tf.keras.layers.Dropout(.25),
        tf.keras.layers.Dense(4 * units, activation=tf.nn.relu, input_shape=(784, )),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(2 * units, activation=tf.nn.relu),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(units, activation=tf.nn.relu),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.keras.optimizers.SGD(lr_schedule),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_flatten, train_labels_1hot, validation_split=.2,
              epochs=100, callbacks=[cp_callback,
                                     stop_callback,
                                     csv_logger,
                                     tensorboard])

    print("Model's performance on test dataset:")
    print(f"Test accuracy: {model.evaluate(test_flatten, test_labels_1hot)[1] * 100:.3f}%")


if __name__ == '__main__':
    train()
