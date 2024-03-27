FROM ubuntu:24.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git python3 python3-pip curl

# rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN python3 -m pip install --upgrade pip  --break-system-packages
RUN pip install numpy matplotlib pandas  --break-system-packages


RUN pip install --upgrade open-interpreter --break-system-packages

WORKDIR /app

