import common
import logging


logging.basicConfig(filename='/Users/ilya.teterin/projects/python/myapp.log', filemode='w', level=logging.INFO)
Jlogger=logging.getLogger("log")
Jlogger.info('just a default logger')


print("loaded") 
