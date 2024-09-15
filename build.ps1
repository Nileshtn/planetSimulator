# Forcefully remove all Docker images
docker rmi -f (docker images -q) # Caution: This removes all Docker images. Edit this before use.

# Build a Docker image with a tag
docker build -t planet_simulator:v0.2 .

# Pause the script and wait for user input
Read-Host -Prompt "Press Enter to continue"
