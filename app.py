from transformers import pipeline

# img to txt
def img_to_txt(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]['generated_text']
    return text

# generate story with gpt2
def generate_story(text):
    create_story = pipeline("text-generation", model="gpt2")

    # You can modify the prompt as needed
    prompt = f"You are a storyteller. Generate a short story under 300 words based on the following narrative caption:\n{text}\nStory:"

    # Adjust the temperature to control randomness (lower for more focused output)
    story = create_story(prompt, max_length=600, num_return_sequences=1, temperature=1)[0]['generated_text']
    return story

def print_paragraph(paragraph):
    # Split the paragraph into lines
    lines = paragraph.split('\n')

    # Print lines starting from the third line
    for line in lines[2:]:
        print(line)

# Example usage:
image_text = img_to_txt("CAT.jpeg")
story = generate_story(image_text)
print("txt cut below============")
print_paragraph(story)


