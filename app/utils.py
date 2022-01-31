import pendulum
import logging 

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
file_handler = logging.FileHandler(filename='logs/app.log', mode='a', encoding='utf-8')
logger.addHandler(file_handler)

def getDateTime():
    timeNow = pendulum.now()
    logger.info(timeNow)
    print(timeNow)