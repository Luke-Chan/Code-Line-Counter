import os

Path = r"D:\Data"
Language = ['py','java','cpp','c','h','php','v','js','css']

def CrawlPath(path):
    path_list = []
    for root, sub, files in os.walk(path):
        for code in files:
            filepath = root + "\\" + code
            path_list.append(filepath)
    return path_list

# count line of a file
def CountLine(path):
    count = 0
    try:
        fileformat = path.split(".").pop()
        if fileformat in Language:
            code = open(path, 'rb')
            file_line = code.readlines()
            # """
            for lines in file_line:
                line = lines.replace(b' ',b'').replace(b'\n',b'')
                line = line.replace(b'\r',b'').replace(b'\t',b'')
                if (line != b''):
                    count += 1
            # """
            
            #if count blank lines:
            #count = len(file_line) 
            
            code.close()
            print('"' + path + '" --- ' + str(count) + " lines")
            return count
        else:
            return 0
    except Exception as e:
        print(e)
        return 0


if __name__ == '__main__':
    
    files = CrawlPath(Path)
    count = 0
    
    for code in files:
        count += CountLine(code)

    print('\nCode in "' + Path + '" --- ' + str(count) + ' Lines\n')
