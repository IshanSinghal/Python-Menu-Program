#!/usr/bin/python3

import os
print("Welcome to Menu Program")
loc = input("\nDo you wish to run commands locally or remote?\n")

print("\nGreat!")
while(True):
    print("""Here are your options:
        ----------------------
        
        PRESS 0 TO EXIT

        COMMON COMMANDS
        ---------------
        S1. Date
        S2. Calender
        S3. NIC

        CONFIGURATIONS
        -------------
        C1. Configure yum
        C2. Configure Webserver
        C3. Configure Docker

        ADDITIONAL STORAGE /  DRIVES
        ----------
        M1. Create Static Partition
        M2. Delete Static Partition
        M3. Format partition
        M4. Mount to folder
        M5. Unmount from folder
        M5. Create LVM

        DOCKER
        ------
        D1. Run container
        D2. Stop container
        D3. Restart container and get shell access
        D4. Delete container
        D5. Show running containers
        D6. Show stopped containers
        
        HADOOP
        ------
        H1. Configure Client
        H2. Configure NameNode
        H3. Configure DataNode
        H4. 
        """)

    choice = input("Enter your option: ")
    if(choice == "0"):
        exit()
    elif(choice == "C1"):
        os.system("cp ishan.repo /etc/yum.repos.d/")
        os.system("yum repolist")
    elif(choice == "C2"):
        os.system("yum install httpd -y")
        os.system("systemctl start httpd")
        os.system("systemctl enable httpd")
        os.system("ifconfig enp0s3")
        print("Put your files in /var/www/html/ and open browser to system IP")
    elif(choice == "C3"):
        os.system("cp docker.repo /etc/yum.repos.d/")
        os.system("yum install docker-ce --nobest -y")
        os.system("systemctl start docker")
        os.system("systemctl enable docker")
    elif(choice == "M1"):
        os.system("fdisk -l")
        diskname = input("Check your drive name and input: ")
        os.system("""echo -e "n\np\n1\n\n\nw\n" | fdisk {}""".format(diskname))
    elif(choice=="M2"):
        diskname = input("Input disk name: ")
        os.system("""echo -e "d\nw\n" | fdisk {}""".format(diskname))
    elif(choice == "M3"):
        pname = input("Enter partition name: ")
        os.system("mkfs.ext4 {}".format(pname))
    elif(choice == "M4"):
        os.system("fdisk -l")
        pname = input("Enter partition name: ")
        fname = input("Enter folder name: ")
        os.system("mount {} {}".format(pname,fname))
    elif(choice == "M5"):
        name = input("Enter folder location/name :")
        os.system("umount {}".format(name))
    elif(choice == "M6"):
        pass
    elif(choice == "D1"):
        name = input("Enter name: ")
        image = input("Enter OS: ")
        os.system("docker run -it --name {} {}".format(name,image))
    elif(choice == "D2"):
        name = input("Enter container name: ")
        os.system("docker stop {}".format(name))
    elif(choice == "D3"):
        name = input("Enter container name: ")
        os.system("docker start {}".format(name))
        os.system("docker attach {}".format(name))
    elif(choice == "D4"):
        name = input("Enter container name :")
        os.system("docker rm -f {}".format(name))
    elif(choice == "D5"):
        os.system("docker ps")
    elif(choice == "D6"):
        os.system("docker ps -a")
    else:
        print("Incorrect Option")
