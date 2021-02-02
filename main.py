from client import client
import loop


def main():
    if client.read_only:
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')
    loop.loop("test")
    pass


if __name__ == '__main__':
    main()
