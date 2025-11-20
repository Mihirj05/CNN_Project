import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions

class MobileNetClassifier:
    def __init__(self):
        print("Loading the model.....")
        self.model = MobileNetV2(weights='imagenet')
        print("Model Ready!")

    def predict(self, frames):
        if len(frames.shape) == 3:
            frames = np.expand_dims(frames, axis=0)

        preds = self.model.predict(frames, verbose=1)

        results = []
        for pred in preds:
            decode = decode_predictions(np.expand_dims(pred, 0), top=5)[0]
            results.append([(name, float(prob)) for _, name, prob in decode])
        return results
