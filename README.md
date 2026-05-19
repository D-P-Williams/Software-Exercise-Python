# Software Exercise Python - QQ EXERCISE MATERIAL NOT FOR DISTRIBUTION

## Note from assessor

One of your senior colleagues has had a quick look at the code and spotted a few errors in it, they have asked you to look at and fix them.
Unfortunately, they have misplaced the list they made!

You have been assigned to the task of getting the code functional again and providing the delivery details for the [three customers they have provided](./customers.json) as test evidence for completion.
Your answers will be confirmed by running your scripts.

Please do not spend more than 1-2 hours on this exercise.

> Note: Avoid using AI for this exercise, we will be checking for AI usage.

## Note From Author

I am not a python developer, I am absolutely sure that I butchered some Python best practice somewhere in this example.
Some of that is intentional, left as improvements for you, most will be my own ineptitude :)

---

**Everything below this point constitutes the exercise**

---

## Introduction

You've inherited some code from a colleagues, and your customer is complaining that it is not working at all.
Additionally, when it was previously working, it didn't seem to be producing the expected results.

They have provided you with their testing data, and verified correct values from their extant tool, [in the test data file provided](test_data.md).

The customer has asked you to investigate the issues in the program, and provide delivery information for the [three customers they have provided](./customers.json) as an acceptance test.

Please can you fix and test the code and provide a user friendly way of getting the transport costs and times for the 3 customer sites.

## Useful Details

The world for this example is a 100 by 100 grid of connected points.
Where every point is connected to it's cardinally adjacent neighbours.
Every connection is 1 mile long, i.e. coordinates 0,0 to 0,1 is 1 mile.

The dispatch center is located at coordinates 20,30.

## Calculations and Details

Digging through the information the customer has previously provided, you find a document containing the specifications
for each transport method and the formulas used to calculate delivery time and costs, below.

Notes:

- `x` in all formulas represents total distance
- Markdown preview should display rendered formulas if easier to view

### Truck

Each truck has the following specification:

- Can only travels along grid lines
- Travels at a speed of 35mph
- Has to stop due to traffic at every 3rd junction, for a time of 2 minutes

Cost: $`(x^2 - 95x + 2880)/12`$

### Canal Boat

Each canal boat has the following specification:

- Can only travels along grid lines
- Travels at a speed of 17mph

Cost: $`(5x/12) + (1280/12)`$

### Helicopter

Each helicopter has the following specification:

- Does not need to follow grid lines and always takes a direct path
- Travels at a speed of 65mph
- Requires an initial 30 minutes to setup and refuel before it can take off
  - Which should be accounted for in delivery time

Cost: $`(x/2) + 195`$
