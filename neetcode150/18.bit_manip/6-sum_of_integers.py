"""11:19am
12:20pm


python has infinite bits...
makes this a little confusing

i figured out the initial solution
ie. creating a carry bit number
constantly adding that carry

but with python you'll need to mask it to a 32 bit integer
and deal with negatives in a special way

"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFF
        carry = (a & b) << 1
        ans = a ^ b
        while carry & mask:
            ans, carry = ans ^ carry, ((carry & ans) << 1)
        return mask & ans if carry else ans
