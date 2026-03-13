# 1. Base image
# We use the uv image from Astral. 
# It already includes Python and the uv package manager installed.
# "debian-slim" keeps the image small while still providing Debian utilities.
FROM ghcr.io/astral-sh/uv:debian-slim

# 2. Set the working directory inside the container
# Every command after this will run inside /app.
# This is where our project will live in the container.
WORKDIR /app

# 3. Copy dependency files first
# We copy only the dependency definition files initially.
# This allows Docker to cache the dependency installation layer.
# If only application code changes, dependencies won't reinstall.
COPY pyproject.toml uv.lock /app/

# 4. Install Python dependencies
# uv sync installs all dependencies defined in pyproject.toml
# using the exact versions locked in uv.lock.
# --locked ensures reproducible builds.
RUN uv sync --locked

# 5. Copy the rest of the application source code
# Now we copy the entire project into the container.
# This happens after dependencies so Docker caching works better.
COPY . /app/

# 6. Expose the application port
# This tells Docker that the container listens on port 8000.
# FastAPI will run on this port.
EXPOSE 8000

# 7. Start the FastAPI development server
# uv run executes commands inside the project's virtual environment.
# fastapi dev starts the FastAPI dev server with auto-reload.
# --host 0.0.0.0 allows external connections (needed for Docker).
# --port 8000 matches the exposed port.
CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]