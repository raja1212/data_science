FROM python:3.7

MAINTAINER name = rajasen9903@gmail.com

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./src

WORKDIR /src

#EXPOSE 8080

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]