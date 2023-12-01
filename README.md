## Testing BARK

Creating a basic gradio app to create audio-text using (bark)['https://github.com/suno-ai/bark']

### Docker

Build container:

```bash
docker build -t bark .
```

Container launch default:

```bash
docker run -ti -p 7860:7860 -p 443:443 -v /path/to/store/generated/files/:/output --gpus all bark
```

Container launch long_text app:

```bash
docker run -ti -p 7860:7860 -p 443:443 -v /path/to/store/generated/files/:/output --gpus all  -e "LAUNCH_APP=app_long_text.py" bark
```

### Browser 

Open your brother using the provided gradio url.