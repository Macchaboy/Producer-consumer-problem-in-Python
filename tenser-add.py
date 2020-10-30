import tensorflow as tf

a = tf.constant(3)
b = tf.constant(4)
c = tf.add(a,b)

sess = tf.Session()

print(c)
print("constant : {}".format(sess.run(c)))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a+b # = tf.add(a+b)

print("placeholder : {}".format(sess.run(c,{a:3,b:4})))

print("placeholder : {}".format(sess.run(c,{a:[1,2],b:[3,4]})))
