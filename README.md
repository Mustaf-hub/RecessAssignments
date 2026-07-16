# Recess-26

This repository contains a simple command-line e-commerce application written in Python.

## What the project does

The app simulates a basic store checkout flow with:
- Role-based login (`admin`, `customer`, `cashier`)
- Price calculation from a subtotal
- Automatic subtotal discounts based on spending tiers
- Optional coupon discounts (`SAVE10`, `SAVE20`, `VIP25`)
- Tax calculation by location (`local`, `state`, `international`)
- A discount cap to prevent total discounts from exceeding 50%

## Main file

- `/home/runner/work/Recess-26/Recess-26/e_commerce.py` – contains all business logic, menus, and CLI interaction.

## How to run

From the repository root:

```bash
python e_commerce.py
```

## Default login credentials

- `admin` / `admin123`
- `customer` / `customer123`
- `cashier` / `cashier123`
