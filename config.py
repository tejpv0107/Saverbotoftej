# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28331645"))
API_HASH = getenv("API_HASH", "021a31c647f7a20ad490b7ab5ee2f150")
BOT_TOKEN = getenv("BOT_TOKEN", "8909926543:AAEP1Emfmtv-V17HZCIBRUQCuEOVha6LdVY")
OWNER_ID = int(getenv("OWNER_ID", "6501759311"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
