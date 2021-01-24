"""
Given a string containing only digits, return all possible valid IP address combinations.

Example:
Input: "25525511135",  Output: ["255.255.11.135", "255.255.111.35"]
"""

"""
First we set up a set of acceptable values for bit parts (i.e. all strings from 0 to 255), for fast O(1) access. Then
we recursively calculate possible parts from the remaining string, bearing in mind the minimum and maximum sizes of
the part (which depend on the existing parts and remaining characters: if we have [1, 1] and remaining is 11111, we 
know the minimum and maximum sizes of the part are 2 and 3) to avoid useless calculation.
"""


bit_numbers = {str(i) for i in range(256)}


def restore_ip_addresses(s):
    results = []
    if len(s) < 4 or len(s) > 12:
        return results

    def get_split_part(existing, remaining):
        num_parts_left = 3 - len(existing)
        min_len = x if (x := len(remaining) - 3*num_parts_left) > 1 else 1
        max_len = x if (x := len(remaining) - num_parts_left) < 3 else 3
        for part_len in range(min_len, max_len+1):
            if (part := remaining[:part_len]) in bit_numbers:
                if len(existing) < 3:
                    recur_existing = existing.copy()
                    recur_existing.append(part)
                    get_split_part(recur_existing, remaining[part_len:])
                else:
                    existing.append(part)
                    results.append(existing)

    get_split_part([], s)
    return ['.'.join(parts) for parts in results]


assert restore_ip_addresses('111') == []
assert restore_ip_addresses('1111') == ['1.1.1.1']
assert restore_ip_addresses('010010') == ['0.10.0.10', '0.100.1.0']
assert restore_ip_addresses('11111') == ['1.1.1.11', '1.1.11.1', '1.11.1.1', '11.1.1.1']
assert restore_ip_addresses('25525511135') == ['255.255.11.135', '255.255.111.35']
assert restore_ip_addresses('172162541') == [
    '17.216.25.41', '17.216.254.1', '172.16.25.41', '172.16.254.1', '172.162.5.41', '172.162.54.1']
assert restore_ip_addresses('1231231231231') == []
