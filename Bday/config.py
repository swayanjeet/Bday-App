SOCIAL_AUTH_FACEBOOK_KEY = '1684099278540839'
SOCIAL_AUTH_FACEBOOK_SECRET = '18f246fc3f69934ace46cf9c76b11a97'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/login/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','user_friends','user_birthday']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '763921416821-iljfhvb1ee2avpc3enmb2hpd2b363mec.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '-HrGAH9CSK9S2-CS42b4Olzv'
SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
	'https://www.googleapis.com/auth/plus.login',
	'https://www.googleapis.com/auth/userinfo.email',
	'https://www.googleapis.com/auth/userinfo.profile',
	'https://www.googleapis.com/auth/plus.me',
]
'''	'https://www.googleapis.com/auth/plus.me',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile' '''