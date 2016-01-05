import os
import time

orignames=[]

name=[]
os.system('ls ./ > ./tmp.txt')

file=open('./tmp.txt')
for i in file:
    orignames.append(i)



for i in range(len(orignames)):
    
    old=orignames[i]
    old=old.replace(' ','\ ')
    old=old.replace('(','\(')
    old=old.replace(')','\)')
    old=old.replace('[','\[')
    old=old.replace(']','\]')
    old=old.rstrip('\n')
    old=old.rstrip()
    new=old.replace('\ ','_')
    new=new.replace('\(','_')
    new=new.replace('\)','_')
    new=new.replace('\[','_')
    new=new.replace('\]','_')

    if old!=new:
        os.system('mv ./{} ./{}'.format(old,new))

os.system('rm ./tmp.txt')
    










    



