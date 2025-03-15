import logging

class logger_class:
    @staticmethod
    def log_gen_method():
        # log_file = logging.FileHandler(".\\Logs\\bankapp.log") # log file
        log_file = logging.FileHandler("G:\\CREDENCE\\CT-REVISION DEC 2024\\BANK_APP_PROJECT\\Logs\\bankapp.log")
        #G:\CREDENCE\CT-REVISION DEC 2024\BANK_APP_PROJECT\Logs
        log_format = logging.Formatter("%(asctime)s : %(levelname)s :%(funcName)s:  %(message)s") # log format
        log_file.setFormatter(log_format) # log file --> set format
        logger = logging.getLogger()
        logger.addHandler(log_file) # log addhandler --> every time add the log
        logger.setLevel(logging.INFO) # set log level
        return logger
