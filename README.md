# Dump analysis

400k potentially Indian email accounts with passwords to be analysed.

---

## Cleaning Log

- Removed pure duplicate entries (same email id and password)

- Removed entries with either a NULL account name or password

- Removed entries with account names having no `@`

### Todo

- [ ] Domain cleaning
  - [ ] Identify a baseline for "good" domains (gmail, yahoo, rediffmail)
    - [ ] Identify the possible variants (case [GMAIL], spelling [gamil])
  - [ ] Calculate the significance and reasonability of removal  
    - Passwords mentioned in pipal analysis at `documentation/README.md` have the weirdest domains (examples listed in the doc): most probably from age old forums as only some of them are still part of the indexed web
    - Possibility of investigation: It will be off the study goals
    - The quantity is statistically insignificant: very less number, can probably proove with some p-value sham

---
