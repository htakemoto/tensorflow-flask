from flask import Flask
import tensorflow as tf
app = Flask(__name__)

@app.route('/')
def hello_world():
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))
    a = tf.constant(10)
    b = tf.constant(32)
    return str(sess.run(a+b))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)