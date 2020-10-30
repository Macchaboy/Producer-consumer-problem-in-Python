def fun(*args,**kwargs):
    for arg in args:
        print('args : {}'.format(arg))
    for kwarg in kwargs:
        print('kwargs: {}'.format(kwarg))


if __name__ == "__main__":
    fun(1,2,3)
    print("")
    fun(a=1,b=2,c=3)
    print("")
    d = {'a':1,'b':2,'c':3}
    fun(d,**d)