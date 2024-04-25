# # Use a Linux-based Python image
# FROM python:3.10-slim-buster

# # Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# # For more information, please refer to https://aka.ms/vscode-docker-python-user-rights
# EXPOSE 80

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install system-level dependencies for Playwright, additional libraries, and application dependencies
# RUN apt-get update && apt-get install -y \
#     libnss3 \
#     libx11-6 \
#     libxcb1 \
#     libxkbcommon0 \
#     libglib2.0-0 \
#     libpango-1.0-0 \
#     libxcomposite1 \
#     libxdamage1 \
#     libxext6 \
#     libxfixes3 \
#     libxrandr2 \
#     libgbm1 \
#     libasound2 \
#     libatk1.0-0 \
#     libatk-bridge2.0-0 \
#     libcups2 \
#     libdbus-1-3 \
#     libatspi2.0-0 \
#     libcairo2 \
#     && rm -rf /var/lib/apt/lists/*

# # Install Chromium browser
# RUN apt-get update && apt-get install -y chromium

# # Install pip requirements including gunicorn
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt gunicorn

# # Install Playwright
# RUN python -m pip install playwright
# RUN python -m playwright install

# WORKDIR /app
# COPY . /app

# # During debugging, this entry point will be overridden.
# CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]





# ************************ unstable ******************************

# # Use a Linux-based Python image
# FROM python:3.10-slim-buster

# # Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# # For more information, please refer to https://aka.ms/vscode-docker-python-user-rights
# EXPOSE 80

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install system-level dependencies for Playwright, additional libraries, and application dependencies
# RUN apt-get update && apt-get install -y \
#     xvfb \
#     libnss3 \
#     libx11-6 \
#     libxcb1 \
#     libxkbcommon0 \
#     libglib2.0-0 \
#     libpango-1.0-0 \
#     libxcomposite1 \
#     libxdamage1 \
#     libxext6 \
#     libxfixes3 \
#     libxrandr2 \
#     libgbm1 \
#     libasound2 \
#     libatk1.0-0 \
#     libatk-bridge2.0-0 \
#     libcups2 \
#     libdbus-1-3 \
#     libatspi2.0-0 \
#     libcairo2 \
#     && rm -rf /var/lib/apt/lists/*

# # Install pip requirements including gunicorn
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt gunicorn

# # Install Playwright
# RUN python -m pip install playwright
# RUN python -m playwright install
# RUN python -m pip install playwright_stealth

# WORKDIR /app
# COPY . /app

# # During debugging, this entry point will be overridden.
# # CMD  gunicorn --bind 0.0.0.0:80 main:app
# CMD ["xvfb-run", "gunicorn", "--bind", "0.0.0.0:80", "main:app"]



























# ************************ Stable ****************************


# Use a Linux-based Python image
FROM python:3.10-slim-buster

# Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# For more information, please refer to https://aka.ms/vscode-docker-python-user-rights
EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install system-level dependencies for Playwright, additional libraries, and application dependencies


RUN apt-get update && apt-get install -y \
    libnss3 \
    libx11-6 \
    libxcb1 \
    libxkbcommon0 \
    libglib2.0-0 \
    libpango-1.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libatspi2.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements including gunicorn
COPY requirements.txt .
RUN python -m pip install -r requirements.txt gunicorn

# Install Playwright
RUN python -m pip install playwright
RUN python -m playwright install

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden.
CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]























# # For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.10-slim

# # Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# # For more information, please refer to https://aka.ms/vscode-docker-python-user-rights
# EXPOSE 80

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt gunicorn

# # Install Playwright and its binaries, and install system-level dependencies
# RUN python -m pip install playwright
# RUN playwright install-deps
# RUN playwright install

# WORKDIR /app
# COPY . /app

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]












# # For more information, please refer to https://aka.ms/vscode-docker-python
# # FROM mcr.microsoft.com/windows/nanoserver:ltsc2022
# FROM mcr.microsoft.com/windows/nanoserver/insider:10.0.20348.1

# # Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# # For more information, please refer to https://aka.ms/vscode-docker-python-user-rights
# EXPOSE 80

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt gunicorn

# # Install Playwright and its binaries, and install system-level dependencies
# RUN python -m pip install playwright
# RUN playwright install-deps
# RUN playwright install

# WORKDIR /app
# COPY . /app

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]







# # For more information, please refer to https://aka.ms/vscode-docker-python
# # FROM mcr.microsoft.com/windows/nanoserver:ltsc2022
# # FROM mcr.microsoft.com/windows/nanoserver:1809
# FROM mcr.microsoft.com/windows/nanoserver/insider:10.0.20348.1

# # Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# # For more information, please refer to https://aka.ms/vscode-docker-python-user-rights
# EXPOSE 80

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt gunicorn

# # Install Playwright and its binaries, and install system-level dependencies
# RUN python -m pip install playwright
# RUN playwright install-deps
# RUN playwright install

# WORKDIR /app
# COPY . /app

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]
