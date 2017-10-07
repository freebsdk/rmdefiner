import os
import re
import sys
import codecs

src_file = ""
dst_file = ""





def read_params():
    if len(sys.argv) != 2+1:
        print('$rmdefiner <source_file_name> <destination_file_name>')
        sys.exit(-1)
    else:
        global src_file, dst_file
        src_file = sys.argv[1]
        dst_file = sys.argv[2]




def process():

    if os.path.exists(src_file) == False:
        print('[!] Could not found the source file. : '+src_file)
        return -1

    p = re.compile('DEFINER=`(.*?)`@`(.*?)`', re.UNICODE)

    try:
        src_fp = codecs.open(src_file, 'r','utf-8')
        dst_fp = codecs.open(dst_file, 'w','utf-8')
    except IOError as ex:
        print('[!] Exception has occurred. : '+ex.strerror)
        sys.exit(-1)

    while True:
        line = src_fp.readline()
        if not line: break
        
        # for debugging
        # t = p.search(line)
        # if t != None :
        #    print(t)

        mod_line = p.sub("",line)
        dst_fp.write(mod_line)

    src_fp.close()
    dst_fp.close()
    




def main():
    read_params()
    process()




main()