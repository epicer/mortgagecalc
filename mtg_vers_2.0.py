
#PREAPPROVAL

print 'Assuming 30 year term and 80% LTV'

income = int(raw_input("Borrower's combined base income: "))
other_exp = int(raw_input("Borrower's other liabilities: "))
down_payment = int(raw_input("Liquid assets available: "))
interest_rate = float(raw_input("Expected Interest rate: "))/100
dti = float(raw_input("Target debt to income %: "))/100




def max_payments(income, other_exp, dti):
    payments = (dti*income) - other_exp
    return payments    

def tax_ins(mortgage):
    tax = mortgage/0.8 * 0.0125/12
    ins = mortgage/0.8/7000 + 20
    return tax + ins

def mortgage(interest_rate, payments):
    mortgage = payments/((interest_rate/12)/(1-(1+(interest_rate/12))**(-360)))
    return mortgage

def new_payments(mortgage, payments):
    return payments - tax_ins(mortgage)

def max_mortgage(interest_rate, payments):
    mtg = 0
    pay = 0
    for i in range(10):
        pay = new_payments(mtg, payments)
        mtg = mortgage(interest_rate, pay)
    return (pay, mtg)

def purchprice(dti, down_payment, max_mortgage, max_payments):
    if max_mortgage/0.8 < down_payment/0.2:
        if dti > 0.45:
            down_payment -= max_payments*6
            if max_mortgage/0.8 < down_payment/0.2:
                return max_mortgage/0.8
            else:
    		    return down_payment/0.2
        else:
		    return max_mortgage/0.8
    else:
        return down_payment/0.2


(payresult, mtgresult) = max_mortgage(interest_rate, max_payments(income, other_exp, dti))
taxresult = mtgresult/0.8 * 0.0125/12
insresult = mtgresult/0.8/7000 + 20
base_purchprice = purchprice(dti, down_payment, mtgresult, (payresult+taxresult+insresult))
max_purchprice = base_purchprice

if dti > 0.45:
    for i in range(10):
        taxresult = max_purchprice * 0.0125/12
        insresult = max_purchprice/7000 + 20
        payresult = (max_purchprice*0.8)*((interest_rate/12)/(1-(1+(interest_rate/12))**(-360)))
        max_purchprice = purchprice(dti, down_payment, mtgresult, (payresult+taxresult+insresult))
        mtgresult = max_purchprice*0.8
		
if base_purchprice == down_payment/0.2:
    mtgresult = base_purchprice*0.8
    payresult = (base_purchprice*0.8)*((interest_rate/12)/(1-(1+(interest_rate/12))**(-360)))
    taxresult = base_purchprice * 0.0125/12
    insresult = base_purchprice/7000 + 20
    


print ''
print '' 
print "Maximum purchase price: $%s." %round(max_purchprice, 2)
print "Maximum loan amount:    $%s." %round(mtgresult, 2)
print "The borrower will be paying:"
print "Principle & interest:   $%s." %round(payresult, 2)
print "Taxes:                  $%s." %round(taxresult, 2)
print "Insurance:              $%s." %round(insresult, 2)

exit = 0
while exit != "x":
	exit = raw_input("")