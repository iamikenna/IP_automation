import os

def txt_reader():
    dict_good = dict()
    dict_bad = dict()
    
    try:
        user_input = input("Enter a file\n")
        file_new = open(user_input, "r")
    except FileNotFoundError:
        print(f"This file can not be found or opened: {user_input}")
    else:
        with file_new:
            for line in file_new: 
                line = line.strip() # removing white spaces
                data_list = line.split()
                response = os.system("ping -c 1 " + data_list[1])
                #and then check the response...
                if response == 0:
                    dict_good[data_list[0]] = [data_list[1], "True"]
                    print( f" {data_list[0]} with ip of {data_list[1]} is up!")
                else:
                    dict_bad[data_list[0]] = [data_list[1], "False"]
                    print( f" {data_list[0]} with ip of {data_list[1]} is down!")
            print(dict_good)
            print(dict_bad)

  
txt_reader()          
            
# os.system("clear")
#ip_text.txt 
