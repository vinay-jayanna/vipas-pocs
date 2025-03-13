import requests
import json
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
img_height = 180
img_width = 180
class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
sunflower_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"
response = requests.get(sunflower_url)
img_array = np.array(Image.open(BytesIO(response.content)).resize((img_height, img_width)))
data = {
    "instances": [img_array.tolist()]
}
headers = {"Host": "flower-class-1-predictor.vps-models.34.23.19.70.sslip.io"}
# Make the prediction requesta
url = "http://34.23.19.70:80/v1/models/flower-class-1:predict"
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.content)
# Process the prediction response
if response.status_code == 200:
    predictions = json.loads(response.text)["predictions"]
    scores = tf.nn.softmax(predictions[0])
    class_index = np.argmax(scores)
    class_name = class_names[class_index]
    confidence = 100 * scores[class_index]
    print("This image most likely belongs to {} with a {:.2f}% confidence.".format(class_name, confidence))
else:
    print("Error:", response.text)
# print(json.dumps(data))
with open("data.json", "w") as file:
    json.dump(data, file)
