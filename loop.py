# 打印九九乘法表
# i=9
# while i>=1:
#     j=1
#     while j<=1:
#         print('%d*%d=%2d\t'%(j,i,i*j),end='')
#         j+=1
#         i-=1
#         print()
# 循环嵌套
# row=1
# row=9
# while row>=1:
#     col=1
#     while col<=row:
#         print("%d*%d=%2d"%(row,col,row*col),end=" ")
#         col+=1
#         pass
#     print()
#     # row+=1
#     row-=1
#     pass
# 打印三角形
# i=1
# i=5
# # while i<=5:
# while i>=1:
#     j=1
#     while j<=i:
#         print('*',end=' ')#end控制其不换行
#         j+=1
#     pass
#     print()#自带换行效果
#     # i+=1
#     i -= 1
# 等腰三角形
# row=1
# while row<=5:
#     j=1
#     while j<=5-row:
#         print(' ',end=' ')
#         j+=1#控制打印空格的数量
#         pass
#     k=1
#     while k<=2*row-1:
#         print('*',end=' ')
#         k+=1#控制打印*的数量
#         pass
#     print()
#     row+=1
