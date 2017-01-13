
### 如何将一个Python time.struct_time对象转换为一个datetime对象

问题 [链接](http://stackoverflow.com/questions/1697815/how-do-you-convert-a-python-time-struct-time-object-into-a-datetime-object)

使用 [time.mktime()]() 将time元组(本地时间)转成秒， 然后使用 datetime.fromtimestamp() 转成datetime对象

    from time import mktime
    from datetime import datetime

    dt = datetime.fromtimestamp(mktime(struct))

### python中如何获取当前时间

问题 [链接](http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python)

时间日期

    >>> import datetime
    >>> datetime.datetime.now()
    datetime(2009, 1, 6, 15, 8, 24, 78915)

如果仅获取时间

    >>> datetime.datetime.time(datetime.datetime.now())
    datetime.time(15, 8, 24, 78915))
    #等价
    >>> datetime.datetime.now().time()

可以从文档中获取更多 [文档](http://docs.python.org/2/library/datetime.html)

如果想避免额外的datetime.

    >>> from datetime import datetime

### Python - time.clock() vs. time.time() - 更精确?

问题 [链接](http://stackoverflow.com/questions/85451/python-time-clock-vs-time-time-accuracy)

哪一个更适合于计时? 哪个更精确,

例如

    start = time.clock()
    ... do something
    elapsed = (time.clock() - start)

    and

    start = time.time()
    ... do something
    elapsed = (time.time() - start)

回答

区别

    clock() -> floating point number

    Return the CPU time or real time since the start of the process or since
    the first call to clock().
    This has as much precision as the system records.

    time() -> floating point number

    Return the current time in seconds since the Epoch.
    Fractions of a second may be present if the system clock provides them.

根据 [time module doc](http://docs.python.org/lib/module-time.html)

    clock()

    On Unix, return the current processor time as a floating point number expressed in seconds. The precision, and in fact the very definition of the meaning of ``processor time'', depends on that of the C function of the same name,

    but in any case, this is the function to use for benchmarking Python or timing algorithms.

简而言之, time.clock()更精确些, 但是如果涉及cpu外的硬件时间统计(e.g. gpu), 只能使用time.time()

另外基于性能的评估, 可以去看下timeit模块

### python和javascript中josn的datetime 

问题 [链接](JSON datetime between Python and JavaScript) 

怎样从python->javascript传递json的datetime?

可以`json.dumps`中加入`default`参数 

    >>> dthandler = lambda obj: (
    ...     obj.isoformat()
    ...     if isinstance(obj, datetime.datetime)
    ...     or isinstance(obj, datetime.date)
    ...     else None)
    >>> json.dumps(datetime.datetime.now(), default=dthandler)
    '"2010-04-20T20:08:21.634121"'

一个更好理解的handler

    ef handler(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif isinstance(obj, ...):
            return ...
        else:
            raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj))

但是上面这种做法, 对于json中包含其他的类型, 会返回None


    import json
    import datetime

    class DateTimeJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.isoformat()
            else:
                return super(DateTimeJSONEncoder, self).default(obj)

    >>> DateTimeJSONEncoder().encode([datetime.datetime.now()])
    '["2010-06-15T14:42:28"]'



