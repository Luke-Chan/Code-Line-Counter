import os

Path = r"D:\Data"
Format = ['py','java','cpp','c','h','php','v','js','css']

def CrawlPath(path):
    path_list = []
    for root, sub, files in os.walk(path):
        for file in files:
            filepath = root + "\\" + file
            path_list.append(filepath)
    return path_list

# count line of a file
def CountLine(path):
    count = 0
    try:
        fileformat = path.split(".").pop()
        if fileformat in Format:
            file = open(path, 'rb')
            file_line = file.readlines()
            """
            for lines in file_line:
                line = lines.replace(b' ',b'').replace(b'\n',b'')
                if (line != b''):
                    count += 1
            """
            count = len(file_line)
            file.close()
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
    
    for file in files:
        count += CountLine(file)

    print('\nAll the Code in "' + Path + '" have ' + str(count) + ' Lines\n')

