#!/bin/bash
# braincannon.sh - Launcher script for braincannon
# Handles Python environment setup and execution

set -e  # Exit on error

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
PYTHON_SCRIPT="$SCRIPT_DIR/braincannon.py"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[braincannon]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[braincannon]${NC} $1"
}

print_error() {
    echo -e "${RED}[braincannon]${NC} $1" >&2
}

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    print_info "Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Check if dependencies need to be installed
if [ ! -f "$VENV_DIR/.deps_installed" ] || [ "$REQUIREMENTS" -nt "$VENV_DIR/.deps_installed" ]; then
    print_info "Installing/updating dependencies..."
    pip install --upgrade pip > /dev/null 2>&1
    
    if [ -f "$REQUIREMENTS" ]; then
        pip install -r "$REQUIREMENTS" > /dev/null 2>&1
    else
        # Install required packages directly
        pip install atproto pyyaml > /dev/null 2>&1
    fi
    
    touch "$VENV_DIR/.deps_installed"
    print_info "Dependencies installed successfully"
fi

# Check if config.yaml exists
if [ ! -f "$SCRIPT_DIR/config.yaml" ]; then
    print_error "config.yaml not found!"
    print_warning "Please copy config.yaml.example to config.yaml and add your credentials"
    print_warning "Run: cp config.yaml.example config.yaml"
    deactivate
    exit 1
fi

# Run the Python script with all arguments passed to this script
python3 "$PYTHON_SCRIPT" "$@"
EXIT_CODE=$?

# Deactivate virtual environment
deactivate

# Exit with the same code as the Python script
exit $EXIT_CODE
