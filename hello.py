import time


def sleep_100ms():
    time.sleep(0.1)


def sleep_500ms():
    time.sleep(0.5)


def main():
    for i in range(0, 10):
        print(i)
        sleep_100ms()

    for i in range(0, 5):
        print(i)
        sleep_500ms()


if __name__ == '__main__':
    main()
