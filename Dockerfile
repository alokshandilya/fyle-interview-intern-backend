FROM python:3.8-slim

# set environment variables
ENV PYTHONUNBUFFERED=1

# set the working directory
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 7755

# run the application
RUN chmod +x /app/run.sh
CMD [ "./run.sh" ]