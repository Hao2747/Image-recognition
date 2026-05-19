import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from image_path import ImagePath

image_path = ImagePath()

def train():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train / 255.0
    x_test = x_test / 255.0
    model = Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

    model.save(image_path.generated_models_path / "fc_model.keras")

    return model


def predict(model, image_file="4.png"):
    test = image_path.generated_digits_path / image_file

    img = tf.keras.preprocessing.image.load_img(test, color_mode='grayscale', target_size=(28, 28))
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28)
    prediction = model.predict(img_array)
    print(f"Predicted digit: {prediction.argmax()}")


if __name__ == "__main__":
    model = train()
    predict(model)
