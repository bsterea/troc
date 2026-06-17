# Securitate

## Scop

Acest document defineste cerintele minime de securitate pentru platforma Troc.

---

## Principiul General

Troc va colecta minimum de date personale necesare functionarii platformei.

Datele care nu sunt necesare nu vor fi colectate.

---

## Autentificare

Utilizatorii se autentifica folosind:

- numar de telefon
- parola

Optional:

- email

---

## Protectia parolelor

- Parolele nu vor fi stocate niciodata in clar.
- Parolele vor fi stocate folosind algoritmi moderni de hash.
- Administratorii nu pot vedea parolele utilizatorilor.

---

## Protectia conturilor

- Limitarea numarului de autentificari esuate.
- Blocare temporara dupa tentative repetate.
- Posibilitate de recuperare a accesului.

---

## Protectia datelor personale

Date considerate personale:

- numar de telefon
- email
- nume
- prenume
- localitate
- mesaje

---

## Vizibilitatea datelor

Numarul de telefon nu este afisat public.

Mesageria interna reprezinta metoda principala de comunicare intre utilizatori.

Utilizatorii pot alege voluntar daca isi comunica numarul de telefon.

---

## Comunicatii

Toate conexiunile vor utiliza HTTPS.

Datele nu vor fi transmise necriptat.

---

## Backup

- Backup periodic al bazei de date.
- Backup periodic al fotografiilor.
- Posibilitate de restaurare.

---

## Principiul de securitate

Cea mai buna securitate este colectarea unui numar minim de date.

# Security

## Purpose

This document defines the minimum security requirements for the Troc platform.

---

## General Principle

Troc will collect only the minimum amount of personal data required for the platform to operate.

Data that is not necessary will not be collected.

---

## Authentication

Users authenticate using:

- phone number
- password

Optional:

- email address

---

## Password Protection

- Passwords must never be stored in plain text.
- Passwords must be stored using modern hashing algorithms.
- Administrators cannot view user passwords.

---

## Account Protection

- Limit failed login attempts.
- Temporary lockout after repeated failed attempts.
- Account recovery mechanisms.

---

## Personal Data Protection

The following are considered personal data:

- phone number
- email address
- first name
- last name
- city and county
- messages

---

## Data Visibility

Phone numbers are not publicly displayed.

Internal messaging is the primary communication method between users.

Users may voluntarily share their phone numbers with each other.

---

## Communications

All connections must use HTTPS.

Data must never be transmitted unencrypted.

---

## Backup

- Regular database backups.
- Regular photo backups.
- Restore procedures must be available.

---

## Security Principle

The best security is collecting the minimum amount of data necessary.
