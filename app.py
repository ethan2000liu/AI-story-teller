from transformers import pipeline

# img to txt
def img_to_txt(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]['generated_text']
    return text

image_text = img_to_txt("CAT.jpeg")
print(image_text)


