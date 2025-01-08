from scipy.stats import poisson

lambda_1_min = 9

x = poisson.pmf(0, lambda_1_min)
y=poisson.pmf(1, lambda_1_min)
z=poisson.cdf(15, lambda_1_min)
print(z,1-z)
