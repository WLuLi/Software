FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY requirements.txt /app/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /app/
