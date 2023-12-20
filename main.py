if __name__ == "__main__":    
    try:
        main()
    except Exception as e:
        error_message = str(e)
        SCRIPT_PATH = os.path.abspath(__file__)
        SCRIPT_NAME = os.path.basename(SCRIPT_PATH)
        send_error_email(SCRIPT_NAME, error_message)
