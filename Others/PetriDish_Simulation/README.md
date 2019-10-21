Class Inheritance in C++

Make the simulation `g++ main.cpp ActiveBacteria.cpp PetriDish.cpp DieteticBacteria.cpp HungryBacteria.cpp LazyBacteria.cpp -o Simulation` in linux environment.

run `./Simulation` to play around with the petridish.

System Description:

A computerized Petri dish simulation. This is a coding exercise, not related to biology...

A Petri dish is a tool for growing bacteria and fungi and a "computerized Petri dish" is a tool
Allowing tracking of a bacterial population in a Petri dish without the need for a microscope.
Simulation process:
1. A new petri dish is set to be food-free (a breeding substrate) and without bacteria.
2. You can add bacteria (bacteria) and food to the dish.
3. For any existing bacteria:
Unique identifier (representing its type) .i
Eating rate (amount of time units after which food is needed)
The amount of food that is needed at any such point in time. .iii
Adulthood) By the age of adulthood the bacterium can replicate itself
4. After adding bacteria and food - lab workers want to get a snapshot of the bacterial population
At the plate a certain time later.
5. For the duration of their life, the bacteria consume food (at the rate set at boot) / replicate themselves and finally,
Once the food is over, die. When the bacterium dies - it disappears from the plate.

For example, the following imput of
```
add_bacteria 1 2 4 4
add_bacteria 3 2 2 2
add_food 25
add_bacteria 5 6 2 2
add_bacteria 7 2 6 5
print
update_time 1
print
update_time 1
print
add_food 20
update_time 2
print
add_food 50
update_time 6
print
add_food 50
update_time 5
print
update_time 2
print
update_time 15
print
quit
```

should result in 
```
Active Bact.Bacteria ID: 1 Age: 0
Lazy Bact.Bacteria ID: 3 Age: 0
Hungry Bact.Bacteria ID: 5 Age: 0
Dietetic Bact.Bacteria ID: 7 Age: 0
Food left: 25
Active Bact.Bacteria ID: 1 Age: 1
Lazy Bact.Bacteria ID: 3 Age: 1
Hungry Bact.Bacteria ID: 5 Age: 1
Dietetic Bact.Bacteria ID: 7 Age: 1
Food left: 13
Active Bact.Bacteria ID: 1 Age: 2
Lazy Bact.Bacteria ID: 3 Age: 2
Hungry Bact.Bacteria ID: 5 Age: 2
Dietetic Bact.Bacteria ID: 7 Age: 2
Food left: 9
Active Bact.Bacteria ID: 1 Age: 5
Lazy Bact.Bacteria ID: 3 Age: 4
Hungry Bact.Bacteria ID: 5 Age: 2
Dietetic Bact.Bacteria ID: 7 Age: 4
Active Bact.Bacteria ID: 1 Age: 1
Hungry Bact.Bacteria ID: 5 Age: 1
Food left: 11
Active Bact.Bacteria ID: 1 Age: 15
Lazy Bact.Bacteria ID: 3 Age: 10
Hungry Bact.Bacteria ID: 5 Age: 8
Dietetic Bact.Bacteria ID: 7 Age: 3
Active Bact.Bacteria ID: 1 Age: 12
Hungry Bact.Bacteria ID: 5 Age: 5
Active Bact.Bacteria ID: 1 Age: 6
Active Bact.Bacteria ID: 1 Age: 5
Hungry Bact.Bacteria ID: 5 Age: 2
Dietetic Bact.Bacteria ID: 7 Age: 3
Active Bact.Bacteria ID: 1 Age: 2
Active Bact.Bacteria ID: 1 Age: 2
Active Bact.Bacteria ID: 1 Age: 1
Hungry Bact.Bacteria ID: 5 Age: 1
Food left: 0
Lazy Bact.Bacteria ID: 3 Age: 15
Hungry Bact.Bacteria ID: 5 Age: 13
Dietetic Bact.Bacteria ID: 7 Age: 1
Hungry Bact.Bacteria ID: 5 Age: 10
Hungry Bact.Bacteria ID: 5 Age: 7
Hungry Bact.Bacteria ID: 5 Age: 6
Dietetic Bact.Bacteria ID: 7 Age: 1
Food left: 0
Hungry Bact.Bacteria ID: 5 Age: 15
Hungry Bact.Bacteria ID: 5 Age: 12
Hungry Bact.Bacteria ID: 5 Age: 9
Hungry Bact.Bacteria ID: 5 Age: 8
Dietetic Bact.Bacteria ID: 7 Age: 3
Food left: 0
Food left: 0
