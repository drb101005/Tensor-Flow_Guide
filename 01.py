import tensorflow as tf
print(tf.__version__)

t = tf.zeros([5,5,5,5,5])
print(t)

# t = tf.reshape(t, [125, -1])
# print(t)
t = tf.reshape(t, [3125])
print(t)