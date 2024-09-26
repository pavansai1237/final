from PIL import Image

def extract_text(image_path):
    image = Image.open(image_path)
    # Preprocess image (e.g., resize, convert to grayscale)
    inputs = tokenizer(image, return_tensors="pt")
    outputs = model.generate(**inputs)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text