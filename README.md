arclogrotator.py
Модуль для инициализации револьверного буфера логов в gzip-архивах.
Создано: 2023-09-14.

Пример использования:
<<
import arclogrotator
logger = arclogrotator.loggerInit()
logger.info('Info!')
logger.warning('Warning!')
logger.debug('Debug!')
>>.