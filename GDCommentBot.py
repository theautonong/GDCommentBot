# Made by sailentcoder and HUGEEEE thanks to rigmatter12
import gd
import asyncio
import random
import time

# ==== CONFIGURATION ====
USERNAME = "YourUsername"      # Your GD username
PASSWORD = "YourPassword"      # Your GD password

# Unique levels and comments (use sets for uniqueness)
LEVEL_IDS = {128, 133, 45678901, 98765432}
COMMENTS = {
    "Nice level",
    "Rateworhthy",
    "XD",
    "This is a bot test "
}

# Delay between comments (seconds)
DELAY_MIN = 15
DELAY_MAX = 45

# Number of comments to send
TOTAL_COMMENTS = 10

# ==== BOT ====
async def comment_bot():
    client = gd.Client()
    
    # --- LOGIN ---
    try:
        await client.login(USERNAME, PASSWORD)
        print(f" Logged in as {USERNAME}")
    except gd.LoginError:
        print(" Login failed: invalid username or password.")
        return

    # --- COMMENT LOOP ---
    for i in range(TOTAL_COMMENTS):
        level_id = random.choice(list(LEVEL_IDS))
        comment = random.choice(list(COMMENTS))
        
        try:
            level = await client.get_level(level_id)
            
            # Retry mechanism (up to 3 tries)
            for attempt in range(3):
                try:
                    await level.comment(comment)
                    print(f"[{time.strftime('%H:%M:%S')}] Commented on {level_id}: {comment}")
                    
                    # Save log
                    with open("bot_log.txt", "a", encoding="utf-8") as f:
                        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                                f"Level {level_id} → {comment}\n")
                    break  # success, exit retry loop

                except gd.CommentBanned:
                    print("Comment failed: you are banned from commenting.")
                    return
                except Exception as e:
                    print(f"Error on attempt {attempt+1} for level {level_id}: {e}")
                    await asyncio.sleep(5)  # small wait before retry

        except Exception as e:
            print(f" Could not load level {level_id}: {e}")
            continue

        # Wait before next comment
        delay = random.randint(DELAY_MIN, DELAY_MAX)
        print(f" Waiting {delay} seconds before next comment...")
        await asyncio.sleep(delay)

asyncio.run(comment_bot())

