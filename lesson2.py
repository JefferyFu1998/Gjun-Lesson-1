#!usr/bin/python3.5

marxes=['groucho','chico','harpo'];
print(len(marxes));

a=[1,2,3];
print(a);
b=a;
print(b)
a[0]='surprise';
print(b);


#1. copy()
#2. use trasform list()
#3. use slice[:]

a=[1,2,3];
b=a.copy();
c=list(a);
d=a[:];
b[0]='b';
c[0]='c';
d[0]='d';
print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)

