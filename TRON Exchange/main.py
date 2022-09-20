import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from binance.client import Client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_KEY, SECRET_KEY, TOKEN
from validate_email import validate_email
import telegram_send

storage = MemoryStorage()
client = Client(API_KEY, SECRET_KEY)
TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
markup0 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup0.add('Exchange USDT', 'Support')
markup1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup1.add('USDT (TRC-20)', 'USDT (BEP-20)', 'Go back to the start')
markup2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup2.add('Exchange USDT for BTC', 'Exchange USDT for TRX', 'Exchange USDT for ETH', 'Back', 'Back to menu')
markup3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup3.add('Select the amount of USDT', 'Back', 'Back to menu')
markup4 = ReplyKeyboardMarkup(resize_keyboard=True)
markup4.add('Yes', 'Back', 'Back to menu')
markup5 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup5.add('I paid', 'Cancel the ticket and back to')
a = ReplyKeyboardRemove()
urlKB = InlineKeyboardMarkup(row_width=1)
urlButton =InlineKeyboardButton(text='Support', url='https://t.me/L1mbbbbb')
urlKB.add(urlButton)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)

class FSMmain(StatesGroup):
    name_net = State()
    choise_coin_trc = State()
    choise_coin_bep = State()
    select_sum_btc = State()
    select_sum_trx = State()
    select_sum_eth = State()
    enter_sum_btc = State()
    enter_sum_trx = State()
    enter_sum_eth = State()
    y_or_n_btc = State()
    y_or_n_trx = State()
    y_or_n_eth = State()
    enter_wallet_btc = State()
    enter_wallet_trx = State()
    enter_wallet_eth = State()
    enter_eMail_btc = State()
    enter_eMail_trx = State()
    enter_eMail_eth = State()
    i_paid_btc = State()
    i_paid_trx = State()
    i_paid_eth = State()
    select_sum_btc_bep = State()
    select_sum_trx_bep = State()
    select_sum_eth_bep = State()
    enter_sum_btc_bep = State()
    enter_sum_trx_bep = State()
    enter_sum_eth_bep = State()
    y_or_n_btc_bep = State()
    y_or_n_trx_bep = State()
    y_or_n_eth_bep = State()
    enter_wallet_btc_bep = State()
    enter_wallet_trx_bep = State()
    enter_wallet_eth_bep = State()
    enter_eMail_btc_bep = State()
    enter_eMail_trx_bep = State()
    enter_eMail_eth_bep = State()
    i_paid_btc_bep = State()
    i_paid_trx_bep = State()
    i_paid_eth_bep = State()
@dp.message_handler(content_types=['text'], state=None)
async def main(message: types.Message):
    if message.text == 'Exchange USDT':
        await FSMmain.name_net.set()
        await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)

        @dp.message_handler(state=FSMmain.name_net)
        async def coin_price_vuvod(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['name_net'] = message.text
            if data['name_net'] == 'USDT (TRC-20)':
                await FSMmain.choise_coin_trc.set()
                await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)

                @dp.message_handler(state=FSMmain.choise_coin_trc)
                async def coin_price_vuvod(message: types.Message, state: FSMContext):
                    async with state.proxy() as data:
                        data['choise_coin_trc'] = message.text
                        if data['choise_coin_trc'] == 'Exchange USDT for BTC':
                            await FSMmain.select_sum_btc.set()
                            btc = client.get_symbol_ticker(symbol='BTCUSDT')
                            btc_get = str(round(float(btc.get('price')), 0) - (round(float(btc.get('price')), 0) / 100 * 10.5))
                            await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  BTC (Bitcoin)\n\nExchange rate: 1 BTC (Bitcoin) = {btc_get} {data["name_net"]}\n\nThe reserve is: 5,3268427  BTC (Bitcoin)\n\nMinimum exchange amount USDT for BTC (Bitcoin) = 100.0 USDT\nMaximum exchange amount USDT for BTC (Bitcoin) = 100000.0\nUSDT', reply_markup=markup3)

                            @dp.message_handler(state=FSMmain.select_sum_btc)
                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                async with state.proxy() as data:
                                    data['select_sum_btc'] = message.text
                                if data['select_sum_btc'] == 'Select the amount of USDT':
                                    await FSMmain.enter_sum_btc.set()
                                    await bot.send_message(message.from_user.id, f'Exchange rate:\n1 BTC (Bitcoin) = {btc_get} {data["name_net"]}\nThe reserve is: 5,3268427 BTC (Bitcoin)\n--------------------------\nHow many USDT do you want to exchange?\n‼️ Minimum USDT - 100 ‼️', reply_markup=a)

                                    @dp.message_handler(state=FSMmain.enter_sum_btc)
                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                        async with state.proxy() as data:
                                            data['enter_sum_btc'] = message.text
                                        if float(data['enter_sum_btc']) < 100:
                                            await FSMmain.enter_sum_btc.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, less than 100 cannot be!\n\nEnter again')
                                        elif float(data['enter_sum_btc']) >= 100:
                                            await FSMmain.y_or_n_btc.set()
                                            await bot.send_message(message.from_user.id, f'You are giving away: {data["enter_sum_btc"]} {data["name_net"]}', reply_markup=markup4)

                                            @dp.message_handler(state=FSMmain.y_or_n_btc)
                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                async with state.proxy() as data:
                                                    data['y_or_n_btc'] = message.text
                                                if data['y_or_n_btc'] == 'Yes':
                                                    await FSMmain.enter_wallet_btc.set()
                                                    you_get_btc = str(float(data['enter_sum_btc']) / float(btc_get))
                                                    await bot.send_message(message.from_user.id, f"You are giving away: {data['enter_sum_btc']} {data['name_net']} You'll get: {you_get_btc} BTC (Bitcoin)")
                                                    await bot.send_message(message.from_user.id, f'Enter your BTC (Bitcoin) wallet to which you want to receive BTC (TRC-20)', reply_markup=a)

                                                    @dp.message_handler(state=FSMmain.enter_wallet_btc)
                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                        async with state.proxy() as data:
                                                            data['enter_wallet_btc'] = message.text
                                                        if len(data['enter_wallet_btc']) == 34:
                                                            await FSMmain.enter_eMail_btc.set()
                                                            await bot.send_message(message.from_user.id, 'Enter your email address to confirm the transaction', reply_markup=a)

                                                            @dp.message_handler(state=FSMmain.enter_eMail_btc)
                                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                async with state.proxy() as data:
                                                                    data['enter_eMail_btc'] = message.text
                                                                is_valid = validate_email(data['enter_eMail_btc'])
                                                                if is_valid == True:
                                                                    await FSMmain.i_paid_btc.set()
                                                                    await bot.send_message(message.from_user.id, f'Wallet where you receive: {data["enter_wallet_btc"]}\n\nAmount of transfer: {data["enter_sum_btc"]} {data["name_net"]}\n\nTotal: {you_get_btc} BTC (Bitcoin)\n\nOpen the client from where you will transfer USDT, and enter the following information:\nTVc2areVhY1h1PTYRzSgAMNos4wgbQywGN\n\n‼️{data["name_net"]}‼️', reply_markup=markup5)
                                                                    await bot.send_message(message.from_user.id, '‼️Your ticket has been created, pay the amount of USDT specified in the application to the wallet specified above, after payment, click the "I paid" button.‼️')

                                                                    @dp.message_handler(state=FSMmain.i_paid_btc)
                                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                        async with state.proxy() as data:
                                                                            data['i_paid_btc'] = message.text
                                                                        if data['i_paid_btc'] == 'I paid':
                                                                            await bot.send_message(message.from_user.id, '✅ Your order has been accepted')
                                                                            await bot.send_message(message.from_user.id, f'Order created!\nYou exchanged: {data["enter_sum_btc"]} {data["name_net"]} on the {you_get_btc}\nBTC (Bitcoin)\nOrder status:\nWaiting for the receipt of funds...', reply_markup=markup0)
                                                                            telegram_send.send(messages=[f'New order!\nName: {message.from_user.full_name}\nLogin: {message.from_user.username}\nName net: {data["name_net"]}\nName coin: {data["choise_coin_trc"]}\nHow many USDT: {data["enter_sum_btc"]} in BTC = {you_get_btc}\nWallet: {data["enter_wallet_btc"]}\nE-mail: {data["enter_eMail_btc"]}'])
                                                                            await state.finish()
                                                                        elif data['i_paid_btc'] == 'Cancel the ticket and back to':
                                                                            await FSMmain.name_net.set()
                                                                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                                                                        else:
                                                                            await FSMmain.i_paid_btc.set()
                                                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup5)
                                                                elif is_valid == False:
                                                                    await FSMmain.enter_eMail_btc.set()
                                                                    await bot.send_message(message.from_user.id, 'E-mail entered incorrectly\n\nEnter again')
                                                        elif len(data['enter_wallet_btc']) > 34 or len(data['enter_wallet_btc']) < 34:
                                                            await FSMmain.enter_wallet_btc.set()
                                                            await bot.send_message(message.from_user.id, 'Sorry, the number of characters must be 34!\n\nEnter again')
                                                elif data['y_or_n_btc'] == 'Back':
                                                    await FSMmain.select_sum_btc.set()
                                                    await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  BTC (Bitcoin)\n\nExchange rate: 1 BTC (Bitcoin) = {btc_get} {data["name_net"]}\n\nThe reserve is: 5,3268427  BTC (Bitcoin)\n\nMinimum exchange amount USDT for BTC (Bitcoin) = 100.0 USDT\nMaximum exchange amount USDT for BTC (Bitcoin) = 100000.0\nUSDT', reply_markup=markup3)
                                                elif data['y_or_n_btc'] == 'Back to menu':
                                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                                    await state.finish()
                                                else:
                                                    await FSMmain.y_or_n_btc.set()
                                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup4)
                                        else:
                                            await FSMmain.select_sum_btc.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                                elif data['select_sum_btc'] == 'Back':
                                    await FSMmain.choise_coin_trc.set()
                                    await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)
                                elif data['select_sum_btc'] == 'Back to menu':
                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                    await state.finish()
                                else:
                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                        elif data['choise_coin_trc'] == 'Exchange USDT for TRX':
                            await FSMmain.select_sum_trx.set()
                            trx = client.get_symbol_ticker(symbol='TRXUSDT')
                            trx_get = str(round(float(trx.get('price')), 2) - (round(float(trx.get('price')), 2) / 100 * 10.5))
                            await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  TRX (BEP-20)\n\nExchange rate: 1 TRX (BEP-20) = {trx_get} {data["name_net"]}\n\nThe reserve is: 671350  TRX (BEP-20)\n\nMinimum exchange amount USDT for TRX (BEP-20) = 100.0 USDT\nMaximum exchange amount USDT for TRX (BEP-20) = 100000.0\nUSDT', reply_markup=markup3)

                            @dp.message_handler(state=FSMmain.select_sum_trx)
                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                async with state.proxy() as data:
                                    data['select_sum_trx'] = message.text
                                if data['select_sum_trx'] == 'Select the amount of USDT':
                                    await FSMmain.enter_sum_trx.set()
                                    await bot.send_message(message.from_user.id, f'Exchange rate:\n1 TRX (BEP-20) = {trx_get} {data["name_net"]}\nThe reserve is: 671350 TRX (BEP-20)\n--------------------------\nHow many USDT do you want to exchange?\n‼️ Minimum USDT - 100 ‼️',reply_markup=a)

                                    @dp.message_handler(state=FSMmain.enter_sum_trx)
                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                        async with state.proxy() as data:
                                            data['enter_sum_trx'] = message.text
                                        if float(data['enter_sum_trx']) < 100:
                                            await FSMmain.enter_sum_trx.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, less than 100 cannot be!\n\nEnter again')
                                        elif float(data['enter_sum_trx']) >= 100:
                                            await FSMmain.y_or_n_trx.set()
                                            await bot.send_message(message.from_user.id, f'You are giving away: {data["enter_sum_trx"]} {data["name_net"]}', reply_markup=markup4)

                                            @dp.message_handler(state=FSMmain.y_or_n_trx)
                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                async with state.proxy() as data:
                                                    data['y_or_n_trx'] = message.text
                                                if data['y_or_n_trx'] == 'Yes':
                                                    await FSMmain.enter_wallet_trx.set()
                                                    you_get_trx = str(float(data['enter_sum_trx']) / float(trx_get))
                                                    await bot.send_message(message.from_user.id, f"You are giving away: {data['enter_sum_trx']} {data['name_net']}\n\nYou'll get: {you_get_trx} TRX")
                                                    await bot.send_message(message.from_user.id, f'Enter your TRX wallet to which you want to receive TRX (TRC-20)',reply_markup=a)

                                                    @dp.message_handler(state=FSMmain.enter_wallet_trx)
                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                        async with state.proxy() as data:
                                                            data['enter_wallet_trx'] = message.text
                                                        if len(data['enter_wallet_trx']) == 42:
                                                            await FSMmain.enter_eMail_trx.set()
                                                            await bot.send_message(message.from_user.id, 'Enter your email address to confirm the transaction', reply_markup=a)

                                                            @dp.message_handler(state=FSMmain.enter_eMail_trx)
                                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                async with state.proxy() as data:
                                                                    data['enter_eMail_trx'] = message.text
                                                                is_valid = validate_email(data['enter_eMail_trx'])
                                                                if is_valid == True:
                                                                    await FSMmain.i_paid_trx.set()
                                                                    await bot.send_message(message.from_user.id, f'Wallet where you receive: {data["enter_wallet_trx"]}\n\nAmount of transfer: {data["enter_sum_trx"]} {data["name_net"]}\n\nTotal: {you_get_trx} TRX (BEP-20)\n\nOpen the client from where you will transfer USDT, and enter the following information:\nTVc2areVhY1h1PTYRzSgAMNos4wgbQywGN\n\n‼️{data["name_net"]}‼️', reply_markup=markup5)
                                                                    await bot.send_message(message.from_user.id, '‼️Your ticket has been created, pay the amount of USDT specified in the application to the wallet specified above, after payment, click the "I paid" button.‼️')

                                                                    @dp.message_handler(state=FSMmain.i_paid_trx)
                                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                        async with state.proxy() as data:
                                                                            data['i_paid_trx'] = message.text
                                                                        if data['i_paid_trx'] == 'I paid':
                                                                            await bot.send_message(message.from_user.id, '✅ Your order has been accepted')
                                                                            await bot.send_message(message.from_user.id, f'Order created!\nYou exchanged: {data["enter_sum_trx"]} {data["name_net"]} on the {you_get_trx}\nTRX (BEP-20)\nOrder status:\nWaiting for the receipt of funds...', reply_markup=markup0)
                                                                            telegram_send.send(messages=[f'New order!\nName: {message.from_user.full_name}\nLogin: {message.from_user.username}\nName net: {data["name_net"]}\nName coin: {data["choise_coin_trc"]}\nHow many USDT: {data["enter_sum_trx"]} in TRX = {you_get_trx}\nWallet: {data["enter_wallet_trx"]}\nE-mail: {data["enter_eMail_trx"]}'])
                                                                            await state.finish()
                                                                        elif data['i_paid_trx'] == 'Cancel the ticket and back to':
                                                                            await FSMmain.name_net.set()
                                                                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                                                                        else:
                                                                            await FSMmain.i_paid_trx.set()
                                                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup5)
                                                                elif is_valid == False:
                                                                    await FSMmain.enter_eMail_trx.set()
                                                                    await bot.send_message(message.from_user.id, 'E-mail entered incorrectly\n\nEnter again')
                                                        elif len(data['enter_wallet_trx']) > 42 or len(data['enter_wallet_trx']) < 42:
                                                            await FSMmain.enter_wallet_trx.set()
                                                            await bot.send_message(message.from_user.id, 'Sorry, the number of characters must be 42!\n\nEnter again')
                                                elif data['y_or_n_trx'] == 'Back':
                                                    await FSMmain.select_sum_trx.set()
                                                    await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  TRX (BEP-20)\n\nExchange rate: 1 TRX (BEP-20) = {trx_get} {data["name_net"]}\n\nThe reserve is: 671350  TRX (BEP-20)\n\nMinimum exchange amount USDT for TRX (BEP-20) = 100.0 USDT\nMaximum exchange amount USDT for TRX (BEP-20) = 100000.0\nUSDT', reply_markup=markup3)
                                                elif data['y_or_n_trx'] == 'Back to menu':
                                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                                    await state.finish()
                                                else:
                                                    await FSMmain.y_or_n_trx.set()
                                                    await bot.send_message(message.from_user.id,'Sorry, I can’t understand you', reply_markup=markup4)

                                elif data['select_sum_trx'] == 'Back':
                                    await FSMmain.choise_coin_trc.set()
                                    await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)
                                elif data['select_sum_trx'] == 'Back to menu':
                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                    await state.finish()
                                else:
                                    await FSMmain.select_sum_trx.set()
                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                        elif data['choise_coin_trc'] == 'Exchange USDT for ETH':
                            await FSMmain.select_sum_eth.set()
                            eth = client.get_symbol_ticker(symbol='ETHUSDT')
                            eth_get = str(round(float(eth.get('price')), 2) - (round(float(eth.get('price')), 2) / 100 * 10.5))
                            await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  ETH (ERC-20)\n\nExchange rate: 1 ETH (ERC-20) = {eth_get} {data["name_net"]}\n\nThe reserve is: 1432  ETH (ERC-20)\n\nMinimum exchange amount USDT for ETH (ERC-20) = 100.0 USDT\nMaximum exchange amount USDT for ETH (ERC-20) = 100000.0\nUSDT', reply_markup=markup3)

                            @dp.message_handler(state=FSMmain.select_sum_eth)
                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                async with state.proxy() as data:
                                    data['select_sum_eth'] = message.text
                                if data['select_sum_eth'] == 'Select the amount of USDT':
                                    await FSMmain.enter_sum_eth.set()
                                    await bot.send_message(message.from_user.id, f'Exchange rate:\n1 ETH (ERC-20) = {eth_get} {data["name_net"]}\nThe reserve is: 1432 ETH (ERC-20)\n--------------------------\nHow many USDT do you want to exchange?\n‼️ Minimum USDT - 100 ‼️',reply_markup=a)

                                    @dp.message_handler(state=FSMmain.enter_sum_eth)
                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                        async with state.proxy() as data:
                                            data['enter_sum_eth'] = message.text
                                        if float(data['enter_sum_eth']) < 100:
                                            await FSMmain.enter_sum_eth.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, less than 100 cannot be!\n\nEnter again')
                                        elif float(data['enter_sum_eth']) >= 100:
                                            await FSMmain.y_or_n_eth.set()
                                            await bot.send_message(message.from_user.id, f'You are giving away: {data["enter_sum_eth"]} {data["name_net"]}', reply_markup=markup4)

                                            @dp.message_handler(state=FSMmain.y_or_n_eth)
                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                async with state.proxy() as data:
                                                    data['y_or_n_eth'] = message.text
                                                if data['y_or_n_eth'] == 'Yes':
                                                    await FSMmain.enter_wallet_eth.set()
                                                    you_get_eth = str(float(data['enter_sum_eth']) / float(eth_get))
                                                    await bot.send_message(message.from_user.id, f"You are giving away: {data['enter_sum_eth']} {data['name_net']}\n\nYou'll get: {you_get_eth} ETH")
                                                    await bot.send_message(message.from_user.id, f'Enter your ETH wallet to which you want to receive ETH (TRC-20)', reply_markup=a)

                                                    @dp.message_handler(state=FSMmain.enter_wallet_eth)
                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                        async with state.proxy() as data:
                                                            data['enter_wallet_eth'] = message.text
                                                        if len(data['enter_wallet_eth']) == 42:
                                                            await FSMmain.enter_eMail_eth.set()
                                                            await bot.send_message(message.from_user.id, 'Enter your email address to confirm the transaction', reply_markup=a)

                                                            @dp.message_handler(state=FSMmain.enter_eMail_eth)
                                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                async with state.proxy() as data:
                                                                    data['enter_eMail_eth'] = message.text
                                                                is_valid = validate_email(data['enter_eMail_eth'])
                                                                if is_valid == True:
                                                                    await FSMmain.i_paid_eth.set()
                                                                    await bot.send_message(message.from_user.id, f'Wallet where you receive: {data["enter_wallet_eth"]}\n\nAmount of transfer: {data["enter_sum_eth"]} {data["name_net"]}\n\nTotal: {you_get_eth} ETH (ERC-20)\n\nOpen the client from where you will transfer USDT, and enter the following information:\nTVc2areVhY1h1PTYRzSgAMNos4wgbQywGN\n\n‼️{data["name_net"]}‼️', reply_markup=markup5)
                                                                    await bot.send_message(message.from_user.id, '‼️Your ticket has been created, pay the amount of USDT specified in the application to the wallet specified above, after payment, click the "I paid" button.‼️')

                                                                    @dp.message_handler(state=FSMmain.i_paid_eth)
                                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                        async with state.proxy() as data:
                                                                            data['i_paid_eth'] = message.text
                                                                        if data['i_paid_eth'] == 'I paid':
                                                                            await bot.send_message(message.from_user.id, '✅ Your order has been accepted')
                                                                            await bot.send_message(message.from_user.id, f'Order created!\nYou exchanged: {data["enter_sum_eth"]} {data["name_net"]} on the {you_get_eth}\nETH (ERC-20)\nOrder status:\nWaiting for the receipt of funds...', reply_markup=markup0)
                                                                            telegram_send.send(messages=[f'New order!\nName: {message.from_user.full_name}\nLogin: {message.from_user.username}\nName net: {data["name_net"]}\nName coin: {data["choise_coin_trc"]}\nHow many USDT: {data["enter_sum_eth"]} in ETH = {you_get_eth}\nWallet: {data["enter_wallet_eth"]}\nE-mail: {data["enter_eMail_eth"]}'])
                                                                            await state.finish()
                                                                        elif data['i_paid_eth'] == 'Cancel the ticket and back to':
                                                                            await FSMmain.name_net.set()
                                                                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                                                                        else:
                                                                            await FSMmain.i_paid_eth.set()
                                                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup5)
                                                                elif is_valid == False:
                                                                    await FSMmain.enter_eMail_eth.set()
                                                                    await bot.send_message(message.from_user.id, 'E-mail entered incorrectly\n\nEnter again')
                                                        elif len(data['enter_wallet_eth']) > 42 or len(data['enter_wallet_eth']) < 42:
                                                            await FSMmain.enter_wallet_eth.set()
                                                            await bot.send_message(message.from_user.id, 'Sorry, the number of characters must be 42!\n\nEnter again')
                                                elif data['y_or_n_eth'] == 'Back':
                                                    await FSMmain.select_sum_eth.set()
                                                    await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  ETH (ERC-20)\n\nExchange rate: 1 ETH (ERC-20) = {eth_get} {data["name_net"]}\n\nThe reserve is: 1432  ETH (ERC-20)\n\nMinimum exchange amount USDT for ETH (ERC-20) = 100.0 USDT\nMaximum exchange amount USDT for ETH (ERC-20) = 100000.0\nUSDT', reply_markup=markup3)
                                                elif data['y_or_n_eth'] == 'Back to menu':
                                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                                    await state.finish()
                                                else:
                                                    await FSMmain.y_or_n_eth.set()
                                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup4)
                                elif data['select_sum_eth'] == 'Back':
                                    await FSMmain.choise_coin_trc.set()
                                    await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)
                                elif data['select_sum_eth'] == 'Back to menu':
                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                    await state.finish()
                                else:
                                    await FSMmain.select_sum_eth.set()
                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you',reply_markup=markup3)
                        elif data['choise_coin_trc'] == 'Back':
                            await FSMmain.name_net.set()
                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                        elif data['choise_coin_trc'] == 'Back to menu':
                            await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                            await state.finish()
                        else:
                            await FSMmain.name_net.set()
                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup2)
            elif data['name_net'] == 'USDT (BEP-20)':
                await FSMmain.choise_coin_bep.set()
                await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)

                @dp.message_handler(state=FSMmain.choise_coin_bep)
                async def coin_price_vuvod(message: types.Message, state: FSMContext):
                    async with state.proxy() as data:
                        data['choise_coin_bep'] = message.text
                        if data['choise_coin_bep'] == 'Exchange USDT for BTC':
                            await FSMmain.select_sum_btc_bep.set()
                            btc = client.get_symbol_ticker(symbol='BTCUSDT')
                            btc_get = str(round(float(btc.get('price')), 0) - (round(float(btc.get('price')), 0) / 100 * 10.5))
                            await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  BTC (Bitcoin)\n\nExchange rate: 1 BTC (Bitcoin) = {btc_get} {data["name_net"]}\n\nThe reserve is: 5,3268427  BTC (Bitcoin)\n\nMinimum exchange amount USDT for BTC (Bitcoin) = 100.0 USDT\nMaximum exchange amount USDT for BTC (Bitcoin) = 100000.0\nUSDT', reply_markup=markup3)

                            @dp.message_handler(state=FSMmain.select_sum_btc_bep)
                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                async with state.proxy() as data:
                                    data['select_sum_btc_bep'] = message.text
                                if data['select_sum_btc_bep'] == 'Select the amount of USDT':
                                    await FSMmain.enter_sum_btc_bep.set()
                                    await bot.send_message(message.from_user.id, f'Exchange rate:\n1 BTC (Bitcoin) = {btc_get} {data["name_net"]}\nThe reserve is: 5,3268427 BTC (Bitcoin)\n--------------------------\nHow many USDT do you want to exchange?\n‼️ Minimum USDT - 100 ‼️', reply_markup=a)

                                    @dp.message_handler(state=FSMmain.enter_sum_btc_bep)
                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                        async with state.proxy() as data:
                                            data['enter_sum_btc_bep'] = message.text
                                        if float(data['enter_sum_btc_bep']) < 100:
                                            await FSMmain.enter_sum_btc_bep.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, less than 100 cannot be!\n\nEnter again')
                                        elif float(data['enter_sum_btc_bep']) >= 100:
                                            await FSMmain.y_or_n_btc_bep.set()
                                            await bot.send_message(message.from_user.id, f'You are giving away: {data["enter_sum_btc_bep"]} {data["name_net"]}', reply_markup=markup4)

                                            @dp.message_handler(state=FSMmain.y_or_n_btc_bep)
                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                async with state.proxy() as data:
                                                    data['y_or_n_btc_bep'] = message.text
                                                if data['y_or_n_btc_bep'] == 'Yes':
                                                    await FSMmain.enter_wallet_btc_bep.set()
                                                    you_get_btc = str(float(data['enter_sum_btc_bep']) / float(btc_get))
                                                    await bot.send_message(message.from_user.id, f"You are giving away: {data['enter_sum_btc_bep']} {data['name_net']} You'll get: {you_get_btc} BTC (Bitcoin)")
                                                    await bot.send_message(message.from_user.id, f'Enter your BTC (Bitcoin) wallet to which you want to receive BTC (BEP-20)', reply_markup=a)

                                                    @dp.message_handler(state=FSMmain.enter_wallet_btc_bep)
                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                        async with state.proxy() as data:
                                                            data['enter_wallet_btc_bep'] = message.text
                                                        if len(data['enter_wallet_btc_bep']) == 34:
                                                            await FSMmain.enter_eMail_btc_bep.set()
                                                            await bot.send_message(message.from_user.id, 'Enter your email address to confirm the transaction', reply_markup=a)

                                                            @dp.message_handler(state=FSMmain.enter_eMail_btc_bep)
                                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                async with state.proxy() as data:
                                                                    data['enter_eMail_btc_bep'] = message.text
                                                                is_valid = validate_email(data['enter_eMail_btc_bep'])
                                                                if is_valid == True:
                                                                    await FSMmain.i_paid_btc_bep.set()
                                                                    await bot.send_message(message.from_user.id, f'Wallet where you receive: {data["enter_wallet_btc_bep"]}\n\nAmount of transfer: {data["enter_sum_btc_bep"]} {data["name_net"]}\n\nTotal: {you_get_btc} BTC (Bitcoin)\n\nOpen the client from where you will transfer USDT, and enter the following information:\n0xf058148b438de5Ff7dA153E9AD353Fe44302d38E\n\n‼️{data["name_net"]}‼️', reply_markup=markup5)
                                                                    await bot.send_message(message.from_user.id, '‼️Your ticket has been created, pay the amount of USDT specified in the application to the wallet specified above, after payment, click the "I paid" button.‼️')

                                                                    @dp.message_handler(state=FSMmain.i_paid_btc_bep)
                                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                        async with state.proxy() as data:
                                                                            data['i_paid_btc_bep'] = message.text
                                                                        if data['i_paid_btc_bep'] == 'I paid':
                                                                            await bot.send_message(message.from_user.id, '✅ Your order has been accepted')
                                                                            await bot.send_message(message.from_user.id, f'Order created!\nYou exchanged: {data["enter_sum_btc_bep"]} {data["name_net"]} on the {you_get_btc}\nBTC (Bitcoin)\nOrder status:\nWaiting for the receipt of funds...', reply_markup=markup0)
                                                                            telegram_send.send(messages=[f'New order!\nName: {message.from_user.full_name}\nLogin: {message.from_user.username}\nName net: {data["name_net"]}\nName coin: {data["choise_coin_bep"]}\nHow many USDT: {data["enter_sum_btc_bep"]} in BTC = {you_get_btc}\nWallet: {data["enter_wallet_btc_bep"]}\nE-mail: {data["enter_eMail_btc_bep"]}'])
                                                                            await state.finish()
                                                                        elif data['i_paid_btc_bep'] == 'Cancel the ticket and back to':
                                                                            await FSMmain.name_net.set()
                                                                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                                                                        else:
                                                                            await FSMmain.i_paid_btc_bep.set()
                                                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup5)
                                                                elif is_valid == False:
                                                                    await FSMmain.enter_eMail_btc_bep.set()
                                                                    await bot.send_message(message.from_user.id, 'E-mail entered incorrectly\n\nEnter again')
                                                        elif len(data['enter_wallet_btc_bep']) > 34 or len(data['enter_wallet_btc_bep']) < 34:
                                                            await FSMmain.enter_wallet_btc_bep.set()
                                                            await bot.send_message(message.from_user.id, 'Sorry, the number of characters must be 34!\n\nEnter again')
                                                elif data['y_or_n_btc_bep'] == 'Back':
                                                    await FSMmain.select_sum_btc_bep.set()
                                                    await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  BTC (Bitcoin)\n\nExchange rate: 1 BTC (Bitcoin) = {btc_get} {data["name_net"]}\n\nThe reserve is: 5,3268427  BTC (Bitcoin)\n\nMinimum exchange amount USDT for BTC (Bitcoin) = 100.0 USDT\nMaximum exchange amount USDT for BTC (Bitcoin) = 100000.0\nUSDT', reply_markup=markup3)
                                                elif data['y_or_n_btc_bep'] == 'Back to menu':
                                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                                    await state.finish()
                                                else:
                                                    await FSMmain.y_or_n_btc_bep.set()
                                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup4)
                                        else:
                                            await FSMmain.select_sum_btc_bep.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                                elif data['select_sum_btc_bep'] == 'Back':
                                    await FSMmain.choise_coin_bep.set()
                                    await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)
                                elif data['select_sum_btc_bep'] == 'Back to menu':
                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                    await state.finish()
                                else:
                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                        elif data['choise_coin_bep'] == 'Exchange USDT for TRX':
                            await FSMmain.select_sum_trx_bep.set()
                            trx = client.get_symbol_ticker(symbol='TRXUSDT')
                            trx_get = str(round(float(trx.get('price')), 2) - (round(float(trx.get('price')), 2) / 100 * 10.5))
                            await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  TRX (BEP-20)\n\nExchange rate: 1 TRX (BEP-20) = {trx_get} {data["name_net"]}\n\nThe reserve is: 671350  TRX (BEP-20)\n\nMinimum exchange amount USDT for TRX (BEP-20) = 100.0 USDT\nMaximum exchange amount USDT for TRX (BEP-20) = 100000.0\nUSDT', reply_markup=markup3)

                            @dp.message_handler(state=FSMmain.select_sum_trx_bep)
                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                async with state.proxy() as data:
                                    data['select_sum_trx_bep'] = message.text
                                if data['select_sum_trx_bep'] == 'Select the amount of USDT':
                                    await FSMmain.enter_sum_trx_bep.set()
                                    await bot.send_message(message.from_user.id, f'Exchange rate:\n1 TRX (BEP-20) = {trx_get} {data["name_net"]}\nThe reserve is: 671350 TRX (BEP-20)\n--------------------------\nHow many USDT do you want to exchange?\n‼️ Minimum USDT - 100 ‼️', reply_markup=a)

                                    @dp.message_handler(state=FSMmain.enter_sum_trx_bep)
                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                        async with state.proxy() as data:
                                            data['enter_sum_trx_bep'] = message.text
                                        if float(data['enter_sum_trx_bep']) < 100:
                                            await FSMmain.enter_sum_trx_bep.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, less than 100 cannot be!\n\nEnter again')
                                        elif float(data['enter_sum_trx_bep']) >= 100:
                                            await FSMmain.y_or_n_trx_bep.set()
                                            await bot.send_message(message.from_user.id, f'You are giving away: {data["enter_sum_trx_bep"]} {data["name_net"]}', reply_markup=markup4)

                                            @dp.message_handler(state=FSMmain.y_or_n_trx_bep)
                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                async with state.proxy() as data:
                                                    data['y_or_n_trx_bep'] = message.text
                                                if data['y_or_n_trx_bep'] == 'Yes':
                                                    await FSMmain.enter_wallet_trx_bep.set()
                                                    you_get_trx = str(float(data['enter_sum_trx_bep']) / float(trx_get))
                                                    await bot.send_message(message.from_user.id, f"You are giving away: {data['enter_sum_trx_bep']} {data['name_net']}\n\nYou'll get: {you_get_trx} TRX")
                                                    await bot.send_message(message.from_user.id, f'Enter your TRX wallet to which you want to receive TRX (BEP-20)', reply_markup=a)

                                                    @dp.message_handler(state=FSMmain.enter_wallet_trx_bep)
                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                        async with state.proxy() as data:
                                                            data['enter_wallet_trx_bep'] = message.text
                                                        if len(data['enter_wallet_trx_bep']) == 42:
                                                            await FSMmain.enter_eMail_trx_bep.set()
                                                            await bot.send_message(message.from_user.id, 'Enter your email address to confirm the transaction', reply_markup=a)

                                                            @dp.message_handler(state=FSMmain.enter_eMail_trx_bep)
                                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                async with state.proxy() as data:
                                                                    data['enter_eMail_trx_bep'] = message.text
                                                                is_valid = validate_email(data['enter_eMail_trx_bep'])
                                                                if is_valid == True:
                                                                    await FSMmain.i_paid_trx_bep.set()
                                                                    await bot.send_message(message.from_user.id, f'Wallet where you receive: {data["enter_wallet_trx_bep"]}\n\nAmount of transfer: {data["enter_sum_trx_bep"]} {data["name_net"]}\n\nTotal: {you_get_trx} TRX (BEP-20)\n\nOpen the client from where you will transfer USDT, and enter the following information:\n0xf058148b438de5Ff7dA153E9AD353Fe44302d38E\n\n‼️{data["name_net"]}‼️', reply_markup=markup5)
                                                                    await bot.send_message(message.from_user.id, '‼️Your ticket has been created, pay the amount of USDT specified in the application to the wallet specified above, after payment, click the "I paid" button.‼️')

                                                                    @dp.message_handler(state=FSMmain.i_paid_trx_bep)
                                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                        async with state.proxy() as data:
                                                                            data['i_paid_trx_bep'] = message.text
                                                                        if data['i_paid_trx_bep'] == 'I paid':
                                                                            await bot.send_message(message.from_user.id, '✅ Your order has been accepted')
                                                                            await bot.send_message(message.from_user.id, f'Order created!\nYou exchanged: {data["enter_sum_trx_bep"]} {data["name_net"]} on the {you_get_trx}\nTRX (BEP-20)\nOrder status:\nWaiting for the receipt of funds...', reply_markup=markup0)
                                                                            telegram_send.send(messages=[f'New order!\nName: {message.from_user.full_name}\nLogin: {message.from_user.username}\nName net: {data["name_net"]}\nName coin: {data["choise_coin_bep"]}\nHow many USDT: {data["enter_sum_trx_bep"]} in TRX = {you_get_trx}\nWallet: {data["enter_wallet_trx_bep"]}\nE-mail: {data["enter_eMail_trx_bep"]}'])
                                                                            await state.finish()
                                                                        elif data['i_paid_trx_bep'] == 'Cancel the ticket and back to':
                                                                            await FSMmain.name_net.set()
                                                                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                                                                        else:
                                                                            await FSMmain.i_paid_trx_bep.set()
                                                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup5)
                                                                elif is_valid == False:
                                                                    await FSMmain.enter_eMail_trx_bep.set()
                                                                    await bot.send_message(message.from_user.id, 'E-mail entered incorrectly\n\nEnter again')
                                                        elif len(data['enter_wallet_trx_bep']) > 42 or len(data['enter_wallet_trx_bep']) < 42:
                                                            await FSMmain.enter_wallet_trx_bep.set()
                                                            await bot.send_message(message.from_user.id, 'Sorry, the number of characters must be 42!\n\nEnter again')
                                                elif data['y_or_n_trx_bep'] == 'Back':
                                                    await FSMmain.select_sum_trx_bep.set()
                                                    await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  TRX (BEP-20)\n\nExchange rate: 1 TRX (BEP-20) = {trx_get} {data["name_net"]}\n\nThe reserve is: 671350  TRX (BEP-20)\n\nMinimum exchange amount USDT for TRX (BEP-20) = 100.0 USDT\nMaximum exchange amount USDT for TRX (BEP-20) = 100000.0\nUSDT', reply_markup=markup3)
                                                elif data['y_or_n_trx_bep'] == 'Back to menu':
                                                    await bot.send_message(message.from_user.id,  'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                                    await state.finish()
                                                else:
                                                    await FSMmain.y_or_n_trx_bep.set()
                                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup4)

                                elif data['select_sum_trx_bep'] == 'Back':
                                    await FSMmain.choise_coin_bep.set()
                                    await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)
                                elif data['select_sum_trx_bep'] == 'Back to menu':
                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                    await state.finish()
                                else:
                                    await FSMmain.select_sum_trx_bep.set()
                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                        elif data['choise_coin_bep'] == 'Exchange USDT for ETH':
                            await FSMmain.select_sum_eth_bep.set()
                            eth = client.get_symbol_ticker(symbol='ETHUSDT')
                            eth_get = str(round(float(eth.get('price')), 2) - (round(float(eth.get('price')), 2) / 100 * 10.5))
                            await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  ETH (ERC-20)\n\nExchange rate: 1 ETH (ERC-20) = {eth_get} {data["name_net"]}\n\nThe reserve is: 1432  ETH (ERC-20)\n\nMinimum exchange amount USDT for ETH (ERC-20) = 100.0 USDT\nMaximum exchange amount USDT for ETH (ERC-20) = 100000.0\nUSDT', reply_markup=markup3)

                            @dp.message_handler(state=FSMmain.select_sum_eth_bep)
                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                async with state.proxy() as data:
                                    data['select_sum_eth_bep'] = message.text
                                if data['select_sum_eth_bep'] == 'Select the amount of USDT':
                                    await FSMmain.enter_sum_eth_bep.set()
                                    await bot.send_message(message.from_user.id, f'Exchange rate:\n1 ETH (ERC-20) = {eth_get} {data["name_net"]}\nThe reserve is: 1432 ETH (ERC-20)\n--------------------------\nHow many USDT do you want to exchange?\n‼️ Minimum USDT - 100 ‼️', reply_markup=a)

                                    @dp.message_handler(state=FSMmain.enter_sum_eth_bep)
                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                        async with state.proxy() as data:
                                            data['enter_sum_eth_bep'] = message.text
                                        if float(data['enter_sum_eth_bep']) < 100:
                                            await FSMmain.enter_sum_eth_bep.set()
                                            await bot.send_message(message.from_user.id, 'Sorry, less than 100 cannot be!\n\nEnter again')
                                        elif float(data['enter_sum_eth_bep']) >= 100:
                                            await FSMmain.y_or_n_eth_bep.set()
                                            await bot.send_message(message.from_user.id, f'You are giving away: {data["enter_sum_eth_bep"]} {data["name_net"]}', reply_markup=markup4)

                                            @dp.message_handler(state=FSMmain.y_or_n_eth_bep)
                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                async with state.proxy() as data:
                                                    data['y_or_n_eth_bep'] = message.text
                                                if data['y_or_n_eth_bep'] == 'Yes':
                                                    await FSMmain.enter_wallet_eth_bep.set()
                                                    you_get_eth = str(float(data['enter_sum_eth_bep']) / float(eth_get))
                                                    await bot.send_message(message.from_user.id, f"You are giving away: {data['enter_sum_eth_bep']} {data['name_net']}\n\nYou'll get: {you_get_eth} ETH")
                                                    await bot.send_message(message.from_user.id, f'Enter your ETH wallet to which you want to receive ETH (BEP-20)', reply_markup=a)

                                                    @dp.message_handler(state=FSMmain.enter_wallet_eth_bep)
                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                        async with state.proxy() as data:
                                                            data['enter_wallet_eth_bep'] = message.text
                                                        if len(data['enter_wallet_eth_bep']) == 42:
                                                            await FSMmain.enter_eMail_eth_bep.set()
                                                            await bot.send_message(message.from_user.id, 'Enter your email address to confirm the transaction', reply_markup=a)

                                                            @dp.message_handler(state=FSMmain.enter_eMail_eth_bep)
                                                            async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                async with state.proxy() as data:
                                                                    data['enter_eMail_eth_bep'] = message.text
                                                                is_valid = validate_email(data['enter_eMail_eth_bep'])
                                                                if is_valid == True:
                                                                    await FSMmain.i_paid_eth_bep.set()
                                                                    await bot.send_message(message.from_user.id, f'Wallet where you receive: {data["enter_wallet_eth_bep"]}\n\nAmount of transfer: {data["enter_sum_eth_bep"]} {data["name_net"]}\n\nTotal: {you_get_eth} ETH (ERC-20)\n\nOpen the client from where you will transfer USDT, and enter the following information:\n0xf058148b438de5Ff7dA153E9AD353Fe44302d38E\n\n‼️{data["name_net"]}‼️', reply_markup=markup5)
                                                                    await bot.send_message(message.from_user.id, '‼️Your ticket has been created, pay the amount of USDT specified in the application to the wallet specified above, after payment, click the "I paid" button.‼️')

                                                                    @dp.message_handler(state=FSMmain.i_paid_eth_bep)
                                                                    async def coin_price_vuvod(message: types.Message, state: FSMContext):
                                                                        async with state.proxy() as data:
                                                                            data['i_paid_eth_bep'] = message.text
                                                                        if data['i_paid_eth_bep'] == 'I paid':
                                                                            await bot.send_message(message.from_user.id, '✅ Your order has been accepted')
                                                                            await bot.send_message(message.from_user.id, f'Order created!\nYou exchanged: {data["enter_sum_eth_bep"]} {data["name_net"]} on the {you_get_eth}\nETH (ERC-20)\nOrder status:\nWaiting for the receipt of funds...', reply_markup=markup0)
                                                                            telegram_send.send(messages=[f'New order!\nName: {message.from_user.full_name}\nLogin: {message.from_user.username}\nName net: {data["name_net"]}\nName coin: {data["choise_coin_bep"]}\nHow many USDT: {data["enter_sum_eth_bep"]} in ETH = {you_get_eth}\nWallet: {data["enter_wallet_eth_bep"]}\nE-mail: {data["enter_eMail_eth_bep"]}'])
                                                                            await state.finish()
                                                                        elif data['i_paid_eth_bep'] == 'Cancel the ticket and back to':
                                                                            await FSMmain.name_net.set()
                                                                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                                                                        else:
                                                                            await FSMmain.i_paid_eth_bep.set()
                                                                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup5)
                                                                elif is_valid == False:
                                                                    await FSMmain.enter_eMail_eth_bep.set()
                                                                    await bot.send_message(message.from_user.id,  'E-mail entered incorrectly\n\nEnter again')
                                                        elif len(data['enter_wallet_eth_bep']) > 42 or len(data['enter_wallet_eth_bep']) < 42:
                                                            await FSMmain.enter_wallet_eth_bep.set()
                                                            await bot.send_message(message.from_user.id, 'Sorry, the number of characters must be 42!\n\nEnter again')
                                                elif data['y_or_n_eth_bep'] == 'Back':
                                                    await FSMmain.select_sum_eth_bep.set()
                                                    await bot.send_message(message.from_user.id, f'Do you want to exchange: {data["name_net"]} to  ETH (ERC-20)\n\nExchange rate: 1 ETH (ERC-20) = {eth_get} {data["name_net"]}\n\nThe reserve is: 1432  ETH (ERC-20)\n\nMinimum exchange amount USDT for ETH (ERC-20) = 100.0 USDT\nMaximum exchange amount USDT for ETH (ERC-20) = 100000.0\nUSDT', reply_markup=markup3)
                                                elif data['y_or_n_eth_bep'] == 'Back to menu':
                                                    await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                                                    await state.finish()
                                                else:
                                                    await FSMmain.y_or_n_eth_bep.set()
                                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you',reply_markup=markup4)
                                elif data['select_sum_eth_bep'] == 'Back':
                                    await FSMmain.choise_coin_bep.set()
                                    await bot.send_message(message.from_user.id, 'Choose which coin you want to get', reply_markup=markup2)
                                elif data['select_sum_eth_bep'] == 'Back to menu':
                                    await bot.send_message(message.from_user.id,'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support',reply_markup=markup0)
                                    await state.finish()
                                else:
                                    await FSMmain.select_sum_eth_bep.set()
                                    await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup3)
                        elif data['choise_coin_bep'] == 'Back':
                            await FSMmain.name_net.set()
                            await bot.send_message(message.from_user.id, 'Choose which network you want to exchange USDT on', reply_markup=markup1)
                        elif data['choise_coin_bep'] == 'Back to menu':
                            await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                            await state.finish()
                        else:
                            await FSMmain.name_net.set()
                            await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup2)
            elif data['name_net'] == 'Go back to the start':
                await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)
                await state.finish()
            else:
                await FSMmain.name_net.set()
                await bot.send_message(message.from_user.id, 'Sorry, I can’t understand you', reply_markup=markup1)
    elif message.text == 'Support':
        photo = open('251-2518346_support-technical-support-black-and-white.png', 'rb')
        await bot.send_photo(message.chat.id, photo=photo, reply_markup=urlKB)
    else:
        await bot.send_message(message.from_user.id, 'Welcome to TRON Exchange!\n\nThis bot was made by "TRON Limited" for the fastest exchange of your USDT to TRX and BTC and ETH.\n\n📈 Our advantages:\n1). Automatic exchange\n2). The most profitable course\n3). Responsive support', reply_markup=markup0)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
else:
    print('бот не работает!')