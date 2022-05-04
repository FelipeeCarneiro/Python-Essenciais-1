#this program computes the number of seconds in a given number of hours.
# this program has been written in november/30/2021 by Felipe Carneiro at 19:39.
name_of_program = "\nThis program computes the number of seconds in a given number of hours"
print( name_of_program,"-"*len(name_of_program),sep="\n")

number_of_hours = ""
seconds_in_1_hour = 3600

while number_of_hours == "":
    number_of_hours = int(input("Insert the number of hours:"))

print("Hours: ", number_of_hours)
print("Seconds in Hours: ", number_of_hours * seconds_in_1_hour)

#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 2 hour
#i don't know if i belive in this, but... was right on time that i finished this program 19:39 >> https://www.numerosdosanjos.com.br/2019/10/anjo-numero-1939.html
