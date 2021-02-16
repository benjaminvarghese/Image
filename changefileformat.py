import shutil, os
from PIL import Image

image_folder = r'/Users/PRIMARY_FOLDER' #source?primary folder containing all images
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')] #change format to JPG | PNG wrt requirement

count = 0

for file_org in image_files:
    count = count + 1
    name = image_folder+'/'+file_org
    Ima = Image.open(name)
    file = str(name).split('/')
    file = file[-1].split('.')
    Ima = Ima.convert('RGB')
    Ima.save(r'/Users/SAVE_TO_FOLDER_PATH/'+file[0]+'.jpg') #path to which images with extention changes have to be saved into
    print(name)

print("COUNT ",count)