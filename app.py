import streamlit as st
import requests
import json
from PIL import Image
from io import BytesIO
from utils import (image_clasifier, 
                   text_to_image_generator_request, 
                   text_to_image_generator_fetch)

def main():
    
    st.title("IMAGE GENERATION AND CLASSIFICATION")
    col1, col2 = st.columns(2)


    # ------- IMAGE GENERATION FROM PROMPT ------- 
    input_text = col1.text_input("Introduce a text: ")
    if  col1.button('Generate Image from Prompt'):

        if input_text != '':
            response_request = text_to_image_generator_request(input_text= input_text)
            
            #Guardamos el json generado del Prompt Actualizado
            with open('model_response.json', 'w') as file:
                json.dump(response_request, file, indent=4)
            
            image_link = text_to_image_generator_fetch(response_request= response_request)
            
            col1.success(f'Image Link: {image_link}')
            col1.image(image_link, caption='Successfully Image Generated')
        else:
            col1.warning("Write a Prompt first before Generate an image")


    # ------- IMAGE CLASIFICACION ------- 
    uploaded_image = col2.file_uploader("Load Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        col2.image(image, caption="Image Uploaded Successfully!!", use_column_width=True)

    if col2.button("Classify Uploaded Image Manually"):
       
        if uploaded_image is not None:
            predicted_class = image_clasifier(image=image)['predicted_class']
            col2.success(f'Class Predicted ==> {predicted_class}')           
        else:
            col2.warning("Upload an image first before trying to classify.")
    
    
    # ------- IMAGE CLASIFICATION FROM GENERATED IMAGE --------
    if col1.button('Classify Generated Image'):
        
        #Cargamos el json generado en el Prompt
        with open('model_response.json', 'r') as file:
            response_request = json.load(file)
            
        image_link = text_to_image_generator_fetch(response_request= response_request)

        if (image_link != '') and (input_text != ''):
            col1.image(image_link, caption='Successfully Image Generated')
            
            image = Image.open(BytesIO(requests.get(image_link).content))
            predicted_class = image_clasifier(image= image)['predicted_class']
            col1.success(f'Class Predicted ==> {predicted_class}')
            
        else:
            col1.warning("Generated Image first before Classify!!")
        

if __name__ == "__main__":
    main()
