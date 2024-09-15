FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libxrandr-dev \
    libxi-dev \
    libxcursor-dev \
    libgl1-mesa-glx \
    libgles2-mesa-dev \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Install Pygame
RUN pip install pygame

ENV XDG_RUNTIME_DIR=/run/user/1000

COPY PlanetSimulation /PlanetSimulation
# Set the working directory
WORKDIR /PlanetSimulation

CMD ["python", "planet_simulator.py"]
