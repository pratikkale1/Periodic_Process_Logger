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

def Remove_DuplicateFile(Checksum_List,):

    fd = open("Log.txt",'a')
    list = Checksum_List
    # for x in list:
    #     print(x)
    for no1 in range(0,len(list)):
        FC = list[no1].split(' ')
        if(no1 < len(list)-1):
            for no2 in range(no1+1,len(list)):
                CS = list[no2].split(' ')
                #print(FC[0]+"=="+CS[0])
                if( FC[1]==CS[1]):
                    if os.path.exists(CS[0]):
                        os.remove(CS[0])
                        fd.write(CS[0]+" Deleted at "+time.ctime()+'\n')
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
    Remove_DuplicateFile(Checksum_List)

if __name__=="__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)    