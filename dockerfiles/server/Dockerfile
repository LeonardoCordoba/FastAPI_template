FROM python:3.12.2

RUN mkdir /test
COPY . /test
WORKDIR /test

RUN apt-get update \
    && apt-get install software-properties-common -y \
    && apt-get install -y --no-install-recommends \
    curl \
    wget \
    git-core \
    htop \
    unzip \
    zsh \
    vim \
    parallel \
    gcc \
    g++ \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/tmp/* /var/lib/apt/lists/*

# ENV PYTHONPATH=${PYTHONPATH}:${PWD}
# ENV GOOGLE_APPLICATION_CREDENTIALS=paper-clippy-770972ecdcaa.json
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install