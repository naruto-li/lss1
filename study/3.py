# 什么是Python中的类型转换？
#
# 类型转换是指将一种数据类型转换为另一种数据类型。
#
# int（）  将任何数据类型转换为整数类型
#
# float（） 将任何数据类型转换为float类型
#
# ord（）  将字符转换为整数
#
# hex（） 将整数转换为十六进制
#
# oct（）  将整数转换为八进制
#
# tuple（） 此函数用于转换为元组。
#
# set（） 此函数在转换为set后返回类型。
#
# list（）  此函数用于将任何数据类型转换为列表类型。
#
# dict（）  此函数用于将顺序元组（键，值）转换为字典。
#
# str（） 用于将整数转换为字符串。
#
# complex（real，imag）  – 此函数将实数转换为复数（实数，图像）数。
# 不可变数据类型:数值型,字符串型string和元组tuple不允许变量的值发生变化，
# 如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存
# 中则只有一个对象（一个地址）
a=3
b=3
print(id(a))
print(id(b))
# 可变数据类型：列表list和字典dict；允许变量的值发生变化，即如果对变量进行append、+=等这种操作后
# ，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，
# 在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，
# 这里不存在引用计数，是实实在在的对象。
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))