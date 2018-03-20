# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import sys,time

from Helper import Helper
Helper = Helper()

def Storage(raid_type,raid_name,disk_count,fs_type,mount_path):
    try:
        if int(raid_type)==5:
            print 'Creating RAID5...'
            if Helper.raid5(raid_name,int(disk_count)):
                print 'Succeed to create a RAID5 on Storage Server '
            else:
                sys.exit('Failed to create RAID5 on the Storage Server')

        elif int(raid_type)==6:
            print 'Creating RAID6...'
            if Helper.raid6(raid_name,int(disk_count)):
                print 'Succeed to create a RAID6 on Storage Server '
            else:
                sys.exit('Failed to create RAID6 on the Storage Server')

        if fs_type=='ext4':
            if Helper.format_ext4(raid_name):
                time.sleep(5)
                if Helper.mount_ext4_point(raid_name,mount_path):
                    print 'Mount the local storage filesystem successfully '
                else:
                    sys.exit('Failed to mount the ext4 FS')
        elif fs_type=='xfs':
            if Helper.format_xfs(raid_name):
                time.sleep(5)
                if Helper.mount_xfs_point(raid_name, mount_path):
                    print 'Mount the local storage filesystem successfully '
                else:
                    sys.exit('Failed to mount the FS')
        return True
    except SystemExit, value:
        print '\033[1;31m Error:\033[0m %s'%(value)
        return False
if __name__=='__main__':
    raid_type=sys.argv[1]
    raid_name=sys.argv[2]
    disk_count=sys.argv[3]
    fs_type=sys.argv[4]
    mount_path = sys.argv[5]

    Storage(raid_type,raid_name,disk_count,fs_type,mount_path)














