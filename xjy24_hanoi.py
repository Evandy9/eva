#coding=utf-8

def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        #put n-1 plates from x to y
        hanoi(n-1,x,z,y)
        print(x,"-->",z)
        #put the last one from x to z
        hanoi(n-1,y,x,z)
        #put n-1 from y to z
n=int(input("please keyin the number:"))
hanoi(n,'x','y','z')

#64个盘子从x已到z，每次只能移动一个盘子，然后必须保证小的在大的上面