FROM python:3.12-slim

# ======================================================
# ENV
# ======================================================

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ======================================================
# SYSTEM DEPENDENCIES
# ======================================================

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# ======================================================
# WORKDIR
# ======================================================

WORKDIR /app

ENV PYTHONPATH=/app

# ======================================================
# DEPENDENCIES
# ======================================================

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# ======================================================
# PROJECT
# ======================================================

COPY . .

# ======================================================
# ENTRYPOINT
# ======================================================

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]