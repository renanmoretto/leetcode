"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.
"""


# -------------------------------- O(n^2) time ------------------------------- #
def solution_on2(s: str) -> int:
    if len(s) == 1:
        return 1

    if len(set(s)) == len(s):
        return len(s)

    subs = []
    for i, _ in enumerate(s):
        sub = []
        for c in s[i:]:
            if c in sub:
                break
            sub.append(c)
        subs.append(sub)

    return max([len(sub) for sub in subs])


# ----------------------------------- O(n) ----------------------------------- #
def solution_on(s: str) -> int:
    if len(s) == 1:
        return 1

    if len(set(s)) == len(s):
        return len(s)

    ans = []
    sub = []
    for c in s:
        if c in sub:
            if sub.index(c) == 0:
                sub.remove(c)
            else:
                c_loc = sub.index(c)
                sub = sub[c_loc + 1 :]
        sub.append(c)
        if len(sub) > len(ans):
            ans = sub.copy()

    print(ans)
    return len(ans)


if __name__ == '__main__':
    s = 'anviaj'
    s = 'abcabcbb'
    s = 'pwwkew'
    s = 'ohvhjdml'
    r = solution_on(s)
    print(r)
