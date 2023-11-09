import numpy as np
import sys
import random
from datetime import datetime



if __name__ == "__main__":
    time1 = datetime.now()
    if len(sys.argv) != 2:
        print("Usage: python loop.py <value>")
        sys.exit(1)

    a = 82
    n = int(sys.argv[1])
    arr = np.random.randint(0,n,size=(n,n))
    #arr.sort(axis=1)
    time2 = datetime.now()
    print("time used: ", (time2-time1).total_seconds())
    