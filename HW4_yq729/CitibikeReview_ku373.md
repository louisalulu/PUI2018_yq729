### Review

Yusu's assignment2 codes are structured very well in a concise mannar.
I can not find H0 and H1. In my understanding, Yusu is trying to examine whether there are differences in tripduration among gender(0=unknown,1=male,2=female). Showing mean values, the bar chart clearly describes the differences, and thus we can expect that the differences can be significant. The sample size looks large enough to test that. 
Initially, I was thinking to suggest to drop 0=unknown gender data because it can be not a LGBT data but a mixed gender data of LGBT data and error data. However, Yusu describes that 0=unknown gender data shows 3times+ higher means of trip duration than others, and it has a large sample size (2996). Therefore, it is meaningful to include the 0=unknow gender data.
Hereby, I can certify that Yusu's dataset is well-prepared to test the differences above statistically.

### My suggestions
- It would be great if the file told us what the null nypothesis and the alternative hypothesis are.
- It would be helpful if the gender information, i.e. 0=unknown,1=male,2=female, was mentioned in the graphs.

### Appropriate test
You can think of using Kruskal-Wallis test. 
- Non-parametric (As you show that there are huge differences in standard deviation among genders, it is safe to use non-parametric test). In order to avoid the multiple testing problem, use non-parametric test here.
- More than two independent variables which are categorical
- One dependent variable 
- Independence of observations

