# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready(): 
  async def message(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))

  print("[ Bot Start ] \n-- 봇이 시작되었습니다 -- \n봇 제작자 : 짱구지롱\n")
  print(("""[ Bot Info ]\n[1] Bot Name : {} \n[2] Bot Discord ID : {}""").format(client.user.name, client.user.id))
  await message(['제작자 : sinzzanggu22 | 짱구 🙇 모든 문의 DM!'])

        # 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio

@client.event
async def on_message(message):
    if message.content == "!안녕": # 메세지 감지
        await message.channel.send ("{} | {}, 웅 안녕!!".format(message.author, message.author.mention))
    
    if message.content == "!수수료": # 메세지 감지
        embed = discord.Embed(title="수수료 계산", color=0x00ff00)

        embed.add_field(name="임베드 라인 1 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)
        embed.add_field(name="임베드 라인 2 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)

        embed.add_field(name="임베드 라인 3 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
        embed.add_field(name="임베드 라인 4 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)

        await message.channel.send (embed=embed)

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('MTIwODI1MDc0NjQ2NzAwMDQxMA.GIM7wo.omsviSprDezasy3ZcszdMiGktgC9VsmVDLU-iM')
