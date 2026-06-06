#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    pref = "__"
    for name in dir(hidden_4):
        if pref not in name:
            print(name)
