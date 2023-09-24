# version 1.0.2

import logging, gzip, shutil, os
from logging.handlers import RotatingFileHandler #TimedRotatingFileHandler

def namer(name):
    return name + ".gz"

def rotator(source, dest):
    with open(source, 'rb') as f_in:
        with gzip.open(dest, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(source)

def loggerInit(file='app.log',directory=os.path.dirname(os.path.realpath(__file__)), maxBytes=524288, backupCount=10, logLevel=logging.WARNING):
    logFile=os.path.join(directory, file)
    logMaxBytes = maxBytes
    logBackupCount = backupCount
    logLevel = logLevel
    logFormat = '%(asctime)s.%(msecs)03d,%(threadName)s,%(levelname)s,%(name)s,%(message)s'
    logDateFormat = '%d.%m.%y %H:%M:%S'
    logFormatter = logging.Formatter(logFormat, datefmt=logDateFormat)
    # Пример инициализации лога, который "вращается" по моменту времени - в частности "каждую полночь":
    #logFileHandler = TimedRotatingFileHandler(logFile, when='midnight', interval=1, backupCount=10)
    # Инициализация лога, который "вращается" по размеру: "каждые maxBytes":
    logFileHandler = RotatingFileHandler(logFile, maxBytes=logMaxBytes, backupCount=logBackupCount, encoding='utf-8')
    logFileHandler.setFormatter(logFormatter)
    logFileHandler.rotator = rotator
    logFileHandler.namer = namer
    logger = logging.getLogger()
    logger.addHandler(logFileHandler)
    logger.setLevel(logLevel)
    return logger