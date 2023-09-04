from sys import argv
import os 
import hashlib
import time

def Directory_Checksum(Dir_Path):

    Files_CheckSum = []
    for Folder_Name, SubFolders, Files in os.walk(Dir_Path):


            for File_Name in Files:
                FilePath = os.path.join(Folder_Name,File_Name)
                fd = open(FilePath,'rb')
                Data = fd.read()
                CheckSum =FilePath+" "+hashlib.md5(Data).hexdigest()
                Files_CheckSum.append(CheckSum)

    return Files_CheckSum

def Display_DuplicateFile(Checksum_List,):

    fd = open("Log1.txt",'a')
    list = Checksum_List

    for no1 in range(0,len(list)):
        FC = list[no1].split(' ')
        if(no1 < len(list)-1):
            for no2 in range(no1+1,len(list)):
                CS = list[no2].split(' ')
                if( FC[1]==CS[1]):
                    fd.write(FC[0]+" & "+CS[0]+" has Same Content "+"\n")

def main():

    print()
    print("Marvellous Directory CheckSum Script")

    if(len(argv) != 2):
        print("Please Give Valid Input Arguments")

    if(argv[1]=='-h' or argv[1]=='-H' ):
        print("This Application is used get Duplicate Files from given folder. ")

    if(argv[1]=='-u' or argv[1]=='-U' ):
        print("Usage : <Applicaion_Name> <Abs_Path_of_Directory>")
    
    Checksum_List = Directory_Checksum(argv[1])
    Display_DuplicateFile(Checksum_List)

if __name__=="__main__":
    main()
  