import zipfile


def unzip_dataset(zipped_location, extraction_destination):
    with zipfile.ZipFile(zipped_location, 'r') as zip_ref:
        zip_ref.extractall(extraction_destination)
