# coding=utf-8

from mist import logger as log
from command.img import EroImage

import re


class MsgHandler:
    TYPE_NONE = [0, "none"]
    TYPE_MSG = [1, "msg"]
    TYPE_IMG = [2, "img"]

    def __init__(self):
        # todo: init corpus file
        return

    def handle(self, msg: str):
        for cmd in EroImage.cmd:
            if re.search(cmd, msg):
                img = EroImage().getRandImg()
                log.i("img: %s" % img)
                return img is not None, self.TYPE_IMG, img

        return True, self.TYPE_NONE, msg
