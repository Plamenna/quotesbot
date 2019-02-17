# -*- coding: utf-8 -*-

class Dealing_with_Files():
    
    def open_file(self,name_of_file,info): 
        file_object  = open(name_of_file, "w+")
        file_object.write(info)
        file_object.close()
        return file_object



        
