import tensorflow as tf

b = 2
n = 3
d = 3
k = 3

dc = 3

x = tf.reshape(tf.range(b*n*d, dtype=tf.float32), [b, n, d])
w = tf.get_variable(initializer=tf.reshape(tf.range(k*d*dc, dtype=tf.float32),shape=[k, d, dc]),name='weight')
conv = tf.nn.conv2d(tf.reshape(x, [b,n,d,1]), 
                    tf.reshape(w, [k,d, 1,dc]),
                    strides=[1,1,d,1], 
                    padding="SAME")

y = tf.reshape(conv, [b, n, dc])

with tf.Session() as session:
  session.run(tf.global_variables_initializer())
  x, w, y = session.run([x, w, y])
  print('*' * 10)
  print(x)
  print('*' * 10)
  print(w)
  print('*' * 10)
  print(y)


# [[[  300.   315.   330.]
#   [  612.   648.   684.]
#   [  300.   333.   366.]]

#  [[ 1191.  1260.  1329.]
#   [ 1584.  1701.  1818.]
#   [  705.   792.   879.]]]