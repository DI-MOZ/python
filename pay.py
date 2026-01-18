# Kenya PAYE bands (monthly)
PAYE_BANDS = [(24000,0.1),(32333,0.25),(500000,0.3),(800000,0.325),(10**9,0.35)]
PERSONAL_RELIEF = 2400

NHIF_RATES = [(5999,150),(7999,300),(11999,400),(14999,500),(19999,600),
              (24999,750),(29999,850),(34999,900),(39999,950),(44999,1000),
              (49999,1100),(59999,1200),(69999,1300),(79999,1400),
              (89999,1500),(99999,1600),(10**9,1700)]

def nssf(g):
    return min(g,6000)*0.06 + min(max(g-6000,0),24000)*0.06

def nhif(g):
    for limit,amt in NHIF_RATES:
        if g <= limit: return amt

def housing(g): return g * 0.015

def paye(t):
    tax, low = 0, 0
    for limit,rate in PAYE_BANDS:
        if t > low:
            tax += (min(t,limit)-low)*rate
            low = limit
    return max(tax - PERSONAL_RELIEF, 0)

def payroll(name, basic, allowance):
    gross = basic + allowance
    nssf_d = nssf(gross)
    house_d = housing(gross)
    nhif_d = nhif(gross)
    taxable = gross - nssf_d - house_d
    paye_d = paye(taxable)
    net = gross - (nssf_d + house_d + nhif_d + paye_d)

    print(f"\nPayslip: {name}")
    print(f"Gross Salary : {gross}")
    print(f"NSSF         : {round(nssf_d,2)}")
    print(f"NHIF         : {nhif_d}")
    print(f"Housing Levy : {round(house_d,2)}")
    print(f"PAYE         : {round(paye_d,2)}")
    print(f"Net Pay      : {round(net,2)}")

# Example run
payroll("Alice", 80000, 10000)
