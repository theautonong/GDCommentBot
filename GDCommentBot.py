import gd
import asyncio
import random
import time

# ==== SETTINGS ====
USERNAME = "YourUsername"
PASSWORD = "YourPassword"

# id of the levels where u want to comment
LEVEL_IDS = [128, 133, 45678901, 98765432]

# possible comments
COMMENTS = [
    "test1",
    "gg easy 1 attempt",
    "your level sucks brou",
    "666 666 666 66 66 66 66 6 6 6 6 6 6 6  6 6 6 6 6 6 6 6 6",
    "this a Tuff",
    "XD",
    "Made By SailentCoder"
]

# delay (seconds)
DELAY_MIN = 15
DELAY_MAX = 45

# ==== BOT ====
async def comment_bot():
    client = gd.Client()
    await client.login(USERNAME, PASSWORD)
    print(f"logged in with {USERNAME}")

    for i in range(999):  # number of comments
        level_id = random.choice(LEVEL_IDS)
        comment = random.choice(COMMENTS)

        try:
            level = await client.get_level(level_id)
            await level.comment(comment)
            print(f"[{time.strftime('%H:%M:%S')}] Comentado en {level_id}: {comment}")

            # save LOG
            with open("bot_log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                        f"Nivel {level_id} → {comment}\n")

        except Exception as e:
            print(f"❌ Error comentando en {level_id}: {e}")

        # delay before comment
        delay = random.randint(DELAY_MIN, DELAY_MAX)
        print(f"waiting {delay} seconds...")
        await asyncio.sleep(delay)

asyncio.run(comment_bot())

