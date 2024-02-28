from formfunction import *
import matplotlib.pyplot as plt
plt.style.use("default")
np.set_printoptions(linewidth=500,precision=2,suppress=True)

z=np.loadtxt('signal.csv',delimiter=',')
x=z[:,0]
y_true=z[:,1]
plt.plot(x,y_true)
plt.title("signal")
plt.show()

a=tf.Variable(1.)
b=tf.Variable(1.)
c=tf.Variable(1.)
nu=tf.Variable(40.)
phi = tf.Variable(2.)
parameters=[a,b,c,nu,phi]

nb_step=500
optimizer=tf.optimizers.Adam(learning_rate=0.1)

for _ in range(nb_step):
  with tf.GradientTape() as tape:
    y = f(a,b,c,nu,phi,x)
    loss = tf.reduce_sum((y-y_true)**2)
  gradient = tape.gradient(loss,parameters)
  optimizer.apply_gradients(zip(gradient,parameters))

y = f(a,b,c,nu,phi,x)

plt.plot(x,y,label='Predict')
plt.plot(x,y_true,label="Actual")
plt.title("Approximation")
plt.legend()
plt.show()

z=np.loadtxt('signal2.csv',delimiter=',')
x=z[:,0]
y_true=z[:,1]

plt.plot(x,y_true)
plt.title("signal2")
plt.show()

a=tf.Variable(1.)
b=tf.Variable(1.)
c=tf.Variable(1.)
nu=tf.Variable(40.)
phi = tf.Variable(2.)
parameters=[a,b,c,nu,phi]

nb_step=500
optimizer=tf.optimizers.Adam(learning_rate=0.1)

for _ in range(nb_step):
  with tf.GradientTape() as tape:
    y = f(a,b,c,nu,phi,x)
    loss = tf.reduce_sum((y-y_true)**2)
  gradient = tape.gradient(loss,parameters)
  optimizer.apply_gradients(zip(gradient,parameters))

y = f(a,b,c,nu,phi,x)

plt.plot(x,y,label = 'Predict')
plt.plot(x,y_true, label = 'Actual')
plt.title("Approximation")
plt.legend()
plt.show()