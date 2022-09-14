from typing import List, Tuple


def gcd(a: int, b: int):
    if a < b:
        a, b = b, a
    if b == a == 0:
        raise Exception("Invalid input")
    if b == 0:
        return a
    return gcd(a % b, b)


def numberExtractor(s: str) -> Tuple[int, int, int, int]:
    """
    Input would be like `10/21 + 21/30`
    Return 10, 21, 21, 30 in this case
    """
    exp1, exp2 = s.split("+")
    a, b = exp1.split("/")
    c, d = exp2.split("/")
    return int(a), int(b), int(c), int(d)


def reducedFractionSums(expressions: List[str]) -> List[str]:
    ans = []
    for s in expressions:
        a, b, c, d = numberExtractor(s)
        num = (a * d) + (c * b)
        den = b * d
        gcd_ = gcd(num, den)
        num //= gcd_
        den //= gcd_
        ans.append("{}/{}".format(num, den))
    return ans


if __name__ == '__main__':
    print(reducedFractionSums(["722/148+360/176","978/1212+183/183"]))