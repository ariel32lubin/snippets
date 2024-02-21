import threading
import time
import schedule
from utils import run_notebook  # Assuming run_notebook is defined in utils

def run_threaded(job_func, *args, **kwargs):
    job_thread = threading.Thread(target=job_func, args=args, kwargs=kwargs)
    job_thread.start()

# Schedule get auths notebook every day at 8 pm 
schedule.every().day.at("20:00").do(run_threaded, run_notebook, notebook_path="scripts/00_get_auths.ipynb")

# Schedule push daily update notebook every day at 8:30 pm
schedule.every().day.at("20:30").do(run_threaded, run_notebook, notebook_path="scripts/01_push_daily_update.ipynb")

# Run get auths notebook right now in a separate thread
run_threaded(run_notebook, notebook_path="01_push_daily_update.ipynb")

while True:
    schedule.run_pending()
    time.sleep(1)
