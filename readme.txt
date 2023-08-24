# Setup Using Docker
# Build a Docker image with the tag "my-bot" using the current directory (.) as the build context.
docker build --no-cache -t my-bot .

# Run a Docker container using the "my-bot" image and map port 5001 on the host to port 5001 in the container.
docker run -p 5001:5001 my-bot

# Run a Docker container in detached mode (background) using the "my-bot" image and map port 5001 on the host to port 5001 in the container.
docker run -d -p 5001:5001 my-bot

# Setup Manually

# Install Python
# Linux:

# Ubuntu/Debian:
sudo apt update
sudo apt install python3

# Fedora:
sudo dnf install python3

# Windows:
# Download the Python installer executable from the official website (https://www.python.org/downloads/windows/).
# Run the installer executable and follow the installation wizard.

# macOS:
# Homebrew:
brew install python
sudo port install python

# Install Dependencies
pip install Flask==2.0.1
pip install requests==2.26.0
pip install llama-index==0.5.6
pip install langchain==0.0.148
pip install flask-basicauth
pip install PyPDF2

# Build Model
python build_model.py 

# Run Server
python server.py
