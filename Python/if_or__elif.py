#prompt for hours worked and rate per hours
#compute gross pay
#up to 40 hours = pay == rate
#over 40 hours = pay == 1.5* rate
#input 45 hours and 10.50 per hours

#input
print("Define pay per hour below:")
payrate= float(input("Pay per hour: "))
print("How many hours worked?")
hours = float(input("Hours: "))
#compute gross pay and checks if there are no typos
if hours * payrate <= 0:
    print("mamaco, você digitou coisa errada")
elif hours > 100 or payrate >100:
    print("Mamaco você não pode ganhar tanto")
elif hours * payrate < 10:
    print("Seu pobre, seu salário é" , hours * payrate)
elif hours  <= 40 and hours >= 0:
    gross = payrate * hours
    print("Your gross pay is:", gross)
#compute gross pay over 40 hours
elif hours > 40:
    hoursplus = hours - 40
    gross = (40 * payrate) + (1.5 * hoursplus * payrate)
    print("Your gross pay for working so long is:" , gross)



#prompt for score between 0.0 and 1.0
#if out of range print error
#if in range assign grades:
# >= 0.9 A
# >= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

score = float(input("Enter Score:"))
if score <0 or score >1.0:
    print("Careca, põe a nota certa")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("Burro")