import os

clsq = "pyfkclsq"
my_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq
print(my_path)
if not os.path.exists(my_path):
    os.mkdir(my_path)
