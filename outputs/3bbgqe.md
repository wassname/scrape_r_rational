## [Q] Likelihood ratio for 3,4,5,n hypotheses. Help

### Post:


Suppose a person get knocked by a car. Car leaves. Five witnesses report that a car was: white, black, pink, red, yellow. Forensics found on a knocked persons clothes pink paint (pp).

We have now: 

P(w), P(b), P(p), P(r), P(y) - priors

P(pp|w), P(pp|b), P(pp|p), P(pp|r), P(pp|b) - likelihoods.

Now, if i have onle two priors (P(w) and P(p)), i will calculate likelihood ratios P(pp|w)/P(pp|p). But how can i calculate likelihood ratios for five hypotheses?

### Comments:

- u/SpeakKindly:
  ```
  You can have ratios of more than two things: for example, 2, 4, and 6 are in a 1:2:3 ratio.

  You probably want to know the ratio P(w|pp) : P(b|pp) : P(p|pp) : P(r|pp) : P(y|pp), which is the likelihood ratio of the car being white to the car being black to the car being pink to the car being red to the car being yellow, given the forensics result.

  Since P(w|pp) = P(pp|w) P(w) / P(pp) by Bayes's law, this ratio is the prior ratio, P(w):P(b):P(p):P(r):P(y), multiplied by P(pp|w):P(pp|b):P(pp|p):P(pp|r):P(pp|y).

  Let's say that all witnesses are equally credible, and all colors equally likely, except black cars occur twice as often. Then the prior ratio is 1:2:1:1:1. Next, let's say all cars are equally likely to leave pink paint, except pink cars do it with five times the probability. Then we multiply by 1:1:5:1:1, to get 1:2:5:1:1. This means if the hypotheses are exhaustive, the probability that the car is pink is 5/(1+2+5+1+1) = 1/2.
  ```

  - u/Muyyd:
    ```
    Thats awesome. Thanks)
    ```

---

