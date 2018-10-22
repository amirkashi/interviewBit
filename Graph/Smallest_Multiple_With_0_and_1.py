"""
You are given an integer N. You have to find smallest multiple of N which
consists of digits 0 and 1 only. Since this multiple could be large, return it 
in form of a string.
Note:
Returned string should not contain leading zeroes.
For example:
For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.
"""
import Queue


class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        if A <= 0:
            return
        if A == 1:
            return "1"
        q = Queue.Queue()
        q.put("1")
        seen_values = set()
        seen_values.add("1")
        while True:
            q_get = q.get()
            if int(q_get) % A == 0:
                return q_get
            else:
                if q_get+"0" not in seen_values:
                    if int(q_get+"0") % A == 0:
                        return q_get+"0"
                    q.put(q_get+"0")
                    seen_values.add(q_get+"0")
                if q_get+"1" not in seen_values:
                    if int(q_get+"1") % A == 0:
                        return q_get+"1"
                    q.put(q_get+"1")
                    seen_values.add(q_get+"1")