import os
from PIL import Image
import streamlit as st
import google.generativeai as genai
import time

from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def get_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded.")

st.set_page_config(page_title="InvoX", layout='wide')
st.title("InvoX")
st.caption("Your multilingual invoice buddy!")

with st.sidebar:
    st.subheader("Upload Invoice")
    uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

input_prompt = """
You are an expert in understanding invoices.
We will upload an image as an invoice and you will have to answer any question based on the uploaded image.
"""

if uploaded_file is None:
    st.sidebar.info("Upload an invoice image to proceed.")

if user_input := st.chat_input("Ask me about the invoice..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if uploaded_file is not None:
        with st.spinner("Analyzing..."):
            try:
                image_data = get_image_details(uploaded_file)
                response_text = get_gemini_response(input_prompt, image_data, user_input)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                with st.chat_message("assistant"):
                    st.markdown(response_text)
            except Exception as e:
                st.error("Something went wrong while processing the invoice.")
    else:
        st.error("Please upload an invoice to ask questions.")
