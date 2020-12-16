import logging



class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:   # these two steps of handler is important for logging inside directory patha as without this , it doesn't work
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
