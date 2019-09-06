"""
  User: Liujianhan
  Time: 12:39
 """
__author__ = 'liujianhan'
import os
from datetime import datetime

import numpy as np
import tensorflow as tf


def reset_graph(seed=42):
    tf.compat.v1.reset_default_graph()
    tf.compat.v1.set_random_seed(seed)
    np.random.seed(seed)


def log_dir(prefix=''):
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    root_logdir = 'tf_logs'
    if prefix:
        prefix += '-'
    name = prefix + 'run-' + now
    return f"{root_logdir}/{name}/"


def shuffle_batch(X, y, batch_size):
    rnd_idx = np.random.permutation(len(X))
    n_batches = len(X) // batch_size
    for batch_idx in np.array_split(rnd_idx, n_batches):
        X_batch, y_batch = X[batch_idx], y[batch_idx]
        yield X_batch, y_batch


logdir = log_dir('mnist_nn')

n_inputs = 28 * 28
n_hidden = 1024
n_outputs = 10
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.astype(np.float32).reshape(-1, 28 * 28) / 255.
X_test = X_test.astype(np.float32).reshape(-1, 28 * 28) / 255.
y_train = y_train.astype(np.int32)
y_test = y_test.astype(np.int32)
X_valid, X_train = X_train[:5000], X_train[5000:]
y_valid, y_train = y_train[:5000], y_train[5000:]


def train():
    reset_graph()

    m, n = X_train.shape
    n_epochs = 10001
    batch_size = 50
    n_batches = int(np.ceil(m / batch_size))
    checkpoint_path = 'tmp/my_nn_mnist_model.ckpt'
    checkpoint_epoch_path = checkpoint_path + '.epoch'
    final_model_path = 'tmp/my_nn_final_model'
    best_loss = np.infty
    epochs_without_progress = 0
    max_epochs_without_progress = 5

    X = tf.compat.v1.placeholder(tf.float32, shape=(None, n_inputs), name='X')
    y = tf.compat.v1.placeholder(tf.int32, shape=(None,), name='y')

    with tf.name_scope('nn'):
        hidden = tf.compat.v1.layers.dense(X, n_hidden, name='hidden')
        logits = tf.compat.v1.layers.dense(hidden, n_outputs, name='outputs')

    with tf.name_scope('loss'):
        xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits)
        loss = tf.reduce_mean(xentropy, name='loss')
        loss_summary = tf.compat.v1.summary.scalar('log_loss', loss)

    learning_rate = .01
    with tf.name_scope('train'):
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
        training_op = optimizer.minimize(loss)

    with tf.name_scope('eval'):
        correct = tf.nn.in_top_k(logits, y, 1)
        accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
        accuracy_summary = tf.compat.v1.summary.scalar('accuracy', accuracy)

    init = tf.compat.v1.global_variables_initializer()
    saver = tf.compat.v1.train.Saver()
    file_writer = tf.compat.v1.summary.FileWriter(logdir, tf.compat.v1.get_default_graph())

    with tf.compat.v1.Session() as sess:
        if os.path.isfile(checkpoint_epoch_path):
            with open(checkpoint_epoch_path, 'rb') as f:
                start_epoch = int(f.read())
            print('Training was interrupted. Continuing at epoch', start_epoch)
            saver.restore(sess, checkpoint_path)
        else:
            start_epoch = 0
            sess.run(init)

        for epoch in range(start_epoch, n_epochs):
            for X_batch, y_batch in shuffle_batch(X_train, y_train, batch_size):
                sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
            accuracy_val, loss_val, accuracy_summary_str, loss_summary_str = \
                sess.run([accuracy, loss, accuracy_summary, loss_summary],
                         feed_dict={X: X_valid, y: y_valid})
            file_writer.add_summary(accuracy_summary_str, epoch)
            file_writer.add_summary(loss_summary_str, epoch)
            if epoch % 5 == 0:
                print(f"Epoch:{epoch} "
                      f"Validation accuracy:{accuracy_val * 100 :.3f}% Loss:{loss_val:.5f} "
                      f"Current epochs_without_progress:{epochs_without_progress}")
                saver.save(sess, checkpoint_path)
                with open(checkpoint_epoch_path, 'wb') as f:
                    f.write(b'%d' % (epoch + 1))
                if loss_val < best_loss:
                    saver.save(sess, final_model_path)
                    best_loss = loss_val
                else:
                    epochs_without_progress += 5
                    if epochs_without_progress > max_epochs_without_progress:
                        print("Early stopping")
                        break
        val_accuracy = accuracy.eval({X: X_test, y: y_test})
        print(val_accuracy)


if __name__ == '__main__':
    train()
