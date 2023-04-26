import bbbroom.bbbclient
import bbbroom.webui

from threading import Thread


def main():
    Thread(target=bbbroom.bbbclient.open_webui).start()
    bbbroom.webui.app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
