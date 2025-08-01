import os
import sys

def error_message_detail(error, sys_module: sys):
    _, _, exc_tb = sys_module.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}]: {str(error)}"
    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(str(error_message))
        self.original_message = str(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
