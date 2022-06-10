i = 1
while i < 4:
    print(i)
    i+=1
else:
    print("I am Morpheus")

red_pill = {'Name': 'Devon', 'Sex': 'Male', 'Linux': 'Bad Ass' }

print(red_pill['Linux'])

damn_list = [38, "buddha", 'true', 7]

print(damn_list[0])

user = "Linux Master Race"

passphrase = input('Please enter user name')

if user == "Linux Master Race":
    print("You chose the Red Pill, it's gonna be a bumpy ride")
elif user != "Linux Master Race":
    print("You've chosen the Blue Pill, Stay proprietary and blinded")

password = "I use arch btw"


passphrase = input('What is the super secret arch linux password')


if password == "I use arch btw":
    print("See Install Guide")
elif password != "I use arch btw":
    print("Please exit stage left")

print("Install Arch Linux, the Arch Way!!") # for a uefi install

print("Go to www.archlinux.org and download the latest iso")

print("Format your flash drive with arch iso and then insert into your computer and boot from it")

print("Now that we're at the command prompt, here we go!!")

print("timedatectl set-ntp true") # to ensure the system clock is correct

print("ping -c3 archlinux.org") # making sure you have internet connection

print("lsblk") # shows you all the drives on your system so that you can choose where to install

print("fdisk /dev/sda.... or fdisk /dev/nvme.... to delete current partitions and create new ones") # allows for deleting and creating partitions

print("mkfs.fat -F32 /dev/sda or /dev/nvme and make your partition +512M") # format boot partition making it 512MB

print("mkswap /dev/sda... or /dev/nvme... make your swap partition 1.5 times your ram or make a swap file") # mkswap to create a swap partition or make a swap file manually

print("mkfs.ext4 /dev/sda.... or /dev/nvme... and make your root partition anywhere between 25 - 50GB depending on how many or types of programs you plan on installing") # creating root partition where arch and all your programs will be installeld

print("mkfs.ext4 /dev/sda.... or /dev/nvme... and make your home partition the remainder of the drive") # your root partition ends up being the rest of the drive

print("pacstrap -i /mnt base base-devel linux-zen linux-zen-headers linux-lts linux-lts-headers linux-firmware git man sudo openssh iwd vim nano") # installs all the base packages that you will need for your arch install and alot of the stuff you will need later on

print("genfstab -U -p /mnt >> /mnt/etc/fstab creates your fstab and changes the indentifier to the drive uuid instead of the /dev/sda or /dev/nvme which can change") # creates the fstab and changed your identifier to the drives UUID

print("arch-chroot /mnt /bin/bash") # changing from the jump drive that the iso is on to the root partition of the new arch install

print("vim /etc/locale.gen select your system language output") # very essential

print("locale-gen will generate your system language output") # will generate data from options selected with previous command

print("echo LANG=en_US.UTF-8 > /etc/locale.conf") #  pushing the correct language to locale.conf that will be used for the entire system.

print("export LANG=en_US.UTF-8") # enables you to display unicode correctly on your system

print("ln -sf /usr/share/zoneinfo/America/Phoenix /etc/localtime") # this command will enable you to have the correct time set and displayed

print ("hwclock --systohc --utc") # this command allows to sync the systems internal clock with UTC (Coordinated Universal Time)

print("passwd") # this commands allow you to set a root passwd

print("vim /etc/pacman.conf") # this command will allow you to edit this file and set parallel downloads to 7 which will in turn make package downloads much much faster and more reliable

print("vim /etc/hostname choose the name of the name of your system and how it will appear on the network") # you get to name the one thing that you'll probably spend as much time if not more than with your significant other

print("vim /etc/hosts and then enter 127.0.0.1 localhost  ::1 localhost 127.0.1.1 localhost.localdomain  nameofcomputer") # setting your system hosts

print("pacman -S networkmanager polkit to install what you need to be able to get online") # gotta have internet access and the ability to run system functions without typing sudo all the time, I'm just sayin

print("systemctl enable NetworkManager") # will create symlinks and enable the NetworkManager and Internet access on boot

print("pacman -S grub efibootmgr") # installs the grub bootloader and the efibootmgr that is essential for a uefi system and without the system won't boot

print("mkdir /boot/efi") # will create your boot directory for the grub and the efibootmgr

print("grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB") # installing grub to the proper directory

print("grub-mkconfig -o /boot/grub/grub.cfg") # will generate the grub config file

print("useradd -m -G wheel -s /bin/bash $USER") # this command allows you to set a regular user and adding them to the group wheel as operating as root is never a good practice

print("passwd $USER") # this command allows you to set a passwd for the $USER account

print("EDITOR=vim visudo") # this command will allow you to uncomment the comment that will allow all members of the group wheel to execute any command

print("exit") # will allows you to exit the chroot and return you to the install media

print("umount -R /mnt") # will allow you to unmount all the partitions so you can reboot safely without damaging the install

print("reboot") # will reboot the system

print("You know have a fresh base Arch Linux install, what you do from here is up too you!!!!!") # you now have completed install the Arch Way and have a fresh Arch Linux base install!!!
