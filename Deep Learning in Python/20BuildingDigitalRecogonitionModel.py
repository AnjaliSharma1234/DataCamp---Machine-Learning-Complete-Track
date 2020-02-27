# Create the model: model
model = Sequential()

# Add the first and second layers
model.add(Dense(50, activation='relu', input_shape = (784,)))
model.add(Dense(50, activation='relu'))

# Add the output layer
model.add(Dense(10, activation='softmax'))

# Compile model_2
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y, validation_split = 0.3)

