from transformers import ViTFeatureExtractor, ViTForImageClassification
import requests
import json

def text_to_image_generator_request(input_text: str) -> dict:
    """Generacion de la imagen y almacenamiento del response.json generado

    Args:
        input_text (str): Ingreso de Prompt

    Returns:
        dict: retorno del response.json()
    """
    
    #Cargamos la api key
    with open('api_keys.json', 'r') as file:
        keys = json.load(file)
    
    #Link del modelo en Hugging Face
    url =  "https://stablediffusionapi.com/api/v4/dreambooth"  

    # Seteamos el prompt a enviar 
    payload = json.dumps({  
        "key":  keys['api_key'],  
        "model_id":  "juggernaut-xl-v5",  
        "prompt":  input_text,  
        "negative_prompt":  "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
        "width":  "512",  
        "height":  "512",  
        "samples":  "1",  
        "num_inference_steps":  "30",  
        "safety_checker":  "no",  
        "enhance_prompt":  "yes",  
        "seed":  None,  
        "guidance_scale":  7.5,  
        "multi_lingual":  "no",  
        "panorama":  "no",  
        "self_attention":  "no",  
        "upscale":  "no",  
        "embeddings":  "embeddings_model_id",  
        "lora":  "lora_model_id",  
        "webhook":  None,  
        "track_id":  None  
    })  

    #Configuramos los Headers
    headers =  {  
        'Content-Type':  'application/json'  
    }  

    #Hace una peticion POST 
    response = requests.request("POST", url, headers=headers, data=payload)  

    #Retorno del link de la imagen generada
    return response.json()
    
    
def text_to_image_generator_fetch(response_request: dict) -> str:
    """Obtencion de la imagen generada con el id_request

    Args:
        response_request (dict): json del response previo generado

    Returns:
        str: url de la imagen generada
    """
    
    #Cargamos la api key
    with open('api_keys.json', 'r') as file:
        keys = json.load(file)
    
    #url of queued/generated image
    url = "https://stablediffusionapi.com/api/v4/dreambooth/fetch"
    payload = json.dumps({
                            "key": keys['api_key'],
                            "request_id": response_request['id']
                            })

    headers = {
                'Content-Type': 'application/json'
                }

    response = requests.request("POST", url, headers=headers, data=payload)

    #return link of image
    return response.json()['output'][0]


def image_clasifier(image) -> dict:
    """Clasificador de imagenes

    Args:
        image (_type_): ingreso de la imagen

    Returns:
        dict: diccionario con la clase predicha
    """
    # Cargar el extractor de características y el modelo de Hugging Face
    feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
    
    # Preprocesar la imagen y prepararla para el modelo
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Realizar la predicción
    outputs = model(**inputs)
    logits = outputs.logits

    # Obtener la clase con la mayor probabilidad
    predicted_class_idx = logits.argmax(-1).item()
    predicted_class = model.config.id2label[predicted_class_idx]

    # Retornar la clase predicha
    return {"message": "La imagen ha sido analizada!", 
            "predicted_class": predicted_class  
            }
