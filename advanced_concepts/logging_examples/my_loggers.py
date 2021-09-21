import logging


def get_laptop_loogers():
    lap_logger = logging.getLogger(__name__)
    lap_logger.setLevel(level=10)
    lap_formatter = logging.Formatter(
        "%(asctime)s -> %(message)s ->at line no %(lineno)d in %(funcName)s, file=%(filename)s")
    lap_filehandler = logging.FileHandler("lap.log")
    lap_filehandler.setFormatter(lap_formatter)
    lap_logger.addHandler(lap_filehandler)
    return lap_logger

def get_emp_logger():
    emp_logger = logging.getLogger(__name__)

    emp_logger.setLevel(level=20)

    emp_formatter = logging.Formatter(
        "%(asctime)s -> %(message)s ->at line no %(lineno)d in %(funcName)s, file=%(filename)s")
    emp_filehandler = logging.FileHandler("emp.log")

    emp_filehandler.setFormatter(emp_formatter)

    emp_logger.addHandler(emp_filehandler)
    return emp_logger
