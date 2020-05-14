import os
import sys

def main():
    dir = sys.argv[1]
    for filename in os.listdir(dir):
        os.system("afplay %s"%dir+'/'+filename)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()

