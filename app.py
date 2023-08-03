# Importing required packages
from docx import Document
import streamlit as st
import openai
import base64

openai.api_key = "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"

# Define a function to handle the translation process
def translate_text(text, target_language):
    system_content = 'Ti si senior menadžer proizvoda u IT kompaniji.'
    user_content = f"Translate '{text}' to {target_language}"

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"{system_content}"},
            {"role": "user", "content": f"{user_content}"},
        ]
    )

    information = completion.choices[0].message.content.strip()
    return information

# Define a function to generate download link for a file
def get_download_link(text, file_name):
    doc = Document()
    doc.add_paragraph(text)

    # Save the docx document
    doc.save(file_name)

    with open(file_name, "rb") as file:
        data = file.read()
    b64_data = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64_data}" download="{file_name}">Download Translated Document</a>'
    return href

# Define the main function that sets up the Streamlit UI and handles the translation process
def main():
    # Set up the Streamlit UI
    st.sidebar.header('🌍💬 Language Translation App 🚀🎯')
    st.sidebar.write('🌐 Izaberi jezik na koji želiš da prevedeš svoj tekst iz padajućeg menija.')
    st.sidebar.write("Klikni na 'Prevedi' dugme i voilà! Tvoj tekst će biti preveden u izabranom jeziku. 🎉")
    st.sidebar.write("Ova aplikacija koristi najmoderniju tehnologiju veštačke inteligencije za prevod teksta, obezbeđujući tačne i prirodne prevode. Bez obzira da li želiš da prevedeš jednostavan tekst, poslovni izveštaj ili knjigu, ova alatka je tu da ti pomogne. 🌟")

    # Create a text input for the user to enter the text to be translated
    text_input = st.text_area('Unesi tekst koji želiš da prevedeš')

    # Create a selectbox for the user to select the target language
    target_language = st.selectbox('Na koji jezik želiš da prevodiš?', ['Arabic', 'English', 'Spanish', 'French', 'German', 'Serbian'])

    # Create a button that the user can click to initiate the translation process
    translate_button = st.button('Prevedi')

    # Handle the translation process when the user clicks the translate button
    if translate_button and text_input:
        st.text('Translating...')
        translated_text = translate_text(text_input, target_language)

        # Display the translated text
        st.write("Translated Text:")
        st.write(translated_text)

        # Create a download link for the translated text in a docx document
        file_name = 'translated_text.docx'
        download_link = get_download_link(translated_text, file_name)
        st.markdown(download_link, unsafe_allow_html=True)

# Call the main function
if __name__ == '__main__':
    main()
