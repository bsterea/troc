# Database Design

## Purpose

This document defines the initial database structure for the Troc MVP.

The database must support private user accounts, published items, item photos, exchange offers, messages, categories, and account deletion.

---

## Main Tables

The MVP database will contain the following main tables:

- users
- profiles
- categories
- items
- item_photos
- exchange_offers
- messages
- account_deletion_requests

---

## users

Stores authentication-related user information.

Fields:

- id
- email
- password_hash
- is_active
- is_suspended
- is_deleted
- created_at
- updated_at
- deleted_at

Rules:

- One email can belong to one account only.
- Passwords must never be stored in plain text.
- Deleted users cannot log in.
- Personal data must be removed or anonymized after account deletion.

---

## profiles

Stores public and personal profile information.

Fields:

- id
- user_id
- username
- first_name
- last_name
- county
- city
- created_at
- updated_at

Rules:

- Each user has one profile.
- County and city are required before publishing items.
- Public profile should not expose email address.

---

## categories

Stores item categories.

Fields:

- id
- name
- description
- is_active
- created_at

Initial categories:

- Vegetables
- Fruits
- Eggs
- Dairy
- Meat and household food
- Preserves
- Tools
- Services
- Miscellaneous

---

## items

Stores goods or services offered for exchange.

Fields:

- id
- owner_id
- category_id
- title
- description
- troc_value
- county
- city
- status
- created_at
- updated_at
- deleted_at

Statuses:

- available
- reserved
- exchanged
- removed

Rules:

- Each item belongs to one user.
- Each item must have a category.
- Troc value is only an estimated reference value.
- Removed items are hidden from search.
- Exchanged items are no longer available.

---

## item_photos

Stores photos attached to items.

Fields:

- id
- item_id
- image_path
- uploaded_at

Rules:

- Each photo belongs to one item.
- One item can have multiple photos.
- Photos must be deleted or detached when an item is deleted.

---

## exchange_offers

Stores proposed exchanges between users.

Fields:

- id
- sender_id
- receiver_id
- offered_item_id
- requested_item_id
- message
- status
- created_at
- updated_at
- completed_at

Statuses:

- pending
- accepted
- rejected
- cancelled
- completed

Rules:

- Sender and receiver must be different users.
- Requested item must be available when the offer is created.
- Sender can cancel a pending offer.
- Receiver can accept or reject a pending offer.
- Completed exchanges cannot be modified.

---

## messages

Stores messages between users.

Fields:

- id
- exchange_offer_id
- sender_id
- receiver_id
- content
- created_at
- read_at

Rules:

- Messages belong to an exchange offer.
- Users can message only inside an exchange context.
- Messages must not be used for spam, threats, fraud, or illegal activity.

---

## account_deletion_requests

Stores account deletion requests.

Fields:

- id
- user_id
- requested_at
- completed_at
- status

Statuses:

- pending
- completed
- cancelled

Rules:

- A user can request account deletion.
- After deletion, personal data must be removed from the active system.
- Historical exchange data may be anonymized if needed for system integrity.

---

## Data Privacy Principles

- Email addresses are personal data.
- Names are personal data.
- Location data may be personal data.
- Messages may contain personal data.
- The system must support account deletion.
- The system must not sell personal data.
- The system must not use personal data for advertising profiling.

---

## MVP Database Restrictions

The MVP database will not include:

- Payments
- Wallets
- Financial transactions
- Company accounts
- Legal entity accounts
- Advertising tables
- Subscription tables
- Tax calculation tables
- AI recommendation tables
