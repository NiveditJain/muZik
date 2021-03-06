# checking all settings
import settings
import warnings

print('Running SETTING Checks!')

if type(settings.PORT) is not int:
    raise Exception('settings.PORT must be an integer')

if settings.PORT < 0:
    raise Exception('settings.PORT Value cannot be negative')

if settings.PORT < 1024:
    warnings.warn('You are using a "Well Known Port"')

if settings.PORT > 65535:
    raise Exception('Invalid PORT number')

if type(settings.EXCHANGE_SIZE) is not int:
    raise Exception('settings.EXCHANGE_SIZE must be an integer')

if settings.EXCHANGE_SIZE < 0:
    raise Exception('settings.EXCHANGE_SIZE must be positive')

if type(settings.STORAGE) is not str:
    raise Exception('settings.STORAGE must be a string')

if type(settings.UPVOTE_VALUE) is not int and type(settings.DOWNVOTE_VALUE) is not int:
    raise Exception('settings.UPVOTE_VALUE and settings.DOWNVOTE_VALUE must be integer')

print('All SETTINGS Checked!')