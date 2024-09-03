import time
import os
from twitchio.ext import commands
import keyboard
import mouse
from pystyle import Center, Colors, Colorate
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.system('title Kichi779 - Twitch Chat Game Controller v1')

print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter("""
                                        Special thanks to:
           
                             ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                             ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                             ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                            ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                           ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                             ███▐██▄   ███   ███    █▄    ███    ███   ███  
                             ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                             ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                             ▀                                             
                               Discord https://discord.gg/aVk4JUFukk       
                               Github  https://github.com/kichi779       
                       
                      
                      """)))
print(Colorate.Vertical(Colors.green_to_yellow, Center.XCenter("""

   __                __           __          __
  / /_____ __ _____ / /____  ____/ /_____ ___/ /
 /  '_/ -_) // (_-</ __/ _ \/ __/  '_/ -_) _  / 
/_/\_\\__/\_, /___/\__/\___/\__/_/\_\\__/\_,_/  
         /___/                                  


                                        version 0.73 Made by Leonid Podhvatilin:)
""")))
class Bot(commands.Bot):

    def __init__(self):
        # Enter the ACCESS TOKEN in the Token section (If you don't know how to get it, read my github page). initial_channels=['xxx']) Enter the name of your channel here.
        super().__init__(token='****', prefix='!', initial_channels=['****'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print(Fore.GREEN + "The bot has started working on your channel !help" + Fore.RESET)
        print(Fore.YELLOW +"This code is open source and free, please don't forget to leave stars on github." + Fore.RESET)

    @commands.command()
    async def help(self, ctx: commands.Context):
      await ctx.send(f'Лист комманд = !a...z, !win, !shift, !alt, !bsp, !dot, !comma, !tab, !ctrl, !tilda !jump, !longjump - с направлениями, к примеру !flongjump длинный прыжок вперёд, !lmb, !rmb, !mmb,  {ctx.author.name}!')


    @commands.command()
    async def a(self, ctx: commands.Context):
        keyboard.press('a')
        time.sleep(0.5)
        keyboard.release('a')
    async def tilda(self, ctx: commands.Context):
        keyboard.press('`')
        time.sleep(0.5)
        keyboard.release('`')
    @commands.command()
    async def one(self, ctx: commands.Context):
        keyboard.press('1')
        time.sleep(0.5)
        keyboard.release('1')
    @commands.command()
    async def two(self, ctx: commands.Context):
        keyboard.press('2')
        time.sleep(0.5)
        keyboard.release('2')
    @commands.command()
    async def three(self, ctx: commands.Context):
        keyboard.press('3')
        time.sleep(0.5)
        keyboard.release('3')
    @commands.command()
    async def four(self, ctx: commands.Context):
        keyboard.press('4')
        time.sleep(0.5)
        keyboard.release('4')
    @commands.command()
    async def five(self, ctx: commands.Context):
        keyboard.press('5')
        time.sleep(0.5)
        keyboard.release('5')
    @commands.command()
    async def six(self, ctx: commands.Context):
        keyboard.press('6')
        time.sleep(0.5)
        keyboard.release('6')
    @commands.command()
    async def seven(self, ctx: commands.Context):
        keyboard.press('7')
        time.sleep(0.5)
        keyboard.release('7')
    @commands.command()
    async def eight(self, ctx: commands.Context):
        keyboard.press('8')
        time.sleep(0.5)
        keyboard.release('8')
    @commands.command()
    async def nine(self, ctx: commands.Context):
        keyboard.press('9')
        time.sleep(0.5)
        keyboard.release('9')
    @commands.command()
    async def zero(self, ctx: commands.Context):
        keyboard.press('0')
        time.sleep(0.5)
        keyboard.release('0')
    @commands.command()
    async def b(self, ctx: commands.Context):
        keyboard.press('b')
        time.sleep(0.5)
        keyboard.release('b')
    @commands.command()
    async def c(self, ctx: commands.Context):
        keyboard.press('c')
        time.sleep(0.5)
        keyboard.release('c')
    @commands.command()
    async def d(self, ctx: commands.Context):
        keyboard.press('d')
        time.sleep(0.5)
        keyboard.release('d')
    @commands.command()
    async def e(self, ctx: commands.Context):
        keyboard.press('e')
        time.sleep(0.5)
        keyboard.release('e')
    @commands.command()
    async def f(self, ctx: commands.Context):
        keyboard.press('f')
        time.sleep(0.5)
        keyboard.release('f')
    @commands.command()
    async def g(self, ctx: commands.Context):
        keyboard.press('g')
        time.sleep(0.5)
        keyboard.release('g')
    @commands.command()
    async def h(self, ctx: commands.Context):
        keyboard.press('h')
        time.sleep(0.5)
        keyboard.release('h')
    @commands.command()
    async def i(self, ctx: commands.Context):
        keyboard.press('i')
        time.sleep(0.5)
        keyboard.release('i')
    @commands.command()
    async def j(self, ctx: commands.Context):
        keyboard.press('j')
        time.sleep(0.5)
        keyboard.release('j')
    @commands.command()
    async def k(self, ctx: commands.Context):
        keyboard.press('k')
        time.sleep(0.5)
        keyboard.release('k')
    @commands.command()
    async def l(self, ctx: commands.Context):
        keyboard.press('l')
        time.sleep(0.5)
        keyboard.release('l')
    @commands.command()
    async def m(self, ctx: commands.Context):
        keyboard.press('m')
        time.sleep(0.5)
        keyboard.release('m')
    @commands.command()
    async def n(self, ctx: commands.Context):
        keyboard.press('n')
        time.sleep(0.5)
        keyboard.release('n')
    @commands.command()
    async def o(self, ctx: commands.Context):
        keyboard.press('o')
        time.sleep(0.5)
        keyboard.release('o')
    @commands.command()
    async def p(self, ctx: commands.Context):
        keyboard.press('p')
        time.sleep(0.5)
        keyboard.release('p')
    @commands.command()
    async def q(self, ctx: commands.Context):
        keyboard.press('q')
        time.sleep(0.5)
        keyboard.release('q')
    @commands.command()
    async def r(self, ctx: commands.Context):
        keyboard.press('r')
        time.sleep(0.5)
        keyboard.release('r')
    @commands.command()
    async def s(self, ctx: commands.Context):
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
    @commands.command()
    async def t(self, ctx: commands.Context):
        keyboard.press('t')
        time.sleep(0.5)
        keyboard.release('t')
    @commands.command()
    async def u(self, ctx: commands.Context):
        keyboard.press('u')
        time.sleep(0.5)
        keyboard.release('u')
    @commands.command()
    async def v(self, ctx: commands.Context):
        keyboard.press('v')
        time.sleep(0.5)
        keyboard.release('v')
    @commands.command()
    async def w(self, ctx: commands.Context):
        keyboard.press('w')
        time.sleep(0.5)
        keyboard.release('w')
    @commands.command()
    async def x(self, ctx: commands.Context):
        keyboard.press('x')
        time.sleep(0.5)
        keyboard.release('x')
    @commands.command()
    async def y(self, ctx: commands.Context):
        keyboard.press('y')
        time.sleep(0.5)
        keyboard.release('y')
    @commands.command()
    async def z(self, ctx: commands.Context):
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z')
    @commands.command()
    async def jump(self, ctx: commands.Context):
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')

    @commands.command()
    async def rjump(self, ctx: commands.Context):
        keyboard.press('d')
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
        keyboard.release('d')

    @commands.command()
    async def ljump(self, ctx: commands.Context):
        keyboard.press('a')
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
        keyboard.release('a')

    @commands.command()
    async def longjump(self, ctx: commands.Context):
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('space')

    @commands.command()
    async def rlongjump(self, ctx: commands.Context):
        keyboard.press('d')
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('d')
        keyboard.release('space')

    @commands.command()
    async def llongjump(self, ctx: commands.Context):
        keyboard.press('a')
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('a')
        keyboard.release('space')
    @commands.command()
    async def fjump(self, ctx: commands.Context):
        keyboard.press('w')
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
        keyboard.release('w')
    async def flongjump(self, ctx: commands.Context):
        keyboard.press('w')
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('space')
        keyboard.release('w')
    @commands.command()
    async def blongjump(self, ctx: commands.Context):
        keyboard.press('s')
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('space')
        keyboard.release('s')
    @commands.command()
    async def shift(self, ctx: commands.Context):
        keyboard.press('shift')
        time.sleep(20)
        keyboard.release('shift')
    @commands.command()
    async def alt(self, ctx: commands.Context):
        keyboard.press('alt')
        time.sleep(20)
        keyboard.release('alt')
    @commands.command()
    async def win(self, ctx: commands.Context):
        keyboard.press('left windows')
        time.sleep(0.5)
        keyboard.release('left windows')
    @commands.command()
    async def ctrl(self, ctx: commands.Context):
        keyboard.press('ctrl')
        time.sleep(1)
        keyboard.release('ctrl')
    async def tab(self, ctx: commands.Context):
        keyboard.press('tab')
        time.sleep(1)
        keyboard.release('tab')
    @commands.command()
    async def dot(self, ctx: commands.Context):
        keyboard.press('.')
        time.sleep(0.5)
        keyboard.release('.')
    @commands.command()
    async def comma(self, ctx: commands.Context):
        keyboard.press(',')
        time.sleep(0.5)
        keyboard.release(',')
    @commands.command()
    async def entr(self, ctx: commands.Context):
        keyboard.press('enter')
        time.sleep(0.5)
        keyboard.release('enter')
    @commands.command() 
    async def lmb(self, ctx: commands.Context):
       mouse.click('left')
    async def rmb(self, ctx: commands.Context):
       mouse.click('right')
    async def mmb(self, ctx: commands.Context):
       mouse.click('middle')

    @commands.command() 
    async def mouser(self, ctx: commands.Context):
       mouse.move(100, 0, absolute=False, duration=0.2)

    @commands.command() 
    async def mousel(self, ctx: commands.Context):
       mouse.move(-100, 0, absolute=False, duration=0.2)

    @commands.command() 
    async def moused(self, ctx: commands.Context):
       mouse.move(0, 100, absolute=False, duration=0.2)

    @commands.command() 
    async def mouseu(self, ctx: commands.Context):
       mouse.move(0, -100, absolute=False, duration=0.2)



bot = Bot()
bot.run()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
