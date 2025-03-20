import pywhatkit as kit

# Group ID (you can get this from the WhatsApp web URL of the group)
group_id = "CoK4INaZyrA4J2OUhOrB75"

# Message to send
message = "Hello, Test message."

# Time to send the message (24-hour format, local time)
hour = 15  # 3 PM
minute = 39

# Send the message
kit.sendwhatmsg_to_group(group_id, message, hour, minute, wait_time=10)