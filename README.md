# Projektarbeit Wintersemester 2021/22
Kuka Murmel sotier Roboter.
# Aufbau:
![Database](./pictures/aufbau.jpg)
# Github Usage:
## Init lokales Repository
1. Install Git
1. Account auf Github erstellen: https://github.com/
1. Namen Marvin mitteilen um als Contributer zu adden
1. Workdir erstellen
1. Shell in workdir öffnen
1. ```git init```
1. ```git remote add https://github.com/marvmilo/projektarbeit_wise_2021-22```
1. ```git pull origin main```
1. Branch setzen: ```git checkout -b main```
1. Username und Email ändern: ```git config --global --edit```

## Updaten des Repositories
1. Update lokales Repository: ```git pull origin main```
1. Lokale Dateien zu Repository hinzufügen: ```git add .```
1. Änderung bestätigen mit Kommentar: ```git commit -m "kommentar"```
1. Ins öffentliche Repository pushen: ```git push origin main```

### Anmerkung:
- Beim ersten mal pushen Access Token erstellen: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token
- Vor dem ersten push: ```git config --global credential.helper store```
- Danach push ausführen, Username und Access Token eingeben: ```git push origin main```
- Änderungen können dann ohne Credentials gepushed werden


