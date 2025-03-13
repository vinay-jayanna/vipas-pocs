import streamlit as st
import requests
import json
import base64
from PIL import Image
from io import BytesIO

def fetch_prediction(image_url, model_url, additional_headers):
    response = requests.get(image_url)
    image_data = base64.b64encode(response.content).decode('utf-8')
    raw = {"instances": [image_data]}

    # Default header
    headers = {"Content-Type": "application/json"}
    # Update the headers dictionary with any additional headers provided
    headers.update(additional_headers)

    pred_response = requests.post(model_url, data=json.dumps(raw), headers=headers)
    print(pred_response)
    print(pred_response.content)

    if pred_response.status_code == 200:
        prediction_data = json.loads(pred_response.content.decode('utf-8'))
        return prediction_data
    else:
        return None

def main():
    st.title("Identify Flowers")
    
    flower_url = st.text_input("Enter Flower Image URL:")
    # model_url = "http://flower-class-1-predictor.vps-models.34.23.19.70.sslip.io/v1/models/flower-class:predict"
    model_url = "http://34.23.19.70:80/v1/models/flower-class-1:predict"
    headers = {"Host": "flower-class-1-predictor.vps-models.34.23.19.70.sslip.io"}

    if st.button("Identify"):
        if flower_url:
            st.image(flower_url, caption="Uploaded Flower Image", use_column_width=True)

            prediction_data = fetch_prediction(flower_url, model_url, headers)
            if prediction_data and "instances" in prediction_data:
                class_name = prediction_data["instances"][0][0]
                confidence = prediction_data["instances"][0][1]
                st.markdown(f"<h1 style='color:red;'>{class_name}</h1>", unsafe_allow_html=True)
                st.success(f"Confidence: {confidence:.2f}%")
            else:
                st.error("Failed to identify.")
        else:
            st.warning("Please enter a valid image URL.")

if __name__ == "__main__":
    main()

