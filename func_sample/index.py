x="5"

def init(ctx):
    global x
    x = "10"

def handler(event, ctx):
    print("x=",x);
    return x
