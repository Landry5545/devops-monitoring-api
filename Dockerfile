# Step 1: Use a lightweight official Python base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the dependencies file first (better layer caching)
COPY requirements.txt .

# Step 4: Install dependencies without cache to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY main.py .

# Step 6: Expose the port the API will run on
EXPOSE 8000

# Step 7: Start the API with Uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
