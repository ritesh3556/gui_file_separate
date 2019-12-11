import os, shutil 

# Note : You can write every single extensions inside tuples

#audio_extensions = ('.mp3','.m4a','.wav','.flac')
#videos_extensions = ('.mp4','MP4','.mkv','.MKV','.flv','.mpeg') 
#documents_extensions = ('.doc','.pdf','.txt')


# main logic 
# first you know path so we take input from user folder path

dict_extensions = {
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
    'videos_extensions' : ('.mp4','MP4','.mkv','.MKV','.flv','.mpeg'), 
    'documents_extensions' : ('.doc','.pdf','.txt'),
}

folderpath = input('enter folder path : ')
# then we find differnt files

def file_finder(folder_path,folder_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in folder_extensions:
            if file.endswith(extension):
                files.append(file)
    return files            


#print(file_finder(folderpath,audio_extensions))
#os.mkdir(file_finder(folderpath,audio_extensions))                

for extension_type, extension_tuple in dict_extensions.items():
    #print('calling file finder ')
    #print(file_finder(folderpath,extension_tuple))
    folder_name = extension_type.split('_')[0] + ' files'
    folder_path = os.path.join(folderpath,folder_name)
    print(folder_path)
    os.mkdir(folder_path)
    for item in (file_finder(folderpath,extension_tuple)):
        item_path = os.path.join(folderpath,item)
        print(item_path)
        item_new_path = os.path.join(folder_path,item)
        print(item_new_path)
        shutil.move(item_path,item_new_path)



