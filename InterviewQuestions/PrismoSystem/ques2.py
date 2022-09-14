"""

 0             1          2
 M            Cloth      Pants
 W            Shoes      Shirts
 G            Belt       Leather
 B            Sock

{
men: {

}

}


"""

class clobj:
    pass


ab = [set(["M", "W"]), set(["C", "S"]), set(["P"])]

# O(1)
# O(n)
ind = 2
a = {
    "men": {
        "cloth": {
            "pants": {
                34: clobj
            }
        },
        "shoes": {}
    },
    "women": {
        "cloth": {}
    }

}