FROM python:alpine3.19
COPY . .
RUN pip3 install -r requirements.txt
CMD python main.py