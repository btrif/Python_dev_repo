#  Created by Bogdan Trif on 12-04-2018 , 12:18 PM.
import os

folder = 'D:/_temp'

def list_directory(folder, level):      # Made by Bogdan Trif @ 12-04-2018 , 12:18 PM
    L = os.listdir(folder)
    for cnt, i in  enumerate(L) :
        if os.path.isdir(folder+'/'+i) :
            print(' '*level+'-'*level+'[' + '/'+ i +']' )
#             print(' '*level+'-'*level+'['+folder + '/'+ i +']' )
            list_directory(folder+'/'+ i, level+1)
        else :
            print(' '*level+'-'*level+' '+i )
#     return  os.listdir(folder)

list_directory(folder, 0)


def disk_usage(path):
    '''Return the number of bytes used by a file/folder and any descendents.'''
    total = os.path.getsize(path) # account for direct usage
    if os.path.isdir(path): # if this is a directory,
        for filename in os.listdir(path): # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath) # add child’s usage to total

            print ( '{0:<7}'.format(total), path) # descriptive output (optional)
    return total

disk_usage(folder)

