import cv2
import numpy as np
import keras


def predict_image(path):
    # mnist = keras.datasets.mnist
    # (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # x_train = keras.utils.normalize(x_train, axis=1)
    # x_test = keras.utils.normalize(x_test, axis=1)

    model = keras.models.load_model("handwritten.model")
    # loss, accuracy = model.evaluate(x_test, y_test)
    # print(f"loss :{loss} Accuracy :{accuracy}")

    img = cv2.imread(path)[:, :, 0]
    img = np.invert(np.array([img]))

    prediction = model.predict(img)
    return np.argmax(prediction)


# print(predict_image("canvas.png"))
