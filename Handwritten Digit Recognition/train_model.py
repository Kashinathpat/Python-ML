import keras

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

model = keras.models.Sequential()

model.add(keras.layers.Flatten(input_shape=(28,28)))

model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(128, activation="relu"))

model.add(keras.layers.Dense(10, activation="softmax"))
model.compile(optimizer="adam", metrics=['accuracy'], loss="sparse_categorical_crossentropy")

model.fit(x_train, y_train, epochs=10)

model.save("handwritten.model")

