def write_name(filename, first_name, last_name):
    f=open(filename,'w')
    print(first_name, last_name, file=f)
    f.close()

write_name('Write_name.txt','Charles','Darwin')