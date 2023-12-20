def log_function(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that logs the function name, arguments, and execution time.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.

    Example:
        @log_execution_time
        def some_function(a: int, b: int) -> int:
            time.sleep(2)  # Simulate some time-consuming operation
            return a + b
    """
    def wrapper(*args: Tuple[Any, ...], **kwargs: Union[str, Any]) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        # Log function name, arguments, and execution time
        if 'url' in kwargs:
            url_argument = kwargs['url']
            url_argument_msg = f" URL Argument: {url_argument},"
        else:
            url_argument = None
            url_argument_msg = ""

        log_msg = f"Function: {func.__name__},{url_argument_msg} Execution Time: {execution_time} seconds"
        logging.info(log_msg)

        return result

    return wrapper

def send_error_email(script_name: str, error_message: str) -> None:
    """
    Send an error email using Microsoft Outlook.

    Args:
        script_name (str): The name of the script where the error occurred.
        error_message (str): The error message to include in the email.

    Returns:
        None

    Example:
        script_name = "YourScriptName.py"
        error_message = "An error occurred in the script."
        send_error_email(script_name, error_message)
    """
    import win32com.client as win32

    # Create an Outlook application instance
    outlook = win32.Dispatch('Outlook.Application')

    # Create a new email
    mail = outlook.CreateItem(0)

    # Set email properties
    mail.To = 'alubin@fiducient.com'
    mail.Subject = f'Error in {script_name}'
    mail.Body = f'There was an error in {script_name}:\n\n{error_message}'

    # Send the email
    mail.Send()
