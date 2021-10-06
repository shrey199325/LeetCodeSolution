parser = None
arg = None

def change_local():
    parser = "serve"
    return parser


def change_global():
    global parser, arg
    parser = [1,2,3,4]
    arg = "alpha"
    return parser


print(parser)
print(arg)
print(change_local())
print(parser)
print(change_global())
print(parser)
print(arg)