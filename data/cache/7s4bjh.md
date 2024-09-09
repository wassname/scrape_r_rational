## I want to test the hypothesis that "Proprietary software is often malware"

### Post:

[removed]

### Comments:

- u/IX-103:
  ```
  Based on the steps from a recent statistics lecture I attended:

  1. What are you deciding? 

      Proprietary software is more frequently malware than free software (so do not use proprietary software?)

  2. Operationalize. Define everything rigorously:

      What is free software?

      What is proprietary software?

      What is malware, and how do you determine if a piece of software is malware?

  3. What is the population of interest?

      Are we looking at all software ever? How are we counting different revisions of the same software? Note that it is important to define the population of interest in a way that we can actually get sufficiently unbiased samples. 

  4. Plan data collection.

      How are going to collect the data? Does this method produce a random, unbiased, subset of the population? You may need to go back to step 3. Note that almost any way I can think of to collect data on free and proprietary software skews heavily to sample more popular software.

  5. Explicitly state your assumptions. You made a lot of assumptions to simplify analysis in the previous steps. Go through and determine exactly what assumptions you made.

      "I assumed results from a Google search are linearly decreasing in popularity"

  6. State your hypothesis clearly:

      Default H0: there is no difference in the rate of malware in free and proprietary software.

      H1: proprietary software is more likely to contain malware.

  7. How will we analyze the data.

      We can probably model whether a given piece of software is malware using a Bernoulli distribution. Under H0 the parameters of the distribution of free and proprietary software are equal, under H1 the parameters are larger for proprietary software. We can perform a binomial test to determine how probable it is that the parameters are equal.

  8. Pick a significance level and determine how many samples you need. You can use 95% significance if you want, and a binomial test may fit your needs. How many samples do you need to tell if they different - it may be useful to perform a pilot study to estimate the distribution of malware so that you can get a good power analysis.

  9. Collect the data. If you cannot collect the data as intended, change your assumptions and set up until you can.

  10. Analyze the data and make a decision. Note that the two conclusions you can come up with are:

   A. With 95% confidence proprietary software is more likely to contain malware.

   B. Proprietary software does not contain statistically more malware than free software.

  *Edit: fix formatting.
  ```

  - u/IX-103:
    ```
    Ack. Where did my whitespace go?
    ```

    - u/xavion:
      ```
      Reddit formatting, put a blank line in between each new line or put two spaces at the end of the line. Otherwise it'll trim it so they merge.
      ```

      - u/IX-103:
        ```
        Thanks. Reddit appears to use a variant of Markdown.
        ```

        - u/xavion:
          ```
          Yeah, it's pretty close but it diverges a few times in sometimes annoying ways from normal Markdown. Markdown based formatting might be a better description.
          ```

- u/eternal-potato:
  ```
  The gnu page you link to has both the definition of malware and lots of examples by category with links to relevant articles. What else do you need?
  ```

- u/ajuc:
  ```
  > every new program that doesn't have a source code is like Harry Potter discovering that there is magic, and none of it is documented and you have to discover it all using science

  That's a bad analogy. Proprietary applications are often better documented than open source software. The differentiating factor is trust (is it doing exactly what it says), not access to information.
  ```

---

