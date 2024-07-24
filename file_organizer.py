# 4.4 - Basic Files Operation Script - Jon Tokarz - July 24, 2024
import os

def main():
    try:
# Use the os.mkdir to create a MyFiles folder
        os.mkdir('MyFiles')

# Use os.mdir to create subdirectories Docs, Images, and Videos
        os.mkdir('MyFiles/Docs')
        os.mkdir('MyFiles/Images')
    finally:
        os.mkdir('MyFiles/Videos')


main()
    
    



    # 4.4 - Basic Files Operation Script - Jon Tokarz - July 24, 2024