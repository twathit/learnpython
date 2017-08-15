class UpperAttrMetaclass(type):
    def __new__(cls,name,bases,dct):
        attrs=((name,value) for name,value in dct.item() if not name.startswith('__')
        uppercase_attrs=dict((name.upper(),value) for name,value in attrs)
        return super().__new__(cls,name,bases,uppercase_attrs)