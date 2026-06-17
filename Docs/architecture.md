# Architecture

## Main Entities

### User

Represents a private individual using the platform.

Fields:
- username
- email
- first_name
- last_name
- county
- city
- registration_date
- account_status

---

### Item

Represents a good or service offered for exchange.

Fields:
- title
- description
- category
- troc_value
- owner
- location
- status

---

### ItemPhoto

Represents photos attached to an item.

Fields:
- item
- image
- upload_date

---

### ExchangeOffer

Represents a proposal between two users.

Fields:
- sender
- receiver
- offered_item
- requested_item
- status
- created_at

---

### Message

Represents communication between users.

Fields:
- sender
- receiver
- content
- created_at

---

### Category

Represents item classification.

Examples:
- Vegetables
- Fruits
- Eggs
- Dairy
- Tools
- Services
- Miscellaneous
