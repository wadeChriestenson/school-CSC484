# Investment Growth Program

principal = 1000
rate = 0.07

print("Yearly Investment Growth at 7% Return")
print("-------------------------------------")

for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f"Year {year}: ${amount:.2f}")

# Specific required outputs
year10 = principal * (1 + rate) ** 10
year20 = principal * (1 + rate) ** 20
year30 = principal * (1 + rate) ** 30

print("\nRequired Results")
print("----------------")
print(f"After 10 years: ${year10:.2f}")
print(f"After 20 years: ${year20:.2f}")
print(f"After 30 years: ${year30:.2f}")