import sys # sys is used for getting detailed information about the exception


def error_message_detail(error,error_detail:sys):  #generates custom error message
    _,_,exc_tb=error_detail.exc_info()  #the error_detail.exc_info() will give 3 info we are only interested in 3 one so we put _,_,for the first 2

    file_name=exc_tb.tb_frame.f_code.co_filename #this will give the filename in which error has occured

    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message



class CustomException(Exception):  #this class inherits python exceptions and more to it
    def __init__(self,error_message,error_detail:sys):
        
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):  #makes the error printable
        return self.error_message
    


# error_message => The original error (e.g., "division by zero")
# self.error_message => The full message with filename, line number, and the original error