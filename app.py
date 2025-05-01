from flask import Flask, request, jsonify, render_template
import io
import base64
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline

app = Flask(__name__)

# Load the Stable Diffusion pipeline.
# You might need to provide your Hugging Face token if the model is gated.
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading model on {device}...")
pipeline = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)
pipeline = pipeline.to(device)

@app.route('/')
def index():
    # Render the frontend HTML
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Generate image from text prompt. The "images" key returns a list of generated images.
        result = pipeline(prompt)
        image = result["images"][0]
        
        # Save image to an in-memory buffer.
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return jsonify({'image': img_str})
    except Exception as e:
        print("Error during image generation:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5001 in debug mode.
    app.run(host='0.0.0.0', port=5001, debug=True)
