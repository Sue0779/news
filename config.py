# config.py (wersja przykładowa na git)

SMTP_USER = "twoj_email@example.com"  # wpisz własny adres email
SMTP_PASSWORD = "twoje_haslo"         # wpisz własne hasło
SMTP_HOST = "smtp.example.com"        # wpisz własny host SMTP
SMTP_PORT = 465                       # zwykle port 465 dla SMTP_SSL

ODBIORCA = "odbiorca@example.com"     # adres odbiorcy wiadomości

# Przykładowe kanały RSS (możesz dowolnie zmieniać)
RSS_FEEDS = {
    'Onet': 'https://wiadomosci.onet.pl/rss',
    'WP': 'https://wiadomosci.wp.pl/rss.xml',
    'TVN24': 'https://tvn24.pl/najnowsze.xml'
}
