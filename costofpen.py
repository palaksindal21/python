<<<<<<< HEAD
number_of_pen = int(input("Total number of pen:")) 
cost_of_1pen = int(input("Cost of one pen:")) 
cost_of_pens = number_of_pen*cost_of_1pen

if  cost_of_pens>1000 :
     discount = cost_of_pens*20/100
     print("you have to pay",cost_of_pens-discount,"rs") 
else :
     discount = cost_of_pens*10/100
=======
number_of_pen = int(input("Total number of pen:")) 
cost_of_1pen = int(input("Cost of one pen:")) 
cost_of_pens = number_of_pen*cost_of_1pen

if  cost_of_pens>1000 :
     discount = cost_of_pens*20/100
     print("you have to pay",cost_of_pens-discount,"rs") 
else :
     discount = cost_of_pens*10/100
>>>>>>> b4a6aa7 (added programs)
     print("you have to pay",cost_of_pens-discount,"rs")