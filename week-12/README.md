# Week 12 - Final Project and Expo Hackathon

## Overview

This week brought together everything from the bootcamp in two projects:

1. **The final Capstone Project, EnterpriseFlow**, a complete Django web application built individually.
2. **The Expo Hackathon (15 to 17 October 2026)**, where my team built **EMAA (إيماء)**, an accessibility app for visitors of Expo 2030 Riyadh.

---

## 1. Capstone Project: EnterpriseFlow

**EnterpriseFlow** is a bilingual (Arabic and English) web application for managing internal service cases, service-level agreements (SLAs), and the vendors and contracts behind them.

It replaces tracking requests by email and spreadsheets with one workflow: a case is created, receives an SLA deadline automatically, is assigned and worked on, then resolved and confirmed by the requester.

### Main Features

- **Case workflow:** create, assign, start, put on hold, resolve, confirm, reopen, and cancel cases, with a unique reference and a full history of every change.
- **SLA monitoring:** deadlines set automatically from the priority, an "at risk" state when 25% of the time remains, and a clock that pauses while waiting on the requester.
- **Vendors and contracts:** vendor and contract records, with SLA compliance and breaches calculated from the linked cases.
- **Leave handover:** an officer's leave request is reviewed by the manager, who reassigns the officer's open cases in the same step.
- **Dashboards and reports:** a dashboard for each role and an SLA report by department, priority, category, and officer, with CSV export.
- **Four roles:** requester, case officer, department manager, and administrator, each enforced on the server.
- **Arabic and English:** a full right-to-left Arabic interface, plus light and dark themes.

### How It Uses the Bootcamp Topics

| Topic | Where it appears |
|---|---|
| Models, relationships, and constraints | Cases, departments, vendors, contracts, and leave requests, protected by database `CheckConstraint`s |
| Migrations | A data migration that merged six roles into four |
| QuerySets, `Q`, and `F` | Search, filters, role scopes, and comparing `resolved_at` with `sla_due_at` |
| Aggregation and annotation | Dashboard figures with `aggregate()`, and per-department, per-vendor, and per-officer figures with `annotate()` |
| Forms and validation | Every action form, with business rules checked on the server |
| Sessions and authentication | Django authentication, with the language and theme saved per user |
| Static and media files | One stylesheet, and permission-checked file attachments |
| Templates and URL routing | Template inheritance, partials, and namespaced URLs |

### Technology

Python, Django 5.2, SQLite, HTML, CSS, and JavaScript. The project has 108 automated tests and full documentation: README, ERD, design, verification record, and demo script.

🔗 The project is maintained in a separate private repository.

---

## 2. Expo Hackathon: EMAA (إيماء)

**Dates:** 15 to 17 October 2026

**EMAA** is an accessibility-first companion app for Deaf, hard-of-hearing, and non-speaking visitors of **Expo 2030 Riyadh**. It helps them plan their visit and communicate at pavilions using **Saudi Sign Language**.

### Main Features

- **Language first:** the visitor chooses Arabic or English, and the interface and sign language follow that choice.
- **Sign language avatar:** an avatar shows Saudi Sign Language, and every screen can be explained in sign language.
- **Visit planning:** suggested pavilions and a visit plan based on the visitor's goals, interests, and available time, with the reason for each suggestion.
- **Communication tools:** type with a sign-language keyboard while the phone speaks the message, and see the other person's words as text and signs.
- **Camera and QR codes:** translate a speaker or video with the camera, and scan a pavilion's QR code to open its details.
- **Pavilion details:** information about each pavilion and its accessibility services.

The content uses demo data built around the official Expo 2030 Riyadh sub-themes, because the pavilions have not been announced yet.

### My Contribution

- Built the **Django REST Framework backend**: visitor profiles, pavilions and activities, visit plans, recommendations, and the communication phrases.
- Built the **Flutter app** from the team's Figma design, including the language choice and the sign language features.
- Merged my teammates' work into the final version and prepared it for the team on GitHub.

### Technology

Django, Django REST Framework, Flutter, and Figma.

🔗 The project is maintained in a separate private repository shared with the team.

---

## Key Takeaways

- A complete product needs more than features: validation, permissions, tests, and documentation.
- Planning the data model and the ERD first made the rest of the capstone easier to build.
- Aggregation and annotation turn stored records into reports that support real decisions.
- A hackathon rewards scope control: build the core journey first, then improve it.
- Working in a team needs clear Git practices, especially when merging parallel work.

---

**Status:** ✅ Completed
