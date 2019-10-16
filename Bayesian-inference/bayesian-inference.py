#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: *
# @Date: 2019-10-16
# @Purpose: https://fr.wikipedia.org/wiki/Inférence_bayésienne
#			https://www.youtube.com/watch?v=x-2uVNze56s
#
#	À partir de lancée de dès non pipé à l'aveugle (le dès utiliser ne change pas 
#	au cours de l'expérience), déterminer le dès utiliser à l'aide de inférence 
# 	bayésienne : p(A|B) = (p(B|A) * p(A)) / p(B)
#	A correspond hypothèse d'un dès particulier utiliser 
#	B correspond le tirage d'un nombre
# 

import numpy as np
import plot

y = [[]]* len([2, 3, 5, 7, 10, 14, 16, 18, 24, 26, 28, 30, 32, 34, 36, 50, 60, 100])

def bayesian_inference(dices : list, id_dice : int, iteration_max : int = 50):
	# varibales
	prob_final = [0] * len(dices)			# p(A|B)
	a_priori = [1/len(dices)] * len(dices)	# p(B|A)
	estimation = [0] * len(dices)			# p(A)
	surface = 0								# p(B)

	
	# Probibilite  de l'hypthèse
	for iteration in range(0, iteration_max):

		tirage = np.random.randint(0, dices[id_dice]) #
		
		# print(str(iteration) + "=> " + str(tirage) + "\t", end = '')
		for i in range(0, len(estimation)):
			if dices[i] < tirage  :
				estimation[i] = 0
			else : 
				estimation[i] = 1 / dices[i]

		# Surface
		surface = 0.0
		for i in range(0, len(estimation)):
			surface = surface + a_priori[i] * estimation[i]

		# prob final // normalisation
		for i in range(0, len(estimation)):
			prob_final[i] = (a_priori[i] * estimation[i]) / surface


		# for i in range(0, len(prob_final)):
		# 	print(str(round(prob_final[i],2)) + " ", end = '')
		# print("")

		# update
		for i in range(0, len(estimation)):
			a_priori[i] = prob_final[i]

		# for i in range(0, len(estimation)):
		# 	y[i] = y[i] + [prob_final[i]]
		
		
		for i in range(0, len(prob_final)):
			if 1 - round(prob_final[i],2) <= 0:
				return iteration

	
	# return prob_final.index(max(prob_final)) 
	return -1


if __name__ == '__main__':
	# dices = [4, 6, 8, 12, 20]
	dices = [2, 3, 5, 7, 10, 14, 16, 18, 24, 26, 28, 30, 32, 34, 36, 50, 60, 100]
	nbexp = 1000

	exp = [[]] * len(dices)
	for  i in range(0, len(dices)):
		for e in range(0, nbexp):
			exp[i] = exp[i] + [bayesian_inference(dices, i, iteration_max = 2000)]

	
	exp_mean = [0] * len(dices)
	confidenceInterval = [0] * len(dices)
	for  i in range(0, len(dices)):
		exp_mean[i] = np.mean(exp[i])

		# https://fr.wikipedia.org/wiki/Intervalle_de_confiance#cite_note-8
		confidenceInterval[i] = 1.96 * (np.std(exp[i], axis = 0) / np.sqrt(nbexp)) 

	
	p = plot.Linesplot()
	p.add_curve(dices, exp_mean, confidenceInterval, label = "x", line = True, marker = True, size = 1)
	p.legend(xlabel = "Dices", ylabel = "Number of rounds", legend = None)
	p.tofile(outfile="convergence-time.pdf")
	p.tofile(outfile="convergence-time.svg")

	

	# p = plot.Linesplot()
	# for i in range(0, len(y)):
	# 	p.add_curve(range(0, len(y[i])), y[i], None, label = str(dices[i]), line = True, marker = True, size = 1)
	# p.legend(xlabel = "Rounds", ylabel = "P", legend = "outside")
	# p.tofile(outfile="dynamic-dice28.pdf")
	# p.tofile(outfile="dynamic-dice28.svg")

