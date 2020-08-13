FROM python:alpine3.6
WORKDIR /usr/src/app
EXPOSE 5001

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]
