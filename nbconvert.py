import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# function to run notebook as py
def run_notebook(notebook_path):
    with open(notebook_path) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
        
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    nb_out = ep.preprocess(nb_in)
