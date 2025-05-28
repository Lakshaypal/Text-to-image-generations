# 🎨 Text-to-Image Generation App

A Flask-based web application that generates images from text descriptions using the Stable Diffusion model. This application provides a simple interface where users can input text prompts and receive AI-generated images in response.

## ✨ Features

- 🖼️ Text-to-image generation using Stable Diffusion v1.5
- 🎯 Simple and intuitive web interface
- ⚡ Real-time image generation
- 🚀 Support for both CPU and GPU (CUDA) processing

## 📋 Prerequisites

- 🐍 Python 3.7 or higher
- 💻 CUDA-capable GPU (optional, but recommended for faster generation)
- 📦 pip (Python package installer)

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd text-to-image-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5001
```

3. Enter your text prompt in the input field and click the generate button to create an image.

## 🔧 Technical Details

- ⚙️ Built with Flask 2.0.3
- 🤖 Uses Stable Diffusion v1.5 from Hugging Face
- 💪 Supports both CPU and GPU processing
- 🖼️ Images are generated in real-time and returned as base64-encoded PNG files

## 📦 Dependencies

- 🔥 torch
- 🎯 diffusers
- 🔄 transformers
- 🖼️ Pillow
- 🌐 Flask==2.0.3
- ⚙️ Werkzeug==2.0.3

## 📝 Notes

- ⏳ The first run will download the Stable Diffusion model, which may take some time depending on your internet connection.
- 🚀 GPU acceleration is automatically enabled if a CUDA-capable GPU is available.
- 🔌 The application runs on port 5001 by default.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- 🎨 Stable Diffusion model by RunwayML
- 🤗 Hugging Face for providing the model and tools
