import tensorflow as tf

rank1_tensor = tf.Variable(["test", "ok", "string"])
rank2_tensor = tf.Variable([["test", "ok", "string"], ["mamunur", "timone", "chix"]])
ones = tf.ones([9])

print(rank2_tensor.shape)
print(ones)

# https://www.youtube.com/watch?v=tPYj3fFJGjk 1:00:00