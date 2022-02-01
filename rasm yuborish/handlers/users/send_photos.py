from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from keyboards.inline.buy_book import book_keys
from loader import dp, bot

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_file_id_photo(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_file_id_video(message: types.Message):
    await message.reply(message.video.file_id)

@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    # id orqali rasm yuborish
    photo_id='AgACAgIAAxkBAANfYcGUc-ygnthAR4ph8b9X2zByF30AAgO5MRuN1whKr-xJW-yh7DsBAAMCAAN4AAMjBA'
    # link orqali rasm yuborish
    # photo_url='https://kitoblardunyosi.uz/image/cache/catalog/001-Kitoblar/003_boshqalar/006_ilmiy_ommabop/python-web-500x500h.jpg'
    # kompyuter dagi rasmlardan foydalanish
    # photo_file=InputFile(path_or_bytesio="photos/kitob.jpg")
    msg="<b>Pythonda Dasturlash Asoslari</b> kitobi.\n"
    msg+="Narxi: 5000 so'm\n\n"
    msg+="<b>Kitob quyidagi do'konlarda sotiladi: </b>\n 👉Kitoblar Olami\n 👉Akadem Nashr\n 👉Azon Kitoblari\n 👉Hilol nashr"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)
    # await message.reply_photo(photo_file, caption="Dasturlash asoslari kitobi\n" "Narxi 50000 so'm")
    # await message.answer_photo(photo_id, caption="Dasturlash asoslari kitobi\n" "Narxi 50000 so'm")
    # await bot.send_photo(chat_id=message.from_user.id, photo=photo_url,
    #                      caption="Dasturlash asoslari kitobi\n" "Narxi 50000 so'm")

@dp.message_handler(Command("mevalar"))
async def send_fruits(message: types.Message):
    album=types.MediaGroup()
    photo1="AgACAgIAAxkBAANwYcHg9XGEpbN6OulqQhaKs1PU-84AArS7MRuN1xBKyQeOxpvzHNkBAAMCAAN4AAMjBA"
    photo2="AgACAgIAAxkBAANyYcHhovMYZf9yvClu05m2gEgDiFMAArW7MRuN1xBK_-lBtkxcpl0BAAMCAAN5AAMjBA"
    photo3=InputFile(path_or_bytesio="photos/ananas.jpeg")
    photo4=InputFile(path_or_bytesio="photos/banana.jpeg")
    photo5="https://www.pngall.com/wp-content/uploads/2016/03/Fruit-Transparent-180x180.png"
    video1="BAACAgIAAxkBAAOEYcHl-UGtgMz9Xqcep49rk5NyygoAAq8VAAKN1xBKBokn7oeeJ8sjBA"
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)
    album.attach_photo(photo=photo5)
    album.attach_video(video=video1)
    await message.reply_media_group(media=album)