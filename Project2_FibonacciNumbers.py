#The Fibonacci sequence is obtained by addition of the present term and its previous term.
#It means the nth term is sum of (n-1)th and (n-2)th term

nth_term = int(input("Enter the number of terms required: "))

n1 = 0
n2 = 1
i = 0 #i is the initial count

if nth_term <= 0:
   print("Please enter a positive value")
else:
   print("Fibonacci sequence:")
   while i < nth_term:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       i= i+1
