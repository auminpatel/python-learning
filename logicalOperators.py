#if applicant has high income AND good credit
#   Eligible for Loan



has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan only if has high income and good credit ")



#if applicant has high income or good credit
#   Eligible for Loan

# AND: both true
# OR: any one



has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
     print("Eligible for loan for Either has high income or good credit ")



#NOT inverted of Boolean
# if a user has good income and doesnot has a crimail record
has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print("Eligible for loan for Either has high income and not crimainal record ")
