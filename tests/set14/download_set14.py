import zipfile
import urllib

path_set14 = r"https://github.com/titu1994/Super-Resolution-using-Generative-Adversarial-Networks/releases/download/v0.1/Set14.zip"

print("Downloading Set14 images")
filehandler, _ = urllib.urlretrieve(path_set14)

zip_file = zipfile.ZipFile(filehandler)

print("Extracting images")
zip_file.extractall()