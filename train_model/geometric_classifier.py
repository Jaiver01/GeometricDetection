from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import tensorflow_hub as hub

MODEL_TFHUB_URL = 'https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4'
DATASET_PATH = './dataset'
NEURONS = 6
EPOCH = 50

# Create the dataset
datagen = ImageDataGenerator(
    rescale = 1. / 255,
    rotation_range = 30,
    width_shift_range = 0.25,
    height_shift_range = 0.25,
    shear_range = 15,
    zoom_range = [0.5, 1.5],
    validation_split = 0.2 # For testing
)

# Generate the datasets for training and testing
data_gen_training = datagen.flow_from_directory(
    DATASET_PATH, target_size = (224, 224), batch_size = 32, shuffle = True, subset = 'training'
)

data_gen_testing = datagen.flow_from_directory(
    DATASET_PATH, target_size = (224, 224), batch_size = 32, shuffle = True, subset = 'validation'
)

mobilenetv2 = hub.KerasLayer(MODEL_TFHUB_URL, input_shape = (224, 224, 3))

# Freeze downloaded model
mobilenetv2.trainable = False

model = tf.keras.Sequential([
    mobilenetv2,
    tf.keras.layers.Dense(NEURONS, activation = 'softmax')
])

# Compile the model
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

# Train the model
historial = model.fit(
    data_gen_training, epochs = EPOCH, batch_size = 32, validation_data = data_gen_testing
)

# Save the model
model.save('./../api/classifier/trained_model/geometric_classifier.h5')