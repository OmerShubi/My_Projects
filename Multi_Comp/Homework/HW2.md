Multiple Comparisons: Homework - 2
================

# Submitted by:

Eyal Bar-Natan - 207630658

Omer Shubi - 312236219

# Question 1

## Part A

### 1\.

``` r
iterations <- 5000
m <- 5
mat <- replicate(iterations, runif(m,0, 1))
vecmin <- apply(mat, 2, min)
hist(vecmin)
```

![](HW2_files/figure-gfm/unnamed-chunk-1-1.png)<!-- -->

``` r
length(vecmin[vecmin<0.05])/iterations
```

    ## [1] 0.2272

Exactly like taking the minimum p\_value, becuase
p-value![\\sim](https://latex.codecogs.com/png.latex?%5Csim "\\sim")
Uni\[0,1\] in ![\\aleph](https://latex.codecogs.com/png.latex?%5Caleph
"\\aleph")

### 2\.

By running the ecdf function we can visual the cdf of both functions
clearly.

``` r
plot(ecdf(vecmin),col='red', main='CDF of U(1)')
lines(ecdf(mat[1,]),col='green')
legend(0, 1, legend=c('pvals1 (mu=0)', 'pvals3 (mu=0.5)'), col=c("red", "green"), lty=1, cex=0.8)
```

![](HW2_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

``` r
# TODO update legend
# TODO update vecmin names
```

It is clear that
![U\_{(1)}](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D
"U_{(1)}") is stochastically smaller
(![\\prec](https://latex.codecogs.com/png.latex?%5Cprec "\\prec")) than
![Uni\[0,1\]](https://latex.codecogs.com/png.latex?Uni%5B0%2C1%5D
"Uni[0,1]")

### 3\.

``` r
iterations <- 5000
m <- 20
mat <- replicate(iterations, runif(m,0, 1))
vecmin <- apply(mat, 2, min)
hist(vecmin)
```

![](HW2_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

``` r
iterations <- 5000
m <- 100
mat <- replicate(iterations, runif(m,0, 1))
vecmin <- apply(mat, 2, min)
hist(vecmin)
```

![](HW2_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

``` r
iterations <- 5000
m <- 2
mat <- replicate(iterations, runif(m,0, 1))
vecmin <- apply(mat, 2, min)
hist(vecmin)
```

![](HW2_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
iterations <- 5000
m <- 1
vecmin <- replicate(iterations, runif(m,0, 1))
hist(vecmin)
```

![](HW2_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

if ![m \> m'](https://latex.codecogs.com/png.latex?m%20%3E%20m%27
"m \> m'") then ![U\_{(1)} \\prec
U\_{(1)}'](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%20%5Cprec%20U_%7B%281%29%7D%27
"U_{(1)} \\prec U_{(1)}'")

if ![m \< m'](https://latex.codecogs.com/png.latex?m%20%3C%20m%27
"m \< m'") then ![U\_{(1)} \\succ
U\_{(1)}'](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%20%5Csucc%20U_%7B%281%29%7D%27
"U_{(1)} \\succ U_{(1)}'")

## Part B.

``` r
# TODO add proof from Eyal of 2 & 3
```

$U\_{(1)}U\_i P(U\_{(1)}a) P(U\_ia) $

``` r
plot(ecdf(vecmin),col='red', main='CDF of U(1)')
lines(ecdf(mat[1,]),col='green')
legend(0, 1, legend=c('pvals1 (mu=0)', 'pvals3 (mu=0.5)'), col=c("red", "green"), lty=1, cex=0.8)
```

![](HW2_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

``` r
# TODO update legend
# TODO update vecmin names
```

![U\_{(1)} \\sim
Beta(1,m)](https://latex.codecogs.com/png.latex?U_%7B%281%29%7D%20%5Csim%20Beta%281%2Cm%29
"U_{(1)} \\sim Beta(1,m)") therefore has the same cdf of Beta(1,m).

## Part C.

``` r
iterations <- 5000
m <- 100
mat <- replicate(iterations, runif(m,0, 1))
vecmin <- apply(mat, 2, min)
hist(vecmin)
```

![](HW2_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

``` r
hist(punif(vecmin))
```

![](HW2_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->
