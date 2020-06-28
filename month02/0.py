import os
pid = os.fork()

if pid < 0:
    print("Error")
elif pid ==0:
    print("200")
else:
    print()