from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from diffusers import DiffusionPipeline
import torch
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")
    pipe = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16 if device == "mps" else torch.float32,
        use_safetensors=True,
        variant="fp16" if device == "mps" else None,
    )
    pipe.to(device)
    app.state.pipe = pipe
    yield
    del pipe


app = FastAPI(
    title="ImagineAI Studio",
    description="Where words become visual masterpieces",
    version="1.0.0",
    lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def generate_image(pipe, prompt: str, negative_prompt: str) -> str:
    images = pipe(prompt=prompt, negative_prompt=negative_prompt).images[0]
    output_path = f"static/{prompt.replace(' ', '_')}.png"
    images.save(output_path)
    return output_path


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request, prompt: str = Form(...), negative_prompt: str = Form(...)
):
    image_path = generate_image(request.app.state.pipe, prompt, negative_prompt)
    return templates.TemplateResponse(
        "index.html", {"request": request, "image_path": image_path}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
