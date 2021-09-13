from functools import wraps
from inspect import getfullargspec


class Function:
    _func_dict = None

    def __init__(self, fn):
        if not Function._func_dict:
            Function._func_dict = {}

        self.fn = fn
        Function._func_dict[self.key()] = fn

    def __call__(self, *args, **kwargs):
        # 获取入参的类型
        args_type = list()
        for param in args:
            args_type.append(param.__class__)

        # 获取参数个数
        args_count = len(args)

        try:
            fn = Function._func_dict[self.key(args_count, args_type)]
        except KeyError:
            raise KeyError("参数数量或类型错误")

        return fn(*args, **kwargs)

    def key(self, args_count=None, args_type=None):
        if args_count is None:
            # getfullargspec() 获取函数参数的名称和默认值，返回一个命名的元组
            # FullArgSpec(args=['l', 'w'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})
            args_count = len(list(getfullargspec(self.fn).args))
        if args_type is None:
            args_type = list(getfullargspec(self.fn).annotations.values())

        return str([self.fn.__module__, self.fn.__class__, self.fn.__name__, args_count, args_type])


def overloads(fn):
    @wraps(fn)  # 该装饰器是为了让被装饰之后的函数还具有装饰之前的部分属性，如__name__,__doc__等
    def wrapper():
        return Function(fn)

    return wrapper()
