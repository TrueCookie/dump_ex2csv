import sys

def test(path1, path2="no path"):
    print(path1)
    print(path2)

if __name__ == '__main__':
    test(sys.argv[1], sys.argv[2])