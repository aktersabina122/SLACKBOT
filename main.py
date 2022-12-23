
import slack                        # importing Slack
import os                           # importing Operating System
from pathlib import Path            # importing Python library pathlib 
from dotenv import load_dotenv      # it will load the env file


env_path = Path('.') / '.env'       # env file path
load_dotenv(dotenv_path=env_path)   # it will laod env file

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])  #we are using WebClient, load the actual value and pass that in as a token
client.chat_postMessage(channel='#test', text="Hello!")    #put our channel name, my one is "Test" and the text I want to see in client.chat_postMessage

