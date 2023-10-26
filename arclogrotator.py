# https://github.com/daryshtaev/arclogrotator
# version 1.0.3

import gzip
import logging
import os
import shutil
from logging.handlers import RotatingFileHandler  # TimedRotatingFileHandler


def namer(name):
    return name + ".gz"


def rotator(source, dest):
    with open(source, 'rb') as f_in:
        with gzip.open(dest, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(source)


def init_logger(file='app.log', directory=os.path.dirname(os.path.realpath(__file__)), max_bytes=524288, backup_count=10, log_level=logging.WARNING):
    log_file = os.path.join(directory, file)
    log_format = '%(asctime)s.%(msecs)03d,%(threadName)s,%(levelname)s,%(name)s,%(message)s'
    log_date_format = '%d.%m.%y %H:%M:%S'
    log_formatter = logging.Formatter(log_format, datefmt=log_date_format)
    # Пример инициализации лога, который "вращается" по моменту времени - в частности "каждую полночь":
    #logFileHandler = TimedRotatingFileHandler(logFile, when='midnight', interval=1, backupCount=10)
    # Инициализация лога, который "вращается" по размеру: "каждые maxBytes":
    log_file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8')
    log_file_handler.setFormatter(log_formatter)
    log_file_handler.rotator = rotator
    log_file_handler.namer = namer
    logger = logging.getLogger()
    logger.addHandler(log_file_handler)
    logger.setLevel(log_level)
    return logger
