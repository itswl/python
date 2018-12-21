
import _init_
print(_init_.b)

# 注意事项：import 与 from import
#         1）如 print t包C7.py中的a
#         import t.c7 ~ print（t.c7.a）   等价于from t.c7 import a ~print（a）
#         等价于from t import c7.a ~print（c7.a）
#         2)import t.c7 ~ print（t.c7.a） 等价于import t.c7 as m ~print（m.a）


#         3）包和模块不会被重复导入
        # 4）避免循环导入
        # 5）from t.c7 import * (导入C7中所有的变量)
        # 6）from t.c7 impor _all_=['a','c'] (导入C7中'a','c'两个变量）    
