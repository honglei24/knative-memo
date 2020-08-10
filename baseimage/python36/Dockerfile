# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.6.11-buster

RUN pip install requests flask gunicorn --index-url https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# TEST START
#ENV VERSION=1.0
#ENV PORT="8080"
#ENV CTYUN_EFC_ENTRY="index.handler"
#ENV CTYUN_EFC_INITIALIZER="index.init"
#ENV CTYUN_EFC_LOCATION="http://125.88.39.147:9001/honglei/index.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=Y3R5dW4K%2F20200810%2F%2Fs3%2Faws4_request&X-Amz-Date=20200810T161354Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e244bb71c23861f078555f0bc26331fbb062185a6d7bfe35986fa849e0170bd1"
# TEST END

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 4 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD curl -s "${CTYUN_EFC_LOCATION}" -o source.zip && unzip source.zip >/dev/null 2>&1 && gunicorn --bind :$PORT --workers 1 --threads 4 --timeout 0 app:app