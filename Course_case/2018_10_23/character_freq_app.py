import sys
from character_freq import CharFreq

def main():
    file_name = sys.argv[1]

    char_freq = CharFreq()

    try:
        f = open(file_name)
    except:
        print("Can't open", file_name)
        return
    for line in f:
        char_freq.count_line(line)
            
    
    print(char_freq.char_count)

main()