import os
import time

source = r"C:\Users\HUITIAN\Desktop\CMake_test"

target_dir = r"C:\Users\HUITIAN\backup"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('成功创建目录', today)

zip_command = 'zip -r {0} {1}'.format(target, source)

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
