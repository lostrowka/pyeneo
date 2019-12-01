import logging

# Create global log file on application startup
# TODO: color logs, set debug logging level as CLI arg --debug
logging.basicConfig(filename='../logs/pyeneo.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)3d | %(name)-22s | %(levelname)-7s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
