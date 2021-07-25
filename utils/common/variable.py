# -*- coding: utf-8 -*-
import inspect


def retrieve_name(var, more_call=False):
    """
    get a name of variables
    :param more_call: 是否是嵌套调用该函数，如果嵌套调用的话，需要再往函数调用栈返一层才能获取变量名了。
    :param var: the variable
    :return: the name of variable
    """
    if more_call:
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
    else:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    var_names = [var_name for var_name, var_val in callers_local_vars if var_val is var]
    if not var_names:
        return None
    return var_names[0]


def inspect_variable(var):
    var_name = retrieve_name(var, more_call=True)
    return {"name": var_name, "type": str(type(var)), "attrs": str(dir(var))}
