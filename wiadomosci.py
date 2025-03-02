import feedparser
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from config import SMTP_USER, SMTP_PASSWORD, SMTP_HOST, SMTP_PORT, ODBIORCA

# Funkcja pobierająca pełne treści artykułów (z uwzględnieniem specjalnego wstępu)
def pobierz_pelny_artykul(url, liczba_paragrafow=10):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    # Specjalny wstęp (lead)
    lead = soup.select_one('div#lead')
    lead_text = lead.get_text(strip=True) if lead else ''

    # Paragrafy artykułu
    paragrafy = soup.select('p')[:liczba_paragrafow]
    paragrafy_text = '\n\n'.join(p.get_text(strip=True) for p in paragrafy)

    # Łączenie leadu z paragrafami
    tresc_artykulu = f"{lead_text}\n\n{paragrafy_text}" if lead_text else paragrafy_text

    return tresc_artykulu if tresc_artykulu else 'Brak dostępnego opisu.'

# Pobiera artykuły z RSS i dodaje pełne treści
def pobierz_artykuly_rss(url, limit=5):
    feed = feedparser.parse(url)
    artykuly = []
    for entry in feed.entries[:limit]:
        tytul = entry.title
        link = entry.link
        pelny_artykul = pobierz_pelny_artykul(link)
        artykuly.append((tytul, link, pelny_artykul))
    return artykuly

# Adresy kanałów RSS
rss_feeds = {
    'Onet': 'https://wiadomosci.onet.pl/rss',
    'WP': 'https://wiadomosci.wp.pl/rss.xml',
    'TVN24': 'https://tvn24.pl/najnowsze.xml'
}

# Zebranie artykułów (format HTML)
tresc = "<h2>Dzisiejsze najnowsze wiadomości:</h2>"

for nazwa, url in rss_feeds.items():
    tresc += f"<h3>{nazwa}</h3>"
    artykuly = pobierz_artykuly_rss(url, limit=15)
    for tytul, link, opis in artykuly:
        tresc += f"<p><strong>{tytul}</strong><br>{opis}<br><a href='{link}'>{link}</a></p>"

# Konfiguracja e-mail
msg = MIMEText(tresc, "html", "utf-8")
msg['Subject'] = "Dzisiejsze wiadomości z Onet, WP i TVN24 (pełne artykuły)"
msg['From'] = SMTP_USER
msg['To'] = ODBIORCA

# Wysyłanie e-maila
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.send_message(msg)

print("Wiadomości wysłane!")
