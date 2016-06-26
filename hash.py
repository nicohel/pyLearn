def hash_string(keyword, size):
    position = 0
    for i in keyword:
        position = position + ord(i) % size
    position = position % size
    return position

print hash_string('udacity', 1000)
