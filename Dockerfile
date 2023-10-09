FROM python:3.7-stretch
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN pip install opencv-python
