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
