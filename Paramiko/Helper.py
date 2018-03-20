# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import os,sys,commands,re,random,time

class Helper(object):

    def get_credential(self):
        host_credential = {}
        with open('credential') as f:
            for line in f.readlines():
                line_list = line.rstrip().split(':')
                host_credential[line_list[0]] = line_list[1]
        f.close()
        return host_credential

    def get_hostinfo(self):
        host_info = {}
        with open('hostconfig') as f:
            for line in f.readlines():
                line_list = re.split(r'\s+', line.rstrip())
                info = [line_list[1], line_list[2]]
                host_info[line_list[0]] = info
        f.close()
        return host_info

    def get_disk(self):
        total_disk_list = []
        nvme_disk_list = commands.getoutput('''lsblk -nd | awk '{print "/dev/"$1}' |grep -E 'nvme' ''').split('\n')
        hdd_disk_list = commands.getoutput('''lsblk -nd | awk '{print "/dev/"$1}' |grep -E 'sd'|grep -v 'sda' ''').split('\n')
        if len(nvme_disk_list) == 0:
            print 'No nvme device found. Checking HDD device now.'
        else:
            total_disk_list =nvme_disk_list

        if len(hdd_disk_list) == 0:
            print 'No HDD device found yet. Exiting...'
            sys.exit(0)
        else:
            total_disk_list = nvme_disk_list+hdd_disk_list

        for disk in total_disk_list:
            raid_info = commands.getoutput('mdadm -E '+disk)
            if 'No md superblock' not in raid_info:
                total_disk_list.remove(disk)
        print 'Available Disk List:',total_disk_list
        return total_disk_list


#raid_info: {raid_name:{raid_type:[device_list]}}
    def check_exist_raid(self):
        raid_info={}
        #raid_tmp = {}
        p = re.compile(r'md\d')

        raid_name_list = p.findall(commands.getoutput('cat /proc/mdstat'))
        for raid_name in raid_name_list:
            raid_tmp = {}
            raid_type = commands.getoutput('mdadm -D /dev/'+raid_name+' |sed -n 4p | cut -d ":" -f 2').lstrip()
            device_list = commands.getoutput('mdadm -D /dev/'+raid_name+' |tail -n 2 | awk \'{print $7}\'').split('\n')
            raid_tmp[raid_type] = device_list
            raid_info[raid_name] = raid_tmp

        return raid_info

#umount /dev/md1
#sed -i '/md1/d' /etc/fstab
#xfs_repair /dev/md1
#mdadm -S /dev/md1
#mdadm --zero-superblock /dev/sdb
#rm -rf /mnt/md1


    def raid1(self,raid_name,disk_count):
        available_disk_list = self.get_disk()
        total_disk_count = int(len(available_disk_list))
        if disk_count>total_disk_count:
            print 'Only %d disks could be created as RAID'%total_disk_count
            sys.exit(0)
        if disk_count < 2:
            print 'The minimum disk count of RAID1 is 2.'
            sys.exit(0)
        if raid_name in self.check_exist_raid().keys():
            print 'The RAID name already exist in the system. Please double check.'
            sys.exit(0)
        raid_disk_list = random.sample(available_disk_list,disk_count)
        time.sleep(5)
        cmd = 'echo y | mdadm --create /dev/'+raid_name+' --level=1 --raid-devices='+str(disk_count)
        for disk in raid_disk_list:
            cmd += ' ' + str(disk)
        print cmd
        os.system(cmd)
        if raid_name in self.check_exist_raid().keys():
            return True
        else:
            return False

    def raid5(self,raid_name,disk_count):
        available_disk_list = self.get_disk()
        total_disk_count = int(len(available_disk_list))
        if disk_count>total_disk_count:
            print 'Only %d disks could be created as RAID' % total_disk_count
            sys.exit(0)
        if disk_count < 3:
            print 'The minimum disk count of RAID1 is 2.'
            sys.exit(0)
        if raid_name in self.check_exist_raid().keys():
            print 'The RAID name already exist in the system. Please double check.'
            sys.exit(0)

        raid_disk_list = random.sample(available_disk_list, disk_count)
        time.sleep(5)
        cmd = 'echo y | mdadm --create /dev/'+raid_name+' --level=5 --raid-devices='+str(disk_count)
        for disk in raid_disk_list:
            cmd += ' ' + str(disk)
        print cmd
        os.system(cmd)
        if raid_name in self.check_exist_raid().keys():
            return True
        else:
            return False

    def raid6(self,raid_name,disk_count):
        available_disk_list = self.get_disk()
        total_disk_count = int(len(available_disk_list))
        print 'len:',total_disk_count
        if disk_count>total_disk_count:
            print 'Only %d disks could be created as RAID' % total_disk_count
            sys.exit(0)
        elif disk_count<4:
            print 'The minimum disk count of RAID1 is 2.'
            sys.exit(0)
        if raid_name in self.check_exist_raid().keys():
            print 'The RAID name already exist in the system. Please double check.'
            sys.exit(0)
        raid_disk_list = random.sample(available_disk_list, disk_count)
        time.sleep(5)
        cmd =  'echo y | sudo mdadm --create /dev/'+raid_name+' --level=6 --raid-devices='+str(disk_count)
        for disk in raid_disk_list:
            cmd += ' ' + str(disk)
        print cmd
        os.system(cmd)
        if raid_name in self.check_exist_raid().keys():
            return True
        else:
            return False

    def raid10(self,raid_name,disk_count):
        available_disk_list = self.get_disk()
        total_disk_count = int(len(available_disk_list))
        if disk_count>total_disk_count:
            print 'Only %d disks could be created as RAID' % total_disk_count
            sys.exit(0)
        if disk_count < 4:
            print 'The minimum disk count of RAID1 is 2.'
            sys.exit(0)
        if raid_name in self.check_exist_raid().keys():
            print 'The RAID name already exist in the system. Please double check.'
            sys.exit(0)
        raid_disk_list = random.sample(available_disk_list, disk_count)
        time.sleep(5)
        cmd = 'echo y | mdadm --create /dev/'+raid_name+' --level=10 --raid-devices='+str(disk_count)
        for disk in raid_disk_list:
            cmd += ' ' + str(disk)
        print cmd
        os.system(cmd)
        if raid_name in self.check_exist_raid().keys():
            return True
        else:
            return False


    def format_ext4(self,raid_name):
        str = commands.getoutput('sudo mkfs.ext4 /dev/'+raid_name)
        if 'error' in str or 'Error' in str:
            print 'Failed to format the RAID'
            sys.exit(0)
        else:
            print str
            print 'Succeed to format the RAID as ext4'
            return True

    def format_xfs(self,raid_name):
        str = commands.getoutput('sudo mkfs.xfs /dev/' + raid_name+' -f')
        if 'error' in str or 'Error' in str:
            print 'Failed to format the RAID'
            sys.exit(0)
        else:
            print 'Succeed to format the RAID as xfs'
            return True


    def mount_ext4_point(self,raid_name,mount_path):
        time.sleep(5)
        p = os.system('sudo mkdir -p /'+mount_path)
        if p!=0:
            print 'Create ext4 mount directory failed'
            sys.exit(0)
        else:
            q = os.system('sudo mount /dev/'+raid_name+' /'+mount_path)
            if q!=0:
                print 'Create ext4 mount point failed'
                sys.exit(0)
            else:
                print 'Ext4:Write the mount info to fstab'
                r = os.system('echo /dev/'+raid_name+' /'+mount_path+' ext4 defaults 0 0 | sudo tee -a /etc/fstab')
                if r!=0:
                    print 'Ext4:Write the fstab failed'
                    sys.exit(0)
                else:
                    return True

    def mount_xfs_point(self,raid_name,mount_path):
        time.sleep(5)
        p = os.system('sudo mkdir -p /'+mount_path)
        if p!=0:
            print 'Create xfs mount directory failed'
            sys.exit(0)
        else:
            q = os.system('sudo mount /dev/'+raid_name+' /'+mount_path)
            if q!=0:
                print 'Create xfs mount point failed'
                sys.exit(0)
            else:
                print 'XFS:Write the mount info to fstab'
                r = os.system('echo /dev/'+raid_name+' /'+mount_path+' xfs defaults 0 0 | sudo tee -a /etc/fstab')
                if r!=0:
                    print 'XFS:Write the fstab failed'
                    sys.exit(0)
                else:
                    return True


















