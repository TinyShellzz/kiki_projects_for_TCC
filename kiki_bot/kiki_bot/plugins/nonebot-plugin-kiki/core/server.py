from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import mcrcon
import re
from ..config.config import *
from .authorization import *

def excute(command):
    rcon = mcrcon.MCRcon(server_ip, rcon_password, rcon_port, timeout=2)
    response  = None
    try:
        rcon.connect()
        response = rcon.command(command)
        logger.info(response)
    except Exception as e:
        logger.warning(e)
    finally:
        rcon.disconnect()

    return response

class ban:
    async def handle(bot: Bot, event: Event):
        if not await auth_qq(bot, event): return
        print('------------server ban-------------')
        msg = str(event.get_message())
        
        match = re.search('^/{0,1}ban (.*)$', msg)
        command = match.groups()[0]
        name = command.split(' ')[0]

        response = excute(f'iban {command}')
        excute(f'ban {command}')

        await bot.send(event, Message(f'{response}--完成'))

class unban:
    async def handle(bot: Bot, event: Event):
        if not await auth_qq(bot, event): return
        msg = str(event.get_message())
        
        user_name = re.search('^/{0,1}unban (.*)$', msg)
        user_name = user_name.groups()[0].strip()

        response = excute(f'iunban {user_name}')
        excute(f'unban {user_name}')

        await bot.send(event, Message(f'{response}--完成'))

class ban_syn:
    async def handle(bot: Bot, event: Event):
        pass