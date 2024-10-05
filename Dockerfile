# Step 1: Use a base image with Python
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file to the working directory
COPY my_graph/requirements.txt ./my_graph/requirements.txt

# Step 4: Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r ./my_graph/requirements.txt

# Step 5: Copy the rest of the application code to the working directory
COPY . .

# Step 6: Ensure the current directory is part of the PYTHONPATH
ENV PYTHONPATH=/app

# Step 7: Run the visualization script
RUN python3 ./my_graph/visualization_graph.py