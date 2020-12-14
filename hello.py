import time


def sleep_(sec: int = 1):
    time.sleep(sec)


def main():
    for i in range(0, 10):
        print(i)
        sleep_()


if __name__ == '__main__':
    main()
