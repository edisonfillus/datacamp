# Load the digits dataset: digits
from keras import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.utils import to_categorical
from sklearn import datasets
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

digits = datasets.load_digits()

# Create feature and target arrays
X = digits.data
y = to_categorical(digits.target)

# Create the model: model
model = Sequential()

n_cols = digits.data.shape[1]

# Add the first hidden layer
model.add(Dense(50,activation='relu',input_shape=(n_cols,)))

# Add the second hidden layer
model.add(Dense(50,activation='relu'))

# Add the output layer
model.add(Dense(10,activation='softmax'))

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Fit the model
history = model.fit(X,y, validation_split=0.3, epochs=30, verbose=False, callbacks=[early_stopping_monitor])

# Create the plot
plt.plot(history.history['val_loss'],'r')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()


#model.save('model_file.h5')
#my_model = load_model('my_model.h5')