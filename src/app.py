import io

from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse

import uvicorn
import align_images
from project_images import project_images
import numpy as np
from pathlib import Path

from src import pretrained_networks
from src.dnnlib import tflib
from starlette.responses import StreamingResponse

app = FastAPI()


@app.post("/get_result_image")
async def get_result_image(model_url: str, style_url: str, image: UploadFile = File(...)):
    original_image = Image.open(image.file)
    original_image.save('./raw/test.jpg')
    project_images('aligned', 'generated', num_steps=500, network_pkl=model_url)
    _, _, Gs = pretrained_networks.load_networks(style_url)

    latent_dir = Path("generated")
    latents = latent_dir.glob("*.npy")
    for latent_file in latents[0:1]:
        latent = np.load(latent_file)
        latent = np.expand_dims(latent, axis=0)
        synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=False),
                                minibatch_size=8)
        images = Gs.components.synthesis.run(latent, randomize_noise=False, **synthesis_kwargs)

        Image.fromarray(images.transpose((0, 2, 3, 1))[0], 'RGB').save(latent_file.parent / (f"example.jpg"))
        result = Image.open("generated/example.jpg")
        return StreamingResponse(io.BytesIO(result.tobytes()), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
