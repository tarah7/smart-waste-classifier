import streamlit as st

from PIL import Image

from src.inference.predictor import load_model, predict_image


st.set_page_config(
    page_title="Smart Waste Classifier",
    page_icon="♻️",
    layout="centered"
)


st.title("♻️ Smart Waste Classifier")

st.write(
    "Capture or upload an image of waste "
    "to classify it."
)


@st.cache_resource
def get_model():
    return load_model()


model = get_model()


image_source = st.radio(
    "Choose image source",
    ["Camera", "Upload"]
)


image = None


if image_source == "Camera":

    image = st.camera_input(
        "Take a picture of the waste"
    )

else:

    image = st.file_uploader(
        "Upload a waste image",
        type=["jpg", "jpeg", "png"]
    )


if image is not None:

    image = Image.open(image)

    st.image(
        image,
        caption="Input image",
        use_container_width=True
    )

    if st.button("Classify Waste"):

        predicted_class, confidence = predict_image(
            model,
            image
        )

        predicted_class = predicted_class.capitalize()

        st.subheader("Prediction")

        st.success(predicted_class)

        st.metric(
            "Confidence",
            f"{confidence:.2%}"
        )