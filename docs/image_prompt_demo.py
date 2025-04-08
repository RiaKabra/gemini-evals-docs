image_path = "image.png"

with open(image_path, "rb") as img_file:
    image_data = img_file.read()

response = model.generate_content(
    contents=[
        {"text": "What do you see in this image?"},
        {"inline_data": {
            "mime_type": "image/png",
            "data": image_data
        }}
    ]
)

print(response.text)
