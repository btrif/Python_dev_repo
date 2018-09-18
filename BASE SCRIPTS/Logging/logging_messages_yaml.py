#this is app.py
import logging.config
import yaml
from os import path

def init_logging(config_file ):
    if path.exists(config_file):
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f.read())
            return config
    else : print('Not a valid file or the file does not exist !')


config = init_logging( config_file= 'logging.yaml' )
logging.config.dictConfig(config['logging'])


def main():
    logger = logging.getLogger('bogdanels app')
    print('--------------------')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message' )
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()




