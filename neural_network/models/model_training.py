# model_training.py

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from models.model_architecture import build_model
from utils.data_preprocessing import get_data_generators

def train_model():
    # Define constants
    input_shape = (150, 150, 3)  # Adjust based on your image dimensions
    num_classes = 1  # Change if you have more than two classes
    batch_size = 32
    num_epochs = 10

    # Build the model
    model = build_model(input_shape=input_shape, num_classes=num_classes)

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Set up data generators
    train_generator, val_generator = get_data_generators(batch_size=batch_size, input_shape=input_shape)

    # Set up callbacks (optional but recommended)
    checkpoint = ModelCheckpoint("model_weights.h5", save_best_only=True)
    early_stopping = EarlyStopping(patience=3, restore_best_weights=True)

    # Train the model
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        epochs=num_epochs,
        validation_data=val_generator,
        validation_steps=val_generator.samples // batch_size,
        callbacks=[checkpoint, early_stopping]
    )

    # Save the entire model (including architecture) after training
    model.save("trained_model.h5")

if __name__ == "__main__":
    train_model()
