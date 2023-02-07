def decor(func):
    def inner(name):
        if name=="hcl":
            print("hello hcl")
        else:
            func(name)
        return inner

