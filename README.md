# ImagineAI Studio

This project demonstrates how to generate images from text prompts using FastAPI and the Stable Diffusion model.

## Requirements

- Python 3.9+
- Docker (optional, for containerization)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Pahinithi/ai-image-generator-fastapi.git
    cd Text-to-Image-Generation
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

### Development Mode

1. Start the FastAPI server in development mode:
    ```sh
    uvicorn app.main:app --reload
    ```
    or
    ```sh
    fastapi dev app/main.py
    ```

2. Open your browser and navigate to `http://localhost:8000` to access the application.

### Production Mode

1. Start the FastAPI server in production mode:
    ```sh
    uvicorn app.main:app
    ```
    or
    ```sh
    fastapi run app/main.py
    ```

2. Open your browser and navigate to `http://localhost:8000` to access the application.

## Using Docker

1. Build the Docker image:
    ```sh
    docker build -t text-to-image .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8000:8000 text-to-image
    ```

## Usage

1. Enter a text prompt and a negative prompt in the provided fields on the web interface.
2. Click the "Generate" button to create an image based on the text prompt.
3. The generated image will be displayed on the page.

## License

This project is licensed under the MIT License.
