import streamlit as st
import pytesseract as pyt
import pypdfium2 as pdfium
from PIL import Image

# ---------------------------------------------------------------------------------------------------
st.set_page_config(layout='wide')
st.title('Hello')

# ---------------------------------------------------------------------------------------------------
pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

file = st.file_uploader("Select the  file", type=["jpg", "jpeg", "png", "pdf"])

col1, col2 = st.columns([1,2])

if file is not None:
    file_name = file.name.lower()

    # for image input
    if file_name.endswith(('.jpg','.jpeg','.png')):
        img = Image.open(file)
        with col1:
            st.image(img, caption='Uploaded Image', use_container_width=True)
        with col2:
            st.text(pyt.image_to_string(img))

    elif file_name.endswith('.pdf'):
        pdf = pdfium.PdfDocument(file)
        for i, page in enumerate(pdf):
            temp = page.get_textpage()
            text = temp.get_text_range()

            st.subheader(f"\nPage {i+1} \n\n")
            st.write(text)
            st.write("\n")

