# Object-Oriented Programming and Domain Systems Design Lab Suite

An industry-grade, progressive suite of computational algorithms, domain-driven architectures, and object-oriented systems. This repository documents a structured learning path transitioning from basic algorithmic puzzle-solving to designing complex, secure transactional business architectures utilizing advanced Python patterns, custom state verification, inheritance hierarchies, and automated unit testing frameworks.

---

## Technical Stack

* **Language**: Python 3.10+
* **Libraries**: 
  * `unittest` (Automated regression testing)
  * `json` (Serialization, parsing, and record state management)
  * `datetime` (Temporal calculations, calendar rules, and maturity verification)
* **Design Paradigms**: Procedural Algorithms, Object-Oriented Programming (OOP), Domain-Driven Design (DDD), Test-Driven Development (TDD) elements.

---

## Project Structure

The codebase is organized into modular segments representing developmental progressions:

```text
OOP/
├── Lab_01/
│   ├── Lab_01_1.py       # Mathematical series term expansion (N + NN + NNN + NNNN)
│   ├── Lab_01_2.py       # Largest palindrome product logic
│   ├── Lab_01_3.py       # Deterministic commercial parking fee calculation system
│   ├── Lab_01_5.py       # Lexicographical minimum sequence arrangement (excluding leading zeros)
│   └── Lab_01_6.py       # Optimal adjacent-element array product optimization
├── Lab_02/
│   ├── Lab_02_1.py       # Gregorian calendar day-of-year calculation with leap year validation
│   ├── Lab_02_2.py       # Absolute temporal duration counter between arbitrary dates
│   ├── Lab_02_3.py       # Dynamic score assignment and statistical computation
│   ├── Lab_02_4.py       # Nested JSON student registry manager
│   ├── Lab_02_4test.py   # Multi-student statistics helper module
│   ├── Lab_02_5.py       # Music collection inventory state controller (Dynamic CRUD operations)
│   └── Lab_02_test.py    # Standalone verification suite for JSON updates
├── Lab_03/
│   └── Lab_03.py         # Academic registration portal (Students, Courses, Grading, GPA computation)
├── Lab_04/
│   └── Lab_04.py         # Basic ATM physical/virtual ledger transaction framework
└── Lab_05/
    └── Lab_05.py         # Production-grade Enterprise Banking Engine & Automated Test Suite
```

---

## Architectural Features

### 1. Algorithmic Processing Engine (Lab 01 & Lab 02)
* **Deterministic Calculations**: Modules handle mathematical transformations such as checking and computing temporal offsets, processing raw text inputs, and performing numerical validation without third-party mathematical wrappers.
* **Leap Year and Date Arithmetician**: Features a complete, zero-dependency calendar management program that validates input format boundaries, identifies Gregorian leap years, and measures temporal gaps down to absolute days.
* **Music Inventory State Machine**: Implements dynamic object updating mimicking real-world database transactions. Modifies tracks, dynamic properties, and artist collections based on explicit transactional priorities.

### 2. Academic Enrollment and Performance Analytics (Lab 03)
* **Domain Model Components**: Contains entities representing physical domain models (`Student`, `Teacher`, `Subject`, `Enroll`).
* **Encapsulation & Mutator Guardrails**: Access to critical data properties is strictly managed using Python property decorators (`@property` and `@setter`), filtering invalid value assignments.
* **Registry Querying**: Supports complex querying mechanisms, including lookup operations by identifiers, registry listings, course rosters, and dynamic GPA evaluations based on credit-weighted scale points.

### 3. Basic Financial Transaction Machinery (Lab 04)
* **Security & Pin Authentication**: Simulates physical transaction flows with validation steps like physical pin entry and database records linking cards to legal owners.
* **Ledger Auditing**: Builds atomic transactions (`Transaction`) documenting state updates: operation categories, timestamp proxies, machine identification codes, and ledger changes.
* **Physical & Policy Constraints**: Monitors hardware cash limits and imposes transaction rules such as maximum daily withdrawal limits of 40,000 units.

### 4. Enterprise Banking Architecture & Automated Testing Suite (Lab 05)
* **Polymorphic Account Hierarchy**:
  * `SavingAccount`: Performs annual compound interest calculations.
  * `FixedAccount`: Tracks deposit dates and enforces lock-up periods, checking dates against maturity targets before executing withdrawals.
  * `CurrentAccount`: Manages high-volume transactional pipelines without individual processing limits.
* **Hierarchical Payment Instruments**: Uses an inheritance hierarchy for payment instruments (`Card` -> `DebitCard` -> `ShoppingDebitCard` / `TravelDebitCard` and `ATMCard`), applying specialized behaviors like card-specific annual fees and merchant point-of-sale cashbacks.
* **Multi-Channel Delivery System**: Executes actions depending on transaction channels:
  * `ATMMachine`: Facilitates automated, self-service transactions.
  * `Counter`: Runs manual transactions requiring government-issued identity verification.
  * `EDCMachine`: Coordinates store-front retail processing with point-of-sale rules.
* **Enterprise Verification Suite**: Integrates 19 unit tests checking for edge cases like negative deposits, withdrawal limit breaches, early maturity withdrawals, and wrong credit card point-of-sale swipes.

---

## Core Domain Models (Lab 05 Class Diagram)

```text
                           ┌──────────┐
                           │   Bank   │
                           └───┬──────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
     ┌───────┐           ┌───────────┐         ┌───────────┐
     │ User  │           │ Account   │         │  Channel  │
     └───────┘           └─────┬─────┘         └─────┬─────┘
                               │                     │
         ┌─────────────────────┼─────────┐           ├──────────────┬──────────────┐
         ▼                     ▼         ▼           ▼              ▼              ▼
  ┌─────────────┐       ┌────────────┐ ┌───┐ ┌───────────┐   ┌───────────┐   ┌───────────┐
  │SavingAccount│       │FixedAccount│ │...│ │ATMMachine │   │  Counter  │   │EDCMachine │
  └─────────────┘       └────────────┘ └───┘ └───────────┘   └───────────┘   └───────────┘
```

---

## Installation & Environment Setup

### Prerequisites
* Python 3.10 or higher.
* No external packages required. Standard library dependencies are used to guarantee stability and security.

### Cloning the Repository
```bash
git clone https://github.com/your-username/OOP-Lab-Suite.git
cd OOP-Lab-Suite
```

---

## Running the Applications

### Executing Standalone Algorithmic Modules (Labs 1 & 2)
To run isolated computational problems, execute the script and input parameters via standard input (stdin):

```bash
# Execute the parking fee calculator
python Lab_01/Lab_01_3.py

# Input format: [Entry Hour] [Entry Min] [Exit Hour] [Exit Min]
# Example Input: 07 30 12 45
```

### Running the Academic Portal (Lab 03)
Execute the registration script to run pre-configured test scenarios mapping the system's database interactions:

```bash
python Lab_03/Lab_03.py
```

### Simulating Financial Transactions (Lab 04)
Run the transactional model to execute physical system simulations, database linking, and transaction history output:

```bash
python Lab_04/Lab_04.py
```

### Running the Enterprise Banking Test Suite (Lab 05)
To execute the automated regression test suite containing 19 test cases, run:

```bash
python -m unittest Lab_05/Lab_05.py
```

#### Test Suite Verification Output Example:
```text
...................
----------------------------------------------------------------------
Ran 19 tests in 0.005s

OK
```

---

## Detailed Test Case Coverage (Lab 05)

The automated test coverage validates the robustness of the enterprise banking system against the following test scenarios:

1. **Normal Deposit**: Verifies ATM deposits update ledger balances and write auditing transactions.
2. **Negative Deposit Rejection**: Ensures negative values are caught and rejected.
3. **Withdrawal Over Limits**: Blocks saving account withdrawal attempts exceeding the 50,000 unit limit.
4. **Interest Calculation**: Confirms compound interest calculations add correct earnings to balances.
5. **Counter Deposit**: Validates bank teller deposit pipelines.
6. **Identity Fraud Prevention**: Confirms deposits/withdrawals over the counter fail when using incorrect citizen credentials.
7. **Fixed Account Initialization**: Tests the creation of locked savings accounts.
8. **Premature Fixed Withdrawal**: Ensures withdrawing before fixed term limits triggers penalty rules.
9. **Zero-Balance Withdrawal Rejection**: Blocks withdrawals from accounts without initial deposits.
10. **Multiple Deposit Layering**: Verifies sequential deposits increment target balances without ledger drift.
11. **Matured Fixed Withdrawal**: Ensures withdrawals at maturity award full calculated interest.
12. **Current Account Deposits**: Checks ledger updates for non-savings accounts.
13. **Large Current Account Withdrawals**: Verifies high-volume transactions bypass savings account limits.
14. **Overdraft Protection**: Validates current account withdrawal attempts exceeding available limits are blocked.
15. **EDC Merchant Payment**: Verifies card swipes subtract customer balances and credit merchant accounts.
16. **Debit Card Fee Deduction**: Tests automated debit card billing cycles.
17. **ATM Card Fee Deduction**: Validates maintenance billing cycles for ATM-only cards.
18. **Cashback Calculations**: Ensures customer payments calculate and add cashback bonuses to customer balances.
19. **Instrument Restrictions**: Prevents ATM cards from being used for payment transactions on EDC machines.



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
