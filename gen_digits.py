from PIL import Image
import numpy as np
import os
from tensorflow.keras.datasets import mnist


def gen_digits():
    output_dir = "generated_digits"
    os.makedirs(output_dir, exist_ok=True)
    print(type(mnist.load_data()))
    print(mnist.load_data()[0])
    print(mnist.load_data()[0][0].shape)
    print(mnist.load_data()[0][1].shape)
    (x_train, y_train), _ = mnist.load_data()
    for digit in range(10):
        pos = (y_train == digit).argmax()
        img_array = x_train[pos]
        img = Image.fromarray(img_array)
        path = os.path.join(output_dir, f"{digit}.png")
        img.save(path)
        print(f"Saved digit {digit} to {path}")


if __name__ == "__main__":
    gen_digits()
