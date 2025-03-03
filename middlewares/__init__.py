from loader import dp
from .throttling import ThrottlingMiddleware
from .checksub import BigBrother


if __name__ == "middlewares":
    dp.message.middleware(ThrottlingMiddleware())
    dp.update.outer_middleware(BigBrother())
