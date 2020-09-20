from aiogram.utils.markdown import *

SYMBOL = '💘'

MALE = '👦🏻Парень'
FEMALE = '👩🏼Девушка'

#  Search Gender
MALE_SEARCH = '👦🏻Парня'
FEMALE_SEARCH = '👩🏼Девушку'

NEXT = 'next'
BACK = 'Вернуться'

SEARCH = '🔎Поиск'
CONVERSE = '💬Общение'
PROFILE = '👤Профиль'
BALANCE = f'{SYMBOL}️Баланс'

LIKE = 'like'
CHAT = 'chat'
MORE = 'profile'

MESSAGE_LINK = 'https://t.me/kusama\\_test\\_bot?start={}'
QUERY_LINK = 'https://t.me/kusama_test_bot?start={}'


def welcome_msg():
    return text(bold(f'Приветствую❗Меня зовут Купидон, Я - Бог Любви!{SYMBOL}'),
                bold('И раз вы обратились ко мне, считайте, что вторая половинка для вас уже найдена!😉'),
                bold('Давайте быстренько заполним анкету и приступим к поиску вашей любви!💞'),
                sep='\n')


def balance_msg(balance, invitation, referrals):
    msg = text(balance, '\n',
               italic(f'  1{SYMBOL} = Свайп при поиске собеседника'),
               italic(f'  5{SYMBOL} = Лайкнуть пользователя'),
               italic(f'10{SYMBOL} = Каждое сообщение пользователю, который вам ещё не ответил'),
               italic(f'  5{SYMBOL} = Просмотр профиля того, кто лайкнул вас или написал вам'),
               '\n',
               bold(f'Вы можете зарабатывать сердечки{SYMBOL}, приглашая в бот своих друзей и знакомых👨‍👦‍👦'),
               '\n',
               italic(f'10{SYMBOL} за приглашение парня'),
               italic(f'50{SYMBOL} за приглашение девушки'),
               '\n',
               code(f'Уже приглашено: {referrals}'),
               '\n',
               bold('Ваша уникальная ссылка для приглашения в бот:'),
               quote_html(invitation),
               sep='\n')
    return msg


def user_info(user):
    return text(text(code('Имя:'), bold(user[1])), text(code('Возраст:'), bold(user[2])),
                text(code('Город:'), bold(user[3])), text(code('Род занятий:'), bold(user[4])),
                text(code('О себе:'), bold(user[5])),
                sep='\n')
