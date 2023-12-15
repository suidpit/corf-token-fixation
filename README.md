# Introduction

Attacking CSRF Synchronizer Token Pattern (STP) in the context of same-site attackers.

More info @ https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina.

## Usage

- Set in your `/etc/hosts/` file two different entries, both pointing to 127.0.0.1, with a same-site relationship (e.g. `victim.tld` and `attacker.victim.tld`).
- Run the two `app.py` files, and explore the attack described in the paper for flask-login (CORF Token Fixation).
