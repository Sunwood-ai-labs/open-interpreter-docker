# FROM ubuntu:22.04
FROM nvcr.io/nvidia/pytorch:23.08-py3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git python3 python3-pip

RUN python -m pip install --upgrade pip
RUN pip install open-interpreter
RUN pip install numpy matplotlib pandas

WORKDIR /root