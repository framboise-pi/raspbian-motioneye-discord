# raspberry-motioneye-discord by umoder.space
# v1.0
from discord_webhook import DiscordWebhook,DiscordEmbed
import glob,os,datetime,urllib

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/CHANGE_THIS_WITH_YOUR_DISCORD_WEBHOOK_URL', username="DISCORDBOTNAME")

# change folder to your Camera folder
# will get the last .jpg from the current day
folder = '/home/pi/motioneye/lib/Camera1/' + datetime.datetime.today().strftime('%Y-%m-%d')
list_of_files = glob.glob(folder + '/*.jpg')
latest_file = max(list_of_files, key=os.path.getctime)
with open(latest_file, "rb") as f:
    webhook.add_file(file=f.read(), filename=latest_file)

embed = DiscordEmbed(title='MOTION DETECTION - ', description = 'timestamp : ' + datetime.datetime.today().strftime('%Y-%m-%d %Hh%mmn'), color=242424)

webhook.add_embed(embed)
response = webhook.execute()
