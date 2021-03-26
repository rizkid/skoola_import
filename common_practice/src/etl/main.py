import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../service"))

from string_transfomer import StringTransformer

if __name__ == "__main__":
    transformer = StringTransformer("x", "y")
    print(transformer.transform("data1"))