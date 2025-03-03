from environs import Env
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
DOMAIN_NAME = env.str("DOMAIN_NAME")  # Bot Domain name
ADMINS = list(map(int,env.list("ADMINS")))  # adminlar ro'yxati

