from sys import argv
import os 
import hashlib

def Directory_Checksum(Dir_Path):

    for Folder_Name, SubFolders, Files in os.walk(Dir_Path):
        
            for File_Name in Files:
                FilePath = os.path.join(Folder_Name,File_Name)
                fd = open(FilePath,'rb')
                Data = fd.read()
                CheckSum = hashlib.md5(Data).hexdigest()
                print(File_Name," : ",CheckSum)

def main():

    print()
    print("Marvellous Directory CheckSum Script")

    if(len(argv) != 2):
        print("Please Give Valid Input Arguments")

    if(argv[1]=='-h' or argv[1]=='-H' ):
        print("This Application is used display checksum of files from given folder. ")

    if(argv[1]=='-u' or argv[1]=='-U' ):
        print("Usage : <Applicaion_Name> <Abs_Path_of_Directory>")
    
    Directory_Checksum(argv[1])

if __name__=="__main__":
    main()    