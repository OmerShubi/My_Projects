Multiple Comparisons: Homework - 2
================


# Question 1

## Part A

We perform
![iterations=5,000](https://latex.codecogs.com/png.latex?iterations%3D5%2C000
"iterations=5,000") simulations, in which each time we randomly pick
![m=5](https://latex.codecogs.com/png.latex?m%3D5 "m=5") values out a
Uniform Distribution (![U\\sim
Uni\[0,1\]](https://latex.codecogs.com/png.latex?U%5Csim%20Uni%5B0%2C1%5D
"U\\sim Uni[0,1]")). In each simulation, out of the picked values we
select the one with the minimum value. The result of these simulations
is stored in
![vecmin\\\_m](https://latex.codecogs.com/png.latex?vecmin%5C_m
"vecmin\\_m").

``` r
iterations <- 5000
```

``` r
m <- 5
mat_5 <- replicate(iterations, runif(m,0, 1))
vecmin_5 <- apply(mat_5, 2, min)
```

and similarly with ![m=20](https://latex.codecogs.com/png.latex?m%3D20
"m=20"):

``` r
m <- 20
mat_20 <- replicate(iterations, runif(m,0, 1))
vecmin_20 <- apply(mat_20, 2, min)
```

and ![m=100](https://latex.codecogs.com/png.latex?m%3D100 "m=100"):

``` r
m <- 100
mat_100 <- replicate(iterations, runif(m,0, 1))
vecmin_100 <- apply(mat_100, 2, min)
```

### 1\.

The proportion of
![U\_{(1)}\<0.05](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%3C0.05
"U_{(1)}\<0.05") when ![m=5](https://latex.codecogs.com/png.latex?m%3D5
"m=5"):

``` r
length(vecmin_5[vecmin_5<0.05])/iterations
```

    ## [1] 0.2256

Similarly to section
![\\aleph](https://latex.codecogs.com/png.latex?%5Caleph "\\aleph") in
H.W. 1 - in which ![p\_{value}\\sim
Uni\[0,1\]](https://latex.codecogs.com/png.latex?p_%7Bvalue%7D%5Csim%20Uni%5B0%2C1%5D
"p_{value}\\sim Uni[0,1]"), and we were requested to retrieve the
minimal ![p\_{value}](https://latex.codecogs.com/png.latex?p_%7Bvalue%7D
"p_{value}").

This is exactly what we are asked to find in this question as well, by
defining ![U\_i={p\_{value}}\_i\\sim
Uni\[0,1\]](https://latex.codecogs.com/png.latex?U_i%3D%7Bp_%7Bvalue%7D%7D_i%5Csim%20Uni%5B0%2C1%5D
"U_i={p_{value}}_i\\sim Uni[0,1]") and ![U\_{(1)} =
min(U\_1,U\_2,\\ldots,U\_m)](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%20%3D%20min%28U_1%2CU_2%2C%5Cldots%2CU_m%29
"U_{(1)} = min(U_1,U_2,\\ldots,U_m)") we are dealing with the same
thing.

### 2\.

Histogram of
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") with ![m=5](https://latex.codecogs.com/png.latex?m%3D5
"m=5"):

``` r
hist(vecmin_5, xlim=c(0,1))
```

![](HW2_files/figure-gfm/unnamed-chunk-6-1.png)<!-- --> Histogram of
![U\_{i}](https://latex.codecogs.com/png.latex?U_%7Bi%7D "U_{i}") with
![m=5](https://latex.codecogs.com/png.latex?m%3D5 "m=5"):

``` r
hist(mat_5, xlim=c(0,1))
```

![](HW2_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

By running the ecdf function we can visual the cdf of both functions
clearly.

``` r
plot(ecdf(vecmin_5),col='red', main='CDF of Uni[0,1] and U(1)', xlim=c(0,1))
lines(ecdf(mat_5),col='green')
legend(0, 1, legend=c(expression(U[(1)]), 'Uni[0,1]'), col=c("red", "green"), lty=1, cex=0.8)
```

![](HW2_files/figure-gfm/unnamed-chunk-8-1.png)<!-- --> As can be seen
from both the histograms and the cdf functions,

it is clear that
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") is stochastically smaller
(![\\prec](https://latex.codecogs.com/png.latex?%5Cprec "\\prec")) than
![Uni\[0,1\]](https://latex.codecogs.com/png.latex?Uni%5B0%2C1%5D
"Uni[0,1]").

### 3\.

Histogram of
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") with ![m=5](https://latex.codecogs.com/png.latex?m%3D5
"m=5"):

``` r
hist(vecmin_5, xlim=c(0,1))
```

![](HW2_files/figure-gfm/unnamed-chunk-9-1.png)<!-- --> Histogram of
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") with ![m=20](https://latex.codecogs.com/png.latex?m%3D20
"m=20"):

``` r
hist(vecmin_20, breaks = 20, xlim=c(0,1))
```

![](HW2_files/figure-gfm/unnamed-chunk-10-1.png)<!-- --> Histogram of
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") with ![m=100](https://latex.codecogs.com/png.latex?m%3D100
"m=100"):

``` r
hist(vecmin_100, xlim=c(0,1))
```

![](HW2_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

``` r
plot(ecdf(vecmin_5),col='red', main='CDF of U(1) with different m values', xlim=c(0,0.65))
lines(ecdf(vecmin_20),col='green')
lines(ecdf(vecmin_100),col='blue')

legend(0.5, 0.5, legend=c(expression(U[(1)],widehat(U[(1)]),widetilde(U[(1)]))), col=c("red", "green", "blue"), lty=1)
```

![](HW2_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") is with ![m=5](https://latex.codecogs.com/png.latex?m%3D5
"m=5"), ![\\widehat
U\_{(1)}](https://latex.codecogs.com/png.latex?%5Cwidehat%20U_%7B%281%29%7D
"\\widehat U_{(1)}") is with
![m=20](https://latex.codecogs.com/png.latex?m%3D20 "m=20") and
![\\widetilde
U\_{(1)}](https://latex.codecogs.com/png.latex?%5Cwidetilde%20U_%7B%281%29%7D
"\\widetilde U_{(1)}") is with
![m=100](https://latex.codecogs.com/png.latex?m%3D100 "m=100").

It can be clearly observed that:

if ![m \> m'](https://latex.codecogs.com/png.latex?m%20%3E%20m%27
"m \> m'") then ![U\_{(1)} \\prec
U\_{(1)}'](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%20%5Cprec%20U_%7B%281%29%7D%27
"U_{(1)} \\prec U_{(1)}'")

if ![m \< m'](https://latex.codecogs.com/png.latex?m%20%3C%20m%27
"m \< m'") then ![U\_{(1)} \\succ
U\_{(1)}'](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%20%5Csucc%20U_%7B%281%29%7D%27
"U_{(1)} \\succ U_{(1)}'")

## Part B.

![F\_{U\_{(1)}}(x) = P(U\_{(1)}\<x) = 1 - P(U\_{(1)}\\geq x) = 1
-P(U\_{1}\\geq x,\\ldots , U\_{m}\\geq
x)](https://latex.codecogs.com/png.latex?F_%7BU_%7B%281%29%7D%7D%28x%29%20%3D%20P%28U_%7B%281%29%7D%3Cx%29%20%3D%201%20-%20P%28U_%7B%281%29%7D%5Cgeq%20x%29%20%3D%201%20-P%28U_%7B1%7D%5Cgeq%20x%2C%5Cldots%20%2C%20U_%7Bm%7D%5Cgeq%20x%29
"F_{U_{(1)}}(x) = P(U_{(1)}\<x) = 1 - P(U_{(1)}\\geq x) = 1 -P(U_{1}\\geq x,\\ldots , U_{m}\\geq x)")

![= 1 - P(U\_{1}\\geq x)\*\\ldots\* P(U\_{m}\\geq x) = 1 -
(1-x)^m](https://latex.codecogs.com/png.latex?%3D%201%20-%20P%28U_%7B1%7D%5Cgeq%20x%29%2A%5Cldots%2A%20P%28U_%7Bm%7D%5Cgeq%20x%29%20%3D%201%20-%20%281-x%29%5Em
"= 1 - P(U_{1}\\geq x)*\\ldots* P(U_{m}\\geq x) = 1 - (1-x)^m"),
![\\forall x : 0\\leq
x\\leq](https://latex.codecogs.com/png.latex?%5Cforall%20x%20%3A%200%5Cleq%20x%5Cleq
"\\forall x : 0\\leq x\\leq"). ![1 : x\\geq 1, 0 :
x\\leq 0](https://latex.codecogs.com/png.latex?1%20%3A%20x%5Cgeq%201%2C%200%20%3A%20x%5Cleq%200
"1 : x\\geq 1, 0 : x\\leq 0")

This comes from independence of
![U\_i](https://latex.codecogs.com/png.latex?U_i "U_i"), definition of
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") and uniform distribution.

Proof of part 2:

![U\_{(1)}\\prec U\_i \\iff P(U\_{(1)}\\leq a) \\geq P(U\_i\\leq
a)](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%5Cprec%20U_i%20%5Ciff%20P%28U_%7B%281%29%7D%5Cleq%20a%29%20%5Cgeq%20P%28U_i%5Cleq%20a%29
"U_{(1)}\\prec U_i \\iff P(U_{(1)}\\leq a) \\geq P(U_i\\leq a)")

![\\iff F\_{U\_{(1)}}(a) \\geq
F\_{U\_{i}}(a)](https://latex.codecogs.com/png.latex?%5Ciff%20F_%7BU_%7B%281%29%7D%7D%28a%29%20%5Cgeq%20F_%7BU_%7Bi%7D%7D%28a%29
"\\iff F_{U_{(1)}}(a) \\geq F_{U_{i}}(a)")

![\\iff 1-(1-F\_{U\_{i}}(a))^{m}\\geq
F\_{U\_{i}}(a)](https://latex.codecogs.com/png.latex?%5Ciff%201-%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%7D%5Cgeq%20F_%7BU_%7Bi%7D%7D%28a%29
"\\iff 1-(1-F_{U_{i}}(a))^{m}\\geq F_{U_{i}}(a)")

![\\iff 1-F\_{U\_{i}}(a)\\geq
(1-F\_{U\_{i}}(a))^{m}](https://latex.codecogs.com/png.latex?%5Ciff%201-F_%7BU_%7Bi%7D%7D%28a%29%5Cgeq%20%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%7D
"\\iff 1-F_{U_{i}}(a)\\geq (1-F_{U_{i}}(a))^{m}")

![\\iff 1\\geq
(1-F\_{U\_{i}}(a))^{m-1}](https://latex.codecogs.com/png.latex?%5Ciff%201%5Cgeq%20%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm-1%7D
"\\iff 1\\geq (1-F_{U_{i}}(a))^{m-1}")

![\\iff 1\\geq 1-F\_{U\_{i}}(a)](https://latex.codecogs.com/png.latex?%5Ciff%201%5Cgeq%201-F_%7BU_%7Bi%7D%7D%28a%29
"\\iff 1\\geq 1-F_{U_{i}}(a)")

![\\iff
F\_{U\_{i}}(a)\\geq 0](https://latex.codecogs.com/png.latex?%5Ciff%20F_%7BU_%7Bi%7D%7D%28a%29%5Cgeq%200
"\\iff F_{U_{i}}(a)\\geq 0")
![\\space\_{\\blacksquare}](https://latex.codecogs.com/png.latex?%5Cspace_%7B%5Cblacksquare%7D
"\\space_{\\blacksquare}")

Proof of part 3:

![U'\_{(1)}\\prec U\_{(1)} \\iff F\_{U'\_{(1)}}(a)\\geq
F\_{U\_{(1)}}(a)](https://latex.codecogs.com/png.latex?U%27_%7B%281%29%7D%5Cprec%20U_%7B%281%29%7D%20%5Ciff%20F_%7BU%27_%7B%281%29%7D%7D%28a%29%5Cgeq%20F_%7BU_%7B%281%29%7D%7D%28a%29
"U'_{(1)}\\prec U_{(1)} \\iff F_{U'_{(1)}}(a)\\geq F_{U_{(1)}}(a)")

![\\iff 1-(1-F\_{U'\_{i}}(a))^{m'}
\\geq 1-(1-F\_{U\_{i}}(a))^{m}](https://latex.codecogs.com/png.latex?%5Ciff%201-%281-F_%7BU%27_%7Bi%7D%7D%28a%29%29%5E%7Bm%27%7D%20%5Cgeq%201-%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%7D
"\\iff 1-(1-F_{U'_{i}}(a))^{m'} \\geq 1-(1-F_{U_{i}}(a))^{m}")

![\\iff (1-F\_{U'\_{i}}(a))^{m'}\\leq
(1-F\_{U\_{i}}(a))^{m}](https://latex.codecogs.com/png.latex?%5Ciff%20%281-F_%7BU%27_%7Bi%7D%7D%28a%29%29%5E%7Bm%27%7D%5Cleq%20%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%7D
"\\iff (1-F_{U'_{i}}(a))^{m'}\\leq (1-F_{U_{i}}(a))^{m}")

![\\iff (1-F\_{U\_{i}}(a))^{m'}\\leq
(1-F\_{U\_{i}}(a))^{m}](https://latex.codecogs.com/png.latex?%5Ciff%20%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%27%7D%5Cleq%20%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%7D
"\\iff (1-F_{U_{i}}(a))^{m'}\\leq (1-F_{U_{i}}(a))^{m}")

![\\iff 1\\geq
(1-F\_{U\_{i}}(a))^{m'-m}](https://latex.codecogs.com/png.latex?%5Ciff%201%5Cgeq%20%281-F_%7BU_%7Bi%7D%7D%28a%29%29%5E%7Bm%27-m%7D
"\\iff 1\\geq (1-F_{U_{i}}(a))^{m'-m}"), ![m'\\geq
m](https://latex.codecogs.com/png.latex?m%27%5Cgeq%20m "m'\\geq m")

![\\Longrightarrow 0\\leq 1-F\_{U\_{i}}(a)\\leq 1](https://latex.codecogs.com/png.latex?%5CLongrightarrow%200%5Cleq%201-F_%7BU_%7Bi%7D%7D%28a%29%5Cleq%201
"\\Longrightarrow 0\\leq 1-F_{U_{i}}(a)\\leq 1")

, which is always true.
![\_{\\blacksquare}](https://latex.codecogs.com/png.latex?_%7B%5Cblacksquare%7D
"_{\\blacksquare}")

## Part C.

![F\_{U\_{(1)}}(x) = 1 - (1-F\_{U\_{i}}(x))^{m} = 1 -
(1-x)^{m}](https://latex.codecogs.com/png.latex?F_%7BU_%7B%281%29%7D%7D%28x%29%20%3D%201%20-%20%281-F_%7BU_%7Bi%7D%7D%28x%29%29%5E%7Bm%7D%20%3D%201%20-%20%281-x%29%5E%7Bm%7D
"F_{U_{(1)}}(x) = 1 - (1-F_{U_{i}}(x))^{m} = 1 - (1-x)^{m}")

Therefore,

![P(U\_{(1)}\\leq g(t,m)) = F\_{U\_{(1)}}(g(t,m)) = 1-(1-g(t,m))^{m} =
t](https://latex.codecogs.com/png.latex?P%28U_%7B%281%29%7D%5Cleq%20g%28t%2Cm%29%29%20%3D%20F_%7BU_%7B%281%29%7D%7D%28g%28t%2Cm%29%29%20%3D%201-%281-g%28t%2Cm%29%29%5E%7Bm%7D%20%3D%20t
"P(U_{(1)}\\leq g(t,m)) = F_{U_{(1)}}(g(t,m)) = 1-(1-g(t,m))^{m} = t")

![\\iff 1-t =
(1-g(t,m))^{m}](https://latex.codecogs.com/png.latex?%5Ciff%201-t%20%3D%20%281-g%28t%2Cm%29%29%5E%7Bm%7D
"\\iff 1-t = (1-g(t,m))^{m}")

![\\iff (1-t)^{1/m} = 1 -
g(t,m)](https://latex.codecogs.com/png.latex?%5Ciff%20%281-t%29%5E%7B1%2Fm%7D%20%3D%201%20-%20g%28t%2Cm%29
"\\iff (1-t)^{1/m} = 1 - g(t,m)")

![\\iff g(t,m)= 1 -
(1-t)^{1/m}](https://latex.codecogs.com/png.latex?%5Ciff%20g%28t%2Cm%29%3D%201%20-%20%281-t%29%5E%7B1%2Fm%7D
"\\iff g(t,m)= 1 - (1-t)^{1/m}")

Therefore, the function is : ![g(t,m)= 1 -
(1-t)^{1/m}](https://latex.codecogs.com/png.latex?g%28t%2Cm%29%3D%201%20-%20%281-t%29%5E%7B1%2Fm%7D
"g(t,m)= 1 - (1-t)^{1/m}").

## Part D.

![P(U\_{(1)}\\leq 1 - (1-t)^{1/m}) =
t](https://latex.codecogs.com/png.latex?P%28U_%7B%281%29%7D%5Cleq%201%20-%20%281-t%29%5E%7B1%2Fm%7D%29%20%3D%20t
"P(U_{(1)}\\leq 1 - (1-t)^{1/m}) = t")

![\\iff P(1-U\_{(1)}\\geq (1-t)^{1/m}) =
t](https://latex.codecogs.com/png.latex?%5Ciff%20P%281-U_%7B%281%29%7D%5Cgeq%20%281-t%29%5E%7B1%2Fm%7D%29%20%3D%20t
"\\iff P(1-U_{(1)}\\geq (1-t)^{1/m}) = t")

![\\iff P((1-U\_{(1)})^{m}\\geq 1 -t) =
t](https://latex.codecogs.com/png.latex?%5Ciff%20P%28%281-U_%7B%281%29%7D%29%5E%7Bm%7D%5Cgeq%201%20-t%29%20%3D%20t
"\\iff P((1-U_{(1)})^{m}\\geq 1 -t) = t")

![\\iff P(1-(1-U\_{(1)})^{m}\\leq t) =
t](https://latex.codecogs.com/png.latex?%5Ciff%20P%281-%281-U_%7B%281%29%7D%29%5E%7Bm%7D%5Cleq%20t%29%20%3D%20t
"\\iff P(1-(1-U_{(1)})^{m}\\leq t) = t")

Therefore the random variable
![Y](https://latex.codecogs.com/png.latex?Y "Y") is given by: ![Y =
h\_m(U\_{(1)})
= 1-(1-U\_{(1)})^{m}](https://latex.codecogs.com/png.latex?Y%20%3D%20h_m%28U_%7B%281%29%7D%29%20%3D%201-%281-U_%7B%281%29%7D%29%5E%7Bm%7D
"Y = h_m(U_{(1)}) = 1-(1-U_{(1)})^{m}")

## Part E.

``` r
Y <- 1-(1-vecmin_100)^100
hist(Y)
```

![](HW2_files/figure-gfm/unnamed-chunk-13-1.png)<!-- --> For
![Y=1-(1-U\_{(1)})^m](https://latex.codecogs.com/png.latex?Y%3D1-%281-U_%7B%281%29%7D%29%5Em
"Y=1-(1-U_{(1)})^m"),

as can be seen, the random variable
![Y](https://latex.codecogs.com/png.latex?Y "Y") that we found , holds
![Y\\sim
Uni\[0,1\]](https://latex.codecogs.com/png.latex?Y%5Csim%20Uni%5B0%2C1%5D
"Y\\sim Uni[0,1]") as expected.

## Part F.

### 1\.

This corresponds exactly to the function we found in part C:

![p\_{value}^{adj}=1-(1-P\_{value})^{\\frac{1}{m}}](https://latex.codecogs.com/png.latex?p_%7Bvalue%7D%5E%7Badj%7D%3D1-%281-P_%7Bvalue%7D%29%5E%7B%5Cfrac%7B1%7D%7Bm%7D%7D
"p_{value}^{adj}=1-(1-P_{value})^{\\frac{1}{m}}")

where ![m](https://latex.codecogs.com/png.latex?m "m") is the total
number of courses (because
![m=m\_0](https://latex.codecogs.com/png.latex?m%3Dm_0 "m=m_0")
according to the question assumptions).

So for
![p\_{value}=0.05](https://latex.codecogs.com/png.latex?p_%7Bvalue%7D%3D0.05
"p_{value}=0.05") we get:

![p\_{value}^{adj}=1-(1-0.05)^{\\frac{1}{m}}
= 1-(0.95)^{\\frac{1}{m}}](https://latex.codecogs.com/png.latex?p_%7Bvalue%7D%5E%7Badj%7D%3D1-%281-0.05%29%5E%7B%5Cfrac%7B1%7D%7Bm%7D%7D%20%3D%201-%280.95%29%5E%7B%5Cfrac%7B1%7D%7Bm%7D%7D
"p_{value}^{adj}=1-(1-0.05)^{\\frac{1}{m}} = 1-(0.95)^{\\frac{1}{m}}")

As we showed and proved in previous sections, this equation provides the
adjusted pvalue, as desired.

For ![m=5](https://latex.codecogs.com/png.latex?m%3D5 "m=5") we get
![p\_{value}^{adj}=1-0.95^\\frac{1}{5}=0.0102](https://latex.codecogs.com/png.latex?p_%7Bvalue%7D%5E%7Badj%7D%3D1-0.95%5E%5Cfrac%7B1%7D%7B5%7D%3D0.0102
"p_{value}^{adj}=1-0.95^\\frac{1}{5}=0.0102"). Therefore the desired
bound should be \~![0.01](https://latex.codecogs.com/png.latex?0.01
"0.01").

# Question 2

## Part 1 - Sidak’s Adjusted p-values

![P\_i
\\leq 1-(1-\\alpha)^{\\frac{1}{m}}=\\alpha\_{sid}](https://latex.codecogs.com/png.latex?P_i%20%5Cleq%201-%281-%5Calpha%29%5E%7B%5Cfrac%7B1%7D%7Bm%7D%7D%3D%5Calpha_%7Bsid%7D
"P_i \\leq 1-(1-\\alpha)^{\\frac{1}{m}}=\\alpha_{sid}") ![\\iff P\_i +
(1-\\alpha)^{\\frac{1}{m}}\\leq 1](https://latex.codecogs.com/png.latex?%5Ciff%20P_i%20%2B%20%281-%5Calpha%29%5E%7B%5Cfrac%7B1%7D%7Bm%7D%7D%5Cleq%201
"\\iff P_i + (1-\\alpha)^{\\frac{1}{m}}\\leq 1") ![\\iff
(1-\\alpha)^{\\frac{1}{m}}\\leq 1-P\_i](https://latex.codecogs.com/png.latex?%5Ciff%20%281-%5Calpha%29%5E%7B%5Cfrac%7B1%7D%7Bm%7D%7D%5Cleq%201-P_i
"\\iff (1-\\alpha)^{\\frac{1}{m}}\\leq 1-P_i")
![\\underbrace{\\iff}\_{\\mbox{both }\\geq0} 1-\\alpha \\leq
(1-P\_i)^m](https://latex.codecogs.com/png.latex?%5Cunderbrace%7B%5Ciff%7D_%7B%5Cmbox%7Bboth%20%7D%5Cgeq0%7D%201-%5Calpha%20%5Cleq%20%281-P_i%29%5Em
"\\underbrace{\\iff}_{\\mbox{both }\\geq0} 1-\\alpha \\leq (1-P_i)^m")
![\\iff \\alpha
\\geq 1-(1-P\_i)^m](https://latex.codecogs.com/png.latex?%5Ciff%20%5Calpha%20%5Cgeq%201-%281-P_i%29%5Em
"\\iff \\alpha \\geq 1-(1-P_i)^m")

Therefore,

![q\_{i\_{sid}}
= 1-(1-P\_i)^m](https://latex.codecogs.com/png.latex?q_%7Bi_%7Bsid%7D%7D%20%3D%201-%281-P_i%29%5Em
"q_{i_{sid}} = 1-(1-P_i)^m")

## Part 2 - Simultaneous CI are FWER controlling Proc.

![P(V\>0) \\underbrace{=}\_{(1)} P(\\exists\\space i: \\mu\_i \\in
M\_0,\\space\\mu\_{i}\\notin I\_{i}'(X)) \\underbrace{\\leq}\_{(2)}
P(\\exists\\space i: \\mu\_i \\in M, \\space\\mu\_{i}\\notin
I\_{i}'(X))\\underbrace{\\leq}\_{(3)}\\alpha](https://latex.codecogs.com/png.latex?P%28V%3E0%29%20%5Cunderbrace%7B%3D%7D_%7B%281%29%7D%20P%28%5Cexists%5Cspace%20i%3A%20%5Cmu_i%20%5Cin%20M_0%2C%5Cspace%5Cmu_%7Bi%7D%5Cnotin%20I_%7Bi%7D%27%28X%29%29%20%5Cunderbrace%7B%5Cleq%7D_%7B%282%29%7D%20P%28%5Cexists%5Cspace%20i%3A%20%5Cmu_i%20%5Cin%20M%2C%20%5Cspace%5Cmu_%7Bi%7D%5Cnotin%20I_%7Bi%7D%27%28X%29%29%5Cunderbrace%7B%5Cleq%7D_%7B%283%29%7D%5Calpha
"P(V\>0) \\underbrace{=}_{(1)} P(\\exists\\space i: \\mu_i \\in M_0,\\space\\mu_{i}\\notin I_{i}'(X)) \\underbrace{\\leq}_{(2)} P(\\exists\\space i: \\mu_i \\in M, \\space\\mu_{i}\\notin I_{i}'(X))\\underbrace{\\leq}_{(3)}\\alpha")

1)  By definition of the test, as we know that rejecting
    ![H\_0](https://latex.codecogs.com/png.latex?H_0 "H_0") by the
    dual-sided test is equivalent to rejecting
    ![H\_0](https://latex.codecogs.com/png.latex?H_0 "H_0") by the eq.
    CI.
2)  ![M\_0 \\subseteq
    M](https://latex.codecogs.com/png.latex?M_0%20%5Csubseteq%20M
    "M_0 \\subseteq M") therefore it holds that ![\\forall x:Pr(x\\in
    M\_0)\\leq Pr(x\\in
    M)](https://latex.codecogs.com/png.latex?%5Cforall%20x%3APr%28x%5Cin%20M_0%29%5Cleq%20Pr%28x%5Cin%20M%29
    "\\forall x:Pr(x\\in M_0)\\leq Pr(x\\in M)").
3)  By definition of simultaneous confidence intervals.

Therefore, the given test is a FWER-controlling procedure at level
![\\alpha](https://latex.codecogs.com/png.latex?%5Calpha "\\alpha").

## Part 3 - Bonferroni CI are Simultaneous CI

As seen in class, bonferroni CI for
![\\mu\_i](https://latex.codecogs.com/png.latex?%5Cmu_i "\\mu_i") at
confidence level
![1-\\alpha](https://latex.codecogs.com/png.latex?1-%5Calpha
"1-\\alpha") if it holds that ![P(\\mu\_i \\in I\_i(X))
= 1-\\frac{\\alpha}{m}](https://latex.codecogs.com/png.latex?P%28%5Cmu_i%20%5Cin%20I_i%28X%29%29%20%3D%201-%5Cfrac%7B%5Calpha%7D%7Bm%7D
"P(\\mu_i \\in I_i(X)) = 1-\\frac{\\alpha}{m}") or alternatively
![(\*)](https://latex.codecogs.com/png.latex?%28%2A%29 "(*)")
![P(\\mu\_i \\notin I\_i(X)) =
\\frac{\\alpha}{m}](https://latex.codecogs.com/png.latex?P%28%5Cmu_i%20%5Cnotin%20I_i%28X%29%29%20%3D%20%5Cfrac%7B%5Calpha%7D%7Bm%7D
"P(\\mu_i \\notin I_i(X)) = \\frac{\\alpha}{m}")

Therefore,

![P(\\exists i: \\mu\_i \\notin I\_i'(X)) = P(\\bigcup\\limits\_{i=1}^m
\\{\\mu\_i \\notin
I\_i'(X)\\})](https://latex.codecogs.com/png.latex?P%28%5Cexists%20i%3A%20%5Cmu_i%20%5Cnotin%20I_i%27%28X%29%29%20%3D%20P%28%5Cbigcup%5Climits_%7Bi%3D1%7D%5Em%20%5C%7B%5Cmu_i%20%5Cnotin%20I_i%27%28X%29%5C%7D%29
"P(\\exists i: \\mu_i \\notin I_i'(X)) = P(\\bigcup\\limits_{i=1}^m \\{\\mu_i \\notin I_i'(X)\\})")
![\\underbrace{\\leq}\_{\\mbox{bonferroni ineq.}} \\sum\\limits\_{i=1}^m
P(\\mu\_i\\notin I\_i'(X)) \\underbrace{=}\_{\\mbox{from }(\*)}
\\sum\\limits\_{i=1}^{m}\\frac{\\alpha}{m} =
\\alpha](https://latex.codecogs.com/png.latex?%5Cunderbrace%7B%5Cleq%7D_%7B%5Cmbox%7Bbonferroni%20ineq.%7D%7D%20%5Csum%5Climits_%7Bi%3D1%7D%5Em%20P%28%5Cmu_i%5Cnotin%20I_i%27%28X%29%29%20%5Cunderbrace%7B%3D%7D_%7B%5Cmbox%7Bfrom%20%7D%28%2A%29%7D%20%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bm%7D%5Cfrac%7B%5Calpha%7D%7Bm%7D%20%3D%20%5Calpha
"\\underbrace{\\leq}_{\\mbox{bonferroni ineq.}} \\sum\\limits_{i=1}^m P(\\mu_i\\notin I_i'(X)) \\underbrace{=}_{\\mbox{from }(*)} \\sum\\limits_{i=1}^{m}\\frac{\\alpha}{m} = \\alpha")

And therefore Bonferroni CI are also Simultaneous CI.

No assumptions are needed for bonferroni.

## Part 4 - Sidak CI

We construct Simultaneous CI that are equivalent to Sidak’s procedure by
constructing Sidak CI that hold:

![P(\\mu\_i \\notin I\_i'(X)) = \\alpha\_{sid}
= 1-(1-\\alpha)^\\frac{1}{m}
\\iff](https://latex.codecogs.com/png.latex?P%28%5Cmu_i%20%5Cnotin%20I_i%27%28X%29%29%20%3D%20%5Calpha_%7Bsid%7D%20%3D%201-%281-%5Calpha%29%5E%5Cfrac%7B1%7D%7Bm%7D%20%5Ciff
"P(\\mu_i \\notin I_i'(X)) = \\alpha_{sid} = 1-(1-\\alpha)^\\frac{1}{m} \\iff")

![P(\\mu\_i \\in I\_i'(X)) = 1- \\alpha\_{sid} = 1-
\[1-(1-\\alpha)^\\frac{1}{m}\] =
(1-\\alpha)^\\frac{1}{m}](https://latex.codecogs.com/png.latex?P%28%5Cmu_i%20%5Cin%20I_i%27%28X%29%29%20%3D%201-%20%5Calpha_%7Bsid%7D%20%3D%201-%20%5B1-%281-%5Calpha%29%5E%5Cfrac%7B1%7D%7Bm%7D%5D%20%3D%20%281-%5Calpha%29%5E%5Cfrac%7B1%7D%7Bm%7D
"P(\\mu_i \\in I_i'(X)) = 1- \\alpha_{sid} = 1- [1-(1-\\alpha)^\\frac{1}{m}] = (1-\\alpha)^\\frac{1}{m}")
![(\*)](https://latex.codecogs.com/png.latex?%28%2A%29 "(*)")

![P(\\forall i: \\mu\_i \\in I\_i'(X))
\\underbrace{=}\_{\\mbox{independent}} \\prod\\limits\_{i=1}^m P(\\mu\_i
\\in
I\_i'(X))](https://latex.codecogs.com/png.latex?P%28%5Cforall%20i%3A%20%5Cmu_i%20%5Cin%20I_i%27%28X%29%29%20%5Cunderbrace%7B%3D%7D_%7B%5Cmbox%7Bindependent%7D%7D%20%5Cprod%5Climits_%7Bi%3D1%7D%5Em%20P%28%5Cmu_i%20%5Cin%20I_i%27%28X%29%29
"P(\\forall i: \\mu_i \\in I_i'(X)) \\underbrace{=}_{\\mbox{independent}} \\prod\\limits_{i=1}^m P(\\mu_i \\in I_i'(X))")

![\\underbrace{=}\_{(\*)}\\prod\\limits\_{i=1}^m\[(1-\\alpha)^\\frac{1}{m}\]
= 1-\\alpha](https://latex.codecogs.com/png.latex?%5Cunderbrace%7B%3D%7D_%7B%28%2A%29%7D%5Cprod%5Climits_%7Bi%3D1%7D%5Em%5B%281-%5Calpha%29%5E%5Cfrac%7B1%7D%7Bm%7D%5D%20%3D%201-%5Calpha
"\\underbrace{=}_{(*)}\\prod\\limits_{i=1}^m[(1-\\alpha)^\\frac{1}{m}] = 1-\\alpha")

![\\iff P(\\exists i: \\mu\_i \\notin I\_i'(X)) =
\\alpha](https://latex.codecogs.com/png.latex?%5Ciff%20P%28%5Cexists%20i%3A%20%5Cmu_i%20%5Cnotin%20I_i%27%28X%29%29%20%3D%20%5Calpha
"\\iff P(\\exists i: \\mu_i \\notin I_i'(X)) = \\alpha")

Therefore Sidak’s CI are also Simultaeous CI and are equivalent to the
procedure.

The assumptions needed are that the test statistics are independent from
each other.
