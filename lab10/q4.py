def html_table_generator(lst, filename):
    f = open(filename, 'w')

    f.write('<html>'+'\n')
    f.write('\t'+'<table'+'\n')
    for i in range(len(lst)):
        f.write('\t\t<tr>' + '\n')
        for j in range(len(lst)):
            f.write('\t\t\t'+'<th>'+(lst[i][j])+'</th>'+'\n')
        f.write('\t\t</tr>'+'\n')
    f.write('\t'+'<table'+'\n')
    f.write('</html>'+'\n')

    f.close()
def main():
    lst=[['header1','header2','header2','header4'],['r1c1','r1c2','r1c3','r1c4'],['r2c1','r2c2','r2c3','r2c4'],['r3c1','r3c2','r3c3','r3c4']]
    html_table_generator(lst,'lab10_q4.txt')

main()