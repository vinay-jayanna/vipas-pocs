#!/bin/bash

# Enable unofficial bash strict mode
set -euo pipefail

echo "Starting entrypoint script..."


echo "created pip.conf"
cat /etc/pip.conf

# Check if the PROJECT_ID environment variable is set
if [ -z "${PROJECT_ID:-}" ]; then
  echo "Error: Environment variable PROJECT_ID is not set."
  exit 1
else
  echo "PROJECT_ID is set to '$PROJECT_ID'."
fi

# Hardcode the Artifact Registry details
PROJECT_ID="ai-platform-414410"
LOCATION="us-east1"
REPOSITORY="vps-app-pkgs-1-1"
PACKAGE_NAME="app.app-id"
PACKAGE_VERSION="0.1.0"

# Construct the Artifact Registry URL
ARTIFACT_REPO_URL="https://${LOCATION}-python.pkg.dev/${PROJECT_ID}/${REPOSITORY}/simple/"

echo "Configuring pip to use Artifact Registry at '$ARTIFACT_REPO_URL'"

# Install the package from the Artifact Registry
echo "Installing package '${PACKAGE_NAME}==${PACKAGE_VERSION}' from Artifact Registry..."
pip install --extra-index-url $ARTIFACT_REPO_URL "${PACKAGE_NAME}==${PACKAGE_VERSION}"

## pip install --extra-index-url https://us-east1-python.pkg.dev/ai-platform-414410/vps-app-pkgs-1-1/simple/ --trusted-host us-east1-python.pkg.dev "app.app-id==0.1.0" --verbose


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
streamlit run "$APP_SCRIPT_PATH" --server.port 8080
echo "Streamlit app launched successfully."
