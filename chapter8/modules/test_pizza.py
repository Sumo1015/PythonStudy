#使用import语句将一个模块导入，导入后当前文件可以使用被导入模块的所有已定义的函数
import pizza
#使用 module_name.function_name()调用函数
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#导入特定的函数
#使用 from module_name import function_name1,function_name2
#若要某个模块的所有函数，可以使用* 即 from module_name import *
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用as给函数指定别名
#如果要导入的函数的名称可能与程序中现有的名称冲突或者函数的名称过长，可指定独一无二的别名，类似于外号
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

#使用as给模块指定别名
#通过给模块指定简短的别名，使我们能更轻松地调用模块中的函数
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')