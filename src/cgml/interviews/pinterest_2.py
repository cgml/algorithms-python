"""
We have a log file in this simple format, and we want to parse it to understand common behavior in the Pinterest app. Given a log file in this format:

timestamp, userid, page type
2016-06-23 20:48:21, 1, PIN
2016-06-23 20:48:22, 1, BOARD
2016-06-23 20:49:24, 2, SEARCH
2016-06-23 20:49:24, 2, BOARD
2016-06-23 20:49:25, 2, PIN
2016-06-23 20:49:26, 1, PIN
2016-06-23 20:50:01, 1, PIN
2016-06-23 20:50:03, 1, SEARCH
2016-06-23 20:50:31, 2, PIN

What is the most commonly visited sequence of 3 page types? (aka sub-seq whose length is 3)

BOARD,PIN,PIN

N lines in this log file
M unique users in this log file
N >> M

Type - O(1) - 2K

PIN -> P
BOARD -> B
SEARCH -> S


Solution 1:
Hashmap (P B P) + count
Space Complexity: O(M)
Time Complexity: O(N)

Task #1:
1: P, B, P, P, S => (P B P) (B P P) (P P S)
2: S, B, P, P


"""


def commonly_visited_sequence(data):
    users_data = {}
    sequence_counts = {}
    max_num = 0
    max_sequence = ""
    for d in data:
        user = d[0]
        page_type = d[1]
        user_data = users_data.get(user, [])
        if len(user_data) == 3:
            user_data.pop(0)
        user_data.append(page_type)
        if len(user_data) == 3:
            k = ",".join(user_data)
            v = sequence_counts.get(k, 0) + 1
            sequence_counts[k] = v
            if max_num < v:
                max_sequence = k
                max_num = v
        users_data[user] = user_data
    return max_sequence


def preprocess(data):
    result = []
    lines = data.split("\n")
    for line in lines:
        result.append([k.strip() for k in line.split(",")][1:])
    return result


data = """2016-06-23 20:48:21, 1, PIN 
2016-06-23 20:48:22, 1, BOARD 
2016-06-23 20:49:24, 2, SEARCH 
2016-06-23 20:49:24, 2, BOARD 
2016-06-23 20:49:25, 2, PIN 
2016-06-23 20:49:26, 1, PIN 
2016-06-23 20:50:01, 1, PIN 
2016-06-23 20:50:03, 1, SEARCH 
2016-06-23 20:50:31, 2, PIN"""

# print (preprocess(data))
print(commonly_visited_sequence(preprocess(data)))