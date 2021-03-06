"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the
directory up a level. Note that the returned canonical path must always begin with a slash /, and there must be only
a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /.
Also, the canonical path must be the shortest string representing the absolute path.

Example 1:
Input: '/home/',  Output: '/home'
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: '/../',  Output: '/'
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: '/home//foo/',  Output: '/home/foo'
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: '/a/./b/../../c/',  Output: '/c'

Example 5:
Input: '/a/../../b/../c//.//',  Output: '/c'

Example 6:
Input: '/a//b////c/d//././/..',  Output: '/a/b/c'
"""

"""
Fairly simple, we just split on / and ignore any . or empty spaces as these are repeated slashes or the same directory.
We append any directories to a stack and if there are any .. we pop an item off the stack, if present. Then at the end
we merely join the items from the stack back up again to form the canonical path.
"""


def simplify_path(path):
    stack = []
    for item in path.split('/'):
        if item in ['', '.']:
            continue
        elif item == '..':
            if stack:
                stack.pop()
        else:
            stack.append(item)
    return '/' + '/'.join(stack)


assert simplify_path('/home/') == '/home'
assert simplify_path('../../') == '/'
assert simplify_path('') == '/'
assert simplify_path('/a/./.') == '/a'
assert simplify_path('/home//foo/') == '/home/foo'
assert simplify_path('/a/./b/../../c/') == '/c'
assert simplify_path('/a/../../b/../c//.//') == '/c'
assert simplify_path('/a//b////c/d//././/..') == '/a/b/c'
