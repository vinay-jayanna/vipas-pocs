# Use Python 3.9 slim image as the base
FROM python:3.9-slim-bullseye

# Set the working directory to /app
WORKDIR /app


# Create pip.conf with Artifact Registry URL
# RUN echo "[global]\nextra-index-url = https://us-east-1-python.pkg.dev/ai-platform-414410/vps-app-pkgs-1-1/simple/" > /etc/pip.conf

# Copy the requirements.txt and install Python dependencies
# Note: If your .whl package already includes all necessary dependencies, this step might be redundant or could be tailored based on minimal external dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .whl package to the container
# Ensure to replace `app.your_project_id-0.1.0-py3-none-any.whl` with the actual filename of your package
COPY dist/app.app_id-0.1.0-py3-none-any.whl /usr/src/app/

# Copy the updated entry script into the container
COPY entry_script.sh /app/
# Make sure the entry script is executable
RUN chmod +x /app/entry_script.sh

# Set an environment variable for the port with a default value
ENV STREAMLIT_PORT=8051

# Expose the port Streamlit apps use
EXPOSE $STREAMLIT_PORT

# Use the entry script to start the container, explicitly calling bash
ENTRYPOINT ["/bin/bash", "/app/entry_script.sh"]
