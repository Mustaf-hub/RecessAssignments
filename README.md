# Recess-26

A simple command-line e-commerce demo application written in Python.

## What this repository is about

This project demonstrates a basic role-based shopping/checkout flow with a price calculator. It includes:

- **Role-based login** for `admin`, `customer`, and `cashier`
- **Pricing rules** based on subtotal tiers
- **Coupon discounts** (`SAVE10`, `SAVE20`, `VIP25`)
- **Tax calculation** by location (`local`, `state`, `international`)
- **Interactive menus** for each user role

The app is intended as a beginner-friendly practice project for Python functions, control flow, input handling, and modular logic.

## Project structure

- `/home/runner/work/Recess-26/Recess-26/e_commerce.py` — main application logic and CLI entry point

## How to run

1. Ensure Python 3 is installed.
2. From the repository root, run:

```bash
python e_commerce.py
```

## Default login credentials

- **Admin**: `admin` / `admin123`
- **Customer**: `customer` / `customer123`
- **Cashier**: `cashier` / `cashier123`

## Notes

- Combined subtotal + coupon discounts are capped at **50%**.
- This is a local CLI practice project and does not include a database, web UI, or payment integration.
