import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
print(sys.winver,sys.platform,sys.__doc__)
print(dir(sys))