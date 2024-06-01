from pathlib import Path
from .User import User
from .DBConfig import *
from ..tools import tools
from ..config.config import *
from .WhitelistCode import WhitelistCode

c = conn_codes.cursor()

class WhitelistCodeMapper:
    def get(code):
        c.execute("SELECT * FROM codes WHERE code=:code", {'code': code})

        res = c.fetchall()

        # 没找到
        if len(res) == 0:
            return None
        
        res = res[0]
        return WhitelistCode(res[0], res[1], res[2])