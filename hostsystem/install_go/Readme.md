# Installation der neuesten Version von GO

Skript muss Ausführbar gemacht werden
> sudo chmod +x go_installer.sh

Ausführen des Skriptes
> ./go_installer.sh

Setzen des Systempfades: Nutzerpfad
> nano ~/.profile
PATH=$PATH:/usr/local/go/bin
GOPATH=$HOME/golang

Bei wechsel des Pfades
> GOPATH=$HOME/golang

Überprüfen
> which go
> 
> go version

Unter Raspbery 4:
sudo usermod -a -G sudo pi

