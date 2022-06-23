from python:3.8.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ /opt
WORKDIR /opt

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app.main:application", "--host", "0.0.0.0", "--port", "8052"]
