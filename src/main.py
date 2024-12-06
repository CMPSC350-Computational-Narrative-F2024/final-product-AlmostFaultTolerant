import os
from openai import OpenAI
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")
OPEN_AI_KEY = CONFIG.get("KEY") or os.environ.get("OPEN_AI_KEY")
OPEN_AI_ORG = CONFIG.get("ORG") or os.environ.get("OPEN_AI_ORG")

client = OpenAI(api_key=OPEN_AI_KEY)

response = client.images.generate(
    model="dall-e-3",
    prompt="a stick figure on brown ground with a blue background holding the leash of his pet rock. Use minimalist art and limited palette colors.",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(f"Image URL: {image_url}")