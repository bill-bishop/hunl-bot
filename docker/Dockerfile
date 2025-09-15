FROM python:3.10-slim

WORKDIR /app

# System deps for OpenSpiel
RUN apt-get update && apt-get install -y \
    cmake \
    g++ \
    git \
    make \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash"]