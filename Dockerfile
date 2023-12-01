FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ENV LAUNCH_APP=app_simple.py
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3.9 \
    python3-pip \
    python3-dev \
    python3.10-venv \
    git \
    ffmpeg \
    google-perftools \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=$HOME/app \
    PYTHONUNBUFFERED=1 \
    SYSTEM=spaces

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

RUN python3 -m pip install --upgrade pip

RUN pip3 install git+https://github.com/suno-ai/bark.git
RUN pip3 install git+https://github.com/huggingface/transformers.git

ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc.so.4

RUN echo "Launch app:$LAUNCH_APP"

CMD python3 $LAUNCH_APP