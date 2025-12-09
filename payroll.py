# -----------------------------------------
# Kenya Payroll System
# -----------------------------------------
# Includes:
# - PAYE calculation (KRA)
# - NSSF (Tier I & II)
# - NHIF (Standard Rates)
# - Housing Levy (1.5%)
# - Personal Relief
# -----------------------------------------

# ---------- PAYE BANDS ----------
PAYE_BANDS = [
    (24000, 0.10),        # First 24,000 at 10%
    (32333, 0.25),        # Next up to 32,333 at 25%
    (500000, 0.30),       # Next up to 500,000 at 30%
    (800000, 0.325),      # Next up to 800,000 at 32.5%
    (float('inf'), 0.35)  # Above 800,000 at 35%
]

PERSONAL_RELIEF = 2400  # Per month

# ---------- NHIF TABLE ----------
NHIF_RATES = [
    (5999, 150),
    (7999, 300),
    (11999, 400),
    (14999, 500),
    (19999, 600),
    (24999, 750),
    (29999, 850),
    (34999, 900),
    (39999, 950),
    (44999, 1000),
    (49999, 1100),
    (59999, 1200),
    (69999, 1300),
    (79999, 1400),
    (89999, 1500),
    (99999, 1600),
    (float('inf'), 1700),
]

# ---------- FUNCTIONS ----------

def calculate_nssf(gross):
    # NSSF Tier I: 6% of first 6,000 (max 360)
    # NSSF Tier II: 6% of next 24,000 (max 1440)
    tier1 = min(6000, gross) * 0.06
    tier2 = min(max(gross - 6000, 0), 24000) * 0.06
    return tier1 + tier2


def calculate_nhif(gross):
    for limit, amount in NHIF_RATES:
        if gross <= limit:
            return amount
    return 0


def calculate_housing_levy(gross):
    return gross * 0.015  # 1.5% employee


def calculate_paye(taxable):
    paye = 0
    lower = 0

    for limit, rate in PAYE_BANDS:
        if taxable > lower:
            band_amount = min(taxable - lower, limit - lower)
            paye += band_amount * rate
            lower = limit
        else:
            break

    paye -= PERSONAL_RELIEF
    return max(paye, 0)


# ---------- EMPLOYEE CLASS ----------

class Employee:
    def __init__(self, emp_id, name, basic_salary, allowances):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.allowances = allowances

    def gross_salary(self):
        return self.basic_salary + self.allowances

    def compute_deductions(self):
        gross = self.gross_salary()
        nssf = calculate_nssf(gross)
        nhif = calculate_nhif(gross)
        housing = calculate_housing_levy(gross)

        taxable = gross - nssf - housing
        paye = calculate_paye(taxable)

        total = nssf + nhif + housing + paye
        return {
            "NSSF": nssf,
            "NHIF": nhif,
            "Housing Levy": housing,
            "PAYE": paye,
            "Total Deductions": total
        }

    def net_salary(self):
        gross = self.gross_salary()
        deductions = self.compute_deductions()["Total Deductions"]
        return gross - deductions

    def display_payslip(self):
        d = self.compute_deductions()

        print("\n========================")
        print("       PAYSLIP")
        print("========================")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Basic Salary  : {self.basic_salary}")
        print(f"Allowances    : {self.allowances}")
        print(f"Gross Salary  : {self.gross_salary()}")
        print("\n--- Deductions ---")
        for k, v in d.items():
            if k != "Total Deductions":
                print(f"{k:<15} : {round(v, 2)}")
        print(f"Total Deductions : {round(d['Total Deductions'], 2)}")
        print("\nNet Salary     :", round(self.net_salary(), 2))
        print("========================\n")


# ---------- MAIN PROGRAM ----------

def main():
    employees = []

    while True:
        print("\n========== PAYROLL MENU ==========")
        print("1. Add Employee")
        print("2. Generate Payslips")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Employee ID: ")
            name = input("Name: ")

            try:
                basic = float(input("Basic Salary: "))
                allowance = float(input("Allowances: "))
            except ValueError:
                print("Invalid input. Salary must be a number.")
                continue

            emp = Employee(emp_id, name, basic, allowance)
            employees.append(emp)
            print("Employee added successfully!")

        elif choice == "2":
            if not employees:
                print("No employees in the system yet.")
            else:
                for emp in employees:
                    emp.display_payslip()

        elif choice == "3":
            print("Exiting payroll system...")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
