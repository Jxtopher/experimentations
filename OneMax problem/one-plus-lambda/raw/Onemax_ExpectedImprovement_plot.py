#!/usr/bin/env python
# -*- coding=utf-8 -*-


from Onemax_ExpectedImprovement_data_flipBitc import *
import plot


y = []
l = []
f = []

fit = range(0, 1000)
x = [fit, fit, fit, fit, fit,fit]
y.append([C1_L1_mean, C2_L1_mean, C4_L1_mean, C8_L1_mean, C16_L1_mean, C32_L1_mean])
l.append([r"c=1 $\lambda = 1$", r"c=2 $\lambda = 1$", r"c=4 $\lambda = 1$", r"c=8 $\lambda = 1$",r"c=16 $\lambda = 1$",r"c=32 $\lambda = 1$",])
f.append("Onemax_ExpectedImprovement_lambda1.svg")

y.append([C1_L2_mean, C2_L2_mean, C4_L2_mean, C8_L2_mean, C16_L2_mean, C32_L2_mean])
l.append([r"c=1 $\lambda = 2$", r"c=2 $\lambda = 2$", r"c=4 $\lambda = 2$", r"c=8 $\lambda = 2$",r"c=16 $\lambda = 2$",r"c=32 $\lambda = 2$",])
f.append("Onemax_ExpectedImprovement_lambda2.svg")

y.append([C1_L4_mean, C2_L4_mean, C4_L4_mean, C8_L4_mean, C16_L4_mean, C32_L4_mean])
l.append([r"c=1 $\lambda = 4$", r"c=2 $\lambda = 4$", r"c=4 $\lambda = 4$", r"c=8 $\lambda = 4$",r"c=16 $\lambda = 4$",r"c=32 $\lambda = 4$",])
f.append("Onemax_ExpectedImprovement_lambda4.svg")

y.append([C1_L8_mean, C2_L8_mean, C4_L8_mean, C8_L8_mean, C16_L8_mean, C32_L8_mean])
l.append([r"c=1 $\lambda = 8$", r"c=2 $\lambda = 8$", r"c=4 $\lambda = 8$", r"c=8 $\lambda = 8$",r"c=16 $\lambda = 8$",r"c=32 $\lambda = 8$",])
f.append("Onemax_ExpectedImprovement_lambda8.svg")

y.append([C1_L16_mean, C2_L16_mean, C4_L16_mean, C8_L16_mean, C16_L16_mean, C32_L16_mean])
l.append([r"c=1 $\lambda = 16$", r"c=2 $\lambda = 16$", r"c=4 $\lambda = 16$", r"c=8 $\lambda = 16$",r"c=16 $\lambda = 16$",r"c=32 $\lambda = 16$",])
f.append("Onemax_ExpectedImprovement_lambda16.svg")

y.append([C1_L32_mean, C2_L32_mean, C4_L32_mean, C8_L32_mean, C16_L32_mean, C32_L32_mean])
l.append([r"c=1 $\lambda = 32$", r"c=2 $\lambda = 32$", r"c=4 $\lambda = 32$", r"c=8 $\lambda = 32$",r"c=16 $\lambda = 32$",r"c=32 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_lambda32.svg")

y.append([C1_L1_mean, C1_L2_mean, C1_L4_mean, C1_L8_mean, C1_L16_mean, C1_L32_mean])
l.append([r"c=1 $\lambda = 1$", r"c=1 $\lambda = 2$", r"c=1 $\lambda = 4$", r"c=1 $\lambda = 8$",r"c=1 $\lambda = 16$",r"c=1 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_flipBitc1.svg")

y.append([C2_L1_mean, C2_L2_mean, C2_L4_mean, C2_L8_mean, C2_L16_mean, C2_L32_mean])
l.append([r"c=2 $\lambda = 1$", r"c=2 $\lambda = 2$", r"c=2 $\lambda = 4$", r"c=2 $\lambda = 8$",r"c=2 $\lambda = 16$",r"c=2 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_flipBitc2.svg")

y.append([C4_L1_mean, C4_L2_mean, C4_L4_mean, C4_L8_mean, C4_L16_mean, C4_L32_mean])
l.append([r"c=4 $\lambda = 1$", r"c=4 $\lambda = 2$", r"c=4 $\lambda = 4$", r"c=4 $\lambda = 8$",r"c=4 $\lambda = 16$",r"c=4 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_flipBitc4.svg")

y.append([C8_L1_mean, C8_L2_mean, C8_L4_mean, C8_L8_mean, C8_L16_mean, C8_L32_mean])
l.append([r"c=8 $\lambda = 1$", r"c=8 $\lambda = 2$", r"c=8 $\lambda = 4$", r"c=8 $\lambda = 8$",r"c=8 $\lambda = 16$",r"c=8 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_flipBitc8.svg")

y.append([C16_L1_mean, C16_L2_mean, C16_L4_mean, C16_L8_mean, C16_L16_mean, C16_L32_mean])
l.append([r"c=16 $\lambda = 1$", r"c=16 $\lambda = 2$", r"c=16 $\lambda = 4$", r"c=16 $\lambda = 8$",r"c=16 $\lambda = 16$",r"c=16 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_flipBitc16.svg")

y.append([C32_L1_mean, C32_L2_mean, C32_L4_mean, C32_L8_mean, C32_L16_mean, C32_L32_mean])
l.append([r"c=32 $\lambda = 1$", r"c=32 $\lambda = 2$", r"c=32 $\lambda = 4$", r"c=32 $\lambda = 8$",r"c=32 $\lambda = 16$",r"c=32 $\lambda = 32$",])
f.append("Onemax_ExpectedImprovement_flipBitc32.svg")

for i in range(0, len(y)):
    p = plot.Linesplot()
    p.legend(xlabel="Fitness", ylabel="Expected Improvement")
    p.auto(x, y[i] , label=l[i], outfile = f[i], line = False, size=5)




