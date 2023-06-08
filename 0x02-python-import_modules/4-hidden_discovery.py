#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for b in dir(hidden_4):
        if b[0] != '_' and b[1] != '_':
            print(b)
