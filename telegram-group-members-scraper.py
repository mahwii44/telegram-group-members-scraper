import telegram
from telegram import ChatMember

# initialize bot with token
bot = telegram.Bot(token='YOUR_API_')

# get the IDs of the source and target groups
source_group_id = 'SOURCE_GROUP_ID'
target_group_id = 'TARGET_GROUP_ID'

# get the list of members in the source group
source_chat_members = bot.get_chat_members(chat_id=source_group_id)

# filter the members list as required
filtered_chat_members = []
for chat_member in source_chat_members:
    if not chat_member.is_bot:
        filtered_chat_members.append(chat_member)

# add the members to the target group
for chat_member in filtered_chat_members:
    bot.add_chat_member(chat_id=target_group_id, user_id=chat_member.user.id)
