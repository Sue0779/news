
# Automatyczny Newsletter RSS do e-mail (pełne artykuły)

## Opis
Ten skrypt automatycznie pobiera najnowsze wiadomości (pełne artykuły) z popularnych polskich serwisów informacyjnych (Onet, WP, TVN24) przy pomocy kanałów RSS, a następnie wysyła je w formacie HTML na wybrany adres e-mail.

## Instalacja

1. Sklonuj repozytorium lub pobierz pliki:

```bash
git clone <link-do-repozytorium>
```

2. Zainstaluj wymagane biblioteki:

```bash
pip install feedparser requests beautifulsoup4
```

## Konfiguracja

Przed pierwszym uruchomieniem utwórz plik `config.py` w katalogu ze skryptem:

```python
# config.py
SMTP_HOST = 'adres_serwera_smtp'
SMTP_PORT = 465
SMTP_USER = 'twoj_adres_email'
SMTP_PASSWORD = 'twoje_haslo_do_email'
FROM_EMAIL = 'twoj_adres_email'
TO_EMAIL = 'adres_odbiorcy'
```

- **SMTP_HOST** - adres serwera SMTP (np. sue.usermd.net)
- **SMTP_PORT** - port serwera SMTP (domyślnie 465 dla SSL)
- **SMTP_USER** - login do konta e-mail
- **SMTP_PASSWORD** - hasło do konta e-mail
- **FROM_EMAIL** - adres e-mail nadawcy
- **TO_EMAIL** - adres e-mail odbiorcy

## Użytkowanie

Uruchom skrypt poleceniem:

```bash
python wiadomosci.py
```

Wiadomości zostaną wysłane automatycznie na wskazany adres e-mail.

## Licencja

Ten projekt udostępniony jest na licencji [Creative Commons CC0](https://creativecommons.org/publicdomain/zero/1.0/), co oznacza, że możesz go dowolnie używać, modyfikować i rozpowszechniać.
