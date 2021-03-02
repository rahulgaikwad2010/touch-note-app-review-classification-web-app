import logging
import os
import stat
import time

from .LoggerError import LoggerError


class Logger:
    def __init__(self, pobj_logger_dir_path='./log/'):
        try:

            mode = 0o777 | stat.S_IRUSR
            if not os.path.exists(pobj_logger_dir_path):
                os.makedirs(pobj_logger_dir_path, mode=0o777)

            # to create daily log files
            current_date = time.strftime("%Y_%m_%d")
            pobj_logger_file_path = pobj_logger_dir_path + "/log_file_" + current_date + ".log"

            if not os.path.exists(pobj_logger_file_path):
                with open(pobj_logger_file_path, 'a') as fp:
                    pass

            self.logger = logging.getLogger("info_logging")
            self.lobj_hdlr = logging.FileHandler(pobj_logger_file_path)
            self.lobj_formatter = logging.Formatter(
                '\n%(asctime)s \n%(levelname)s \n%(filename)s \nMethod name:%(funcName)s \n%(message)s')
            self.lobj_hdlr.setFormatter(self.lobj_formatter)
            self.logger.addHandler(self.lobj_hdlr)
            self.logger.setLevel(logging.DEBUG)
        except:
            raise LoggerError("ERROR PYTHON LOGGER - APPLICATION")


class AuditLogger:

    def __init__(self, pobj_logger_dir_path='./audit_log/'):
        try:
            mode = 0o777 | stat.S_IRUSR
            if not os.path.exists(pobj_logger_dir_path):
                os.makedirs(pobj_logger_dir_path, mode=0o777)

            # to create monthly folder
            current_month = time.strftime("%b_%Y")
            mode = 0o777 | stat.S_IRUSR
            if not os.path.exists(pobj_logger_dir_path + "/" + current_month):
                os.makedirs(pobj_logger_dir_path + "/" + current_month, mode=0o777)

            # to create monthly log files
            current_month_year = time.strftime("%b_%Y")
            pobj_audit_logger_monthly_file_path = pobj_logger_dir_path + "/" + current_month + "/" + current_month_year + ".csv"

            if not os.path.exists(pobj_audit_logger_monthly_file_path):
                with open(pobj_audit_logger_monthly_file_path, 'a') as fp:
                    pass

            self.monthly_audit_logger = logging.getLogger("monthly_audit_logging")
            self.lobj_hdlr = logging.FileHandler(pobj_audit_logger_monthly_file_path)
            self.lobj_formatter = logging.Formatter('%(asctime)s,%(message)s')

            self.lobj_hdlr.setFormatter(self.lobj_formatter)
            self.monthly_audit_logger.addHandler(self.lobj_hdlr)
            self.monthly_audit_logger.setLevel(logging.DEBUG)
        except:
            raise LoggerError("ERROR PYTHON LOGGER - AUDIT")
