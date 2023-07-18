import filecmp
import os
# from pathlib import Path
import time

dir = 'D:\myWork/4th year-myWork/graduated project/Project development/model/code/remove the duplicated data/RemoveDupliDataProject/data'
files_list=os.listdir(dir)
print(files_list)



for pics in files_list:
    if pics != 'img_name.png':
        targetDir = os.path.join( dir,pics)
        print(targetDir)
        if filecmp.cmp("img_name.png",targetDir):
            os.remove(os.path.join(dir,pics))
            print("similar")
        else:
            print("non similar")

#---------------------------------------------------------------------------------------------------------------------------------------------
#
# import filecmp
# import os
# # from pathlib import Path
# import time
#
# dir = 'D:\myWork/4th year-myWork/graduated project/Project development/model/code/remove the duplicated data/RemoveDupliDataProject/data'
#
# # print(files_list)
#
# #to enter in each folder in dir --> file1 , file2
# for category in os.listdir(dir):
#     print(category)
#     #set files_list value which is photos names
#     files_list = os.listdir(os.path.join(dir,category))
#     # print(files_list)
#     #make for loop to access the first photo to compare it with all photos in folder then second photo and third .....
#     for main_photo in files_list:
#         #make for loop to acces each photo in the folder and compare it with main photo
#         for photo in files_list:
#             if photo != main_photo :
#                 TargetComparDir = os.path.join(dir,category)
#                 TargetComparDirPhto = os.path.join(TargetComparDir,photo)
#                 print(TargetComparDirPhto)
#                 print(main_photo)
#                 print(photo)
#                 if filecmp.cmp(main_photo, TargetComparDirPhto):
#                     os.remove(os.path.join(dir,photo))
#                     print("similar")
#                 else:
#                     print("non similar")
#

#----------------------------------------------------------------------------------------
# import filecmp
# import os
# # from pathlib import Path
# import time
#
# dir = 'D:\myWork/4th year-myWork/graduated project/Project development/model/code/remove the duplicated data/RemoveDupliDataProject/data'
#
# # print(files_list)
#
# #to enter in each folder in dir --> file1 , file2
# files_list = os.listdir(os.path.join(dir))
#     #make for loop to access the first photo to compare it with all photos in folder then second photo and third .....
# for main_photo in files_list:
#     #make for loop to acces each photo in the folder and compare it with main photo
#     for photo in files_list:
#         if photo != main_photo :
#             TargetComparDir = os.path.join(dir)
#             TargetComparDirPhto = os.path.join(TargetComparDir,photo)
#             print(TargetComparDirPhto)
#             print(main_photo)
#             print(photo)
#             if filecmp.cmp(main_photo, TargetComparDirPhto):
#                 os.remove(os.path.join(dir,photo))
#                 print("similar")
#             else:
#                 print("non similar")
#
