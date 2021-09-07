"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3,  Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4,  Output: "PINALSIGYAHRPI"
Explanation:

P     I     N
A   L S   I G
Y A   H R
P     I
"""

"""
We can see that the 'columns' of the zigzag occur at 2 * (num_rows-1). The first and last columns follow this pattern
exactly. All other columns have an additional character between the columns, which can be found at 2 * num_rows from
the next column. Hence we iterate down the rows, adding characters according to this pattern to the output until the
string is exhausted.
"""


def convert(s, num_rows):
    if num_rows == 1:
        return s
    output = ''
    len_s = len(s)
    for row in range(num_rows):
        idx = row
        while idx < len_s:
            output += s[idx]
            if row == 0 or row == num_rows - 1:
                idx += 2 * (num_rows-1)
            else:
                idx += 2 * (num_rows-1-row)
                if idx >= len_s:
                    break
                output += s[idx]
                idx += 2 * row
    return output


assert convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
