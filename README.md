# PySimpleNS
 A simple Natural Selection model in Python. 
 Based on: Orr, 2009. Fitness and its role in evolutionary genetics.  Nature Reviews (Genetics) vol. 10, p. 531-539.
 
 Description
 Two alleles 'p' and 'q' compete with relative fitness 'w' (= 'W(q)'/'W(p)') and selection coeficient 's'.
 
 How to:
	1 - First choose the value for 'w' (ex: 0.1, 0.5, 0.92).
		The relative fitness 'w' representes the absolute fitness of the allele 'q' divided by the absolute fitness of allele 'p'.
		Type a number between 0 and 1 and press enter.
	
	2 - Then, choose the initial frequency of the less fit allele ('q0') in the population.
		The proportion of individuals in the population that carry the allele q.
		Type a number between 0 and 1 and press enter.
		
	3 - Finally, choose the number of generations (ex: 5, 22, 90).
		Type an integer greater than 0 and press enter.
	
	4 - Choose a folder for saving the results.
		The results can be found within 'results.csv' file in the selected folder.
		
	
