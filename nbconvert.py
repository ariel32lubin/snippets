def run_notebook(notebook_path):
    # log starting 
    print(f"Running notebook {notebook_path}")
    with open(notebook_path) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
        
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    nb_out, resources = ep.preprocess(nb_in)  # Unpack the tuple to get the notebook object and resources

    # Save output notebook
    with open(notebook_path, mode="wt") as ff:
        nbformat.write(nb_out, ff)
    # log completion
    print(f"Notebook {notebook_path} ran successfully")
