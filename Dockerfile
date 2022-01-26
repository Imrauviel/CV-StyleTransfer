FROM python:3.8.0-alpine
WORKDIR /usr/src/app
COPY ./ ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["hypercorn", "src/app:app", "--reload", "-b", "127.0.0.1:9000"]