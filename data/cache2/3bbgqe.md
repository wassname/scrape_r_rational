## [Q] Likelihood ratio for 3,4,5,n hypotheses. Help

* Author: u/Muyyd *
* URL: https://www.reddit.com/r/rational/comments/3bbgqe/q_likelihood_ratio_for_345n_hypotheses_help/
* Score: 0

* Created: 2015-06-27T16:56:53

### Post:


Suppose a person get knocked by a car. Car leaves. Five witnesses report that a car was: white, black, pink, red, yellow. Forensics found on a knocked persons clothes pink paint (pp).

We have now: 

P(w), P(b), P(p), P(r), P(y) - priors

P(pp|w), P(pp|b), P(pp|p), P(pp|r), P(pp|b) - likelihoods.

Now, if i have onle two priors (P(w) and P(p)), i will calculate likelihood ratios P(pp|w)/P(pp|p). But how can i calculate likelihood ratios for five hypotheses?

### Comments:

> **u/SpeakKindly** [+3]  (3 days later)
> 
> You can have ratios of more than two things: for example, 2, 4, and 6 are in a 1:2:3 ratio.
> 
> You probably want to know the ratio P(w|pp) : P(b|pp) : P(p|pp) : P(r|pp) : P(y|pp), which is the likelihood ratio of the car being white to the car being black to the car being pink to the car being red to the car being yellow, given the forensics result.
> 
> Since P(w|pp) = P(pp|w) P(w) / P(pp) by Bayes's law, this ratio is the prior ratio, P(w):P(b):P(p):P(r):P(y), multiplied by P(pp|w):P(pp|b):P(pp|p):P(pp|r):P(pp|y).
> 
> Let's say that all witnesses are equally credible, and all colors equally likely, except black cars occur twice as often. Then the prior ratio is 1:2:1:1:1. Next, let's say all cars are equally likely to leave pink paint, except pink cars do it with five times the probability. Then we multiply by 1:1:5:1:1, to get 1:2:5:1:1. This means if the hypotheses are exhaustive, the probability that the car is pink is 5/(1+2+5+1+1) = 1/2.

>> **u/Muyyd** [+2]  (3 days later)
>> 
>> Thats awesome. Thanks)

> **u/DataPacRat** [+1]  *Amateur Immortalist* (28 minutes later)
> 
> That depends on the nature of the hypotheses. Does each hypothesis mean that none of the hypotheses are true? Or is the truth of the third hypothesis a separate question from the truth of the fifth?

>> **u/Muyyd** [+0]  (9 hours later)
>> 
>> Suppose a person get knocked by a car. Car leaves. Five witnesses report that a car was: white, black, pink, red, yellow. Forensics found on a knocked persons clothes pink paint (pp).
>> 
>> We have now: 
>> 
>> P(w), P(b), P(p), P(r), P(y) - priors
>> 
>> P(pp|w), P(pp|b), P(pp|p), P(pp|r), P(pp|b) - likelihoods.
>> 
>> Now, if i have onle two priors (P(w) and P(p)), i will calculate likelihood ratios P(pp|w)/P(pp|p). But how can i calculate likelihood ratios for five hypotheses?

>>> **u/DataPacRat** [+2]  *Amateur Immortalist* (11 hours later)
>>> 
>>> Hm... Does the term 'probability mass' mean anything to you?

>>>> **u/Muyyd** [+1]  (11 hours later)
>>>> 
>>>> No. But if it would, i'd be able to solve my questions?

>>>>> **u/DataPacRat** [+1]  *Amateur Immortalist* (20 hours later)
>>>>> 
>>>>> Possibly; it might provide at least a framework.
>>>>> 
>>>>> For any given question, such as P(pp), the sum of all the hypotheses (such as P(pp|w), P(pp|b), P(pp|p), etc) adds up to 1; that's the total 'probability mass'. That mass gets divvied out amongst the possibilities. When there's just two hypotheses, then it's easy, since all the probability mass that's not in one hypothesis is in the other. With more than two, it's a little harder, since the total probability if P(w) is false is P(b) + P(p) + etc.
>>>>> 
>>>>> If you gain a piece of evidence which increases P(p), then, by necessity, that probability mass has to be taken from all the other hypotheses. Depending on a few details, then it can be feasible to run a straight Bayesian update on P(p), and then "renormalize" all the other hypotheses to shrink them to fit in the remaining amount of probability mass.
>>>>> 
>>>>> Does that sound like it makes sense?

>>>>>> **u/Muyyd** [+1]  (23 hours later)
>>>>>> 
>>>>>> A bit. But it not how bayesian probability works (to my knowledge). Or (more probably) i need go deeper in respective math (and i know direction: probability mass). But thanks for answering though.

> **u/Calamitizer** [+1]  *Shears* (38 minutes later)
> 
> If you're assuming that exactly one of your hypotheses is true (not none of them in favor of something you failed to hypothesize, and not a conjuction of multiple), i.e. H1 v H2 v ... v Hn is true and the hypotheses are disjoint,  then ~H1 = H2 v ... v Hn.

>> **u/Muyyd** [+0]  (9 hours later)
>> 
>> Suppose a person get knocked by a car. Car leaves. Five witnesses report that a car was: white, black, pink, red, yellow. Forensics found on a knocked persons clothes pink paint (pp).
>> 
>> We have now: 
>> 
>> P(w), P(b), P(p), P(r), P(y) - priors
>> 
>> P(pp|w), P(pp|b), P(pp|p), P(pp|r), P(pp|b) - likelihoods.
>> 
>> Now, if i have onle two priors (P(w) and P(p)), i will calculate likelihood ratios P(pp|w)/P(pp|p). But how can i calculate likelihood ratios for five hypotheses?

---

