# Monitoring Status Record

Version:

v1.0.0

---

## Purpose

Define the record structure for reference state monitoring activities.

---

## Record Fields

Includes:

- monitoring identifier;
- reference state version;
- observed architecture state;
- comparison result;
- detected changes;
- impact indication;
- historical record.

---

## Monitoring Lifecycle


MONITORING INITIATED

↓

STATE OBSERVED

↓

REFERENCE COMPARED

↓

CONDITION RECORDED

↓

STATUS PRESERVED


---

## Monitoring States

Possible states:

- INITIALIZED;
- OBSERVING;
- ALIGNED;
- REVIEW REQUIRED;
- DRIFT IDENTIFIED;
- HISTORICAL.

---

## Principle

Monitoring Status Records preserve the operational history of certified architecture observation.
