# Technology Stack

## Purpose

This document defines the initial technology choices for the Troc MVP.

The main goal is to build a simple, secure, maintainable and low-cost application that can later scale.

---

## Backend

The initial backend will be built with Django.

Reasons:

- Fast development
- Built-in user authentication
- Built-in admin interface
- Strong database integration
- Good security defaults
- Suitable for civic and community platforms
- Easy to maintain by a small team

---

## Database

The initial database will be PostgreSQL.

Reasons:

- Reliable relational database
- Good support for structured data
- Suitable for users, items, exchanges and messages
- Can later support location-based search
- Works well with Django

---

## Frontend

The first version will use Django templates.

Reasons:

- Simple implementation
- No need for a separate frontend framework in MVP
- Faster development
- Lower maintenance cost
- Easier deployment

A separate frontend framework may be considered later if the platform grows.

---

## Mobile Strategy

The first mobile version will be a responsive web application.

Later, the platform may become a PWA.

Native mobile applications for Android and iOS are not required for the MVP.

---

## Hosting Strategy

The preferred long-term hosting model is:

- VPS
- Romanian hosting provider
- Community infrastructure
- Partner infrastructure
- Own server infrastructure

The platform should avoid unnecessary dependency on foreign corporate cloud providers whenever possible.

---

## File Storage

Item photos will initially be stored using simple server-based storage.

Later, a dedicated object storage solution may be added if needed.

---

## Authentication

The MVP will use email and password authentication.

Future options may include:

- Email confirmation
- Password reset
- Two-factor authentication

---

## Not Used in MVP

The MVP will not use:

- Firebase
- AWS-specific architecture
- Blockchain
- Cryptocurrency systems
- Payment processors
- Complex microservices
- AI infrastructure

---

## Development Principle

The first version must be simple.

The goal is not to build a perfect platform from the beginning.

The goal is to build a working platform that allows private individuals to create accounts, publish items, search locally and propose direct exchanges.

# Tehnologii Utilizate

## Scop

Acest document defineste tehnologiile initiale folosite pentru dezvoltarea MVP-ului Troc.

Obiectivul principal este construirea unei aplicatii simple, sigure, usor de intretinut si cu costuri reduse, care sa poata fi extinsa ulterior.

---

## Backend

Backend-ul initial va fi construit folosind Django.

Motive:

- Dezvoltare rapida
- Sistem integrat de autentificare a utilizatorilor
- Interfata administrativa inclusa
- Integrare puternica cu baza de date
- Setari de securitate solide din fabrica
- Potrivit pentru platforme civice si comunitare
- Usor de administrat de o echipa mica

---

## Baza de date

Baza de date initiala va fi PostgreSQL.

Motive:

- Baza de date relationala stabila si maturizata
- Suport excelent pentru date structurate
- Potrivita pentru utilizatori, produse, schimburi si mesaje
- Permite implementarea ulterioara a cautarilor geografice
- Functioneaza foarte bine impreuna cu Django

---

## Frontend

Prima versiune va utiliza Django Templates.

Motive:

- Implementare simpla
- Nu este necesar un framework frontend separat pentru MVP
- Dezvoltare mai rapida
- Costuri reduse de mentenanta
- Publicare mai simpla

Pe masura ce platforma creste, poate fi analizata utilizarea unui framework frontend dedicat.

---

## Strategia Mobila

Prima versiune mobila va fi o aplicatie web responsiva.

Ulterior, platforma poate fi transformata intr-un PWA (Progressive Web Application).

Aplicatiile native Android si iOS nu sunt necesare pentru MVP.

---

## Strategia de Gazduire

Modelul preferat de gazduire pe termen lung este:

- VPS
- Furnizor de hosting din Romania
- Infrastructura comunitara
- Infrastructura a partenerilor
- Infrastructura proprie

Platforma trebuie sa evite dependenta inutila de furnizori cloud corporativi straini atunci cand exista alternative viabile.

---

## Stocarea Fisierelor

Fotografiile produselor vor fi stocate initial pe server.

Daca volumul de date va creste, se poate implementa ulterior o solutie dedicata de stocare.

---

## Autentificare

MVP-ul va utiliza autentificare prin:

- Email
- Parola

Optiuni viitoare:

- Confirmare email
- Resetare parola
- Autentificare cu doi factori (2FA)

---

## Tehnologii Neutilizate in MVP

Prima versiune nu va utiliza:

- Firebase
- Arhitecturi AWS specifice
- Blockchain
- Criptomonede
- Procesatori de plati
- Microservicii complexe
- Infrastructura AI

---

## Principiul de Dezvoltare

Prima versiune trebuie sa fie simpla.

Obiectivul nu este construirea unei platforme perfecte de la inceput.

Obiectivul este construirea unei platforme functionale care permite persoanelor fizice sa isi creeze conturi, sa publice produse sau servicii, sa caute oferte locale si sa propuna schimburi directe.
