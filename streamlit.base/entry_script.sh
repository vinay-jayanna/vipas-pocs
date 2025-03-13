#!/bin/bash

# Enable unofficial bash strict mode
set -euo pipefail

echo "Starting entrypoint script..."

# Check if the PROJECT_ID environment variable is set
if [ -z "${PROJECT_ID:-}" ]; then
  echo "Error: Environment variable PROJECT_ID is not set."
  exit 1
else
  echo "PROJECT_ID is set to '$PROJECT_ID'."
fi

# Assuming the .whl package naming convention includes the PROJECT_ID
PACKAGE_NAME="app.${PROJECT_ID}-0.1.0-py3-none-any.whl"
PACKAGE_PATH="/usr/src/app/${PACKAGE_NAME}"

echo "Package name resolved to '$PACKAGE_NAME'."
echo "Looking for the package at '$PACKAGE_PATH'..."

# Check if the .whl file exists at the specified location
if [ ! -f "$PACKAGE_PATH" ]; then
  echo "Error: Package '$PACKAGE_NAME' not found at '$PACKAGE_PATH'."
  exit 1
else
  echo "Package found. Proceeding with installation..."
fi

# Install the package
echo "Installing package '$PACKAGE_NAME'..."
pip install "$PACKAGE_PATH"
echo "Package installation completed."

# Dynamically find the installation path of the app package
echo "Finding installation path of the package..."
APP_PATH=$(python -c "import app; print(app.__path__[0])")
echo "Package installed at: '$APP_PATH'"

# Construct the path to the Streamlit app script
APP_SCRIPT_PATH="${APP_PATH}/app.py"
echo "Constructed Streamlit app script path: '$APP_SCRIPT_PATH'"

# Check if the Streamlit app script exists
if [ ! -f "$APP_SCRIPT_PATH" ]; then
  echo "Error: Streamlit app script not found at '$APP_SCRIPT_PATH'."
  exit 1
else
  echo "Streamlit app script found. Launching the app..."
fi

# Run your Streamlit app
streamlit run "$APP_SCRIPT_PATH" --server.port $STREAMLIT_PORT --logger.level='debug' --global.logLevel='debug' --server.enableCORS=False --server.enableXsrfProtection=False  --logger.enableRich=False
echo "Streamlit app launched successfully."
