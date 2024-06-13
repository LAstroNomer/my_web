import os 
import subprocess as sp
import time

files = sorted(os.listdir('blogs'))

ff = open('Blog.html', 'w')
with open('Blog0.html', 'r') as r:
    for line in r.readlines():
        print(line, end='', flush=True, file=ff)

# move txt to html
aa = [] 
for file in files:
    path = './blogs/'+file
    if '.txt' in path:
        path1 = path[:-3]+'html'
        sp.call('cp %s %s' %(path, path1), shell=True)
        file_info = os.path.getctime(path)
        date = file_info
        aa.append([date, path1])

# connect font file
for date, path in sorted(aa):
    f = open(path,'r+')
    lines = f.readlines() # read old content
    f.seek(0) # go back to the beginning of the file
    f.write('<link rel="stylesheet" type="text/css" href="Fonb.css" />\n') # write new content at the beginning
    for line in lines: # write old content after new
        f.write(line)
    f.close()


# load to main html
for date, path in sorted(aa, reverse=True):
    print('''
    <div class="blogdate"> &#x2022; %s</div>
    <div class="blogtext" width=70%%>
    ''' %(time.ctime(date)), file=ff)

    with open(path, 'r') as r:
        for line in r.readlines()[1:]:
            print(line, end='', file=ff, flush=True)

    print('</div>', file=ff, flush=True)

print('</body>', '</html>', sep = '\n', file=ff)
