import tensorflow as tf
import numpy as np

def f(a,b,c,nu,phi,x):
    return c*x**a*(1-x)**b*tf.cos(2*np.pi*nu*x - phi)