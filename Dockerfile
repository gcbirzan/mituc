FROM nvidia/cuda:10.1-cudnn7-devel

RUN ldconfig; apt-get update; apt-get install -y python3.7 python3-pip

WORKDIR /code
ADD requirements.txt /code/
RUN python3.7 -m pip install --upgrade pip setuptools wheel
RUN python3.7 -m pip install  -r /code/requirements.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libnvinfer-plugin6=6.0.1-1+cuda10.1 libnvinfer6=6.0.1-1+cuda10.1 cuda-10-1

ADD . /code/
