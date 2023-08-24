# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install Flask==2.0.1
RUN pip install requests==2.26.0
RUN pip install llama-index==0.5.6
RUN pip install langchain==0.0.148
RUN pip install flask-basicauth
RUN pip install PyPDF2

# Generate index.json during image build
RUN python3 build_model.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "server.py"]
