import logging
log_filename = 'log.txt'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename,encoding='utf-8'),
        logging.StreamHandler(),
    ]
)
