# model_training.py

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from models.model_architecture import build_model
from utils.data_preprocessing import get_data_generators
from config.config import Config

def train_model():
    # Define constants
    input_shape = Config.INPUT_SHAPE
    num_classes = Config.NUM_CLASSES  # Change if you have more than two classes
    batch_size = Config.BATCH_SIZE
    num_epochs = Config.NUM_EPOCHS
    learning_rate = Config.LEARNING_RATE

    # Build the model
    model = build_model(input_shape=input_shape, num_classes=num_classes)

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=learning_rate),
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
