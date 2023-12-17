#!/bin/bash                                                       
# Define colors                                                   
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if required packages are already installed
if pip freeze | grep -Fq -f requirements.txt; then
    echo -e "${GREEN}Server is starting${NC}\n"
else
# Install required packages
    echo -e "${BLUE}Installing required packages...${NC}"
    pip install -r requirements.txt --quiet
    echo -e "${GREEN}Required packages installed${NC}"
fi

# Start server

python main.py