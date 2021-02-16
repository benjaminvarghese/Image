import shutil, os
from PIL import Image, ImageStat

image_folder = r'/Users/###########################' #primary folder containing all images.

image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]

images_location = image_folder
dup_location = '/Users/DDDDDDDDD' #folder name to move duplicate images into.
sloc = '/Users/IIIIIIIIIIIIIII' #folder name to move unique images into.

duplicate_files = []

count = 0
print(len(image_files))

while len(image_files) != 0:
    for file_org in image_files:
        try:
            count = count + 1
            print(f"\n {count}. FILE in obs : ",file_org)
            image_org = Image.open(os.path.join(image_folder, file_org))
            pix_mean1 = ImageStat.Stat(image_org).mean 

            for file_check in image_files:
                if file_check != file_org:
                    image_check = Image.open(os.path.join(image_folder, file_check))
                    pix_mean2 = ImageStat.Stat(image_check).mean 

                    if pix_mean1 == pix_mean2:
                        print("\n DUPLICATE FILE of ",file_org," found : ",file_check)
                        shutil.move(images_location+'/'+file_check, dup_location)
                        image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]
            print(f"\n {count}. \t Moving FILE in obs : ",file_org)
            shutil.move(images_location+'/'+file_org, sloc)
            image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]
        except(FileNotFoundError, IOError):
            image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpg')]

print(f"\n******{count}******\n")