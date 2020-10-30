Instrukcja instalowania nowych bibliotek (po pullu):

pip install -r requirements.txt

Instrukcja dodawania nowych bibliotek do requirements.txt (przed pushem):

pip freeze > requirements.txt ( najlepiej* później usunać to co dodało sie z daną biblioteką żeby było tylko to co zainstalowaliśmy pipem)

*ale nie trzeba :d
