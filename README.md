## Testing BARK

Just create a basic gradio app to create audio-text using [bark]('https://github.com/suno-ai/bark')
### Docker

```bash
docker build -t bark .
docker run -ti -p 7860:7860 -p 443:443 -v /path/to/store/generated/files/:/output --gpus all bark
```

### Browser 

Open your brother using the provided gradio url.