FROM python:3.9.7
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload"]
