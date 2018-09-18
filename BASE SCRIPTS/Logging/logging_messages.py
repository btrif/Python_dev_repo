#  Created by Bogdan Trif on 30-07-2018 , 12:38 PM.
import logging



### VERY BASIC EXAMPLE      #######
#
# logging.basicConfig(format='%(asctime)s, %(levelname)s :    %(message)s', filename='logging_messages.log',
#                     datefmt='%Y-%m-%d %H:%M:%S' )
# logging.warning('-------------------')
# logging.warning('An example message.')
# logging.warning('Another message')


#####       MORE DETAILED EXAMPLE       ########


# create FORMATER
datefmt='%Y-%m-%d %H:%M:%S'
# format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
format = '%(asctime)s - %(levelname)s - %(message)s'
log_filename='logging_messages.log'
formatter = logging.Formatter(format, datefmt=datefmt )
level = [ 'INFO' , 'DEBUG' , 'WARNING', 'ERROR', 'CRITICAL'  ]

# logging.basicConfig(format='%(asctime)s, %(levelname)s :    %(message)s', filename=log_filename, datefmt=datefmt )
logging.basicConfig(format='%(asctime)s, %(levelname)s :    %(message)s', filename=log_filename, datefmt=datefmt )


# create LOGGER FILE
logger = logging.getLogger('simple example')
logger.setLevel(logging.DEBUG)

### create CONSOLE HANDLER      ###
console = logging.StreamHandler()
console.setLevel(logging.DEBUG )

# add formatter to Console Handler
console.setFormatter(formatter)

# add Console Handler to logger
logger.addHandler(console)


#### 'application' code
logger.critical('--------- ALERT ----------')
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message' )
logger.error('error message')
logger.critical('critical message')



###############################