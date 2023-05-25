print('this is image to pdf program')

import os
from PIL import Image 

output_dir = './PDFs'
input_dir = './imgs'

def ret_and_remove_file(d, file_name):
    for f in os.listdir(d):
        print(" the ", f)
        if f == file_name:
            os.remove(file_name)

def ret_file(pt, name):
    files = os.listdir(pt)
    for f in files:
        if f == name:
            print("file name is", type(f))
            return open(os.path.join(pt, f), 'r')
        
for file in os.listdir(input_dir):
    if file.split(".")[-1] in ('jpg'):
        image = Image.open(os.path.join(input_dir,file))
        image_converted = image.convert('RGB')
        # print(image_converted.save(f'{file.split(".")[-2]}.pdf'))
        o_d = os.path.join(output_dir)
        name = f'{file.split(".")[-2]}.pdf'
        image_converted.save(os.path.join(output_dir, f'{file.split(".")[-2]}.pdf'))
        # ret_and_remove_file(o_d ,name)
        r_f = ret_file(o_d, name)
        for line in r_f:
            print(line)



# for file in os.listdir(output_dir):
#     if file:
#         print(type(file))


