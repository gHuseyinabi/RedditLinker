from client import client, client_info
import loop
TEMP_URL = 'https://i.hizliresim.com/zewPHP.png'
def main():
    if client.read_only:
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')

    loop.loop("kgbtr")

    pass


if __name__ == '__main__':
    main()
