#coding=utf-8

print(__name__)


def c2f(cel):
    fah=cel*1.8+32
    return fah
def f2c(fah):
    cel=(fah-32)/1.8
    return cel

def test():
    print("test 0摄氏度=%.2f华氏度" % c2f(0))
    print("test 0华氏度=%.2f摄氏度" % f2c(0))
if __name__ == "__main__":  #让python知道是作为程序运行还是导入到其他程序中,作为模块导入
    test()

#-------------------------------------------------------------------------------
#搜索路径 就是个列表
import sys
print(sys.path)
#site-packages是用来存放模块的
#类似与添加环境变量
sys.path.append("/home/evandy/Video")
print(sys.path)

#-------------------------------------------------------------------------------
