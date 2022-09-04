# Python allows you to catch specific types of errors, but what if you want to be able to catch any type
# of error in an `except` block for debugging and logging purposes? Catching any type of error requires a 
# bit more work. This module can be used to catch any type of error in a plain `except` block. For example:

"""
import logging
from utils.log_error import log_error

@app.get("/api/get-todos")
async def get_todos(request: Request):
    try:
        response = { "todos": ["Eat", "Sleep", "Debug Code"] }
        return response
    except:
        logging.error(log_error())
"""

# NOTES:
# * The ideas used for formatting errors were found here: https://pythonprogramming.net/headless-error-handling-intermediate-python-tutorial/
# * How to get the full file path where a function was called: https://stackoverflow.com/a/34367572/9453009
# * You can catch all errors and error messages with `sys.exc_info()`.
# * If you want to catch a specific type of error, then you should catch that error like you normally
# would in Python instead of using this module to catch that specific type of error. For example,
# you should do this:

"""
except TypeError:
    logging.error("This is a message for a TypeError exception.")
"""


import os, sys

def log_error():
    """Formats an error object (no matter what error type) into a formatted string."""
    return f"""
    FILE PATH: {os.path.realpath(sys.argv[0])}
    LINE NUMBER: {sys.exc_info()[2].tb_lineno}
    ERROR TYPE: {sys.exc_info()[0]}
    ERROR MESSAGE: {sys.exc_info()[1]}"""
