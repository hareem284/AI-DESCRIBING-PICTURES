
import requests
import json
from config import HF_API_KEY
# Model endpoint on Hugging Face
MODEL_ID = "nlpconnect/vit-gpt2-image-captioning" 
""
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

# Prepare headers with your API key
headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}
def print_menue():
    print("select one of the outputs: ")
    print("1.caption 5 words")
    print("2.description 30 to 50 words")
    print("3.summary 50 words")
    print("4.exit")


def truncate_text(caption,no_of_Words):
    words=caption.strip().split()
    return " ".join(words[:no_of_Words])


#derining a function
def generate_text(prompt, model="gpt2",max_new_tokens=50):
    print("generating text with prompt {} ".format(prompt))
    payload={"inputs":prompt,
              "parameters":{"max_new_tokens":max_new_tokens}}
    headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
    }
    response=requests.post(API_URL,headers=headers,json=payload,files=None )
    if response.status_code==200:
        print("this was sucsesful")
        text_byte=response.content
        result=json.loads(text_byte.decode("utf-8"))
        if isinstance(result, dict) and "error" in result:
           print(f"[Error] {result['error']}")
           return
        # 4. Extract caption
        generated_caption = result[0].get("generated_text", " ")
        return generated_caption







    
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
       print(f"[Error] {result['erro2r']}")
       return
    # 4. Extract caption
    caption = result[0].get("generated_text", "No caption found.")
    print("Image:", image_source)
    print("Caption:", caption)
    return caption





if __name__=="__main__":
   basic_caption=caption_image()
   while True:
        print_menue()
        choice=input("enter your choice")
        if choice=='1':
            #i need to take 5 words from the caption_image
            caption=truncate_text(basic_caption,5)
            print(caption)
        elif choice=='2':
            print("i need to make a description of the picture of atleast 30 words")
            promt_text=f"Expand the basic caption to 30 words: {basic_caption}"
            generate_text=generate_text(promt_text,max_new_tokens=40)
            print(generate_text)
            generate_text=generate_text(promt_text, model="gpt2",max_new_tokens=40)
            if generate_text!=None:
               caption=truncate_text(generate_text,30)
               print(caption)
    

