import kagglehub

def file_download():
    path = kagglehub.dataset_download("../data/rohitsahoo/sales-forecasting")

    print("Path to dataset files:", path)