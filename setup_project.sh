#!/bin/bash

# Create folders
mkdir -p templates
mkdir -p static

# Create files in the root
touch app.py requirements.txt

# Create files in templates
touch templates/login.html templates/dashboard.html templates/log_detail.html

# Create files in static
touch static/style.css

echo "✅ Project structure for 'isp-log-ui' has been created."