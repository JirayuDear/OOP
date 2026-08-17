## Lab Directory Progression (Lab_01 to Lab_05)

### Lab_01: Fundamental Object-Oriented Domain Model
`Lab_01` establishes the foundational enterprise domain model of the application. It maps real-world entities into clean Python classes, enforcing data encapsulation and entity-relationship boundaries.
*   **Key Implementations**:
    *   Design of the `User` class to hold demographic details (Citizen ID, Phone, Birth Date).
    *   Design of the basic `Account` base class with automated ID generation rules (`get_next_account_id`).
    *   Implementation of the `Court` class containing sport metadata (Tennis, Football, Table Tennis) alongside hourly pricing schedules and loyalty point incentives.
    *   Creation of the `System` class acting as the root orchestrator (Aggregator Pattern) to register users, accounts, and courts.

### Lab_02: Business Logic & Scheduling Operations
`Lab_02` introduces logical operators, temporal checks, and operational scheduling routines to resolve real-world booking conflicts.
*   **Key Implementations**:
    *   Creation of the `CourtBooking` entity tracking reservation status, total cost, and booking schedules.
    *   Conflict resolution algorithms: Implementation of booking validation rules to ensure no court is double-booked for overlapping time ranges (e.g., 10:00-11:00 vs. 11:00-12:00) within a 30-day scheduling horizon.
    *   Dynamic time range logic using Python `datetime` and `timedelta` libraries to parse, sort, and isolate booked time slots.

### Lab_03: Interactive Web User Interface & Session Management
`Lab_03` ports the core domain logic into an interactive web interface using FastHTML, providing real-time responsive elements without full-page reloads.
*   **Key Implementations**:
    *   Integration of FastHTML components (`Container`, `Div`, `Form`, `Table`, `Select`) to replace terminal output.
    *   Authentication workflows: Secure login and sign-up mechanics with data validation rules (e.g., verifying phone lengths, preventing duplicate usernames or emails).
    *   Active session management: Leveraging Starlette sessions to preserve stateful user interactions (`account_id`) across routing contexts.
    *   Dynamic court schedule visualization tables showcasing available, pending, and reserved slots based on sports categorization.

### Lab_04: Payments, Loyalty Points, and Redemption System
`Lab_04` introduces financial transactions, promotional code parsing, and point redemptions within customer accounts.
*   **Key Implementations**:
    *   **Promotional System**: Implementation of the `Coupon` class with percentage discounts and expiration constraints.
    *   **Transactional Branching**: Dual payment execution models:
        1.  *QR Code Payments*: Interactive receipt upload interface using HTMX progress-bar listeners and server-side storage handling.
        2.  *DMIS Coins*: Virtual currency balance checking and debit logic (`deduct_dmis_coins`).
    *   **Redemption Store**: Mechanics to redeem system rewards (`Redeem` class) using accumulated member loyalty points, complete with automatic inventory deduction validations.
    *   **Countdowns**: Asynchronous front-end countdown scripts redirecting users upon payment session expiration (5-minute limits).

### Lab_05: Equipment Rental & Booking Cancellation Lifecycle
`Lab_05` completes the application cycle by introducing auxiliary equipment rentals linked to active bookings and safe transaction reversal workflows.
*   **Key Implementations**:
    *   **Equipment Rental Engine**: Dynamic inventory matching where members can rent specific sports gear (rackets, balls) corresponding exclusively to the sport type of their active reserved slot.
    *   **Booking Cancellation Lifecycle**:
        *   Initiation of cancellation requests by customers (`รอยืนยันการยกเลิก`).
        *   Administrative dashboard interface enabling validation, approval, and decline of cancellations.
        *   Auto-refund engine: Automatically calculates and processes an 80% monetary refund credited directly back to the member's DMIS Coin balance upon approved cancellation.



# DMIS Court Booking and Management System

The DMIS Court Booking and Management System is a comprehensive, real-time sports facility reservation and equipment rental platform. Built using clean Object-Oriented Programming (OOP) principles in Python, the system utilizes the FastHTML framework combined with HTMX to deliver a dynamic, single-page-like user experience without heavy client-side Javascript frameworks. 

The application facilitates complete court scheduling (for Tennis, Football, and Table Tennis), promotional coupon management, a loyalty point-and-coin redemption program, equipment rentals, and a dedicated administrator workflow for booking and cancellation approvals.

---

## Tech Stack

* **Backend Framework**: FastHTML (built on top of FastAPI, Starlette, and Uvicorn)
* **Frontend Library**: HTMX (integrated natively via FastHTML) for asynchronous HTML swaps and reactive components
* **Programming Language**: Python 3.10+
* **Styling**: Embedded Custom CSS with responsive modern layouts
* **Database**: Transient In-Memory Data Structures (Object Collections) with persistent session handling

---

## Features

### 1. Member Operations
* **Account Registration & Security**: Secure validation for user sign-ups (checks for citizen ID format, 10-digit telephone structures, password matching, and unique email/username constraints).
* **Profile Management**: Profile viewing and editing capabilities for personal data (name, birthday, gender, email, phone) with dynamic updates.
* **Interactive Court Booking**:
  * Real-time slot lookup showing availability over a 30-day window.
  * Instant dynamic calculations of pricing, incorporating membership promotional coupon discounts.
* **Dual Payment Channels**:
  * **QR Code Payment**: Upload payment receipts/slips to the server with interactive upload progress tracking.
  * **DMIS Coins**: Use virtual currency (DMIS Coins) directly with automatic verification of account balances.
* **Redemption Program**: Redeem physical rewards (Evian water, cooling towels, Yeti tumblers, Whey protein) using loyalty points accumulated from bookings.
* **Booking Cancellation Request**: Request cancellation of future scheduled events with an automated refund rate of 80% returned in DMIS Coins upon Admin approval.

### 2. Administrator Operations
* **Central Reservation Validation**: View all pending court reservations, verify uploaded bank transfer receipts, and transition reservations from "Pending" to "Approved".
* **Cancellation Management**: Review submitted cancellation requests and approve them to automatically trigger coin refunds and release court slots.
* **Interactive Timetable Scheduler**: Monitor court schedules across sports (Tennis, Football, Table Tennis) with real-time status indicators (Available, Pending, Reserved).
* **Equipment Rental Desk**: Hand-deliver sport-specific rental equipment (rackets, soccer balls, tennis packs) to users with active court sessions, calculating bills instantly.

---

## Project Structure

```
├── fullproj.py           # Unified codebase combining models, routing, UI, and startup configurations
├── uploads/              # Server-side directory for uploaded payment slips and receipts
└── img/                  # Static assets directory (e.g., QR Code images)
```

### Core Architecture Classes (OOP Design)
* **`System`**: Act as the Facade and Controller. Manages in-memory database arrays, handles user validation, searches entities, checks available slots, and handles core registration/login processes.
* **`User`**: Entity containing base biological and contact details.
* **`Account`**: Superclass managing base authorization keys. Generates unique, zero-padded five-digit Account IDs sequentially.
* **`Member` (extends `Account`)**: Stores transactional history, loyalty points, DMIS Coin balances, unclaimed coupons, and tracks daily coupon claims.
* **`Admin` (extends `Account`)**: Grants elevated access levels to manage reservations and verify receipts.
* **`Court`**: Defines court specifications, hourly base rates, sport types, and booking point rewards.
* **`CourtBooking`**: Represents a physical transaction booking. Tracks schedule constraints, user association, selected payment options, transaction receipts, and tracks sequential booking IDs.
* **`History`**: Archive entity wrapping a completed booking.
* **`Coupon`**: Configures promotional campaign structures with dynamic percentage discounts and expiration constraints.
* **`Payment`**: Provides static calculations for currency exchange, coin deduction limits, and discount applications.
* **`Equipment`**: Represents physical rentable equipment with rental rates and image associations.
* **`EquipmentRental`**: Records live equipment hand-outs, binding renters to timing slots.

---

## Data Flow Diagram

```
[Member Client] 
     │ 
     ├─► Select Sport, Court, & Time (Dynamic checks via HTMX)
     ├─► Choose Payment (QR Code with File Upload OR DMIS Coins)
     └─► Submit Reservation (State: Pending Approval)
              │
              ▼
[Admin Dashboard] 
     │
     ├─► Verify uploaded receipt image
     ├─► Confirm Booking -> Triggers: State to Approved, awards Loyalty Points to Member
     └─► Confirm Cancellation -> Triggers: Releases slot, refunds 80% value in DMIS Coins
```

---

## How to Run

### Prerequisites
Make sure Python 3.10 or higher is installed on your workstation.

### Installation

1. Clone the repository to your local directory:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install python-fasthtml fastapi uvicorn
   ```

### Running the Application

Execute the unified codebase file:
```bash
python fullproj.py
```

The system will start a local development server. Open your web browser and navigate to:
```
http://127.0.0.1:5032
```

---

## Default Accounts for Testing

To assist with initial system evaluation, the following pre-configured mock credentials are loaded automatically during initialization:

### 1. Administrator Account
* **Username**: `Adminaccount`
* **Password**: `adminloginpassword`

### 2. Member Accounts
* **Username**: `Dear`
  * **Password**: `12345678`
  * **DMIS Coins**: 500 Coins
  * **Loyalty Coupons**: Dynamic codes AAAA, BBBB, CCCC, DDDD pre-assigned
* **Username**: `john_doe`
  * **Password**: `password123`
* **Username**: `jane_doe`
  * **Password**: `password456`
* **Username**: `SigmaO_o`
  * **Password**: `1234`
* **Username**: `Catt`
  * **Password**: `5555`

---

## Route and API Map

| Route | Method | Access Level | Description |
|---|---|---|---|
| `/` | GET | Public | Landing homepage of DMIS Court |
| `/signup` | GET/POST | Public | New member registration page and input validation endpoint |
| `/login` | GET/POST | Public | Standard authentication processing and session instantiation |
| `/home` | GET | Member | Interactive Dashboard with scheduling and promotional links |
| `/booking_tennis_court` | GET | Member | Step-by-step tennis booking interface powered by HTMX |
| `/booking_football_court` | GET | Member | Step-by-step football booking interface powered by HTMX |
| `/booking_table_tennis_court` | GET | Member | Step-by-step table tennis booking interface powered by HTMX |
| `/Submitnocoupon` | GET/POST | Member | Core reservation summary page without active coupons |
| `/Coupon` | POST | Member | Displays available personal coupons for discount selection |
| `/Submitwithcoupon` | POST | Member | Reservation summary incorporating percentage-based discounts |
| `/QRCODE` | POST | Member | Displays bank transfer details, file upload for receipts, and session countdown |
| `/upload` | POST | Member | Asynchronous handler for binary receipt image uploads |
| `/Dmis_pay` | POST | Member | Finalizes checkout deduction against member DMIS Coin balances |
| `/ConfirmReserve` | POST | Member | Finalizes booking request and sends to Admin pending verification queue |
| `/bookingHis` | POST | Member | Displays reservation history table with active cancel request handlers |
| `/choose_order` | GET | Member | Selection portal to cancel eligible future bookings |
| `/requestcanceldone` | POST | Member | Submits court booking cancellation to Admin approval queue |
| `/redeem` | GET/POST | Member | Point-redemption store interface for physical products |
| `/my-profile` | GET | Member | Access personal records |
| `/edit-profile` | GET/POST | Member | Profile modification gateway and persistence |
| `/admin` | GET | Admin | Base operational control dashboard for administrators |
| `/accept_reserve` | GET | Admin | Verifies slip uploads and executes booking activation transitions |
| `/accept_cancel` | GET | Admin | Processes and approves member cancellation requests with coin refunds |
| `/equipment-rental` | GET/POST | Admin | Dispatches rentable gear bound to member checkout slots |
| `/court_checking` | GET | Public | Dynamic viewer for public timetable availability searches |
