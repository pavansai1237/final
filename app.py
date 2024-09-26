import streamlit as st
from PIL import Image
import easyocr
import numpy as np
import re
import json

# Initialize the EasyOCR reader without GPU (CUDA/MPS)
reader = easyocr.Reader(['en', 'hi'], gpu=False)  # Disable GPU by setting gpu=False

# OCR function using EasyOCR
def extract_text(image):
    # Convert PIL Image to OpenCV format
    image = np.array(image)
    
    # Perform OCR
    results = reader.readtext(image)

    # Extract and concatenate text from results
    extracted_text = ' '.join([result[1] for result in results])
    return extracted_text

# Highlight search keywords in the text
def highlight_text(text, keyword):
    if not text or not keyword:
        return text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    highlighted_text = re.sub(pattern, lambda m: f"<span style='color: red; font-weight: bold;'>{m.group(0)}</span>", text)
    return highlighted_text

# Create the Streamlit app
def main():
    st.title("Text Scanner and Generator")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        extracted_text = extract_text(image)
        st.text_area("Extracted Text", extracted_text, height=200)

        keyword = st.text_input("Enter a keyword")
        if st.button("Search"):
            highlighted_text = highlight_text(extracted_text, keyword)
            st.markdown(highlighted_text, unsafe_allow_html=True)

        # Prepare text for download
        if extracted_text:
            json_data = json.dumps({"extracted_text": extracted_text}, ensure_ascii=False)
            st.download_button(
                label="Download Text as JSON",
                data=json_data,
                file_name='extracted_text.json',
                mime='application/json'
            )

if __name__ == "__main__":
    main()
