#WAF to find the factorial n. (n is the parameter)

n=6 

def cal_fact(n):
  fact=1
  for i in range(1, n+1):
    fact *= 1 
  print(fact)

#WAF to convert USD to INR

def convertor(usd_val):
  inr_val= usd_val *83
  print(usd_val, "USD=", inr_val, "INR")

convertor(1)
convertor(76)  
