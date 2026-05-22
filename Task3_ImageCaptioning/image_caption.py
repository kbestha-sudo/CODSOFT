from transformers import pipeline
from PIL import Image

# Load AI model
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

# Open image
image = Image.open("sample.jpg")

# Generate caption
result = captioner(image)

# Print caption
print("Caption:", result[0]['generated_text'])
