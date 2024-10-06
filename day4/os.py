import os

my_path = "c:/"
folderContents = os.listdir(my_path)

print(folderContents)

my_path = "C:/"
def findSubDirs (directory) : 
sub_dir = []
for root, dir , files in os.walk(my_path):
 for dir_name in dir :
     sub_dir.append(os.path.join(root, dir_name))
     
 print(sub_dir)    
