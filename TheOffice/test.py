import numpy as np

if __name__ == "__main__":
    a = np.arange(40.0)
    ran = (np.random.rand(30) * 100).astype("int8")
    print(ran)
    print(a.reshape((4,10)))
    print(a.reshape((10,4),order='F').T)
