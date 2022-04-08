import discord
import os
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
import requests
import pandas as pd

intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

TOKEN = os.environ.get('BOT_TOKEN')

raw_data = requests.get("https://sdh.sen.hs.kr/index.do")

url = requests.get("https://sdh.sen.hs.kr/index.do")


@bot.event
async def on_ready():
    print('봇 이름 : ' + bot.user.name)
    print('성공적으로 봇이 시작되었습니다.')
soup = BeautifulSoup(raw_data.text, 'html.parser')

lunch = soup.select_one("div.index_mlsv_box")

link = BeautifulSoup(url.text, 'html.parser')

time = {"​​​​​​​​      월": ["영어", "영어", "음악", "직업", "직업", "직업", "직업"], " 화": ["탐색", "국어", "수학", "체육", "체육", "음악", "음악", ], "수":
        ["국어", "탐색", "탐색", "창체", "창체", "창체", "없음"], "목": ["언어", "언어", "체육", "논술", "국어", "수학", "수학"], "금": ["화면", "화면", "화면", "탐색", "논술", "체육", "언어"]}

# time = {" 월,화,수,목,금":["영어 영어 음악 직업 직업 직업 직업","","3","4","5","6","7"]}

time_chart = pd.DataFrame(
    time, index=["1교시", "2교시", "3교시", "4교시", "5교시", "6교시", "7교시"])


@bot.event
async def on_message(message):
    if message.content == "!오늘 급식" or message.content == "!오늘급식" or message.content == "!급식" or message.content == "!급식 확인" or message.content == "!":
        embed = discord.Embed(title="서울디지텍고등학교 급식", description="**```" + str(lunch.text).replace("급식 전체보기", '').replace(
            "\n", '').replace("\t", '').replace(" ", "") + "```**", color=0x62c1cc)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        await message.channel.send(embed=embed)  # embed를 포함 한 채로 메시지를 전송합니다.
    if message.content == "!시간표":
        embed = discord.Embed(title="서울디지텍고등학교 시간표", description="**```" +
                              str(time_chart).replace("           ", "")+"```**")
        await message.channel.send(embed=embed)

bot.run(TOKEN)
