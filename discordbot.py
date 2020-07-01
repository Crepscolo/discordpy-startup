import discord
import urllib.request
from pdf2image import convert_from_path

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzI3OTk4NjIyODkyODE4NDQz.Xv0ADg.HT5xNZHdm3b84OQWaAs6YQiB-z8'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # !yoyakuで予約状況確認
    if message.content == '!yoyaku':
        #pdf取得
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/14R5ACADBt7byWchsQqhUIPvFEKkQySfymOcHbTHnih4"
        spreadsheet_gid = "0"
        pdf_export_url = spreadsheet_url + "/export?format=pdf&gid=" + spreadsheet_gid + "&range=A1:I30&portrait=false&size=8&fitw=true&vertical_alignment=top&horizontal_alignment=CENTER&scale=4&top_margin=0.00&bottom_margin=0.00&left_margin=0.00&right_margin=0.00"
        # scale 1= Normal 100% / 2= Fit to width / 3= Fit to height / 4= Fit to Page
        pdf_name = "output.pdf"
        urllib.request.urlretrieve(pdf_export_url, pdf_name)
        
        #画像変換
        image = convert_from_path(pdf_name)
        image[0].save('output.png', 'png')

        #変換した画像ファイル送信
        await message.channel.send(file=discord.File('output.png'))
    # !totsuで凸状況確認
    if message.content == '!totsu' or message.content == '!totu':
        #pdf取得
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/1hQaqjBtOYnbdzfZOvAFWa5hSQuX4ccMmW1KDXhyXAo0"
        spreadsheet_gid = "216084460"
        pdf_export_url = spreadsheet_url + "/export?format=pdf&gid=" + spreadsheet_gid + "&range=B8:R39&portrait=false&size=8&fitw=true&vertical_alignment=top&horizontal_alignment=CENTER&scale=4&top_margin=0.00&bottom_margin=0.00&left_margin=0.00&right_margin=0.00"
        pdf_name = "totsu.pdf"
        urllib.request.urlretrieve(pdf_export_url, pdf_name)
        
        #画像変換
        image = convert_from_path(pdf_name)
        image[0].save('totsu.png', 'png')

        #変換した画像ファイル送信
        await message.channel.send(file=discord.File('totsu.png'))
    # !timeで凸終了希望時間出力
    if message.content == '!time':
        #pdf取得
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/14R5ACADBt7byWchsQqhUIPvFEKkQySfymOcHbTHnih4"
        spreadsheet_gid = "666886204"
        pdf_export_url = spreadsheet_url + "/export?format=pdf&gid=" + spreadsheet_gid + "&range=D1:P36&portrait=false&size=8&fitw=true&vertical_alignment=top&horizontal_alignment=CENTER&scale=4&top_margin=0.00&bottom_margin=0.00&left_margin=0.00&right_margin=0.00"
        pdf_name = "time.pdf"
        urllib.request.urlretrieve(pdf_export_url, pdf_name)
        
        #画像変換
        image = convert_from_path(pdf_name)
        image[0].save('time.png', 'png')

        #変換した画像ファイル送信
        await message.channel.send(file=discord.File('time.png'))
    if message.content == '!キャルちゃん':
        await message.channel.send('ヤバいわよ！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
