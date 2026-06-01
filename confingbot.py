import re
from telethon.sync import TelegramClient

# --- تنظیمات شما ---
# مقادیر زیر را با اطلاعاتی که از my.telegram.org گرفتید جایگزین کنید
api_id = 1234567  # فقط عدد بدون کوتیشن
api_hash = 'YOUR_API_HASH_HERE'

# آیدی کانالی که می‌خواهید کانفیگ‌ها را از آن بردارید (بدون @ یا با @)
channel_username = 'Channel_ID_Here' 

# تعداد پیام‌های آخری که می‌خواهید اسکریپت بررسی کند
limit_messages = 200 
# -------------------

# الگوهای رایج کانفیگ برای جستجو در متن
config_pattern = r'(vmess://\S+|vless://\S+|trojan://\S+|ss://\S+)'

client = TelegramClient('my_session', api_id, api_hash)

async def main():
    configs = []
    print(f"در حال جستجو در کانال {channel_username}...")
    
    # دریافت پیام‌های کانال
    async for message in client.iter_messages(channel_username, limit=limit_messages):
        if message.text:
            # پیدا کردن تمام لینک‌هایی که با الگوهای بالا مطابقت دارند
            found = re.findall(config_pattern, message.text)
            configs.extend(found)
    
    # حذف کانفیگ‌های تکراری
    configs = list(set(configs))
    
    # ذخیره در فایل متنی
    with open('sub.txt', 'w', encoding='utf-8') as f:
        for config in configs:
            f.write(config + '\n')
            
    print(f"عملیات موفقیت‌آمیز بود! تعداد {len(configs)} کانفیگ در فایل sub.txt ذخیره شد.")

# اجرای برنامه
with client:
    client.loop.run_until_complete(main())
