
import requests
from config import HF_API_KEY
# Model endpoint on Hugging Face
MODEL_ID = "nlpconnect/vit-gpt2-image-captioning" 
""
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

# Prepare headers with your API key
headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}
#defining a function
def caption_image():
#Loads the local image file "testing.jpg" and sends it to the Hugging Face Inference API for captioning.
    image_source="testing.jpg"
    #trying to load the image bytes
    try:
        with open(image_source,'rb')as ap:
            image_byts=ap.read()
    except Exception as e:
        print(f"Could not load image from {image_source}.\nError: {e}")
        return
    #sending a request to hugging face 
    response=requests.post(API_URL,headers=headers,data=image_byts)
    result=response.json()
    # 3. Check for errors
    if isinstance(result, dict) and "error" in result:
       print(f"[Error] {result['error']}")
       return
    # 4. Extract caption
    caption = result[0].get("generated_text", "No caption found.")
    print("Image:", image_source)
    print("Caption:", caption)




if __name__=="__main__":
   caption_image()
