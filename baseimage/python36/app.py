import os

from flask import Flask, request
import index
import time
import logging

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def efc():
    header=request.headers
    data=request.stream.read()
    app.logger.info(header)
    app.logger.info(data)

    flag = os.environ.get('INIT')
    initializer = os.environ.get('CTYUN_EFC_INITIALIZER')
    if flag == None and initializer != None:
        app.logger.info("FC Init Invoke Start. %s", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        exec("import " + initializer.split(".",1)[0])

        init=eval(initializer)
        init(header)

        os.environ['INIT']="1"
        app.logger.info("FC Init Invoke End. %s", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    entry = os.environ.get('CTYUN_EFC_ENTRY')
    exec("import " + entry.split(".",1)[0])
    func=eval(entry)
    app.logger.info("FC Invoke Start. %s", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    ret = func(data, header)
    app.logger.info("FC Invoke End. %s", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    return ret

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
