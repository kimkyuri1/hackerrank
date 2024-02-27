import numpy as np

def arrays(arr):
    return np.array(arr, dtype=float)

if __name__ == "__main__":
    def arrays(arr):
        return np.array(arr, dtype=float)[::-1]

    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)
