import numpy as np

seed = 123

def generate_simple_linear_data(seed:int = seed,n:int = 100):
    np.random.seed(seed)
    x = np.linspace(0,10,n)
    # y = b0 + b1x + e
    b_0 = np.random.normal()*10
    b_1 = np.random.normal()*5
    e = np.random.normal(loc = 0, scale = 3, size = n)

    y = b_0 + b_1*x + e

    #Add random variance to the y values.
    return x.flatten(), y.flatten()


def generate_hetroskedastic_data(seed:int = seed,n:int = 100):
    np.random.seed(seed)
    x = np.linspace(0,10,n)
    # y = b0 + b1x + e
    b_0 = np.random.normal()*10
    b_1 = np.random.normal()*5
    e = np.random.normal(loc = 0, scale = 3 + (x**2)/2, size = n)

    y = b_0 + b_1*x + e

    return x.reshape(100,), y.reshape(100,)