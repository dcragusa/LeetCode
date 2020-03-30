"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before
implementing. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."

Of course, the context of these characters also matters in the input.
"""

"""
This can be trivial thanks to float() which does all the checking for us. I have also included a frankly monstrous 
regex for 'fun', both in verbose mode with copious comments and in devil form.
"""

import re


def is_num_simple(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_num_regex_commented(s):
    return bool(re.fullmatch(r"""
        (?P<sign>                       # sign part
            (?<![+-])[+-](?![+-])       # + or - (if not before or after another + or -)
        )?                              # the above, 0 or 1 times
        
        (?P<number>                     # number part
            \d+                         # 1 or more digits
        )?                              # the above, 0 or 1 times (we do not need a num if there is a decimal)
        
        (?(number)                      # if we have a number:
            (?P<decimal_with_num>           # decimal part
                \.                          # a dot
                \d?                         # 0 or more digits (we do not need digits after the dot if there is a num)
            )?                              # the above, 0 or 1 times (we do not need a decimal if there is a num)
        |                               # if we do not have a number:
            (?P<decimal_without_num>        # decimal part
                \.                          # a dot
                \d+                         # 1 or more digits (we need digits after the dot if there is no num)
            )                               # the above, 1 time (we need a decimal if there is no num)
        )
        
        (?P<exponent>                   # exponent part
            [eE]                        # an e
            ((?<![+-])[+-](?![+-]))?    # a single sign, as above
            \d+                         # 1 or more digits
        )?                              # the above, 0 or 1 times
    """, s.strip(), re.X))


def is_num_regex_devil(s):
    return bool(re.fullmatch(
        r'((?<![+-])[+-](?![+-]))?(?P<n>\d+)?(?(n)(\.\d?)?|(\.\d+))([eE]((?<![+-])[+-](?![+-]))?\d+)?', s.strip()
    ))


assert is_num_simple("0") is is_num_regex_commented("0") is is_num_regex_devil("0") is True
assert is_num_simple(" 0.1 ") is is_num_regex_commented(" 0.1 ") is is_num_regex_devil(" 0.1 ") is True
assert is_num_simple("abc") is is_num_regex_commented("abc") is is_num_regex_devil("abc") is False
assert is_num_simple("1 a") is is_num_regex_commented("1 a") is is_num_regex_devil("1 a") is False
assert is_num_simple("+157") is is_num_regex_commented("+157") is is_num_regex_devil("+157") is True
assert is_num_simple("-145") is is_num_regex_commented("-145") is is_num_regex_devil("-145") is True
assert is_num_simple("2e10") is is_num_regex_commented("2e10") is is_num_regex_devil("2e10") is True
assert is_num_simple("-2e10") is is_num_regex_commented("-2e10") is is_num_regex_devil("-2e10") is True
assert is_num_simple(" -90e3   ") is is_num_regex_commented(" -90e3   ") is is_num_regex_devil(" -90e3   ") is True
assert is_num_simple(" 1e") is is_num_regex_commented(" 1e") is is_num_regex_devil(" 1e") is False
assert is_num_simple("e3") is is_num_regex_commented("e3") is is_num_regex_devil("e3") is False
assert is_num_simple(" 6e-1") is is_num_regex_commented(" 6e-1") is is_num_regex_devil(" 6e-1") is True
assert is_num_simple(" 99e2.5 ") is is_num_regex_commented(" 99e2.5 ") is is_num_regex_devil(" 99e2.5 ") is False
assert is_num_simple("53.5e93") is is_num_regex_commented("53.5e93") is is_num_regex_devil("53.5e93") is True
assert is_num_simple(" --6 ") is is_num_regex_commented(" --6 ") is is_num_regex_devil(" --6 ") is False
assert is_num_simple("-+3") is is_num_regex_commented("-+3") is is_num_regex_devil("-+3") is False
assert is_num_simple("95a54e53") is is_num_regex_commented("95a54e53") is is_num_regex_devil("95a54e53") is False
assert is_num_simple(".1") is is_num_regex_commented(".1") is is_num_regex_devil(".1") is True
assert is_num_simple("3.") is is_num_regex_commented("3.") is is_num_regex_devil("3.") is True
