import logging

# Create global log file on application startup
# TODO: color logs, set debug logging level as CLI arg --debug
logging.basicConfig(filename='../logs/pyeneo.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d | %(name)s | %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
