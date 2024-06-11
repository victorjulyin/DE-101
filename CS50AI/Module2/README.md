
# Uncertainty

## Definitions

    When we talk about some uncertainty, we can imagine that there are several possible worlds, like parallel worlds or realities that can happen. For example, when we throw a dice, there are 6 options - 1, 2, 3, 4, 5 or 6. And these are different possible "worlds".
    - ω - symbol to define this "possible world"
    - P(ω) - probability of this "possible world". Additional things about probability:
        * Probability is always from 0 to 1 (0 <= P(ω) <= 1)
        * The sum of probabilities of all possible worlds equals 1:
$$
\sum_{\omega \in \Omega} P(\omega) = 1
$$
    
    - Unconditional probability - degree of belief in a proposition in the absence of any other evidence
    - Conditional probability - degree of belief in a proposition given some evidence that has already been revealed. It looks like this:
        - P(a | b). Where "a" is a statement that we want to know the probability of and "b" is the evidence that we know for certain that is true. Examples:
            - P(raining today | rained yesterday) - we want to know the probability of raining today, and we know for sure that yesterday it was raining.
            - P(disease | test results) - we have evidences - results of the blood test and we want to know the probability of a certain disease for a patient
            - And in a mathematical way it looks like this (probability of a AND b are true / probability of b is true):
$$
P(a|b) = \frac{P(a \land b)}{P(b)}
$$

        - It is also possible to represent it like this (math rules):
            - P(a Ʌ b) = P(b) * P(a|b)
            - P(a Ʌ b) = P(a) * P(b|a)
    - Random variable - a variable in probability theory with a domain of possible values it can take on. For example:
        - dice_roll = {1,2,3,4,5,6}
        - weather = {sun, rain, snow, wind, clouds}
        - flight = {on_time, delayed, cancelled}
    - Probability distribution. Probabilities for every value in a domain. For example, for "flight" random variable:
        - P(flight = on_time) = 0.6
        - P(flight = delayed) = 0.3
        - P(flight = cancelled) = 0.1
        - Also possible to represent it as vector. We only need to know the order of values:
            - P(flight) = <0.6, 0.3, 0.1>

    - Independence - the knowledge that one event occured does not affect the probability of the other event. So when the events are independent, we can simplify the formula above:
        - P(a Ʌ b) = P(b) * P(a). Because if they are independent it doesn't matter which value is "b" event here P(a|b), so we can just omit it
        - And if the events are not independent, we still need to use the original formula

## Baye's rule

We can get it with some mathematical convertations:
P(a Ʌ b) = P(b) * P(a|b)
P(a Ʌ b) = P(a) * P(b|a)

Knowing this we can convert it to this:
P(b) * P(a|b) = P(a) * P(b|a)

And then to this:

$$
P(b|a) = \frac{P(b) \, P(a|b)}{P(a)}
$$

So it means that we can find the probability of "b" with given "a" if we know the P(a|b)

So knowing:
    - P(cloudy morning | rainy afternoon)
We can calculate:
    - P(rainy afternoon | cloudy morning)

Here is an example of how it works:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability1.jpg" width=70% height=70%></p>

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability2.jpg" width=70% height=70%></p>

## Joint probability

For example, we have some pieces of information about probability of some events.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability3.jpg" width=70% height=70%></p>

But while this info is not connected we can't make any conclusions from it. And that's when we need Joint probability. It is a probability distribution of all possible combinations of values that can take on.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability4.jpg" width=70% height=70%></p>

For example, we need to know:
    P(cloud | rain)

We can use this formula:

$$
P(a|b) = \frac{P(a \land b)}{P(b)}
$$

So we have this:
$$
P(cloud | rain) = \frac{P(cloud, rain)}{P(rain)}
$$

Interesting thing here that sometimes we don't even need this P(rain). Because it is a constant (number), we can represent it as multiplication (reverse value of P(rain)):
P(cloud | rain) = α * P(cloud, rain)

So we get this vector as a probability distribution:
P(cloud | rain) = α * <0.08, 0.02>

And as we know, the sum in the probability distribution must be equal 1. And now we need α.
α - is some constant that normalizes the values in the vector, so their sum == 1.
In this case α = 10. Then:

P(cloud | rain) = <0.8, 0.2>

## Probability rules (for Joint probability)
    - Negation:
        - P(¬a) = 1 - P(a)

    - Inclusion-Exclusion:
        - P(a V b) = P(a) + P(b) - P(a Ʌ b)

    - Marginalization:
        - P(a) = P(a, b) + P(a, ¬b)
        - And sometimes a and b are not just some events but those are probability distributions. And in this case we need to sum up these distributions:
$$
P(X = x_i) = \sum_j P(X = x_i, Y = y_j)
$$


    - Conditioning:
        - P(a) = P(a | b)*P(b) + P(a | ¬b)*P(¬b)
        - And there is also the thing with the sum:
$$
P(X = x_i) = \sum_j P(X = x_i \mid Y = y_j) P(Y = y_j)
$$

## Bayesian networks
It is a data structure that represents the dependencies among random variables.

    - directed graph
    - each node represents a random variable (weather etc.)
    - arrow from X to Y means X is a parent of Y
    - each node X has probability distribution P(X | Parents(X))

For example, we have an appointment somewhere outside of the city. We're going to get there by train. And we try to find the probability if we'll gonna miss the appointment or not. So we have this graph:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability5.jpg" width=70% height=70%></p>

So the probabilities for the rain are gonna be like this (for example):

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability6.jpg" width=70% height=70%></p>

And the probabilities for the Maintenance on the railroad are gonna be conditional probabilities:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability7.jpg" width=70% height=70%></p>

So if the train gonna be on time or will be delayed depends on "rain" and "maintenance":

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability8.jpg" width=70% height=70%></p>

And the probability of the appointment now depends only on the train (directly):

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/probability9.jpg" width=70% height=70%></p>

---------------------------------------

Ok, so now we can get the probabilities of different events. For instance:
    1) We want to get the P(light) (probability of light rain).
        - as rain is the root node, we can just get this information from the table we have
    
    2) We want: P(light, no) (probability of light rain AND no maintenance)
        - In this case we need to get this:
            P(light) * P(no | light) (probability of light rain * probability of no maintenance with given light rain)

    3) We want: P(light, no, delayed)
        - We need to get:
            P(light) * P(no | light) * P(delayed | P(no, light))

    4) We want: P(light, no, delayed, miss)
        - We need to get:
            P(light) * P(no | light) * P(delayed | P(no, light)) * P(miss | delayed)


## Inference

What we have:
    - Query X: variable for which to compute distribution (for example, we want to know if the train is delayed)
    - Evidence variables E: observed variables for event e (for example, we know that there is a light rain)
    - Hidden variables Y: non-evidence, non-query variable. (for example, we don't know if there is maintenance of the railroad)

The goal is:
    - Calculate P(X | e)


--------------------------------------------

Example:
We want to know:
P(Appointment | light, no)

So what we have here:
    - Appointment is our goal that we need to calculate (X)
    - P(light, no) is our given information, event (e)

And we can say that:
P(Appointment | light, no) =  P(Appointment, light, no) / P(light, no) = α * P(Appointment, light, no)

And on this stage we can use that Marginalization trick.
As the only hidden variable is "Train" and we need all 4 variables to know the probability of "Appointment":

α * P(Appointment, light, no) = α * [P(Appointment, light, no, on time) + P(Appointment, light, no, delayed)]

## Approximate Inference

If we have a big Baesian Network, it will take a lot of time to calculate all the possible nodes. In this case we can use some of the optimization strategies.

### Sampling
For example, we have the Network as before.
1) For example, we're creating a loop for 10k iterations.
2) We're taking a one sample value from every level step by step.
3) Adding them to a dictionary for example. So for every iteration we have a dictionary with samples of every level.

#### Rejection sampling
We have a dictionary with samples on every iteration.
So we can count the values we're interested in by rejection the nodes we are not interested in. For example, we want to consider only those nodes where the train is delayed:
    ```
        res = [doc['appointment'] for doc in docs if doc['train'] == 'delayed']
    ```
That's how we can get all the values of the "appointment" level. And if we count it, we'll get an approximate probability of the event.

#### Likelihood Weighting
Sometimes the Rejection sampling may be not efficient. For example, when we have an event that occures very rarely, maybe 1 out of 1000 cases. And in this case if we make 10k iterations, we'll get only 10 events, but we've made a lot of computations.

That's when we can use Likelihood Weighting. That's how it works:
    - Start by fixing the values for evidence variables and not sampling those.
    - Sample the non-evidence variable using conditional probabilities in the Beyesian Network.
    - Weight each sample by its likelihood: the probability of all of the evidence.

For example:
    - We want to know:
        P(rain=light | train=on_time)
    What we do:
        - We're fixing that the train is on time. So we won't change this level later, it is always gonna be "on_time".
        - Taking all the other samples randomly just as before.
        - Adding the "weight" for the probability of this certain cituation (probability of occuring of this certain sample). For example, we habe a sample [light, no, on_time]. And in the case when the rain is light and there is no maintenance, the probability of the train on_time == 0.6, so this is the weight we're saving. And continue iterating.

## Markov Models
For example, we need to get some probabilities for a time period. We have a weather data for the whole past year and now we need to predict the tomorrow's weather. But the thing is that the tomorrow's weather doesn't depend on the whole previous data, but at least a couple of previous days. So we need to consider only several previous days.

    - Markov assumption - the assumption that the current state depends on only a finite fixed number of previous states.

    - Markov Chain - a sequence of random variables where the distribution of each variable follows the Markov assumption. We can see here the sequence of approximate values for weather for every next day:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/markov_chain.jpg" width=70% height=70%></p>

## Hidden Markov Models
Sometimes we don't have the exact information about our current state. But we have some observation information that depends on the current state:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/hidden_model1.jpg" width=70% height=70%></p>

1) For example, there is a robot who observes some new area and it doesn't know where it is. But he have sensors to see the objects around.
2) If we say some words, the computer doesn't know which words we are saying. But it has the waveforms so it can take them and try to predict which words we said. 
3) ...
4) For example, the AI doesn't know or see what the weather is outside. But if there is a camera inside of the building, it can count how many umbrellas were brought and basing on this can predict which weather is outside.

#### Sensor model (Emission Probability)

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/hidden_model2.jpg" width=70% height=70%></p>

    - Sensor Markov assumption - the assumption that the evidence variable depends only the corresponding state.

Example of the emission data (Emission probability):

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module2/hidden_model3.jpg" width=70% height=70%></p>
