
import os
import time

def bulk_file_rename(path):

    dir_tree = path.split('\\')    


    os.chdir(path)

    file_list = os.listdir()
    if len(file_list) == 0:
        return 'The Directory is Empty!!'


    new_name = input('Enter the New File Name: ').strip()


    length = len(str(len(file_list)))
    j = 1

    for i in file_list:

        if os.path.isdir(i):
            os.rename(i, (new_name + '_') + str(j).rjust(length, '0'))


        elif os.path.isfile(i):

            extension = '.' + i.split('.')[-1]
            os.rename(i, (new_name + '_') + str(j).rjust(length, '0') + extension)

        j += 1
    
    
    choice = input('\nUNDO Renaming ? (Y/N): ')

    if choice in ('y', 'Y'):
        file_list_new = os.listdir()
        
        for i in range(len(file_list_new)):
            os.rename(file_list_new[i], file_list[i])
        
        return '***************** UNDO Completed. *****************'

    return '***************** File Renaming Completed. *****************'
    


path = input('Enter Path: ').strip()

print(bulk_file_rename(path))


