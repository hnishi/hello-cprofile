import sys
import pstats
from pstats import SortKey


def main():
    print(sys.argv)
    p = pstats.Stats(sys.argv[1])
    p.sort_stats(SortKey.TIME).print_stats(10)


if __name__ == '__main__':
    main()
