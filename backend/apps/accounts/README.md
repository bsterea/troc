# Accounts App

## Purpose

The Accounts app manages user identity and access to the Troc platform.

This app is responsible for registration, authentication, user profiles, account status, and GDPR-related account deletion.

---

## Main Responsibilities

- User registration
- Login
- Logout
- Password management
- Phone number authentication
- Optional email storage
- User profile management
- County and city information
- Account suspension
- Account deletion
- Personal data removal or anonymization

---

## User Data

The account system may store:

- phone_number
- email optional
- password_hash
- first_name
- last_name
- county
- city
- account_status
- created_at
- updated_at
- deleted_at

---

## Privacy Rules

- Phone numbers are not public.
- Email addresses are optional and not public.
- Users communicate through internal messaging.
- Users may voluntarily share their phone number with another user.
- Users can request account deletion.
- Deleted accounts cannot be restored.

---

## Account Status

Possible account statuses:

- active
- suspended
- deleted

---

## MVP Scope

Included in MVP:

- Register with phone number and password
- Login
- Logout
- Edit profile
- Delete account

Not included in MVP:

- Social login
- Google login
- Facebook login
- Two-factor authentication
- Advanced identity verification
# Aplicatia Accounts

## Scop

Aplicatia Accounts gestioneaza identitatea utilizatorilor si accesul acestora la platforma Troc.

Aceasta aplicatie este responsabila pentru inregistrare, autentificare, profil utilizator, starea contului si operatiunile legate de GDPR.

---

## Responsabilitati Principale

- Inregistrare utilizator
- Autentificare
- Deconectare
- Gestionare parola
- Autentificare prin numar de telefon
- Stocare optionala a adresei de email
- Gestionare profil utilizator
- Gestionare judet si localitate
- Suspendare cont
- Stergere cont
- Eliminarea sau anonimizarea datelor personale

---

## Date Utilizator

Sistemul poate stoca:

- numar_telefon
- email (optional)
- parola_hash
- prenume
- nume
- judet
- localitate
- stare_cont
- creat_la
- actualizat_la
- sters_la

---

## Reguli de Confidentialitate

- Numarul de telefon nu este public.
- Adresa de email este optionala si nu este publica.
- Utilizatorii comunica prin sistemul intern de mesaje.
- Utilizatorii pot decide voluntar sa isi comunice numarul de telefon.
- Utilizatorii isi pot sterge contul.
- Conturile sterse nu pot fi recuperate.

---

## Starea Contului

Posibile stari:

- activ
- suspendat
- sters

---

## Functionalitati MVP

Incluse:

- Inregistrare cu numar de telefon si parola
- Autentificare
- Deconectare
- Modificare profil
- Stergere cont

Neincluse:

- Autentificare Google
- Autentificare Facebook
- Autentificare cu doi factori (2FA)
- Verificare avansata de identitate
- 
