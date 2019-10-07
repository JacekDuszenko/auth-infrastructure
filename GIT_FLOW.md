# Ten dokument mówi o tym jak powinna wyglądać praca z branchami podczas realizowania projeku.

## Wspólne branche
Są dwa wspólne branche dla wszystkich zespołów - `master` i `dev`.
Każdy zespół, po uzgodnieniu tego co chce wrzucić na deva, robi rebase swojego teamowego brancha z branchem `dev`, po drodze rozwiązuje ewentualne konflikty, a następnie wystawia pull requesta do brancha `dev`.
Po każdym sprincie ja (Jacek Duszenko) robię pull request z brancha `dev` na brancha `master` i rzeczy z tego brancha pokazujemy Kubiakowi podczas zajęć.

## Teamowe branche
Każdy zespół będzie miał swój branch: `auth`, `ocsp`, `ldap`, `test`, `devops`, który będzie zbiorczym branchem zadań wykonywanych przez ten zespół. Każdy członek zespołu, realizując jakieś zadanie tworzy nowy tzw. feature branch, który, po skończeniu swojego pomniejszego taska rebaseuje z branchem swojego teamu, rozwiązuje konflikty, a następnie wystawia pull request z tego brancha na brancha swojego teamu. Feature branche nazywają się tak jak zadania na Trello, poprzedzone slashem i nazwą brancha swojego teamu. Przykładowy branch do zadania z teamu test może nazywać się `test/unit-tests-for-ldap-tls`


## Przykład 1
Developer z teamu ocsp zaczyna pracę nad zadaniem. Developer tworzy nowego brancha

  `$ git checkout -b skrypt_tworzacy_certyfikat `
  
Po skończonej pracy developer commituje swoje zmiany i robi rebase z branchem swojego zespołu

 ` $ git add * && git commit `
  
  `$ git rebase -i origin/ocsp`
  
  `... (rozwiązanie ewentualnych konfliktów) ...` 
  
  
Potem developer pushuje swojego brancha na repo

  `$ git push -f origin/skrypt_tworzacy_certyfikat`
  
Potem developer wystawia poprzez githuba Pull Request tego konkretnego zadania i czeka na akceptację swojego team leadera

## Przykład 2 
Developerzy z teamu ldap skończyli jedno całe zadanie, team test napisał do niego testy, zadanie jest na branchu `ldap` i jest gotowe do wrzucenia na branch `dev`.
Team leader z teamu `ldap` robi rebase z branchem `dev`, rozwiązując wszystkie konflikty.

  `$ git checkout ldap`
  
  `$ git rebase -i origin/dev`
  
 `... (rozwiązanie ewentualnych konfliktów) ... `
 
Następnie team leader pushuje brancha `ldap` na repo i wystawia z tego Pull Request do brancha `dev` poprzez githuba.

 `$ git push origin/ldap`