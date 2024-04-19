import os

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from models.model_architecture import build_model
from utils.data_preprocessing import get_data_generators
from config.config import Config

def train_model():

    # Build the model
    model = build_model(input_shape=Config.INPUT_SHAPE, num_classes=Config.NUM_CLASSES)
    model.summary() # show model summary
    input("Press ENTER to train the model")
    os.system("clear")

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=Config.LEARNING_RATE),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Set up data generators
    train_generator, val_generator = get_data_generators(batch_size=Config.BATCH_SIZE, input_shape=Config.INPUT_SHAPE)

    # Set up callbacks (optional but recommended)
    checkpoint = ModelCheckpoint(Config.MODEL_CHECKPOINT_PATH, save_best_only=True)
    early_stopping = EarlyStopping(patience=Config.EARLY_STOPPING_PATIENCE, restore_best_weights=True)

    # Train the model
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // Config.BATCH_SIZE,
        epochs=Config.NUM_EPOCHS,
        validation_data=val_generator,
        validation_steps=val_generator.samples // Config.BATCH_SIZE,
        callbacks=[checkpoint, early_stopping]
    )

    # Save the entire model (including architecture) after training
    model.save(Config.MODEL_OUTPUT_PATH)


if __name__ == "__main__":
    train_model()
