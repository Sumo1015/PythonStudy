#使用函数的优点之一是可将代码块与主程序分离。通过给指定函数指定描述性名称，可让主程序容易理解得多
#可以更进一步将函数存储在称为模块的独立文件中，再将模块导入到主程序中
#import语句允许在当前运行的程序文件中使用模块中的代码

#导入整个模块
#模块是扩展名为.py的文件，包含要导入到程序中的代码

def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")