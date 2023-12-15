# Introduction

Attacking CSRF Synchronizer Token Pattern (STP) in the context of same-site attackers.

More info @ https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina.

## Usage

- Set in your `/etc/hosts/` file two different entries, both pointing to 127.0.0.1, with a same-site relationship (e.g. `victim.tld` and `attacker.victim.tld`).
- Run the two `app.py` files, and explore the attack described in the paper for flask-login (CORF Token Fixation).

## Attack Steps

1. The web application is running at `victim.tld:5000`.
2. The hacker runs its malicious app at `attacker.victim.tld:8000`.
3. The hacker tricks the victim browser into visiting `https://attacker.victim.tld:8000/cookie`. When doing this, the malicious app will fetch a "guest" session and a valid CSRF token from the web application, and it will inject the session fetched with a cookie scoped to the domain `victim.tld` into the victim browser.
4. Now, when the victim visits `https://victim.tld:5000/login` to login, it will present the injected cookie to the login page. The CSRF secret will be therefore be persisted even after logging in.
5. The hacker now tricks the victim browser into visiting `https://attacker.victim.tld/csrf`, where a CSRF attack to steal money is mounted with the CSRF token computed on the guest session fetched earlier. The victim browser sends the request, and the CSRF token is valid for the victim session!
