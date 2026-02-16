# Rihal Codestacker 2026 (Backend): Queue & Appointment Booking System

## Background

Rihal operates **“FlowCare”**, a growing network of service branches across Oman that handles high daily traffic: government-style counters, clinics, customer care desks, and internal support services.

Over the past year, FlowCare expanded quickly, but appointment handling didn’t. Branches are now struggling with:

- Overlapping bookings and “double-booked” staff
- Walk-ins flooding the queue while booked customers wait
- No clear audit trail when appointments are edited or canceled
- Branch managers unable to control schedules outside their branch
- No consistent system-wide visibility for admins

Your mission is to build the backend that powers **FlowCare’s Queue & Appointment Booking System**, a secure, role-based platform that supports scheduling, rescheduling, cancellations, and staff/branch controls, while maintaining accountability through audit logs.

---

## Problem Statement

Build a backend API system that enables customers to book service appointments at specific branches with available time slots and assigned staff.

The system must support:

- Booking / cancelling / rescheduling appointments
- Branch-based access control
- Staff roles + permissions
- Authentication & authorization
- Seed data import (provided file) to populate the database at startup
- Audit logging for sensitive actions (booking changes, cancellations, schedule updates, etc.)

> This is a backend-only challenge. You are expected to build an API server and database schema that meets the requirements below.

---

## Entities

You must model at least the following entities:

- **Branch**
- **ServiceType**
- **Slot**
- **Staff**
- **Customer**
- **Appointment**
- **AuditLog**

You may add supporting entities such as:

- `Role`
- `StaffServiceType`
- `WorkingHours`
- `Attachment`
- etc.

---

## Roles, Authentication, and Authorization

All APIs must be protected with authentication except where explicitly stated.

### Authentication

- The system must support **Basic Authentication**.
- The system must start with a **default Admin user**.
- All APIs must be protected using authentication except where explicitly stated (public endpoints).

---

## Roles & Permissions

The system must support the following roles:

### 1) Admin (System-wide)

Can:

- Manage all branches, service types, staff, and customers
- View and manage all appointments in all branches
- Create/update slots across branches
- View the full audit log

---

### 2) Branch Manager (Branch-scoped)

Can:

- Manage only their assigned branch
- Create/update slots for their branch
- Assign staff to service types in their branch
- View/manage appointments in their branch
- View audit logs for their branch

Cannot:

- Access or modify data belonging to other branches

---

### 3) Staff (Branch-scoped)

Can:

- View their schedule and assigned appointments
- Update appointment status (e.g., `checked-in`, `no-show`, `completed`)
- Add internal notes (optional)

Cannot:

- Create slots
- Cancel/reschedule appointments on behalf of customers  
  (unless explicitly allowed by Branch Manager policy)

---

### 4) Customer

Can:

- Register / login
- View available service types and slots
- Book appointment
- Cancel own appointment
- Reschedule own appointment
- View own appointment history

---

## Seed / Example Data

You will be provided with a seed file (`JSON`) containing example data.

Your application must import and populate the database on startup.

At minimum, the seed data must include:

- Branches (at least 2 branches)
- ServiceTypes (at least 3 service types per branch)
- Staff users (at least 2 staff per branch)
- Branch Managers (at least 1 manager per branch)
- Slots for the next 3–7 days (minimum 10 slots total)

### Important Seeding Rules

- Seeding must be **idempotent** (running the app multiple times must not duplicate rows).
- Slots must be tied to:
  - A `Branch`
  - A `ServiceType`
  - Optionally a `Staff` member (if your model uses staff-specific slots)

---

## Required APIs (Minimum Expected)

Route naming is flexible. The following capabilities must exist.

---

### Public (No Authentication)

- List branches
- List services by branch
- List available slots by branch + service type (+ optional date filter)

---

### Authentication

- Register customer (including storing the required image of the customer’s ID)
- Login (Basic Auth)

---

### Customer (Authenticated)

- Book appointment (including storing an optional attachment). Each slot can be booked once only.
- List my appointments
- Get my appointment details (including the attachment if present)
- Cancel my appointment
- Reschedule my appointment (move to a different slot)

---

### Staff / Manager / Admin (Authenticated)

- List appointments
  - Admin → all branches
  - Manager → branch-only
  - Staff → assigned-to-me
- Update appointment status  
  (`checked-in`, `no-show`, `completed`)
- View audit logs of the branch that the manager is assigned to.

---

### Manager / Admin

- Create slots for a branch (single or bulk)
- Update slot
- Remove slot (must be implemented as a **soft delete**)
- List staff
  - Admin → all
  - Manager → branch-only
- Assign staff to services / branch
  - Admin → system-wide
  - Manager → branch-only
- List customers
- Get customer (including the ID image)
- Configure the soft-delete retention period number of days value (more info in `Soft Delete Requirements`). This can only be done by admins.
- Clean-up (hard-delete) soft-deleted slots that passed the retention period (more info in `Soft Delete Requirements`). This can only be done by admins.
- View all audit logs. This can only be done by admins.
- Export all audit logs as a `.csv` file. This can only be done by admins.

---

## File Storage Requirements

The system must support secure file storage and retrieval for:

1. **Customer ID Image**
   - Required during customer registration.
   - Must validate that the uploaded file is a valid image.
   - Must enforce file size limits (define a reasonable limit, e.g., 2–5 MB).
   - Must store file reference in the database.

2. **Appointment Attachment (Optional)**
   - Customers may upload an optional attachment during booking.
   - Allowed types: images and/or PDF (define clearly).
   - Must validate file type and size.
   - Attachment must be associated with a specific appointment.

You have the choice between storing files using local filesystem or object storage (MinIO).

### File Retrieval APIs

Authenticated users with proper permissions must be able to:

- Retrieve customer ID image (Admins only)
- Retrieve appointment attachment (staff and above, or the customer if he or she is the creator of the appointment)
- Return correct content-type headers
- Handle cases where file does not exist

---

## Soft Delete Requirements

Soft delete rules:

- Soft delete is required for slots.
- Soft-deleted records must not appear in normal listing endpoints.
- Admins should still be able to see soft-deleted records.
- A `deleted_at` timestamp must be stored.
- All soft delete actions must create an `AuditLog` entry.
- Soft-deleted records must be hard-deleted after a retention period has passed. The retention period should be set as a `number of days` value in the database.
- Hard-delete must not remove the audit log entry for the soft-delete action.
- Hard-delete must deal with all the data that is related to the slot being deleted. Either remove that data or set the reference to be null.
- Cleanup must be **idempotent** (running it multiple times should not cause errors or remove more data than intended).

---

## Audit Log Requirements

Sensitive actions must be logged, including:

- Appointment creation
- Appointment reschedule
- Appointment cancellation
- Slot creation/update/delete
- Hard delete actions
- Staff assignment changes

Each `AuditLog` record must include:

- Action type
- Actor (user ID + role)
- Target entity type
- Target entity ID
- Timestamp
- Optional metadata (JSON)

Admin must be able to view all logs.  
Branch Managers must only view logs for their branch.

---

## Technical Requirements

- Must use PostgreSQL
- Must use Git
- Must publish code to GitHub
- Must include README with:
  - Setup instructions
  - Environment variables
  - Seeding instructions
  - Example API usage (curl or Postman)
- Must include migration scripts
- Must handle seeding idempotently

---

## Bonus Challenges (Optional)

Want an edge over your competition? You have an opportunity to do so by solving these extra problems that we are facing in **FlowCare**. These are not required, but solving as many as you can enhance your chances of winning by demonstrating your capability to tackle real-world BE application like scalability, performance, and reliability.

### 1) Input and Output Enhancements

Enhance the listing APIs with the following improvements:

- Pagination:
  - Listing APIs must support pagination using page and size query parameters.
  - The response must include:
    - results: array of records for the current page
    - total: total number of matching records (ignoring pagination)
  - Example response format:
    ```
    {
      "results": [...],
      "total": 125
    }
    ```
  - If page or size is not provided, you may apply sensible defaults.

- Search:
  - Listing APIs must support a term query parameter to search records.
  - The term parameter should match one or more relevant fields (e.g., name, email, branch name, service name, etc.).
  - Search should be case-insensitive.
  - Search must apply before pagination.

### 2) Queue Position Logic

- Add real-time queue position calculation
- Expose endpoint to get live queue number per branch

### 3) Rate Limiting

- Limit customers to X bookings per day
- Limit rescheduling frequency

### 4) Background Scheduling Service

- Make a background scheduling service using cron, for example, to hard-delete soft-deleted records automatically after the retention period has passed. This would replace the clean-up API described above.

### 5) Deployment

- Dockerize project
- Provide docker-compose file
- Deploy to cloud and provide live API URL
- Provide a README explaining how we can deploy your application.

---

## Deliverables

Your submission must include:

- GitHub repository link
- Clear README
- Database schema
- Seed file + import logic
- Working API server

This is a backend-only challenge. No frontend is required.

# Unleash Your Creativity ✨💡!!