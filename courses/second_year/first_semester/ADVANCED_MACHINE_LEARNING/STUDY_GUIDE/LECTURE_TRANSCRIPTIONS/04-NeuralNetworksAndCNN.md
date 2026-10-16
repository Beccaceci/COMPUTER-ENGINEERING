# Lecture Transcription

- **Source**: `temp_audio_27869.wav`
- **Model**: `base.en`
- **Device**: `mps`

---

**[00:30 -> 00:59]** So the zoom battery is on, everything should work, and we should be able to start. Actually, I want to dedicate the very first five minutes just to remind what we did last time. So in the meanwhile, that you get seeded.

**[00:59 -> 01:02]** the further minutes and then we start this.

**[01:07 -> 01:08]** Okay.

**[01:08 -> 01:10]** So what I've been discussing

**[01:10 -> 01:13]** about what we have been discussing last time

**[01:14 -> 01:17]** was that we will,

**[01:19 -> 01:24]** we are trying to minimize the error

**[01:24 -> 01:27]** that we do on our trading side, right?

**[01:27 -> 01:32]** So our model has to go to properly fit the data observed

**[01:35 -> 01:38]** at training time, calculated error.

**[01:38 -> 01:43]** So measure what we call loss function, right?

**[01:45 -> 01:49]** And then we need to minimize this loss function.

**[01:49 -> 01:51]** What we have been looking at last time,

**[01:51 -> 01:55]** just as a big reminder is exactly on this landscape

**[01:55 -> 02:00]** as the loss function, that as you see,

**[02:00 -> 02:03]** it can have a lot of minimum.

**[02:03 -> 02:07]** And we need to find the best minimum word,

**[02:07 -> 02:11]** our model as a target for our model.

**[02:11 -> 02:16]** So the procedure that we discussed about is called gradient

**[02:16 -> 02:18]** cent, and the goal is indeed that

**[02:18 -> 02:23]** of starting from certain set of parameters for our model,

**[02:23 -> 02:26]** And then updating these parameters

**[02:26 -> 02:28]** to get to a minimum of the loss.

**[02:28 -> 02:34]** Now, we do that exactly with the load that you see here,

**[02:34 -> 02:36]** down there.

**[02:36 -> 02:37]** Sorry, just went on.

**[02:37 -> 02:40]** You will stay on interval here.

**[02:40 -> 02:43]** So the new set of parameters will be equal to the old 1

**[02:43 -> 02:48]** minus coefficient, which is called learning rate,

**[02:48 -> 02:51]** multiplied by the derivative of the loss.

**[02:51 -> 02:59]** And the loss depends on the function that we choose to define our model and the function itself depends on a set of parameters.

**[02:59 -> 03:02]** So that's exactly what we are trying to target.

**[03:02 -> 03:06]** That's our objective, find minimize the number of errors that we commit.

**[03:06 -> 03:08]** So in practice that we do.

**[03:08 -> 03:12]** So in practice that the loss functions are the number of mistakes.

**[03:12 -> 03:15]** Okay, so we discuss about it.

**[03:15 -> 03:19]** So then of course, I will not go again through all the lecture.

**[03:19 -> 03:26]** We discussed about the fact that there are several kinds of optimization procedure to

**[03:26 -> 03:32]** be able to find the minimum and the standard procedure indeed is the gradient descent,

**[03:32 -> 03:33]** right?

**[03:33 -> 03:38]** But there can be other approaches like the momentum kind of strategy that allows to

**[03:38 -> 03:44]** accumulate the gradient and go quickly towards the minimum and possibly also escape from

**[03:44 -> 03:55]** minimum that we don't like and gets a better minimum. So in practice this is what we saw last time

**[03:55 -> 04:03]** and what we got, so where we got at the end of the lecture was that so to calculate the gradients

**[04:03 -> 04:11]** of our loss function means considering checking general all the data that we have in our training

**[04:11 -> 04:19]** set. So right, for each sample in the training set, we calculate the error and so we evaluate

**[04:19 -> 04:30]** the loss. But this can be quite costly because this loss then depends on the number of samples

**[04:30 -> 04:36]** that we are dealing with and the number of parameters of our model. So since of course,

**[04:36 -> 04:41]** we need to optimize all the parameters.

**[04:41 -> 04:45]** We want to find a way to simplify our life.

**[04:45 -> 04:49]** So what we can do is reduce the number of examples

**[04:49 -> 04:53]** with which we deal at every optimization step.

**[04:53 -> 04:54]** And how do we do that?

**[04:54 -> 04:59]** Well, we just, rather than considering the whole training

**[04:59 -> 05:01]** set, so the whole set of samples,

**[05:01 -> 05:08]** and we select the subset of samples out of our training set.

**[05:08 -> 05:12]** Now, this can be done and is helpful,

**[05:12 -> 05:18]** so reduces the cost of every training step or optimization step.

**[05:18 -> 05:25]** But of course, we have to pay attention as the number of samples that we are selecting,

**[05:25 -> 05:29]** it should be representative of the whole training set.

**[05:29 -> 05:33]** So of course, we can select an M, which is much lower

**[05:33 -> 05:37]** with respect to the whole dimensionality

**[05:37 -> 05:39]** in terms of number of samples of cardinality

**[05:39 -> 05:40]** of our data set.

**[05:40 -> 05:46]** But this set should be representative of the training set.

**[05:46 -> 05:49]** And so what we have in this way is what

**[05:49 -> 05:51]** is close to casting right in the sense,

**[05:51 -> 05:54]** because the optimization does not happen over the whole training

**[05:54 -> 05:58]** set but on batches, subset of the data, which

**[05:58 -> 06:02]** are called the new batch.

**[06:02 -> 06:06]** And this allows to speed up the training procedure,

**[06:06 -> 06:08]** because now the optimization does not

**[06:08 -> 06:11]** depend anymore on the number of samples that we see,

**[06:11 -> 06:15]** but the number is fixed as a dimensional idea of the batch.

**[06:15 -> 06:18]** So we have a significant speed up.

**[06:18 -> 06:22]** So once we have completed, we have

**[06:22 -> 06:25]** covered the old data set with our batches.

**[06:25 -> 06:29]** we have practically completed the NIPOC, okay?

**[06:29 -> 06:32]** But then the trading procedure continues

**[06:32 -> 06:35]** because generally the optimization requires more

**[06:35 -> 06:36]** than one NIPOC.

**[06:36 -> 06:39]** So we restart in the beginning and look at the batches again.

**[06:41 -> 06:45]** So this was the difference between ground ascent

**[06:45 -> 06:47]** and stochastic ground ascent, right?

**[06:47 -> 06:49]** So rather using the whole dataset

**[06:49 -> 06:51]** or using a subset of it.

**[06:51 -> 06:53]** And of course, since we are introducing

**[06:53 -> 06:58]** little bit of stochasticity. Our model would not look, I mean, the laws would not throw down

**[06:58 -> 07:05]** perfectly in a smooth way, but we will see some bumps and oscillation, but then I mean usually

**[07:05 -> 07:11]** get to a reasonable minimum. And these as we said, allows to have much lower cost in terms of

**[07:11 -> 07:19]** iteration that will depend only on the dimensionality of our parameter set. So only on D and not on N.

**[07:19 -> 07:28]** Okay, so now here it's just a quite complex way to indicate how close we get to the perfect

**[07:28 -> 07:29]** accuracy.

**[07:29 -> 07:33]** So how really I mean our rather than the center of the CDER can lead us to the true

**[07:33 -> 07:38]** say ever, I mean the true risk and so on.

**[07:38 -> 07:43]** But these I mean requires a little bit more theory than the value of this part.

**[07:43 -> 07:45]** But I mean you can disregard this.

**[07:45 -> 07:48]** Eventually you can check what this paper says.

**[07:48 -> 07:51]** If you want to know more about this,

**[07:51 -> 07:54]** what we are mainly focusing on is on this part of the table

**[07:54 -> 07:57]** that says that the stochastic learning center

**[07:57 -> 08:01]** provide us with a gain in terms of a speed up

**[08:01 -> 08:03]** of the training performance.

**[08:04 -> 08:08]** And since we are introducing a little bit of stochasticity

**[08:08 -> 08:13]** as we said, this helps to avoid memorizing the training set

**[08:13 -> 08:19]** set and so have a sort of regularization effect on the model and provides better

**[08:19 -> 08:26]** geolization. So now after the past lecture and after these, let's say,

**[08:26 -> 08:32]** you saw Marie, I expect you to know what is the loss function, what is gradient

**[08:32 -> 08:36]** descent, what's the difference between gradient descent and stochastic gradient

**[08:36 -> 08:43]** descent, what is the gradient of what? So we have something,

**[08:43 -> 08:45]** We have a gradient in this procedure.

**[08:45 -> 08:46]** It's a gradient of what?

**[08:46 -> 08:49]** It's a gradient of the loss, right?

**[08:49 -> 08:53]** And so everything that the main concept that we've been discussing

**[08:53 -> 08:59]** is something that is super relevant and are pillars, let's say,

**[08:59 -> 09:03]** that you need to remember about the optimization procedure

**[09:03 -> 09:05]** for a machine learning model.

**[09:05 -> 09:07]** This holds in general.

**[09:07 -> 09:11]** It holds for, I mean, shallow model holds for a deep learning model.

**[09:11 -> 09:18]** course, we afford the early, it works for a different model where you have a lot of parameters.

**[09:20 -> 09:29]** Okay, so then, yeah, we can go to the next step of slide, the one that I prepared for today.

**[10:11 -> 10:14]** So we have seen the basics,

**[10:14 -> 10:18]** let's say of the transition procedure,

**[10:18 -> 10:20]** what is the loss and so on.

**[10:21 -> 10:24]** And now I want to get just quickly back

**[10:24 -> 10:26]** to the history of machine learning

**[10:26 -> 10:28]** that we have been talking about, right?

**[10:28 -> 10:32]** So we have seen that people that were talking about AI

**[10:32 -> 10:35]** and then machine learning and then deep learning

**[10:35 -> 10:39]** as I mean, each of them is a subset of the other.

**[10:39 -> 10:57]** And let's go back for a minute to the 1950s when, let's say, the first idea of having a model that can learn from the data was started to be formalized.

**[10:57 -> 11:07]** And actually the grand-grandfather of what we call the neural networks is the perceptron.

**[11:07 -> 11:08]** Okay?

**[11:08 -> 11:10]** So what is the perceptron?

**[11:10 -> 11:17]** It's something that has been formalized by Rosenblatt and is the thing that you practically

**[11:17 -> 11:22]** see here just like we have over here, right?

**[11:22 -> 11:23]** And what do we have?

**[11:23 -> 11:28]** We have a vector as input, vector of numbers,

**[11:28 -> 11:32]** also including a constant one plus some numbers.

**[11:32 -> 11:37]** All these numbers are linearly combined with weights.

**[11:37 -> 11:43]** And then this part, which is actually a linear function,

**[11:43 -> 11:48]** is then passing through a non-linear function, which

**[11:48 -> 11:51]** is this step function.

**[11:51 -> 11:55]** And this gives an out.

**[11:55 -> 11:59]** So as you see here, this concept of linearity

**[11:59 -> 12:01]** and then combination with nonlinearity

**[12:01 -> 12:03]** is exactly what we saw when we discussed

**[12:03 -> 12:04]** about logistic regression.

**[12:04 -> 12:07]** So we have a linear function and then there is a sigmoid.

**[12:07 -> 12:09]** Well, here is not a sigmoid.

**[12:09 -> 12:11]** It's just a very simple step function.

**[12:11 -> 12:18]** And this small object was a thing that in 1950s

**[12:18 -> 12:25]** was considered as, let's say, the root of a model that could produce a prediction automatically.

**[12:25 -> 12:36]** But this object was highly criticized by an initial, let's say, collaborator of Oros and Blat,

**[12:36 -> 12:46]** which is Mr. Martin Minsky, who practically underlined how this model is only able to

**[12:46 -> 12:48]** to solve very simple problems.

**[12:48 -> 12:53]** And it's not really able to instead tackle complex cases

**[12:55 -> 13:00]** with high, no linear kind of tasks.

**[13:01 -> 13:05]** So let's see, the logic of perception per se

**[13:05 -> 13:10]** was inspired by how neural works.

**[13:10 -> 13:13]** But of course, I mean, nowadays from this object,

**[13:13 -> 13:16]** with respect to what is today a deep neural network.

**[13:16 -> 13:21]** I mean, the inspiration is becoming more and more,

**[13:23 -> 13:24]** let's say brittle,

**[13:24 -> 13:26]** I mean, that's just more and more far away,

**[13:26 -> 13:30]** especially in the way in which we define back propagation,

**[13:30 -> 13:33]** which is something that we will probably discuss today,

**[13:33 -> 13:35]** the transition procedure is completely different

**[13:35 -> 13:37]** with respect to what happens in our neurons.

**[13:37 -> 13:39]** But this very, I mean,

**[13:39 -> 13:42]** ground ground father of the neural network

**[13:42 -> 13:43]** was actually inspired.

**[13:43 -> 13:46]** Where you see, I mean, I'm not the biologist,

**[13:46 -> 13:51]** but you see here the nucleus and the cell of the neuron itself,

**[13:53 -> 13:57]** but that is its nucleus with these extensions of dendrites,

**[13:57 -> 13:58]** and then you have the axon.

**[13:58 -> 14:02]** So in practice, these dendrites are just receiving information

**[14:02 -> 14:06]** from the other neurons, and they are, of course,

**[14:06 -> 14:08]** electrical signals.

**[14:08 -> 14:10]** And you can imagine as if all this information

**[14:10 -> 14:14]** and then sum together at the nucleus level.

**[14:14 -> 14:18]** And then if this information is over a certain threshold,

**[14:18 -> 14:21]** then the neuron fires and information is passed

**[14:21 -> 14:24]** over the action to other neurons.

**[14:24 -> 14:27]** And everything is based on electrical signals.

**[14:27 -> 14:29]** And so you see that indeed somehow

**[14:29 -> 14:31]** is connected with this logic.

**[14:31 -> 14:34]** You have the input, then you have a sort of linear combination.

**[14:34 -> 14:36]** And then you have, I mean, if this linear combination

**[14:36 -> 14:40]** is over a certain threshold than the neuron virus.

**[14:43 -> 14:46]** Yeah, so exactly what the logic that we saw before.

**[14:46 -> 14:50]** And we can simply say, okay, really, we have a threshold.

**[14:50 -> 14:52]** So if for instance, it's over zero,

**[14:52 -> 14:53]** then we have a positive output.

**[14:53 -> 14:57]** If it's below zero, we have a negative output.

**[14:57 -> 14:59]** Very simple structure in this sense.

**[15:01 -> 15:05]** And indeed, I mean, this is representing

**[15:05 -> 15:08]** simple linear classifier, right?

**[15:08 -> 15:13]** So where we have a linear combination of the xi element

**[15:13 -> 15:16]** weighted by W, I mean our weight,

**[15:16 -> 15:18]** we can have a coefficient B, you remember,

**[15:18 -> 15:20]** I mean the first line we saw the one

**[15:20 -> 15:23]** that was in front of all the X's.

**[15:23 -> 15:26]** And indeed what we are doing is that we are extending X

**[15:26 -> 15:29]** with a one and we have W that becomes WB.

**[15:29 -> 15:31]** So this is the set of our parameters

**[15:31 -> 15:34]** and we are just performing a dot product

**[15:34 -> 15:37]** and we have this, which is the linear part of the model.

**[15:37 -> 15:40]** And then we have a nonlinearity that as simple as it can be,

**[15:40 -> 15:44]** it's just a sine function, positive or negative.

**[15:44 -> 15:50]** And the W vector, if you visualize it as a linear classifier,

**[15:50 -> 15:54]** the W vector is the vector orthogonal with respect

**[15:54 -> 15:57]** to the line that is dividing our set of data.

**[15:57 -> 16:00]** Of course, x can be D dimensional.

**[16:00 -> 16:01]** So here we're just showing what happens

**[16:01 -> 16:03]** in a two dimensional space.

**[16:03 -> 16:07]** but it can get to a higher dimensional.

**[16:07 -> 16:09]** So positive example, negative example,

**[16:09 -> 16:12]** and just right or left of this line,

**[16:12 -> 16:14]** positive or negative for the prediction.

**[16:14 -> 16:19]** And of course, the line itself is the logus of points

**[16:19 -> 16:22]** where this dot product plus B is equal to zero.

**[16:22 -> 16:24]** So it's just the collection of all the points

**[16:24 -> 16:27]** where the equality to zero holds.

**[16:28 -> 16:30]** Okay, so it's just very simple the accuracy pair.

**[16:30 -> 16:32]** And then we have this prediction

**[16:32 -> 16:34]** that connects with the nonlinearity

**[16:34 -> 16:37]** with just a sine function, right?

**[16:37 -> 16:42]** So if we identify the label of the data,

**[16:43 -> 16:47]** S plus one and minus one, okay?

**[16:47 -> 16:50]** We can also replace this expression here with this.

**[16:50 -> 16:52]** I mean, the definition of our prediction,

**[16:52 -> 16:56]** we can check if our prediction is correct or not,

**[16:56 -> 16:59]** but just evaluating if the scalar value

**[16:59 -> 17:06]** that we get out of this product has the same sign of the y or not.

**[17:06 -> 17:13]** So if they have the same sign, then we have a value which is higher than 0,

**[17:13 -> 17:15]** so we have a positive and incorrect classification.

**[17:15 -> 17:22]** If instead these two things here have different sign, then the prediction is wrong.

**[17:22 -> 17:26]** Of course, this does not hold if y is formalized as 0, 1.

**[17:26 -> 17:29]** So it has to be finalized as minus one plus one.

**[17:30 -> 17:34]** Okay, so what is the perceptron for save?

**[17:34 -> 17:38]** The perceptron is, I mean, was defined at a time

**[17:38 -> 17:39]** as an online algorithm.

**[17:41 -> 17:45]** So it means that it was looking at every single sample

**[17:45 -> 17:47]** in a training set and making a prediction.

**[17:47 -> 17:49]** And if the prediction was wrong,

**[17:49 -> 17:52]** the set of parameter of the model was updated.

**[17:52 -> 17:54]** So how does it work?

**[17:54 -> 17:55]** Well, let's look here.

**[17:55 -> 17:57]** We have a set of points.

**[17:57 -> 18:01]** We have an initial initialization of our model.

**[18:01 -> 18:03]** So the W is defined by a self parameter

**[18:03 -> 18:07]** that brings our line in this position.

**[18:08 -> 18:10]** And so this is our W.

**[18:10 -> 18:13]** And now let's say that we look at the first points here.

**[18:13 -> 18:15]** This is a negative point.

**[18:15 -> 18:17]** So it's labeled with minus one.

**[18:17 -> 18:21]** So as usual, what we do when we define vectors,

**[18:21 -> 18:24]** we start from the origin and we take the vector

**[18:24 -> 18:26]** that touches the point itself.

**[18:27 -> 18:30]** So now the dot product between W and X,

**[18:30 -> 18:32]** in this case is positive.

**[18:32 -> 18:36]** I mean, it's the magnitude of the double vector multiplied

**[18:36 -> 18:38]** by the magnitude of the X vector multiplied

**[18:38 -> 18:42]** by the cosine of the angle between them, right?

**[18:42 -> 18:44]** That's the position of the dot product per se

**[18:44 -> 18:47]** and if you want to formalize it.

**[18:49 -> 18:52]** And this angle is lower than 90 degrees.

**[18:52 -> 18:57]** So we get a positive value because of course the magnitude of the vector is something positive.

**[18:57 -> 19:02]** So three positive elements, but the label is minus one.

**[19:02 -> 19:07]** So what we have is that these we have a positive value, but the label is negative.

**[19:07 -> 19:13]** So when we consider the product between y and wtx,

**[19:13 -> 19:20]** we obtain the fact that these specifier is making a mistake on this data.

**[19:20 -> 19:23]** So what happens then?

**[19:23 -> 19:27]** Then we follow the rule that the perception tell us

**[19:27 -> 19:31]** that we need to update this vector.

**[19:31 -> 19:33]** How do we update it?

**[19:33 -> 19:35]** We updated according to this rule here.

**[19:35 -> 19:40]** So the new w will be equal to the old one

**[19:40 -> 19:45]** plus the label of the object multiplied by x.

**[19:45 -> 19:55]** Right? So in practice, since the label, the ground truth is minus one, what I have to do here here is to update the W.

**[19:55 -> 20:00]** So the new W will be equal to the old one minus X.

**[20:01 -> 20:10]** Right? So I define W T minus X is this one, which means that I have to rotate my line.

**[20:10 -> 20:14]** So now the new classifier will be this one.

**[20:14 -> 20:19]** And so I will check another sample and I will go on like this.

**[20:19 -> 20:23]** Every time I make a mistake, my line will change.

**[20:23 -> 20:26]** If I don't make a mistake on that data instead,

**[20:26 -> 20:30]** the W stays as the one that it was before.

**[20:30 -> 20:32]** Okay, so it does not change.

**[20:32 -> 20:36]** So the rule of the perception was to update rule

**[20:36 -> 20:41]** So this was this one, and it was just working online,

**[20:42 -> 20:45]** one sample at a time, and updating the set of parameters.

**[20:46 -> 20:49]** So it should be quite easy to visualize.

**[20:51 -> 20:55]** So the perception was the first algorithm

**[20:55 -> 20:58]** that was able to make, let's say prediction at the end,

**[20:58 -> 21:01]** and that came out with strong formal guarantees

**[21:01 -> 21:04]** about their ability and the instability

**[21:04 -> 21:05]** to make prediction a test time.

**[21:06 -> 21:14]** So, in practice, it is possible to demonstrate that the perception will find a separating

**[21:14 -> 21:19]** a brain, but of course, there are some conditions.

**[21:19 -> 21:25]** So the condition is that the data is, by its nature, linearly separable.

**[21:25 -> 21:32]** And so if this is the case, then the perception guarantees to find a good solution to be able

**[21:32 -> 21:35]** to predict the test time on new data properly,

**[21:35 -> 21:39]** and it will be able to find it in a finite number of updates.

**[21:39 -> 21:41]** So I have a training set.

**[21:41 -> 21:43]** I look at one sample at the time.

**[21:43 -> 21:45]** I do this update progressively.

**[21:45 -> 21:50]** I change my W. And at the end, this model

**[21:50 -> 21:53]** comes out with a theoretical guarantee

**[21:53 -> 21:57]** that I will be certainly able to find a solution.

**[21:57 -> 21:59]** That works well at this time.

**[21:59 -> 22:02]** But I have to start from the hypothesis

**[22:02 -> 22:04]** that my data linear is a parallel.

**[22:04 -> 22:08]** If not, I will not be able to find a good search,

**[22:08 -> 22:09]** because this model is only linear.

**[22:09 -> 22:12]** And by the way, it's also only binary.

**[22:12 -> 22:15]** It's a very simple binary classifier.

**[22:15 -> 22:18]** It's linear, binary, and classifier.

**[22:18 -> 22:23]** So it is possible to demonstrate this, this guarantee.

**[22:23 -> 22:26]** And in practice, the Turing sense

**[22:26 -> 22:33]** that I can find the number of steps that I need to do.

**[22:33 -> 22:36]** I mean, I can also formalize and quantify the number of steps

**[22:36 -> 22:38]** that I need to do to find a good solution.

**[22:38 -> 22:41]** So if all these things hold and we'll go over it,

**[22:41 -> 22:45]** then the perceptual algorithm makes it most one over gamma

**[22:45 -> 22:46]** square mistakes.

**[22:46 -> 22:48]** So what is this one?

**[22:48 -> 22:51]** I mean, what is this gamma?

**[22:51 -> 22:55]** So we can always take our data and renormalize them

**[22:55 -> 22:57]** to leave in a sphere.

**[22:57 -> 22:59]** This is something that you can always do.

**[22:59 -> 23:01]** You're not changing the relative position of the data.

**[23:01 -> 23:05]** You're just squeezing or enlarging the dimensionality.

**[23:05 -> 23:09]** I mean, the way in which the data are distributed in the space.

**[23:09 -> 23:11]** So they leave now in a unit circle.

**[23:11 -> 23:13]** It's a unit sphere.

**[23:13 -> 23:17]** And then we can find if the data is available,

**[23:17 -> 23:20]** then we can find a W star.

**[23:20 -> 23:23]** This W star now, since everything leaves in a sphere,

**[23:23 -> 23:28]** considered as the vector of magnitude 1.

**[23:28 -> 23:31]** So this is just the vector that touches the sphere.

**[23:31 -> 23:33]** And in this formalization, then the gamma

**[23:33 -> 23:37]** is practically the distance from the optimal hyperplane

**[23:37 -> 23:41]** to the closest data point.

**[23:41 -> 23:44]** So it is possible to demonstrate this.

**[23:44 -> 23:45]** It's a theorem.

**[23:45 -> 23:48]** This algorithm is super solid, but of course,

**[23:48 -> 23:49]** has some constraints.

**[23:49 -> 23:51]** So it works.

**[23:51 -> 23:54]** only if the data are linearly separable.

**[23:54 -> 23:57]** If they don't, then we don't have guarantees

**[23:57 -> 23:59]** on the ability of the model.

**[23:59 -> 24:01]** And the model itself indeed has the limitation.

**[24:01 -> 24:06]** So I mean, Minsky was correct in criticizing it.

**[24:07 -> 24:10]** Although I mean, it was reliable,

**[24:10 -> 24:12]** solid, it comes with theoretical guarantees,

**[24:12 -> 24:13]** but I had some limitation.

**[24:14 -> 24:19]** First of all, we don't live in a world without friction,

**[24:19 -> 24:21]** So data are noisy.

**[24:21 -> 24:24]** And so inevitably, even though, I mean,

**[24:24 -> 24:27]** the data come from a phenomenon that

**[24:27 -> 24:31]** should produce linearly separable sets,

**[24:31 -> 24:33]** then they might not be linearly separable

**[24:33 -> 24:35]** when you do the observations.

**[24:35 -> 24:38]** And then if they are not linearly separable,

**[24:38 -> 24:42]** then the algorithm will end up oscillating

**[24:42 -> 24:45]** and never ending the optimization procedure.

**[24:45 -> 24:47]** So the line will change progressively.

**[24:47 -> 24:48]** I will never stop.

**[24:48 -> 24:51]** you will never find one line that satisfies

**[24:51 -> 24:54]** the minimization of the error on the training set.

**[24:55 -> 24:57]** So this of course is an issue

**[24:57 -> 25:00]** and you can immediately see it here, right?

**[25:00 -> 25:02]** So if the data is not linearly separable,

**[25:02 -> 25:04]** as in this case,

**[25:04 -> 25:07]** you cannot find the line that separate this set.

**[25:08 -> 25:12]** Now, of course, yes, Minsky was right.

**[25:12 -> 25:15]** And so we cannot expect that the world is done,

**[25:15 -> 25:19]** I mean, can be solved only by linear classifier.

**[25:19 -> 25:21]** The word is much more complicated

**[25:21 -> 25:23]** and we expect to need nonlinearities

**[25:23 -> 25:27]** like can be cases of this nature.

**[25:27 -> 25:29]** And indeed this case here

**[25:30 -> 25:35]** practically is mirroring what one would do,

**[25:35 -> 25:37]** one needs to solve the kind of task,

**[25:37 -> 25:38]** one need to solve when formalizing

**[25:38 -> 25:41]** the XOR function logic term.

**[25:41 -> 25:44]** Now, in practice, the perception has been shown

**[25:44 -> 25:48]** to be able to define n function, not function, or function,

**[25:48 -> 25:53]** but explore by itself cannot be solved just with one linear

**[25:53 -> 25:54]** classifier.

**[25:54 -> 25:59]** So again, Minsky was right, but just because you cannot solve

**[25:59 -> 26:02]** this kind of task with one linear classifier.

**[26:02 -> 26:06]** But if you combine many of them, and so like in this case,

**[26:06 -> 26:08]** I mean the logic case, then you are

**[26:08 -> 26:12]** able to rebuild something that goes

**[26:12 -> 26:15]** to the direction of representing its sort.

**[26:15 -> 26:18]** And so also being able to solve this task.

**[26:18 -> 26:22]** So one little classifier with a simple nonlinearity

**[26:22 -> 26:26]** is not enough, we know, the perception is not enough.

**[26:26 -> 26:30]** But maybe combining multiple perception together,

**[26:30 -> 26:33]** we can get to something that can provide the solution,

**[26:33 -> 26:35]** even for complex tasks.

**[26:35 -> 26:38]** And indeed, this is where we are going in neural networks.

**[26:38 -> 26:40]** I mean, it will be a combination of multiple

**[26:40 -> 26:43]** of this kind of very basic logic,

**[26:43 -> 26:46]** I mean, and the basic elements

**[26:46 -> 26:48]** like the perceptron pursuit.

**[26:50 -> 26:52]** Okay, but what else?

**[26:52 -> 26:56]** Where the perceptron stops

**[26:56 -> 26:59]** when it finds the first good solution.

**[27:00 -> 27:03]** So, and indeed it comes with the guarantee

**[27:03 -> 27:05]** that it can find it, I mean,

**[27:05 -> 27:07]** when the data is already available.

**[27:07 -> 27:12]** But it can also be a solution that does not necessarily

**[27:12 -> 27:14]** generalize well.

**[27:14 -> 27:16]** It can be a barely separating solution.

**[27:16 -> 27:20]** It can eventually touch some of the data,

**[27:20 -> 27:25]** which is usually not ideal if you think about what SVN does,

**[27:25 -> 27:27]** that tries to search for a margin that

**[27:27 -> 27:30]** separates the two set of data.

**[27:30 -> 27:33]** So we know that this is not the ideal solution that we want,

**[27:33 -> 27:36]** because otherwise, very small variation,

**[27:36 -> 27:40]** then will lead to possible errors, even on the training set itself.

**[27:41 -> 27:43]** So this is something we don't want.

**[27:43 -> 27:52]** And moreover, I mean, it can end up also over-training, but this is related also to what happens if you don't have data which are very well separable.

**[27:53 -> 27:58]** So you might end up in something which is over-training, which is related to, I mean, over-fitting.

**[27:58 -> 28:03]** So at the end, the only thing you have is your training samples

**[28:03 -> 28:07]** and there's no regularization element that is added here.

**[28:07 -> 28:10]** It's just looking and perfectly trying to classify your training set.

**[28:13 -> 28:17]** And indeed, as we said, the evolution over the perception,

**[28:17 -> 28:24]** we're trying to reason a little bit more on what one can do

**[28:24 -> 28:27]** when searching for good classifiers.

**[28:27 -> 28:30]** So rather than just having a line that's separate,

**[28:30 -> 28:33]** positive from negative data or two group of data,

**[28:33 -> 28:35]** maybe you would like to have something

**[28:35 -> 28:38]** that takes into consideration how far the data are

**[28:38 -> 28:41]** from the line, right?

**[28:41 -> 28:43]** The separating line, which again,

**[28:43 -> 28:47]** goes into the direction of a SVM with the margin and so on.

**[28:47 -> 28:49]** And you can simply think about,

**[28:49 -> 28:51]** I mean, translating a simple line,

**[28:51 -> 28:54]** that the Miese classifier into something

**[28:54 -> 28:55]** which is a probabilistic decision

**[28:55 -> 28:59]** that the more, I mean, the further you are from the line,

**[28:59 -> 29:03]** the stronger and more solid your classification can be.

**[29:03 -> 29:06]** So like the more you go in this direction,

**[29:06 -> 29:10]** the higher is the probability that your prediction,

**[29:10 -> 29:13]** I mean, it is correct in terms of assigning a label

**[29:13 -> 29:14]** to the blue class, right?

**[29:14 -> 29:17]** So probability zero dot seven, probability zero dot nine.

**[29:17 -> 29:21]** So the farther you go, the higher is the probability

**[29:21 -> 29:24]** that that sample belongs to the blue class.

**[29:24 -> 29:27]** And the other way around, the lower is the probability

**[29:27 -> 29:30]** that your data belongs to the red class.

**[29:30 -> 29:33]** And of course, the other way around is, I mean,

**[29:33 -> 29:38]** it holds the same in the other direction for the red class.

**[29:39 -> 29:41]** And how does it work?

**[29:41 -> 29:43]** I mean, this changing,

**[29:43 -> 29:46]** let's also connect with what we have seen till now.

**[29:46 -> 29:48]** This changing is in practice,

**[29:48 -> 29:51]** connected to an internal changing,

**[29:51 -> 29:54]** going from just a step function

**[29:54 -> 29:57]** to something which is a smoother function

**[29:57 -> 29:58]** as smoother nonlinearity,

**[29:58 -> 30:02]** like the sigmoid function you have been seeing

**[30:02 -> 30:04]** for logistic regression, right?

**[30:04 -> 30:06]** So that's exactly the logic from a step function,

**[30:06 -> 30:10]** simple discrete, so simple, let's say,

**[30:10 -> 30:12]** perceptron on the original one,

**[30:12 -> 30:14]** to something which is instead smooth

**[30:14 -> 30:16]** and is connected to probability.

**[30:17 -> 30:20]** Yeah, but the logic of the perceptron when we move,

**[30:20 -> 30:21]** let's say from the step function

**[30:21 -> 30:24]** to the continuous function is practically the same.

**[30:24 -> 30:26]** I mean, it's just that we are changing

**[30:26 -> 30:30]** that kind of nonlinearity that we are putting in front

**[30:30 -> 30:33]** to the linear function.

**[30:33 -> 30:35]** And here we have just one.

**[30:35 -> 30:36]** Here we start defining something

**[30:36 -> 30:38]** that is connected to probability.

**[30:38 -> 30:40]** And that's also the reason why you remember,

**[30:40 -> 30:42]** we discussed a bit of the beginning

**[30:42 -> 30:45]** about statistical learning and probabilities.

**[30:47 -> 30:49]** Okay, so yeah.

**[30:49 -> 30:53]** So now we have this connection with logistic regression,

**[30:53 -> 30:56]** what we have been discussing last time.

**[30:56 -> 30:59]** And these holes, when we are dealing with just

**[30:59 -> 31:03]** a very simple binary classifier, okay?

**[31:03 -> 31:05]** So we want to predict the score.

**[31:05 -> 31:07]** I mean, the probability that the sample belongs

**[31:07 -> 31:09]** to a certain class or not.

**[31:09 -> 31:12]** So a certain class, and then the rest is,

**[31:12 -> 31:14]** I mean, it's just binary.

**[31:16 -> 31:17]** And this is just going in that direction.

**[31:17 -> 31:22]** So connecting what we saw in terms of the sigmoid function

**[31:22 -> 31:25]** to the conditional probability,

**[31:25 -> 31:28]** this case belonging to the red class or the blue class.

**[31:28 -> 31:32]** So the probability of that the sample X belongs

**[31:32 -> 31:35]** to the red class goes to one,

**[31:35 -> 31:37]** the more you move towards the right, right?

**[31:37 -> 31:39]** And instead goes to zero,

**[31:39 -> 31:41]** the more you move towards the left.

**[31:41 -> 31:43]** So you're focusing only on one class

**[31:43 -> 31:46]** and the probability of the other class is one minus

**[31:46 -> 31:49]** the probability of the red class in this case,

**[31:49 -> 31:50]** this very simple case.

**[31:51 -> 31:54]** But in practice, you can also extend this logic

**[31:54 -> 31:57]** to a multi-class classifier.

**[31:57 -> 32:02]** So in this case, rather than using a sigmoid function,

**[32:02 -> 32:06]** what you use is the softmax expression.

**[32:06 -> 32:10]** So now you have multiple categories, right?

**[32:10 -> 32:14]** And you define the probability,

**[32:14 -> 32:19]** try to represent the probability with a fraction, but rather just being the fraction of time

**[32:19 -> 32:24]** you see that the one divided by the fraction of time you see the two and the three. Now it's just

**[32:24 -> 32:29]** expressed with an exponential to resemble again really a probability and make sure that you have

**[32:29 -> 32:37]** a score that goes between 0 and 1. Okay, so the just a fraction that now becomes an expression of

**[32:37 -> 32:43]** probability in this sense. And this is just logistic regression back in its multi-class version.

**[32:44 -> 32:51]** So now in practice, what we have been discussing, so logistic regression connects to probabilities

**[32:52 -> 32:57]** in the way that you see here. What we are applying is what is called maximum likelihood estimation

**[32:57 -> 33:03]** at the end, but there's nothing more than calculating the loss in practice than what we're doing.

**[33:03 -> 33:08]** This is just to show you the connection with the probabilities that you have been discussing

**[33:08 -> 33:15]** at the beginning of the course. These holds for logistic regression, right? So now you have a model,

**[33:15 -> 33:20]** so you have your data and you have a model and the model is defined by the parameter W.

**[33:20 -> 33:26]** And you're trying to maximize a set of parameters such that you fit well the probability right

**[33:26 -> 33:32]** for the data that you're observing. So yeah, so there's the conditional probability we are trying

**[33:32 -> 33:37]** to what we are considering. And when we go to the multi-class regression, we just have this

**[33:37 -> 33:43]** expression exploiting the soft ones, what we saw before. And so we have a prediction,

**[33:43 -> 33:50]** a multi-class prediction. So it's not just binary, but you can have multiple categories.

**[33:50 -> 33:57]** So yi here, yi is not just plus one or minus one, but it can be a set of categories.

**[33:57 -> 34:15]** And indeed, I mean, last time there was someone also asking about the connection between logistic regression and what we saw in terms of losses and the loss that you might be written also in papers in the future, where reading them cross entropy

**[34:15 -> 34:21]** right? So that's standard cross-centropy. Well, what you have on the left is what is called

**[34:21 -> 34:28]** binary cross-centropy. So this is the loss we are trying to minimize. N is the number of samples.

**[34:29 -> 34:36]** K is the number of classes, but it holds only on the right. So here is just the binary cross-centropy.

**[34:37 -> 34:41]** So we have the logarithm of the prediction, and the prediction depends on the

**[34:41 -> 34:48]** a sigmoid function, right, where the linear part is in here in the exponent of the E,

**[34:48 -> 34:54]** right, at the denominator. While the case of the cross entropy, we are using the expression

**[34:54 -> 34:59]** of the softmax. This is the connection with the probability, right, so probability assigned

**[34:59 -> 35:04]** to a certain class. And now the loss is written in this term, again summing over the training

**[35:04 -> 35:10]** samples, summing over all the possible classes, right. So this is the multi-class logistic

**[35:10 -> 35:14]** regression and connects to what we call cross as a cross-entro

**[35:14 -> 35:23]** belongs. Okay. Good. Then we have been discussing about

**[35:23 -> 35:28]** gradient descent, right? And indeed, if you look at what the

**[35:28 -> 35:31]** perception is doing, so the rule that we defined for the

**[35:31 -> 35:37]** perception that we said, the new w is equal to the old w

**[35:37 -> 35:40]** plus the ground truth y multiplied by x,

**[35:40 -> 35:44]** which can be plus one or minus one, right?

**[35:44 -> 35:45]** If you have a positive sample,

**[35:45 -> 35:47]** if you have a negative sample,

**[35:47 -> 35:50]** I mean, this update rule here

**[35:50 -> 35:53]** is exactly right in the samples.

**[35:53 -> 35:55]** It's exactly the same logic.

**[35:55 -> 35:57]** You have a loss, which in this case,

**[35:57 -> 35:59]** just a hinge loss.

**[35:59 -> 36:02]** So it's calculating the number of mistakes

**[36:02 -> 36:05]** and number of samples that you have at training time.

**[36:05 -> 36:08]** You have the y's or the label.

**[36:08 -> 36:09]** This is your loss.

**[36:09 -> 36:13]** You are taking, I mean, the new w is the previous w

**[36:13 -> 36:16]** minus coefficient of the learning rate

**[36:16 -> 36:18]** multiplied by the gradient of the loss.

**[36:18 -> 36:20]** And this brings you to this expression.

**[36:20 -> 36:24]** And this is exactly what the perception,

**[36:24 -> 36:28]** the rule of update, the fit rule of the perception is applying.

**[36:28 -> 36:30]** The only thing that changes here is that

**[36:30 -> 36:32]** we are setting the learning rate.

**[36:32 -> 36:34]** I mean, this coefficient equal to one

**[36:34 -> 36:36]** It's just a simplified version.

**[36:36 -> 36:39]** But of course, this coefficient can also change its values,

**[36:39 -> 36:42]** not just necessarily to be fixed to one.

**[36:43 -> 36:45]** So you see everything connects, right?

**[36:45 -> 36:49]** So perceptron is a very simple structure.

**[36:49 -> 36:52]** Was born in the 1950s.

**[36:52 -> 36:53]** Apparently was not working,

**[36:53 -> 36:56]** although it comes with very good guarantees.

**[36:56 -> 36:59]** Well, okay, you can make it work.

**[36:59 -> 37:01]** We can combine multiple perceptron together,

**[37:01 -> 37:03]** but then how we will optimize them?

**[37:03 -> 37:06]** Well, at the end we followed the rule

**[37:06 -> 37:11]** that was originally thought by some of the order.

**[37:11 -> 37:16]** But, I mean, actually this rule is rounder set.

**[37:16 -> 37:18]** It has the same logic and the same basics

**[37:18 -> 37:22]** of what we will use also for much more complex

**[37:22 -> 37:23]** kind of functions.

**[37:27 -> 37:31]** Yeah, so remember the perception per se is brittle,

**[37:31 -> 37:38]** can make mistakes if the data are not linearly separable through just one single perception.

**[37:38 -> 37:44]** But if we put several of them together, we will be able to solve complex kind of tasks like this

**[37:44 -> 37:51]** one. So Minsky, I mean, the one who criticized the receptor actually was right. But I mean,

**[37:51 -> 37:59]** his critics was taken a little bit too, in a too strict way, because it was not just,

**[37:59 -> 38:02]** It was not destroying, you didn't want to destroy the logic,

**[38:02 -> 38:05]** it was just saying it has some limitation.

**[38:05 -> 38:09]** And actually after that critic,

**[38:09 -> 38:13]** it started a period for AI, sort of winter of AI,

**[38:13 -> 38:16]** and then it needs quite some years to get back,

**[38:16 -> 38:19]** I mean, to demonstrate that model could work again,

**[38:19 -> 38:22]** AI not only machine learning model could work again,

**[38:22 -> 38:24]** but the new waves started with the model

**[38:24 -> 38:27]** like super vector machine connected to the probability

**[38:27 -> 38:31]** I mean, on the kind of statistical learning model

**[38:31 -> 38:35]** that you probably know that we connected

**[38:35 -> 38:37]** to a few slides back.

**[38:39 -> 38:42]** But at the same time, I mean, in the 80s,

**[38:42 -> 38:46]** this logic of combining multiple perception

**[38:46 -> 38:48]** was still alive.

**[38:49 -> 38:51]** Although, I mean, it was for long periods

**[38:51 -> 38:54]** or passed by the modern science of all that machine.

**[38:54 -> 38:59]** It was still alive and it took quite some time to Lecan

**[38:59 -> 39:03]** and all his team in practice to bring it back

**[39:03 -> 39:06]** to their, I mean, bright honors,

**[39:06 -> 39:09]** meant to be able to work properly.

**[39:09 -> 39:14]** So let's try to see what this logic of narrow network

**[39:15 -> 39:16]** is actually doing, I mean,

**[39:16 -> 39:19]** how a narrow network is composed.

**[39:19 -> 39:22]** At the end, it's just, as we said,

**[39:22 -> 39:24]** combination of multiple perceptions.

**[39:24 -> 39:28]** So you see here, we have a certain amount of inputs

**[39:28 -> 39:32]** that connect to a certain amount of outputs.

**[39:32 -> 39:36]** And you can have, let's say,

**[39:36 -> 39:39]** n input element, m output elements.

**[39:39 -> 39:41]** And every single element of the input

**[39:41 -> 39:45]** is connected to the elements of the output with weights.

**[39:45 -> 39:50]** So w11, w12, w13, w1m.

**[39:50 -> 39:55]** Okay, and what are we doing here is exactly the linear combination we mentioned before, right?

**[39:55 -> 39:57]** So nothing more than that.

**[39:57 -> 40:06]** We have a linear combination of the inputs with the weights combined over all the N elements

**[40:06 -> 40:09]** plus a nonlinearity in front.

**[40:09 -> 40:10]** Here I'm calling it sigma.

**[40:10 -> 40:11]** It can be the sigma right now.

**[40:11 -> 40:17]** I mean, it can be any nonlinear function in different kind of nonlinear function can be

**[40:17 -> 40:18]** used.

**[40:18 -> 40:32]** And indeed, as you will see, one of the most widely used nonlinearity for the network is called ReLU, rectified linear unit.

**[40:32 -> 40:34]** And it has this shape here.

**[40:34 -> 40:48]** It's not anymore the sigmoid function is just this expression here that takes the input and keep it as the original value if it is positive.

**[40:48 -> 40:52]** But instead, if it is negative, it puts it to zero.

**[40:52 -> 40:53]** Nothing more than that.

**[40:53 -> 40:55]** It's a super simple equation.

**[40:55 -> 40:58]** I mean, a super simple formula that has a discontinuity

**[40:58 -> 41:00]** because on one side is zero and the other instead

**[41:00 -> 41:04]** has a slope, it is equal to the input.

**[41:04 -> 41:06]** And it's indeed nonlinear.

**[41:06 -> 41:10]** So we can use it in the sense for our goal.

**[41:10 -> 41:14]** Well, the W themselves are just the weights of our model.

**[41:14 -> 41:16]** Now, I'm not explicitly adding a B.

**[41:16 -> 41:19]** I mean, an extra coefficient, what we call Tobias,

**[41:19 -> 41:23]** but you can think about it as included

**[41:23 -> 41:26]** in the set of dumping values.

**[41:27 -> 41:32]** And so we are starting many of these elements together.

**[41:33 -> 41:38]** And so it's just having many of these layers.

**[41:39 -> 41:43]** And indeed this brings to something which is very deep,

**[41:43 -> 41:45]** it can become very deep.

**[41:45 -> 41:49]** But the elements inside, I mean, this thing

**[41:49 -> 41:51]** that we are looking at are practically doing the same thing.

**[41:51 -> 41:55]** So every step you have, I mean, W1, W2, W3,

**[41:55 -> 41:58]** all the weights that connect input to output,

**[41:58 -> 41:59]** and so on and so forth.

**[41:59 -> 42:03]** And here I'm just supposing that the sigma function

**[42:03 -> 42:07]** is always the relu, but it might also not always be the case.

**[42:07 -> 42:10]** I mean, every layer can also have a different kind

**[42:10 -> 42:11]** of non-linearities.

**[42:11 -> 42:22]** So here, just writing everything in sort of matricial form, nothing more than that.

**[42:22 -> 42:31]** Now first of all, you see that we have something which is very heavy because we have lots of

**[42:31 -> 42:33]** parameters for every layer.

**[42:33 -> 42:38]** I mean that connects all these input and output elements.

**[42:38 -> 42:45]** And we need to find a way to somehow simplify our life, because if we build a model like

**[42:45 -> 42:47]** this, and again, what do we expect?

**[42:47 -> 42:53]** Well, we want to have as always our inputs, our function, and our output, right?

**[42:53 -> 42:57]** So the function will be a function of a lot of parameters, so it will be this monster

**[42:57 -> 42:59]** in here.

**[42:59 -> 43:04]** But then we discuss about optimizing these parameters.

**[43:04 -> 43:09]** optimize the parameters, what we'll need to do is to go through a network, calculate the loss,

**[43:09 -> 43:14]** take the derivative and update the parameters. And if you have a lot of parameters and we have

**[43:14 -> 43:20]** a monster like this and it can be super heavy, so we need to try to somehow simplify our life

**[43:20 -> 43:26]** and make sure that the shape of the function that we are trying to build somehow provides us

**[43:26 -> 43:33]** sort of guarantees of the fact that this monster is really able to solve a

**[43:33 -> 43:39]** difficult task. So we started from the thing that saying that a perception per

**[43:39 -> 43:44]** se only solve linear problems. So we certainly need to combine many of them to

**[43:44 -> 43:51]** solve nonlinear tasks. But yeah, I mean you see I mean the model can become

**[43:51 -> 43:56]** arbitrary complex, the number of parameters can explode, this thing can

**[43:56 -> 44:00]** become very difficult to optimize and also very difficult to achieve a generalization.

**[44:00 -> 44:07]** So we need somehow to guide the way which we build this function, I mean, this neural network,

**[44:07 -> 44:11]** also hoping to have a model that can be as universal as possible,

**[44:12 -> 44:20]** meaning that we don't choose the shape of the function and then need to change it every time we

**[44:20 -> 44:28]** solve a task. So ideally we would like to have a sort of a high level shape of our model that somehow

**[44:28 -> 44:34]** works for many tasks and can be reused so it can be as universal as possible. And what does it mean

**[44:34 -> 44:40]** to be a universal? Well ideally we would like to have a function again that is able to approximate

**[44:40 -> 44:47]** any complex kind of shape of the world or difficult task.

**[44:47 -> 44:50]** So this is what we want.

**[44:50 -> 45:03]** We want this function here somehow to be able to adapt also to difficult conditions and describe nonlinear complex phenomena.

**[45:03 -> 45:08]** How do we do that at the same time not becoming crazy

**[45:08 -> 45:11]** and then trying to optimize a monster, see?

**[45:12 -> 45:17]** So certainly we want to be able to describe,

**[45:17 -> 45:20]** I mean models and phenomena that are linear.

**[45:20 -> 45:22]** So how do we capture there?

**[45:22 -> 45:24]** So we would like to have a model

**[45:24 -> 45:26]** that is also as universal as possible

**[45:27 -> 45:30]** and at the same time should be easy to work with.

**[45:30 -> 45:31]** So what can we do?

**[45:31 -> 45:36]** Well, this idea of composition is already something good.

**[45:36 -> 45:40]** And it comes with this logic of combining multiple pieces.

**[45:40 -> 45:42]** Each of them is doing something that the singular

**[45:42 -> 45:44]** was doing the previous piece.

**[45:44 -> 45:49]** So compositionality is something that per se

**[45:49 -> 45:53]** is a sort of prior of the way in which we are building

**[45:53 -> 45:56]** our complex function, right?

**[45:56 -> 45:59]** And this goes already in line with the logic

**[45:59 -> 46:00]** of the neural network.

**[46:00 -> 46:01]** But let's see exactly what we mean.

**[46:01 -> 46:03]** and then we compositionality.

**[46:04 -> 46:09]** So we can think about combining,

**[46:10 -> 46:14]** so to get the nonlinear model, nonlinear parametric model,

**[46:14 -> 46:16]** of course, we cannot think about combining

**[46:16 -> 46:18]** two linear function, right?

**[46:18 -> 46:20]** Because a combination of linear function

**[46:20 -> 46:23]** is again a linear function.

**[46:23 -> 46:27]** So even in this thing here,

**[46:27 -> 46:30]** we need something which is nonlinear.

**[46:30 -> 46:33]** Because otherwise, if we just have linear combination

**[46:33 -> 46:36]** of linear combination of linear combination,

**[46:36 -> 46:39]** it's just summarizes of just one single linear function.

**[46:39 -> 46:42]** So again, we would get back to what,

**[46:42 -> 46:45]** I mean, to the limitations somehow of the single perception.

**[46:45 -> 46:49]** So we need nonlinearities, okay?

**[46:49 -> 46:51]** So this is the reason why we have

**[46:51 -> 46:54]** this kind of element in here.

**[46:54 -> 46:57]** So linear function of linear function and just linear.

**[46:57 -> 46:58]** So this is not what we want.

**[46:58 -> 47:01]** We certainly want some nonlinearity in the middle

**[47:01 -> 47:04]** and want to work with something of this shape, right?

**[47:04 -> 47:05]** Which is actually what we do

**[47:05 -> 47:07]** when we combine multiple layers.

**[47:07 -> 47:11]** The input linear part of the function nonlinearity,

**[47:11 -> 47:13]** this becomes the input of another layer

**[47:13 -> 47:18]** and it enters in the linear part of the function,

**[47:18 -> 47:21]** then it goes to another nonlinearity and so on and so forth.

**[47:21 -> 47:24]** And so we have n layers of this shape.

**[47:24 -> 47:32]** So, yeah, of course, I mean, this composition is a social tip, so I'm just putting the

**[47:32 -> 47:36]** parentheses just to look at what happens at every single layer.

**[47:36 -> 47:40]** The nonlinearities are super important.

**[47:40 -> 47:45]** So again, if it happens that I asked you, why do we name nonlinearities in a function?

**[47:45 -> 47:50]** I mean, why are we introducing nonlinearities in a deep neural network?

**[47:50 -> 47:54]** Well, because otherwise, since everything is based on this compositional logic,

**[47:54 -> 47:58]** if we compose linear function without a linear function,

**[47:58 -> 48:00]** it's just having one single linear function.

**[48:00 -> 48:09]** A linear function cannot approximate highly non-linear events and phenomena of the world.

**[48:09 -> 48:13]** So we need non-linearity to resemble complex,

**[48:13 -> 48:16]** I mean, to describe complex events

**[48:16 -> 48:20]** and to be able to make prediction on complex data.

**[48:20 -> 48:22]** So which kind of nonlinearity do we want?

**[48:22 -> 48:24]** Well, it can be, I mean, maybe a sigmoid,

**[48:24 -> 48:27]** it can be a relu, as we saw.

**[48:27 -> 48:31]** And this function here, so these nonlinearities

**[48:31 -> 48:34]** are also called activation function

**[48:34 -> 48:39]** when they enter this system of compositional structure.

**[48:39 -> 48:43]** structure. So they're also called activation function.

**[48:45 -> 49:03]** Okay, so as we said, we have an input, then we have a linear part. This linear part passes through no linearity. Right? So, there's a, let's say that the linear part is just, I mean, this is just a simple

**[49:03 -> 49:08]** and then this becomes by combining every elements together

**[49:09 -> 49:11]** and multi-layer perception.

**[49:11 -> 49:14]** And this is also called deep feed forward narrow mode.

**[49:14 -> 49:17]** So once we start combining it in this way.

**[49:18 -> 49:20]** While it's called feed forward,

**[49:20 -> 49:22]** well, because we have again an input

**[49:22 -> 49:27]** and when we calculate, we feed the data in the network

**[49:27 -> 49:30]** and we forward it till the end of the network itself.

**[49:30 -> 49:34]** So that's, let's say the direction with which we first of all read the net.

**[49:35 -> 49:39]** Then how we optimize it, we do it in the other direction, backward.

**[49:40 -> 49:43]** And this backward process is something that our neurons, I mean,

**[49:43 -> 49:46]** they don't know absolutely anything about backward propagation.

**[49:46 -> 49:47]** They don't work like this.

**[49:47 -> 49:51]** It's just an optimization procedure that we use to optimize the networks.

**[49:52 -> 49:52]** Okay.

**[49:53 -> 49:57]** But yeah, per se, this kind of structure, which is modular,

**[49:57 -> 50:04]** which is compositional is what we call multilayer perception or deeply forward neural network.

**[50:07 -> 50:15]** Yeah, so the weights are inside a scatter along all the network itself in the linear part.

**[50:15 -> 50:20]** So you see here the weights are inside the F part and the F part is the linear part.

**[50:21 -> 50:26]** There's no weights in the sigmoid or in the, in this nonlinearity, the activation function

**[50:26 -> 50:31]** They don't usually have weights. The weights is in the linear part of the function.

**[50:31 -> 50:34]** But then you have many of them, right, at different layers.

**[50:36 -> 50:45]** Okay. Yeah. So these, once we have our linear part, the nonlinearity, then we get to something

**[50:45 -> 50:53]** which is the internal hidden representation of our model. Every layer outputs produces an output.

**[50:53 -> 50:57]** This is the hidden representation that then becomes the new input for the next layer.

**[50:59 -> 51:04]** So here, just, I mean, to do some notation that you will see multiple times later on.

**[51:05 -> 51:10]** Okay. Yeah, and as usual, I mean here, the linear part, you can write it as a matrix,

**[51:10 -> 51:16]** I mean, in a matrixial form, you can just summarize the B inside the W, so you just have to W itself.

**[51:16 -> 51:20]** And you suppose that x also has a 1 in front or below.

**[51:20 -> 51:29]** I mean, just to simplify this expression for how did the calculation is done with the linear part and the linear idea.

**[51:29 -> 51:38]** Okay, so the f is the linear part of the function here, so the model, and is the linear part that depends on the parameters.

**[51:38 -> 51:42]** Again, so this is the linear part where you see the parameters.

**[51:42 -> 51:48]** the activation function, which can be relu, which can be sigma, which can be tanh, or some other

**[51:48 -> 51:58]** nonlinearity, they don't have parameters. Okay, so this is what you see at each hidden layer,

**[51:58 -> 52:04]** right? So now we are summarizing, you don't see the b, it's just wx, and what is happening?

**[52:04 -> 52:09]** Well, you have your x with all its dimensionality, let's say that you are at the very beginning,

**[52:09 -> 52:18]** that's the first layer. So this is the input x and then you have the weights, okay. So every

**[52:18 -> 52:25]** row of these w matrix has the same dimensionality of the x, right, because you have to multiply it's

**[52:25 -> 52:30]** one row, multiply by the column and so on and so forth. It's just a matricial product, okay.

**[52:30 -> 52:38]** So every row here has the same dimensionality of x, but then depending on how many rows you have,

**[52:38 -> 52:42]** you will have as many outputs, right?

**[52:42 -> 52:46]** So this procedure is bringing us to something like,

**[52:46 -> 52:50]** let's say the X that leaves in a P-dimensional space.

**[52:50 -> 52:53]** So it's even X has dimension B,

**[52:53 -> 52:56]** to a new space that has dimension Q,

**[52:56 -> 53:01]** where Q depends on, so corresponds to the number of rows

**[53:01 -> 53:02]** of your W matrix.

**[53:02 -> 53:07]** So as many rows you have as many output you will get, right?

**[53:08 -> 53:12]** So in practice, you can also read as every single row is producing a

**[53:12 -> 53:16]** scholar and then you have cool scholars, right?

**[53:16 -> 53:18]** So now nothing more than that.

**[53:18 -> 53:21]** This is what happens inside one layer.

**[53:21 -> 53:27]** So in this case, it's also hidden unit because you have the input layer,

**[53:27 -> 53:30]** I mean the input layer, then all the layers that you have inside are hidden, right?

**[53:30 -> 53:32]** So inside the network.

**[53:33 -> 53:35]** So that's the reason why also called hidden units.

**[53:35 -> 53:38]** and then you have the output layer at the end.

**[53:40 -> 53:40]** Okay.

**[53:41 -> 53:44]** So you can go ahead.

**[53:44 -> 53:46]** So exactly what this is what you see, right?

**[53:46 -> 53:53]** So every row multiplies by the input, which is in practice saying that you have your W

**[53:53 -> 53:58]** and you are multiplying all the elements by one elements of this row here.

**[53:58 -> 53:59]** Okay.

**[53:59 -> 54:02]** and then you go to the output y,

**[54:02 -> 54:07]** and then these y's go through the nonlinearity.

**[54:07 -> 54:10]** So first do the product, I mean calculate the product,

**[54:10 -> 54:13]** you get let's say y, and then this y enters,

**[54:13 -> 54:15]** and then goes through the nonlinearity.

**[54:15 -> 54:18]** So you do it, of course, for all the rows, right?

**[54:18 -> 54:23]** So starting from row one, getting to row m,

**[54:23 -> 54:25]** and then you have the nonlinearity.

**[54:25 -> 54:29]** that here is visualizing exactly as the relook function,

**[54:29 -> 54:34]** rectifying a unit is zero when you have a negative input

**[54:35 -> 54:39]** and it becomes equal to the input when the input is positive.

**[54:39 -> 54:42]** So it's zero till zero itself

**[54:42 -> 54:44]** and then it becomes y equal x,

**[54:44 -> 54:46]** it's just exactly as the input.

**[54:48 -> 54:53]** Okay, so well, with the sigmoid,

**[54:53 -> 55:00]** you know if you use the sigmoid rather than rectifying a unit as a activation function so as nonlinearity

**[55:00 -> 55:06]** What you expect is that every single element you get as output would be available between 0 1 right?

**[55:06 -> 55:12]** So you remember that the sigmoid squeeze everything so every input you provide it gives you as output

**[55:12 -> 55:20]** Available between 0 1 so if you use the sigmoid then the output will be q elements each of them is available between 0 1

**[55:20 -> 55:25]** which might resemble, I mean, a score and a probability.

**[55:26 -> 55:28]** But you can also have the site to have

**[55:28 -> 55:29]** a different kind of output.

**[55:29 -> 55:33]** So rather than having cool values between zero and one,

**[55:33 -> 55:37]** you might also decide to have a more general kind of output.

**[55:37 -> 55:40]** So in this case, what you can do is that you can add

**[55:40 -> 55:42]** another linear function, right,

**[55:42 -> 55:44]** before rather than exiting.

**[55:44 -> 55:47]** So if you read the function in this way, right,

**[55:47 -> 55:50]** so from the input to the output,

**[55:50 -> 55:52]** Here the last element is a sigmoid,

**[55:52 -> 55:54]** so everything will be provided to you

**[55:54 -> 55:57]** as available between student one.

**[55:57 -> 56:00]** If instead you add another linear function here,

**[56:00 -> 56:02]** then the output can be a real deal.

**[56:02 -> 56:04]** So it depends on what you need to do.

**[56:04 -> 56:06]** So these works very well.

**[56:06 -> 56:10]** In the case you need, again, to classify something.

**[56:10 -> 56:13]** And most probably will not necessarily be just a sigmoid,

**[56:13 -> 56:15]** but you will use the soft ones

**[56:15 -> 56:18]** because you want a multi-class classifier, right?

**[56:18 -> 56:22]** But instead, if your goal is a regressor,

**[56:22 -> 56:25]** then you don't want just this kind of output.

**[56:25 -> 56:28]** You might want a vector of the machine IDQ,

**[56:28 -> 56:30]** but with values, which are just real values,

**[56:30 -> 56:32]** not necessarily within general one.

**[56:32 -> 56:35]** So depending on the task that you need to solve,

**[56:35 -> 56:38]** you formalize your network, I mean the shape,

**[56:38 -> 56:41]** and that the number of layers and the type of layers

**[56:41 -> 56:41]** is different.

**[56:43 -> 56:44]** Okay.

**[56:44 -> 57:12]** I'm not sure again, I'm looking at the questions but maybe I will answer directly during the break. So sorry, just avoid stopping.

**[57:12 -> 57:17]** Okay, so the question of the chat, but I will answer later on.

**[57:19 -> 57:24]** Okay, so, yeah, I mean, depending on what we want to do,

**[57:24 -> 57:27]** as we said, we combine different functions,

**[57:27 -> 57:29]** the nonlinearities of the activation pattern

**[57:29 -> 57:31]** can be of different nature.

**[57:32 -> 57:34]** And so we saw the sigma, we saw the relos.

**[57:34 -> 57:37]** So here we're looking at the relos, I mean, in the eyes.

**[57:37 -> 57:40]** So it's zeros, wherever the input is negative

**[57:40 -> 57:45]** and becomes y equal x when the input is positive.

**[57:46 -> 57:48]** So it's just a real function, right?

**[57:50 -> 57:53]** And what we are doing,

**[57:53 -> 57:55]** so we said, we started from the logic that saying,

**[57:55 -> 57:57]** okay, we want the model which is compositional

**[57:57 -> 57:59]** and we want the model that is universal

**[57:59 -> 58:04]** that is able to approximate even complex function

**[58:04 -> 58:06]** because at the end of the day,

**[58:06 -> 58:07]** our model is just, yeah,

**[58:07 -> 58:11]** making a sort of trying to approximate the function

**[58:11 -> 58:12]** that brings us from the input to the output.

**[58:12 -> 58:14]** It can be as complex as we want, right?

**[58:14 -> 58:19]** So the reality is so nuanced that we cannot really know

**[58:19 -> 58:21]** our priori how this function is made.

**[58:21 -> 58:24]** But if we do it like this, so if we follow this logic

**[58:24 -> 58:28]** of compositionality and we combine linearities

**[58:28 -> 58:30]** and nonlinearities, what do we have at the end?

**[58:30 -> 58:32]** Think about combining all these layers

**[58:32 -> 58:36]** where we have, I mean, all relu function, right?

**[58:36 -> 58:38]** At the end, in practice, the solution

**[58:38 -> 58:41]** will be nothing more than a linear combination

**[58:41 -> 58:43]** of nonlinearities.

**[58:43 -> 58:46]** And linear combination of nonlinearities,

**[58:46 -> 58:50]** in practice, they are constructing a shape in the space,

**[58:50 -> 58:53]** in a higher dimensional space.

**[58:53 -> 58:57]** So these are all reluze that combines together.

**[58:57 -> 59:01]** So they build a shape.

**[59:01 -> 59:03]** I mean, a piecewise linear shape.

**[59:03 -> 59:10]** Okay. And this piece was linear shape is exactly what we use to make the prediction at the end, right?

**[59:10 -> 59:23]** Even when our data very complexly, I mean, distributed in the space, we will try, we are trying to understand how to fit the data and be able maybe to separate them into three classes, right?

**[59:23 -> 59:32]** So this is what we are doing. We are literally combining nonlinearities and trying to build this complex function, which is in the case of which all the functional

**[59:32 -> 59:37]** Brelou art is just this complex kind of a piecewise linear

**[59:37 -> 59:43]** Let's say it's not a blade right, but it's a it's a shape

**[59:43 -> 59:45]** Okay

**[59:45 -> 59:51]** So this is what we do in practice. This is our I mean x f of theta y is f of theta will be

**[59:52 -> 59:54]** combination of this kind of function and

**[59:56 -> 59:58]** And in practice

**[59:58 -> 60:00]** This is what is behind.

**[60:00 -> 60:08]** I mean, one of the relevant theorem also that holds at the base of deep network,

**[60:08 -> 60:11]** which is this universal approximation theorem.

**[60:11 -> 60:15]** So in practice, it's saying that with

**[60:15 -> 60:20]** the linear combination of this non-linear transformation,

**[60:20 -> 60:27]** we are actually able to span the entire space of continuous function.

**[60:27 -> 60:30]** So we'll be able to approximate any function that we want.

**[60:30 -> 60:33]** If you read the all universal approximation theorem,

**[60:33 -> 60:37]** it exactly says that we can practically get

**[60:37 -> 60:40]** as close as possible with this linear combination

**[60:40 -> 60:41]** or nonlinearities.

**[60:41 -> 60:45]** We can get as close as possible to any function in the world.

**[60:45 -> 60:49]** This is what the universal approximation theorem says.

**[60:49 -> 60:51]** With an error that is very small,

**[60:51 -> 60:54]** it's of course different from zero, it's larger from zero,

**[60:54 -> 60:58]** but we can get this video can get as small as possible.

**[60:58 -> 61:01]** We can get it very close to June.

**[61:01 -> 61:04]** And moreover, I mean, the first universal approximation

**[61:04 -> 61:08]** theorem was formalized when thinking about just sigmoid

**[61:08 -> 61:11]** and also supposing to have just couple of layers.

**[61:11 -> 61:15]** I mean, one layer with this multiple perceptron

**[61:15 -> 61:17]** that are combined together.

**[61:17 -> 61:23]** So it's a very relevant basin which we are building our mode.

**[61:23 -> 61:28]** So the fact that we are composing an network in these ways

**[61:28 -> 61:31]** with multiple layers, so this compositionality,

**[61:31 -> 61:33]** or linearities with nonlinearities,

**[61:33 -> 61:37]** allow us to have a function that is as universal as possible

**[61:37 -> 61:40]** and gets close to any complex function in the world.

**[61:40 -> 61:44]** Okay, but this, I mean, of course,

**[61:44 -> 61:47]** there are many version of this universal approximation theorem.

**[61:47 -> 61:50]** We will not of course discuss the demonstration of this.

**[61:50 -> 61:51]** It's just a blyum in the reference.

**[61:51 -> 61:54]** You can also read here the paper,

**[61:54 -> 61:56]** I mean, the discussion about it.

**[61:58 -> 62:00]** There are also universal approximation theorem

**[62:00 -> 62:01]** based on the value function.

**[62:01 -> 62:03]** So getting back to exactly the kind of shape

**[62:03 -> 62:05]** we were discussing before,

**[62:05 -> 62:07]** not only with a sigma.

**[62:07 -> 62:10]** And moreover, I mean, this discuss about

**[62:10 -> 62:11]** a limited amount of layers,

**[62:11 -> 62:13]** and you can imagine that this holds you more

**[62:13 -> 62:15]** when the number of layers flows.

**[62:16 -> 62:21]** So the issue, although with this universal approximation

**[62:21 -> 62:24]** and the summation theorem is that they're really nice.

**[62:24 -> 62:27]** I mean, they are really somehow reassuring

**[62:27 -> 62:29]** because they are telling us we are doing the right thing,

**[62:29 -> 62:33]** but they're not constructive in the sense

**[62:33 -> 62:38]** that they're not really providing us with a strategy

**[62:41 -> 62:43]** to get to this optimal solution

**[62:43 -> 62:48]** and really be able to find the optimal F of X.

**[62:48 -> 62:49]** So we know we can do that

**[62:49 -> 62:54]** And we know that we are putting ourselves in the right condition to be able to do this,

**[62:54 -> 62:59]** but it does not exactly tell us how to find the optimal function.

**[63:02 -> 63:07]** Yeah, so they are interesting, although I mean, they say that they are able to go work.

**[63:08 -> 63:14]** So yeah, this is just, we still need to find, I mean, of course,

**[63:14 -> 63:18]** we have empirical evidence that we are doing right and that this function

**[63:18 -> 63:21]** are really helpful to provide us good solution,

**[63:21 -> 63:24]** but still we will have to hack our way through

**[63:24 -> 63:26]** to be able to optimize a model.

**[63:27 -> 63:30]** And what does it mean to optimize a model?

**[63:30 -> 63:34]** So again, so now we are quite positive on the fact

**[63:34 -> 63:38]** that we are using the right formulation,

**[63:38 -> 63:41]** I mean, this compositionality is the right thing to do,

**[63:41 -> 63:43]** but then we have again this anyway,

**[63:43 -> 63:45]** this is a sort of monster that we need to optimize,

**[63:45 -> 63:50]** And we need to find the optimal W's for our task.

**[63:54 -> 63:57]** So if our model is done like this,

**[64:00 -> 64:04]** even when we consider the most simple possible kind of loss,

**[64:04 -> 64:07]** so let's say means forever like an L2 loss,

**[64:08 -> 64:12]** it means that we need to use this function

**[64:12 -> 64:14]** and we need to compare it with the ground truth,

**[64:14 -> 64:19]** why take the difference squared and we need to minimize this.

**[64:19 -> 64:23]** So training, what does mean to train a model?

**[64:23 -> 64:25]** It means exactly to take this loss and trying to minimize it

**[64:25 -> 64:30]** and find the theta, find the weights that

**[64:30 -> 64:33]** minimizes loss for instance, in a particular case

**[64:33 -> 64:37]** of a regression problem with a means-corral loss.

**[64:37 -> 64:41]** And the issue is that now this maybe is also nicely formulated.

**[64:41 -> 64:44]** it seems a parabola, right?

**[64:44 -> 64:46]** It seems convex.

**[64:46 -> 64:48]** But the truth is that, I mean,

**[64:48 -> 64:53]** the parameters are inside this function,

**[64:53 -> 64:57]** inside the G in a highly non-convex way.

**[64:57 -> 64:59]** I mean, they are combined with their linear function,

**[64:59 -> 65:00]** combining nonlinearities,

**[65:00 -> 65:03]** or another linear function, another nonlinearities.

**[65:03 -> 65:06]** And in general, the loss is non-convex

**[65:06 -> 65:07]** with respect to theta.

**[65:07 -> 65:12]** So yeah, I mean, it will be quite complex again

**[65:12 -> 65:14]** to be able to minimize this thing.

**[65:14 -> 65:16]** So we know we are doing the right thing,

**[65:16 -> 65:18]** it's correct, so the structure of the function

**[65:18 -> 65:22]** using this compositional logic is the right thing,

**[65:22 -> 65:25]** it's universal, okay, but how do we optimize it?

**[65:25 -> 65:27]** So we know gradient descent, right?

**[65:27 -> 65:32]** That will be the card that we use to solve it,

**[65:32 -> 65:36]** but the computation of the gradient itself,

**[65:36 -> 65:38]** I mean, for the guy in the center itself

**[65:38 -> 65:39]** can be quite quite complex.

**[65:39 -> 65:42]** I mean, it's not really a little.

**[65:42 -> 65:44]** So you see here, we are just putting

**[65:44 -> 65:48]** a red dependency with a primary or a t-t-t.

**[65:48 -> 65:50]** And it becomes a monster, right?

**[65:50 -> 65:55]** When you start writing it down with all its components,

**[65:55 -> 65:57]** of this function, a function of function,

**[65:57 -> 66:01]** this matriosca effect makes it quite impressive.

**[66:01 -> 66:10]** Yeah, so you know, for sure that completing the gradient by hand is invisible.

**[66:10 -> 66:17]** And also thinking about searching for approximation, like, I mean, not really the derivatives,

**[66:17 -> 66:22]** but finite differences might be complex.

**[66:22 -> 66:25]** We know that the chain rule is our strategy.

**[66:25 -> 66:30]** I mean, we already saw it in previous lecture when we have complex loss function.

**[66:30 -> 66:34]** Of course, you have a derivative when you have a function of a functional function,

**[66:34 -> 66:38]** you are, I mean, the mathematical tool is the chain rule.

**[66:38 -> 66:45]** But anyway, I mean, the computation of these when you have a very complex model,

**[66:45 -> 66:51]** although the logic is perfectly fine, how to implement it is not trivial at all.

**[66:51 -> 66:53]** And we need to do it in an efficient way, right?

**[66:53 -> 66:59]** Okay, I mean, computers are powerful, okay, we can use a lot of computational capacity,

**[66:59 -> 67:05]** But how do we actually instruct our model to do it in an efficient way, to optimize it,

**[67:05 -> 67:07]** to really be able to optimize it properly?

**[67:07 -> 67:10]** So we need to, a way to automatize this step, right?

**[67:10 -> 67:14]** And we need some trick to do that.

**[67:14 -> 67:16]** And what is this trick?

**[67:16 -> 67:23]** This trick is formalizing what is called a computational graph.

**[67:23 -> 67:24]** Okay?

**[67:24 -> 67:26]** So we have functional function of function.

**[67:26 -> 67:30]** So we know already that our function will be complex.

**[67:30 -> 67:33]** So we need to decompose them somehow

**[67:33 -> 67:36]** to then be able to properly take the derivatives.

**[67:36 -> 67:38]** So let's try to see what do we mean

**[67:38 -> 67:39]** with computational graph.

**[67:39 -> 67:42]** And let's do, I mean, a very basic sort of exercise

**[67:42 -> 67:45]** with a basic kind of function.

**[67:45 -> 67:47]** So let's say that, so in practice, yeah,

**[67:47 -> 67:49]** we need to decompose this, right?

**[67:49 -> 67:51]** So let's think about this function here.

**[67:51 -> 67:56]** Is a function of x, but the x is inside the logarithm.

**[67:56 -> 68:00]** and you also have the square root of the logarithm of X.

**[68:00 -> 68:04]** So building the computational graph

**[68:04 -> 68:08]** means starting from the most simple element like X.

**[68:08 -> 68:11]** Then the function that repeats

**[68:11 -> 68:13]** most in this case is the logarithm.

**[68:13 -> 68:16]** So the first thing you would do is really

**[68:16 -> 68:19]** trying to think about the fact that you have to write

**[68:19 -> 68:21]** this function in code.

**[68:21 -> 68:24]** You know that you will need to reuse

**[68:24 -> 68:28]** pieces of this function multiple times. So we'll try to define some intermediate variables,

**[68:29 -> 68:35]** like x is, for example, in the first element, and then you define log of x, and you call it y,

**[68:35 -> 68:41]** and then you define the square root of log of x, and you call it z. And then what you can do,

**[68:41 -> 68:48]** I mean, to re-obtain f, then you have to combine y, which is the square root of log of x, plus z,

**[68:48 -> 68:52]** So z, which is the square root of log of x,

**[68:52 -> 68:54]** and y, which was log x itself.

**[68:54 -> 68:58]** So we are just making a simple exercise,

**[68:58 -> 69:02]** taking a complex function, and decomposing it in pieces,

**[69:02 -> 69:04]** as if we had to code it, right,

**[69:04 -> 69:07]** to define intermediate variables.

**[69:07 -> 69:09]** And these intermediate variables will be the one

**[69:09 -> 69:12]** that will help you then calculate the function itself.

**[69:14 -> 69:17]** So let me provide you another example.

**[69:17 -> 69:20]** then we take a break, promise.

**[69:21 -> 69:24]** So f of x, like in this case,

**[69:24 -> 69:27]** there's a little bit more complex, right?

**[69:27 -> 69:29]** So you have a logarithm of x,

**[69:29 -> 69:30]** then you have x square,

**[69:30 -> 69:34]** x square plus one under the square root.

**[69:35 -> 69:37]** And so you start from x,

**[69:37 -> 69:41]** then you take the most simple element, x square,

**[69:41 -> 69:42]** you go to y, right?

**[69:42 -> 69:45]** So you define y as x square.

**[69:45 -> 69:48]** Then you define the square root of y plus one,

**[69:48 -> 69:50]** and you get z.

**[69:50 -> 69:55]** And then from z, you define the logarithm of,

**[69:56 -> 69:58]** in this case, x plus z.

**[69:58 -> 70:01]** So I'm considering two elements here.

**[70:01 -> 70:04]** So the logarithm of x plus z.

**[70:04 -> 70:06]** So this term, which is practically

**[70:06 -> 70:09]** on the numerator of this fraction, okay?

**[70:09 -> 70:11]** You call it r.

**[70:11 -> 70:15]** And then you actually also need R raised to the power of three.

**[70:15 -> 70:20]** Well, you need, I mean, this is just taking intermediate step

**[70:20 -> 70:22]** because you want to divide it by Y,

**[70:22 -> 70:25]** which was the square root of X squared plus one.

**[70:25 -> 70:31]** So you define S, and then you take also R raised to the power of three,

**[70:31 -> 70:34]** which is this element, you define it like T,

**[70:34 -> 70:40]** and then you take T divided by Z again, so which was the X squared.

**[70:40 -> 70:42]** and then you combine all the elements together.

**[70:42 -> 70:44]** So your function will be s minus u.

**[70:44 -> 70:47]** So you just define intermediate variables, right?

**[70:47 -> 70:50]** That's divided in pieces, your function.

**[70:50 -> 70:54]** And this corresponds to what we call computational graph,

**[70:54 -> 70:55]** right?

**[70:55 -> 70:57]** It's the logic that we use to be able to write

**[70:57 -> 70:59]** down our function in sub-pieces,

**[70:59 -> 71:02]** such that we will be able to read our model

**[71:02 -> 71:05]** in the whole network in an easier way

**[71:05 -> 71:07]** and provide the instruction to our computer

**[71:07 -> 71:14]** to be able to, let's say, digest the big function,

**[71:14 -> 71:16]** the complex function.

**[71:16 -> 71:20]** And of course, I mean, this might look complex,

**[71:20 -> 71:22]** but it's just simple example.

**[71:22 -> 71:27]** You can imagine that in practice, what we'll deal with

**[71:27 -> 71:31]** is, I mean, it's a big beast of things with connection.

**[71:31 -> 71:34]** We've got the connection, lots of norms in the middle.

**[71:34 -> 71:39]** So the graph we're dealing with will be extremely complex.

**[71:41 -> 71:44]** And again, we need to hack our way through.

**[71:44 -> 71:45]** So this is just a function.

**[71:45 -> 71:48]** And then we'll need to take the derivatives.

**[71:48 -> 71:51]** In theory, I mean, this structure that we built

**[71:51 -> 71:55]** will be useful to simplify our life when we take the derivatives.

**[71:55 -> 71:58]** So let's take a break, 15 minutes,

**[71:58 -> 72:01]** and then we start and we'll go more in depth.

**[72:01 -> 72:03]** Yes.

**[72:31 -> 72:33]** you

**[73:01 -> 73:03]** you

**[73:31 -> 73:33]** you

**[74:01 -> 74:03]** you

**[74:31 -> 74:33]** you

**[75:01 -> 75:03]** you

**[75:31 -> 75:33]** you

**[76:01 -> 76:03]** you

**[76:31 -> 76:33]** you

**[77:01 -> 77:03]** you

**[77:31 -> 77:33]** you

**[78:01 -> 78:03]** you

**[78:31 -> 78:33]** you

**[79:01 -> 79:03]** you

**[79:31 -> 79:33]** you

**[80:01 -> 80:03]** you

**[80:31 -> 80:33]** you

**[81:01 -> 81:03]** you

**[81:31 -> 81:33]** you

**[82:01 -> 82:03]** you

**[82:31 -> 82:33]** you

**[83:01 -> 83:03]** you

**[83:31 -> 83:33]** you

**[84:01 -> 84:03]** you

**[84:31 -> 84:33]** you

**[85:01 -> 85:03]** you

**[85:31 -> 85:33]** you

**[86:01 -> 86:03]** you

**[86:31 -> 86:33]** you

**[87:01 -> 87:03]** you

**[87:31 -> 87:33]** you

**[88:01 -> 88:03]** you

**[88:31 -> 88:33]** you

**[89:01 -> 89:03]** you

**[89:31 -> 89:33]** you

**[90:01 -> 90:03]** you

**[90:31 -> 90:33]** you

**[91:01 -> 91:03]** you

**[91:31 -> 91:43]** You.

**[91:43 -> 92:11]** So, we're just saying that we are starting from function that can appear quite complex

**[92:11 -> 92:14]** And we are trying to do compositing subparts

**[92:14 -> 92:18]** such that we build what is called the computational graph.

**[92:18 -> 92:23]** And we will expect to have very complex computational graphs

**[92:23 -> 92:27]** for our model, since the network per se is a combination

**[92:27 -> 92:29]** of multiple functions.

**[92:29 -> 92:33]** So we'll need to, again, get the idea

**[92:33 -> 92:36]** is to use this logic of the computational graph

**[92:36 -> 92:39]** to be able to properly take the derivatives

**[92:39 -> 92:42]** and simplify the rather than the center procedure,

**[92:42 -> 92:44]** the optimization of the parameters.

**[92:44 -> 92:49]** So now, let's think about this function here, right?

**[92:49 -> 92:51]** Let's say that we need to take derivatives

**[92:51 -> 92:54]** and there are two ways in which we can do it.

**[92:56 -> 93:00]** We can either do it by starting from the input

**[93:01 -> 93:03]** and taking the derivative of every,

**[93:03 -> 93:06]** let's say intermediate variable that we defined

**[93:06 -> 93:09]** with respect to the input itself.

**[93:09 -> 93:12]** Or, as we will see, we can do it the other way around.

**[93:12 -> 93:16]** We start from the end and take the derivative backwards.

**[93:16 -> 93:19]** So first of all, let's start with a forward mode.

**[93:19 -> 93:23]** So what we do is that we start from the input, so from x.

**[93:23 -> 93:27]** And then for every intermediate variable that we defined,

**[93:27 -> 93:30]** we take the corresponding derivative.

**[93:30 -> 93:31]** So let's say we start from the derivative,

**[93:31 -> 93:35]** it's from the input itself, so that the derivative of x

**[93:35 -> 93:38]** with respect to itself is of course one, right?

**[93:38 -> 93:39]** So very, very soon.

**[93:40 -> 93:44]** Let's see, the derivative of y with respect to x,

**[93:44 -> 93:48]** well, we can simply write it as itself multiplied

**[93:48 -> 93:50]** by the derivative x with respect to x, right?

**[93:50 -> 93:52]** This is just one.

**[93:52 -> 93:56]** So y is the logarithm of x.

**[93:56 -> 94:00]** So the logarithm of x, the derivative with respect to x

**[94:00 -> 94:01]** is one over x.

**[94:01 -> 94:03]** And we're just reporting this,

**[94:03 -> 94:05]** I mean, just a multiplication,

**[94:05 -> 94:12]** is just one. And the goal is to reuse what we have seen in the previous line. Now,

**[94:12 -> 94:18]** the derivative of z with respect to x, so we are always deriving with respect to the input.

**[94:19 -> 94:23]** Well, this will be the derivative of z with respect to y,

**[94:24 -> 94:34]** multiplied by the derivative of y with respect to x. So now, what is z is the square root of y,

**[94:35 -> 94:41]** And so it's the reality is one over two multiplied by the square root of y.

**[94:41 -> 94:45]** And then we multiply by the real y with respect to x.

**[94:45 -> 94:50]** So we are practically reusing what we had in a previous line, right?

**[94:50 -> 94:53]** We just write it in the case.

**[94:53 -> 95:01]** Then the real deal with respect to x, so the final element in this graph is,

**[95:01 -> 95:04]** so now we have two paths to get to n, right?

**[95:04 -> 95:09]** So we have these and we have these. So it will be the real deal f with respect to y

**[95:10 -> 95:17]** multiplied by the real deal y with respect to x plus the real deal f with respect to z

**[95:17 -> 95:23]** multiplied by the real deal z with respect to x. So f is just a summation of y and z.

**[95:24 -> 95:31]** So I mean the real deal with respect to y is just, I mean, it's just one. And so we keep

**[95:31 -> 95:37]** the real deal of y respond to x here and saying for this other term so we have just this to

**[95:37 -> 95:47]** turn here which is practically reusing what we had again in the previous step okay so apparently

**[95:49 -> 95:57]** the cost of all these derivatives is more or less analogous to the cost of just calculating

**[95:57 -> 96:02]** the output itself, right? So we calculate all the elements in the middle and we take the derivative

**[96:02 -> 96:08]** and we'll reuse the pieces that we have. So I mean, since we can proceed in this way to date the

**[96:08 -> 96:18]** calculation. Yeah, so of course, what we are expecting is that we use this logic of the

**[96:18 -> 96:26]** computational graphs such that we can reuse some formulas for the derivatives, right? So,

**[96:26 -> 96:34]** as in the case of defining the intermediate variable, the goal was being able to reuse

**[96:34 -> 96:39]** this intermediate variable, the same holds for the derivative, we will use some formulation for

**[96:39 -> 96:44]** the calculating each partial derivative, and then we will be able to reuse it, and then, I mean,

**[96:44 -> 96:47]** and calculate the prediction of the body.

**[96:47 -> 96:49]** As we said, the cost of completing this

**[96:49 -> 96:52]** is more or less the cost of completing all the pieces

**[96:52 -> 96:57]** in the middle of the, of the puncturing itself, apparently.

**[96:58 -> 97:02]** But the truth is that this holds when X

**[97:04 -> 97:08]** is only one dimensional or we're not really dealing

**[97:08 -> 97:13]** with a vector, but with maybe a simple scalar.

**[97:13 -> 97:16]** The truth is that the input for our model

**[97:16 -> 97:20]** will be something like p dimensional vectors, right?

**[97:20 -> 97:24]** So this x will not really be just a scalar.

**[97:24 -> 97:27]** So we'll need to take care of partial derivatives

**[97:27 -> 97:29]** on the separate directions, I mean,

**[97:29 -> 97:32]** dimensionality of x.

**[97:32 -> 97:36]** And so this will imply that the cost actually

**[97:36 -> 97:38]** will depend on p, right?

**[97:38 -> 97:42]** So on the dimensionality of the input vector x.

**[97:43 -> 97:48]** Okay, and this is an issue and we would like to avoid it.

**[97:48 -> 98:01]** How can we do that? Well, yeah, so of course, I mean, what we observed is just an application of the chain rule, right? So we didn't do much respect to that.

**[98:01 -> 98:06]** But so the tool that we'll try to use.

**[98:06 -> 98:08]** What is it often?

**[98:10 -> 98:12]** Someone open the mic.

**[98:17 -> 98:20]** Check. Okay. So seems that stopped. Okay.

**[98:22 -> 98:28]** So in practice, we will not, so we use a tool which is called autograd

**[98:28 -> 98:33]** that performs automatic differentiation to calculate all this derivative in a little.

**[98:33 -> 98:40]** So we're not using, let's say, symbolic differentiation or the formula of the derivative.

**[98:40 -> 98:47]** We'll have, say, a coding tool that automatically provides us with the value of the derivative.

**[98:47 -> 98:54]** And this is called autograd. And this autograd will leverage the computational graph that we define.

**[98:54 -> 98:58]** And exploiting the intermediate derivatives that we define.

**[98:58 -> 99:01]** So this will directly provide us with evaluation,

**[99:01 -> 99:04]** not with the expression of the form of the derivative,

**[99:04 -> 99:07]** and this will be reused by the network itself.

**[99:09 -> 99:14]** But still, I mean, the issue is that exactly what we saw,

**[99:14 -> 99:16]** I mean, if the input is pigimational,

**[99:16 -> 99:20]** then taking the derivatives can be quite costly.

**[99:20 -> 99:22]** It will depend on the machine ID of P.

**[99:22 -> 99:26]** So we might think about reversing the direction

**[99:26 -> 99:31]** which we take the derivatives. Rather than starting from the input and considering the intermediate

**[99:31 -> 99:38]** elements, we can start from the output. So we adopt not any more the forward mode, but the reverse

**[99:38 -> 99:44]** mode. So we take the derivative of f, so the final element with respect to intermediate

**[99:46 -> 99:53]** variable that we define z, y, till getting them to x. So the logic is the same. I mean,

**[99:53 -> 99:55]** I mean, at the end, we get to the same derivative.

**[99:55 -> 99:59]** It's just a different way to using this computational graph

**[99:59 -> 100:01]** in a forward or in a backward mode,

**[100:01 -> 100:04]** so a reverse mode, to really calculate

**[100:04 -> 100:05]** the derivatives themselves.

**[100:05 -> 100:07]** So we start from the end.

**[100:08 -> 100:11]** The derivative of f with respect to itself is one.

**[100:11 -> 100:15]** Then the derivative of f with respect to z

**[100:15 -> 100:20]** is f over itself, multiplied by f with respect to z.

**[100:20 -> 100:22]** And here, I mean, it's simply linear,

**[100:22 -> 100:29]** it's a one, so it remains the real-de-of-f respect to itself. Then we take the real-de-of-f with respect

**[100:29 -> 100:36]** to y, and this depends both on the path that goes through, let's say, z, and the path that

**[100:36 -> 100:42]** directly goes to y, so you see up to paths. So the real-de-of-f with respect to z multiplied by

**[100:42 -> 100:49]** the real-de-of-f with respect to y, and f with respect to itself and f with respect to y.

**[100:49 -> 100:59]** So now z is this one, so we know that the reality would be this one, and it said this is linear, so we just have a one, and we get this one.

**[100:59 -> 101:09]** And then at the end we have the real deal f with respect to x, which is exploiting the real deal f with respect to y, multiply with the real y with respect to x.

**[101:09 -> 101:15]** Okay, so this is what we get. At the end the components are the same, but we are just doing it in a different direction. Okay,

**[101:16 -> 101:24]** we will need to recombine I mean these elements. They are always the same elements, but just look we are looking at them in a different order and

**[101:25 -> 101:27]** the

**[101:27 -> 101:29]** In practice, I mean this reverse mode

**[101:30 -> 101:32]** has the advantage of

**[101:33 -> 101:36]** not depending anymore on the dimensionality

**[101:36 -> 101:41]** Let's say of x itself or of the in.

**[101:41 -> 101:44]** F, what is F in our case?

**[101:44 -> 101:45]** So think about our application.

**[101:45 -> 101:51]** At the end, what we want to calculate is the loss, and we will derivative the loss, right?

**[101:51 -> 101:58]** That will depend on the internal parameter of the original function.

**[101:58 -> 102:00]** And the loss is a scalar.

**[102:00 -> 102:02]** It's not a vector.

**[102:02 -> 102:04]** So it has just one dimensionality.

**[102:04 -> 102:11]** And so in terms of calculation is much easier and much less costly to derivate on the, let's

**[102:11 -> 102:18]** say reverse mode, so backward mode rather than doing in a forward mode.

**[102:18 -> 102:21]** So how do we really, I mean, run the procedure?

**[102:21 -> 102:22]** So how does it work?

**[102:22 -> 102:29]** So what happens is that we built the computational graph and then we read it.

**[102:29 -> 102:33]** I mean, we input the data, we input the x,

**[102:33 -> 102:36]** and at every single element inside this computational graph,

**[102:36 -> 102:39]** we calculate the values.

**[102:39 -> 102:42]** We calculate the values of y of z, of all the intermediates,

**[102:42 -> 102:45]** let's say variable that we defined.

**[102:45 -> 102:46]** We calculate them.

**[102:46 -> 102:49]** So in the forward mode, we just pass the input in,

**[102:49 -> 102:51]** and we explicitly calculate the sub-partum

**[102:51 -> 102:55]** and the sub-function which are in the middle of these nodes.

**[102:55 -> 103:00]** And once we get to the end, then we use the backward pass

**[103:00 -> 103:03]** of the reverse mode to take the derivative

**[103:03 -> 103:07]** and trying to minimize the loss.

**[103:07 -> 103:08]** So this will be the procedure.

**[103:08 -> 103:12]** This forward pass is not the forward mode.

**[103:12 -> 103:13]** It's a different thing.

**[103:13 -> 103:15]** So the forward mode and reverse mode

**[103:15 -> 103:19]** are two modes to take the derivatives.

**[103:19 -> 103:23]** So now we are saying we adopt the reverse mode,

**[103:23 -> 103:27]** only the backward direction for the derivative,

**[103:27 -> 103:30]** but still we need to do first a forward pass

**[103:30 -> 103:33]** to calculate what is inside each node.

**[103:34 -> 103:35]** There are some slides later on,

**[103:35 -> 103:37]** but we see in practice, what does it mean?

**[103:37 -> 103:39]** Okay, really with the numbers.

**[103:39 -> 103:42]** But this is just the procedure.

**[103:42 -> 103:45]** Forward, calculate the elements of the graph,

**[103:45 -> 103:48]** and then backwards to calculate the derivatives.

**[103:49 -> 103:51]** So, and that's the, I mean,

**[103:51 -> 103:55]** Why we adopted the backward mode is because in the backward

**[103:55 -> 103:58]** since the output is just one dimensional, it's a scalar,

**[103:58 -> 104:00]** it's a loss, it does not depend on P.

**[104:00 -> 104:02]** And so the derivatives, although I mean,

**[104:02 -> 104:05]** the concept is the same, the result is the same,

**[104:05 -> 104:09]** it allows us to have a less costly procedure

**[104:09 -> 104:12]** for our computer itself and into a form of a procedure

**[104:12 -> 104:15]** to really calculate the derivative.

**[104:15 -> 104:19]** So in a forward mode, this is the dimensionality

**[104:19 -> 104:22]** the elements that we have inside the steps for the derivatives.

**[104:22 -> 104:26]** And so the issue here is the dependence on P in one case

**[104:26 -> 104:30]** and the dependence on one, which is instead the loss function,

**[104:30 -> 104:32]** which is just one dimensional idea.

**[104:32 -> 104:34]** So the reverse mode out of the div,

**[104:34 -> 104:37]** although these two things are the same,

**[104:37 -> 104:39]** I mean, we're just putting the parentheses

**[104:39 -> 104:41]** in different ways, but the branches

**[104:41 -> 104:42]** don't make really any sense.

**[104:42 -> 104:46]** It's just there to show you how we are doing the calculation.

**[104:46 -> 104:50]** Well, this reverse mode has the effect of making

**[104:50 -> 104:52]** the calculation more efficient.

**[104:55 -> 105:00]** Okay, so then the back propagation

**[105:00 -> 105:03]** is of course exploiting the chain rule,

**[105:03 -> 105:06]** but the chain rule per se is just a mathematical tool.

**[105:06 -> 105:09]** The backward propagation is a specific choice

**[105:09 -> 105:13]** motivated by all the things we said till now

**[105:13 -> 105:15]** in terms of dimensionality.

**[105:16 -> 105:23]** And this helps to obtain the derivation in reasonable time

**[105:23 -> 105:25]** and optimize our model properly.

**[105:27 -> 105:29]** When we say that the back propagation

**[105:29 -> 105:32]** goes through the computational graph of the loss,

**[105:32 -> 105:35]** is also, I mean, like saying, we are back propagating

**[105:35 -> 105:36]** through the nut.

**[105:36 -> 105:38]** It's exactly the same thing.

**[105:38 -> 105:39]** So back propagating through the nut

**[105:39 -> 105:43]** means that you first constructed your computational

**[105:43 -> 105:47]** rough and then over it you're taking the derivatives.

**[105:47 -> 105:50]** So you back probe through the math.

**[105:50 -> 105:55]** Okay. Now, as we said, of course,

**[105:55 -> 105:59]** I mean the whole model builds up a function which is

**[105:59 -> 106:02]** high and non complex, non complex.

**[106:02 -> 106:06]** We might end up having a function that has many local

**[106:06 -> 106:09]** mediums. So the basic thing is that right,

**[106:09 -> 106:12]** we take the derivative, put it then equal to zero and then

**[106:12 -> 106:14]** we move towards the minimum,

**[106:14 -> 106:16]** but we know that we might be trapped

**[106:16 -> 106:17]** in many local minimums,

**[106:17 -> 106:21]** then we might need to escape as we saw,

**[106:21 -> 106:23]** I mean, using momentum and so on.

**[106:23 -> 106:26]** And of course, the optimum that is reached

**[106:26 -> 106:28]** depend on where I started.

**[106:28 -> 106:32]** So weight initialization makes, of course, a difference.

**[106:32 -> 106:35]** So where we started to descend, okay?

**[106:35 -> 106:38]** So how we initialize the model.

**[106:38 -> 106:39]** And of course, as we said,

**[106:39 -> 106:41]** I mean, reaching a global optimum

**[106:41 -> 106:46]** not be always the right thing to do as this might means overfitting. But overall, we're always

**[106:46 -> 106:52]** doing, I mean, talking about the same thing. So what we saw in the previous slide is just a procedure

**[106:52 -> 106:57]** to get there, so to proceed or to search for this minimum. And indeed, to do that, we need to take

**[106:57 -> 107:02]** to the derivative and we have to be smart to do it in a proper way, such that our model,

**[107:02 -> 107:10]** and our procedure does not explode. Yeah, we know that in general, the model can be not differentiable,

**[107:10 -> 107:15]** And indeed, the law we know that it's not differentiable in zero, but yeah, I mean, we are,

**[107:17 -> 107:23]** our model, our computer works in a discretized work, and we don't necessarily always, I mean,

**[107:23 -> 107:29]** it's very rare that we exactly happen to be in zero. So, which means zero, zero, zero, zero,

**[107:29 -> 107:35]** zero with an infinite number of zero, right? So, there's always something in the neighborhood of

**[107:35 -> 107:42]** zero, so the model does not break. But of course, there might be in general numerical

**[107:42 -> 107:47]** issue, you have to take care of. So in general, as I was saying to one of your colleagues before,

**[107:48 -> 107:53]** if your model is not converging, and there is something strange in the procedure,

**[107:53 -> 107:58]** the way in which the loss is behaving when you are training a model, I mean, the culprit is not

**[107:58 -> 108:03]** the level. You should not think, okay, I have to remove this activation function and put a

**[108:03 -> 108:07]** the different one because there is a non-differentiability there and maybe that is breaking my model.

**[108:08 -> 108:12]** Most of the time this is not that the culprit, right? So you can trust

**[108:12 -> 108:18]** relu function. So this non-differentiability is not the main reason why a model is not converging,

**[108:18 -> 108:24]** right? So we will see that in practice there might be many other causes but not this one.

**[108:24 -> 108:33]** Yeah, and in general, all the procedure to train a model is a far from a solved problem.

**[108:33 -> 108:42]** And I mean, there are always new strategies to any optimization strategies that are proposed to improve it.

**[108:42 -> 108:46]** Okay, so these are just some general observation.

**[108:46 -> 108:54]** But I think that it can be very useful to really, I mean, look at how back

**[108:54 -> 109:00]** propagation works and say both the forward mode, let's say not the forward

**[109:00 -> 109:04]** mode in terms of differential, but there's no just calculation. So the forward

**[109:04 -> 109:10]** path, let me call it forward path work and how the backward path work. In the

**[109:10 -> 109:14]** In case we have a very simple kind of computational graph,

**[109:14 -> 109:16]** poor simple function, let's say.

**[109:18 -> 109:22]** Like in this case, so let's say that I have a function

**[109:22 -> 109:25]** and I have x plus y multiplied by z.

**[109:25 -> 109:28]** So how would I decompose it in a computational graph?

**[109:28 -> 109:32]** Well, it's just x, y, they sum up together

**[109:32 -> 109:35]** in something that's an intermediate variable that I call Q

**[109:35 -> 109:39]** and then I multiply by z and I get the output, right?

**[109:39 -> 109:45]** the value of the function. Okay, so this is just the structure of the computational graph.

**[109:46 -> 109:53]** Then someone provides me with the data, right, that I can input to my model, my function. So

**[109:53 -> 110:00]** x is minus 2, y is 5, z is minus 4. And what I'm doing is that I'm just putting them inside the

**[110:00 -> 110:05]** So x is minus two, y is five, z is minus four,

**[110:06 -> 110:09]** and then I start also calculating the intermediate value.

**[110:09 -> 110:13]** So Q is just three, right?

**[110:13 -> 110:15]** And I can also calculate the overall function,

**[110:15 -> 110:17]** which is minus 12.

**[110:17 -> 110:20]** So I'm just putting a value inside, of course, the input

**[110:20 -> 110:24]** and also populating the intermediate nodes.

**[110:24 -> 110:28]** Let's say this in this graph.

**[110:28 -> 110:30]** So when I say that I run, I mean, I do,

**[110:30 -> 110:36]** execute the forward pass, this is what I'm doing. I'm putting the value inside the

**[110:37 -> 110:43]** places of this graph. I'm computing these intermediate variables.

**[110:44 -> 110:50]** And then I want to take the backward pass, so I need to calculate the relays. And I will calculate

**[110:50 -> 110:56]** the real value of F, respect to Z, respect to Y, and respect to X. But this is what we want.

**[110:56 -> 111:01]** So we start from the end, the degree of the

**[111:01 -> 111:04]** respect to itself, we know that is simply one, right?

**[111:04 -> 111:08]** Nothing more than that, exactly as the sample that we saw before.

**[111:08 -> 111:13]** The degree of the of f with respect to z is just, so

**[111:13 -> 111:15]** you see this is linear in terms of z, right?

**[111:15 -> 111:17]** So it's just x plus y.

**[111:17 -> 111:21]** And so it's exactly q, so it's exactly three.

**[111:21 -> 111:24]** So I can put it in here.

**[111:24 -> 111:28]** So just, so f is just this product here, right?

**[111:28 -> 111:32]** If I derive the respect to z, I get, and ku is 3.

**[111:32 -> 111:34]** So I just, I'm just putting it here.

**[111:34 -> 111:38]** Okay, so this is what I'm doing in terms of calculation.

**[111:38 -> 111:40]** Right, nothing more than that.

**[111:40 -> 111:44]** Then let's see, the real of f with respect to p,

**[111:44 -> 111:47]** well, is z, and we know that z is minus 4.

**[111:47 -> 111:51]** So I'm putting it here, I'm populating my graph

**[111:51 -> 111:55]** with partial derivatives, right?

**[111:55 -> 111:59]** And then the derivative of F with respect to Y

**[111:59 -> 112:03]** is just, yeah, this here.

**[112:03 -> 112:06]** So the derivative of Q with respect to Y

**[112:06 -> 112:08]** and multiply the derivative with respect to Q,

**[112:08 -> 112:11]** which now I'm just using

**[112:11 -> 112:15]** and just presenting you the names of these elements.

**[112:15 -> 112:19]** So now F in practice,

**[112:19 -> 112:22]** I'm using this intermediate variable Q

**[112:22 -> 112:25]** and I'm also considering having the Y

**[112:25 -> 112:27]** which is the region input.

**[112:27 -> 112:32]** So I say that the gradient,

**[112:32 -> 112:33]** that the overall gradient,

**[112:33 -> 112:36]** so the radial length with respect to Y

**[112:36 -> 112:38]** in terms of this component here

**[112:38 -> 112:41]** is called downstream gradient here

**[112:41 -> 112:43]** and it to consider a local gradient

**[112:43 -> 112:46]** which I'm considering just the intermediate variable

**[112:46 -> 112:47]** with respect to Y.

**[112:47 -> 112:51]** And then the rhythm F with respect to Q,

**[112:51 -> 112:53]** which is this intermediate set here,

**[112:53 -> 112:55]** which is called upstream gradient.

**[112:55 -> 112:58]** Okay, so I'm just adding some names

**[112:58 -> 113:02]** because it might happen that you see them in papers

**[113:02 -> 113:05]** or when you really implement some code,

**[113:05 -> 113:06]** you might find these kind of names

**[113:06 -> 113:09]** in the comments of the code.

**[113:09 -> 113:12]** Okay, so well, the derivative of Q

**[113:12 -> 113:16]** with respect to Y is just one.

**[113:16 -> 113:19]** And the derivative of f with respect to cool

**[113:19 -> 113:21]** is something that we already saw before.

**[113:21 -> 113:24]** So I'm just reporting the minus four here,

**[113:24 -> 113:26]** which is what we saw before.

**[113:26 -> 113:29]** So again, I'm populating the graph

**[113:29 -> 113:31]** and I can do it also for the other one.

**[113:31 -> 113:35]** And so we can verify that this is another minus four here.

**[113:35 -> 113:40]** Okay, so this is what I mean with the procedure

**[113:40 -> 113:42]** for back propagation.

**[113:42 -> 113:47]** And of course, if you have a more complex graph,

**[113:47 -> 113:50]** then things become a little bit more complicated.

**[113:50 -> 113:54]** But let's say that the logic is the same.

**[113:54 -> 113:59]** So again, in the, let's say we have this function here,

**[114:01 -> 114:04]** in the forward pass, you're just computing the output.

**[114:04 -> 114:08]** So let's say that the forward pass has been already done.

**[114:08 -> 114:10]** So now all the values that you see there

**[114:10 -> 114:13]** are the values that have been obtained

**[114:13 -> 114:18]** by calculating and running the forward pass.

**[114:18 -> 114:22]** And then you have to calculate the derivatives.

**[114:22 -> 114:25]** So again, you start from the end.

**[114:25 -> 114:28]** Now the real divide by itself is always one, right?

**[114:28 -> 114:32]** And then you have to consider, so here,

**[114:32 -> 114:35]** I mean, this complex function has been divided

**[114:35 -> 114:36]** in many parts.

**[114:36 -> 114:41]** So you have W0, X0, W1, X1, W2,

**[114:41 -> 114:43]** which are all in this exponent here.

**[114:43 -> 114:46]** And then there is this product,

**[114:46 -> 114:49]** I mean, this intermediate product, summation,

**[114:49 -> 114:51]** summation again.

**[114:51 -> 114:53]** And then there is,

**[114:53 -> 114:55]** since you have a minus in front,

**[114:55 -> 114:59]** you always also have here the multiplication by minus one.

**[114:59 -> 115:02]** Then everything is raised to the exponent.

**[115:02 -> 115:05]** So inside the exponent of the E.

**[115:05 -> 115:08]** and then you are adding plus one, so you are adding this term,

**[115:08 -> 115:12]** and then one over everything that you are putting.

**[115:12 -> 115:15]** So this is the, sorry about this,

**[115:15 -> 115:17]** I'm not sure if I can move it,

**[115:17 -> 115:20]** I want to create an issue, but it's one over

**[115:20 -> 115:22]** all that part here, right?

**[115:22 -> 115:26]** So when I start from the end, then the real effects

**[115:26 -> 115:28]** when the, with respect to a function,

**[115:28 -> 115:29]** which is one over x, you know,

**[115:29 -> 115:33]** this minus one over x squared.

**[115:33 -> 115:38]** And so x is this, right?

**[115:38 -> 115:43]** So it's minus one over 1.37 raised to the power of two.

**[115:44 -> 115:46]** And this is the value that you get.

**[115:46 -> 115:50]** So this is the x, then what you're doing is one over x, right?

**[115:50 -> 115:52]** So the x is this element here.

**[115:52 -> 115:55]** So you have to calculate the derivative, just this form,

**[115:55 -> 115:57]** and this is the output that you get.

**[115:58 -> 116:01]** Then again, upstream gradient downstream radium,

**[116:01 -> 116:07]** here local gradient that you have to calculate, then here you have x plus one which per se is

**[116:07 -> 116:13]** it's just one, so it's just copying the, I mean the, what you have to do is to multiply

**[116:13 -> 116:18]** what we have before by the new derivative, right? So we are taking, we're just multiplying

**[116:18 -> 116:24]** that the business is the chain rule. So one multiplied by this is itself, right?

**[116:24 -> 116:31]** So then, I mean the exponent, the real value of e of x is again e of x.

**[116:31 -> 116:41]** So now is, yeah, so is e to the power of minus 1.

**[116:41 -> 116:49]** So multiplied by minus dot 53, because minus 1 is this one.

**[116:49 -> 116:51]** So E of x is this.

**[116:51 -> 116:54]** So what we have as x is this, this is x.

**[116:54 -> 116:56]** So when we have to calculate this,

**[116:56 -> 116:59]** so is e raised to the power of minus one,

**[116:59 -> 117:02]** multiplied by the element that you had before.

**[117:02 -> 117:05]** So the upstream gradient 0.53,

**[117:05 -> 117:09]** and it turns out to be minus 0.2.

**[117:11 -> 117:12]** And then you go on like this.

**[117:12 -> 117:15]** So you calculate then the next step.

**[117:15 -> 117:19]** This is the derivative of minus x, which is minus one.

**[117:19 -> 117:22]** And so it changes the sign of what you had before.

**[117:22 -> 117:23]** All right.

**[117:23 -> 117:25]** And then here starts becoming, I mean,

**[117:25 -> 117:30]** apparently it's more complex, but I mean, it's not that much

**[117:30 -> 117:34]** because then you have to multiply these by one again.

**[117:34 -> 117:38]** So you're just reporting the same value.

**[117:38 -> 117:41]** And then when you happen to be here, it's again one.

**[117:41 -> 117:42]** So it's nothing more than this.

**[117:42 -> 117:46]** So summation is not that, I mean, this operation here

**[117:46 -> 117:47]** is not changing anything with respect

**[117:47 -> 117:56]** the upstream gradient and then you get back here, well you have practically, so this is

**[117:57 -> 118:05]** two and these two goes here because they are the other way around. The derivative xy with respect

**[118:05 -> 118:11]** to x is y and the derivative y of xy is x, right? So it's inverting the two. So now this was not

**[118:11 -> 118:19]** exactly 0.2 it was 0.96 something so it becomes I mean more or less 0.4 0.39

**[118:19 -> 118:24]** why this other one is just minus one so it's this multiplied by minus one so it's

**[118:24 -> 118:29]** minus two and you see I mean this is just repeated for the rest so you can

**[118:29 -> 118:34]** just double check by yourself I mean how all these steps are done and this is

**[118:34 -> 118:39]** what will happen thanks to the autogram and through and so the autogram will

**[118:39 -> 118:46]** calculated derivatives, the structure of the computational graph allow you to decompose

**[118:46 -> 118:53]** the function pieces and to easily calculate the derivatives. So this is what happens inside,

**[118:53 -> 119:01]** will happen inside your code. I mean, you will not have to formalize it by hand in most of the

**[119:01 -> 119:10]** cases, but still you need to know what's happening. Okay. So just to summarize what we saw in here.

**[119:11 -> 119:17]** So we discussed about the perception and the simulation. We discussed about how

**[119:17 -> 119:24]** minesological perception connects with probabilities. So the DC regression, multi-class statistical

**[119:24 -> 119:29]** the progression and the loss binary percent of the and cross-centropy per se.

**[119:29 -> 119:33]** We then connect perception to neural network.

**[119:33 -> 119:35]** What does it mean multi-layer perception?

**[119:35 -> 119:37]** What is a fit-forward network?

**[119:37 -> 119:45]** We mentioned the universal approximation theorem that tells us that by building a network in this way,

**[119:45 -> 119:49]** so by building a function with this composed of multiple parts,

**[119:49 -> 119:52]** really allow us to have this universality and to be able to

**[119:52 -> 119:54]** approximate any complex function.

**[119:56 -> 119:59]** And then we entered into really how we

**[120:00 -> 120:03]** will be able to optimize this complex function,

**[120:03 -> 120:05]** okay, that are universal.

**[120:05 -> 120:07]** But as we said, okay, very nice, they're universal,

**[120:07 -> 120:09]** but then how do we optimize them?

**[120:09 -> 120:12]** We said, of course we'll use Gladi and the sand,

**[120:12 -> 120:17]** but we also have to put a little bit of grain of salt,

**[120:17 -> 120:19]** let's say of a smartness in the way

**[120:19 -> 120:22]** which you formalize the optimization problem.

**[120:22 -> 120:26]** So we define the computational graph and we explain what does it mean,

**[120:26 -> 120:29]** training a model via vector variation.

**[120:29 -> 120:31]** So we run a forward pass,

**[120:31 -> 120:34]** if the input is passed through the network,

**[120:34 -> 120:36]** we calculate all the elements,

**[120:36 -> 120:39]** I mean the components of this computational graph,

**[120:39 -> 120:42]** and then the backward derivatives will provide us with

**[120:42 -> 120:46]** indication about how to optimize the parameter of the model.

**[120:46 -> 120:50]** So the direction in which you will need to move the parameter

**[120:50 -> 120:53]** to be able then to decrease the loss function.

**[120:54 -> 120:59]** Okay, so I got to, I think the last slide of this deck.

**[120:59 -> 121:04]** So the idea is to pass now to the last part of the lecture

**[121:04 -> 121:09]** where we start putting the basis of what does it mean

**[121:09 -> 121:12]** passing from a neural network,

**[121:12 -> 121:15]** which is the thing that we have seen now,

**[121:15 -> 121:20]** standard neural network to something which is instead a convolutional neural network.

**[121:21 -> 121:29]** Because again, we know how to optimize this model, but they contain a lot of connection.

**[121:29 -> 121:36]** So the kind of layer that we saw are called fully connected layers, right? So I'll go back

**[121:36 -> 121:41]** weights in the next depth of slide, but we'll stop on that.

**[121:41 -> 121:46]** So a network of these kind, all the elements

**[121:46 -> 121:48]** are connected to the other.

**[121:48 -> 121:53]** So this is a typical fully connected network.

**[121:53 -> 121:57]** And these, anyway, it's very heavy.

**[121:57 -> 122:00]** And as well as we had to put a little bit of, I'll

**[122:00 -> 122:05]** say, hours of hardness in formalizing the function

**[122:05 -> 122:08]** and optimizing it, we also want to,

**[122:08 -> 122:11]** say make this architecture a little bit lighter

**[122:11 -> 122:13]** and avoid many of these parameters.

**[122:13 -> 122:15]** So let's see how to do that.

**[122:16 -> 122:19]** So I'll change the decos diet.

**[122:19 -> 122:22]** If there are questions, just raise your hand to the meanwhile.

**[122:35 -> 123:01]** Okay.

**[123:01 -> 123:02]** Okay.

**[123:02 -> 123:03]** Okay.

**[123:03 -> 123:17]** I'm not sure we'll be able to finish this deck of life, but then we'll continue on filing

**[123:17 -> 123:18]** case.

**[123:18 -> 123:19]** Okay.

**[123:19 -> 123:21]** So as we said, this is the kind of monster.

**[123:21 -> 123:23]** Anyway, we are dealing with, right?

**[123:23 -> 123:24]** Okay.

**[123:24 -> 123:29]** we try to understand how to optimize it

**[123:29 -> 123:31]** and finding a strategy to do that.

**[123:31 -> 123:34]** But anyway, we know that it's universal

**[123:34 -> 123:37]** because it's compositional in the way in which is defined.

**[123:37 -> 123:41]** But the number of parameters anyway is very, very big.

**[123:41 -> 123:46]** So we would like to be able to try to simplify our life.

**[123:46 -> 123:48]** And how do we simplify our life?

**[123:48 -> 123:51]** So you remember that in past lectures,

**[123:51 -> 123:56]** We talked about introducing some prior.

**[123:56 -> 124:01]** So some knowledge about the kind of data we are dealing with.

**[124:01 -> 124:07]** To then guide our model to avoid searching in all the possible huge space of function

**[124:07 -> 124:12]** that we might adopt and just restrict the space such that maybe, I mean,

**[124:12 -> 124:18]** we can also reduce the number of parameters of the model and speed up the optimization

**[124:18 -> 124:20]** and find the assumption.

**[124:20 -> 124:24]** So, yeah, so, still, we would like to have, again,

**[124:24 -> 124:26]** I mean, to stick to the universal theorem,

**[124:26 -> 124:27]** so we want to have solution,

**[124:27 -> 124:29]** which are as universal as possible,

**[124:29 -> 124:33]** which means keeping this logic of the compositionality,

**[124:33 -> 124:36]** but is there a way to reduce somehow

**[124:36 -> 124:38]** the number of parameters in the model?

**[124:38 -> 124:43]** And we can be guided a bit by the data themselves

**[124:43 -> 124:48]** to simplify the network.

**[124:48 -> 124:53]** And in particular, as we said, the big revolution of AI

**[124:53 -> 124:55]** happened dealing with images.

**[124:55 -> 124:58]** So you remember that the figure that we saw

**[124:58 -> 125:01]** at the beginning there was the games like

**[125:02 -> 125:04]** chats or checkers, okay?

**[125:04 -> 125:07]** And then we went through maybe more natural language

**[125:07 -> 125:10]** processing, spam and legitimate email

**[125:10 -> 125:12]** like the typical kind of application.

**[125:12 -> 125:14]** And then the third revolution

**[125:14 -> 125:16]** when we really entered the deep learning area

**[125:16 -> 125:18]** is based on images.

**[125:18 -> 125:21]** And indeed dealing with images actually

**[125:21 -> 125:24]** guided a bit the kind of architecture

**[125:24 -> 125:28]** and the backbone that is in the shape of the function

**[125:28 -> 125:31]** that we want to use.

**[125:31 -> 125:35]** And that can actually simplify the model themselves.

**[125:35 -> 125:38]** So let's try to understand what is the spryer that I'm

**[125:38 -> 125:39]** trying to put you on the table.

**[125:39 -> 125:43]** So what to do with images?

**[125:43 -> 125:45]** Well, I mean, in more in general,

**[125:45 -> 125:49]** with data that have an inherent and internal structure,

**[125:49 -> 125:51]** well, to bring information,

**[125:51 -> 125:54]** this structure has to be there.

**[125:54 -> 125:56]** So if you look at something like the thing

**[125:56 -> 125:58]** we are looking at here, I mean,

**[125:58 -> 126:00]** it's not a natural image, this is noise, right?

**[126:00 -> 126:02]** So it doesn't have a structure.

**[126:04 -> 126:07]** And what you expect to see for real image

**[126:07 -> 126:10]** is something where the information is there

**[126:10 -> 126:15]** And the pattern really comes with a connection

**[126:15 -> 126:18]** between the pixel and the senses as structured, right?

**[126:18 -> 126:22]** So of course, I mean, this is a particular kind of image.

**[126:23 -> 126:25]** But I mean, there are parts of the image

**[126:25 -> 126:27]** that are practically repeated,

**[126:27 -> 126:32]** like this rectangle on this wheel

**[126:32 -> 126:37]** or the windows in this building.

**[126:37 -> 126:40]** But these are maybe very particular images

**[126:40 -> 126:43]** the structure is there only on this image.

**[126:43 -> 126:44]** Well, the truth is that the structure

**[126:44 -> 126:46]** is there in any natural image,

**[126:46 -> 126:49]** because regardless of this particular case,

**[126:49 -> 126:51]** in any image we have perspective, we have line,

**[126:51 -> 126:54]** we have factors that rebates.

**[126:54 -> 126:57]** So the existence of this structure

**[126:57 -> 127:00]** is something that we can use and exploit

**[127:00 -> 127:04]** to guide the definition of our architecture.

**[127:04 -> 127:06]** Okay, even because if you think,

**[127:06 -> 127:08]** I mean, okay, we were looking at the noise

**[127:08 -> 127:12]** and noise, okay, it's really unstructured.

**[127:12 -> 127:14]** But when we look at something like these,

**[127:14 -> 127:17]** we have the feeling that is not noise.

**[127:17 -> 127:21]** The information is there because you see some patterns,

**[127:21 -> 127:25]** but they're not just positioning the right way, okay?

**[127:25 -> 127:28]** But the information is there, of course, it's scrambled,

**[127:28 -> 127:31]** and in our mind automatically we get to something that,

**[127:31 -> 127:33]** I mean, we start putting pieces together.

**[127:33 -> 127:34]** There is a structure there.

**[127:34 -> 127:36]** It's just a matter of finding it out, right?

**[127:36 -> 127:39]** so extracting it from the image.

**[127:39 -> 127:42]** So the fact that we are dealing with the data

**[127:42 -> 127:44]** that have a structure again can guide us

**[127:44 -> 127:46]** and can guide the architecture.

**[127:46 -> 127:48]** Let's see what are the basic concepts.

**[127:48 -> 127:50]** So when we say structure, what do we mean?

**[127:50 -> 127:54]** We mean that usually images with a structure,

**[127:54 -> 127:56]** images is the kind of data with a structure,

**[127:56 -> 128:00]** have pieces that tend to repeat, I mean in general.

**[128:00 -> 128:03]** There can be, I mean, pieces like them in an object

**[128:03 -> 128:06]** or an edge that is repeated,

**[128:06 -> 128:08]** patches that are repeated in a sense.

**[128:08 -> 128:10]** But they can be also shade of colors

**[128:10 -> 128:13]** that not the color itself, but the way

**[128:13 -> 128:15]** which the color is distributed might be similar.

**[128:15 -> 128:18]** So like on the forefront of this, the face of this girl,

**[128:18 -> 128:20]** and maybe this part of the background.

**[128:20 -> 128:23]** It's just that the way which the color is distributed

**[128:23 -> 128:24]** may be the same.

**[128:24 -> 128:26]** Maybe the color is not exactly the same,

**[128:26 -> 128:31]** but let's say the perspective brings a certain amount,

**[128:33 -> 128:35]** so a certain way to distribute the color.

**[128:35 -> 128:41]** And then there are some kind of patterns that might be repeated also in different parts of the image and so on and so forth.

**[128:41 -> 128:46]** So usually images contain this as a characteristic of being self-seamidar.

**[128:47 -> 128:49]** So there are pieces that tends to be repeated.

**[128:49 -> 128:55]** And you might not be convinced about what I said because maybe you can say, well, but it just depends on the kind of image you look.

**[128:55 -> 128:58]** Maybe there are images where the self-seam guard is not there.

**[128:58 -> 129:05]** No, I guarantee the kind of structure that is there in natural images is inherently self-seamidar.

**[129:05 -> 129:12]** And you can get it by the fact that, for instance, if you take an image and you remove an object,

**[129:12 -> 129:17]** you will be able to reconstruct this hole and to fill in this hole,

**[129:17 -> 129:21]** but just taking pieces, other pieces in the image.

**[129:21 -> 129:28]** So you can remove the eagle here and just fill in this hole by taking pieces of the image itself,

**[129:28 -> 129:31]** and just you can fill the hole this way, right?

**[129:31 -> 129:34]** This is what standard Photoshop will do for you.

**[129:34 -> 129:40]** This is exploiting self-singularity and this is a natural, I mean, characteristic of natural images.

**[129:41 -> 129:49]** There are other things that are compared to structural data, like translation invariance.

**[129:50 -> 129:57]** The semantic content of an image is there regardless of where the exact position of the

**[129:57 -> 130:00]** the origin is the image itself.

**[130:00 -> 130:04]** So I mean, when we look at this kind of image,

**[130:04 -> 130:08]** well, we think about predicting something.

**[130:08 -> 130:10]** Well, the prediction of a cut,

**[130:10 -> 130:12]** I mean, if the whole image is this one,

**[130:12 -> 130:13]** I will predict cut for this cloth,

**[130:13 -> 130:15]** for this image and cut also for this image,

**[130:15 -> 130:18]** regardless of where the position of the object is, right?

**[130:18 -> 130:22]** So there's also invariance in the semantics

**[130:22 -> 130:27]** of the content, semantic content of the image and this sense.

**[130:27 -> 130:29]** Okay, what else?

**[130:29 -> 130:32]** Well, we said a sub-scolarity,

**[130:32 -> 130:34]** we said that there is this translation variance

**[130:34 -> 130:37]** in terms of the semantic content.

**[130:37 -> 130:41]** There's also hierarchy and compositionality, right?

**[130:41 -> 130:45]** Because we might think about extracting various more blobs

**[130:45 -> 130:48]** of color or edges from an image,

**[130:48 -> 130:50]** and then combine them together to construct

**[130:50 -> 130:52]** a part of the object,

**[130:52 -> 130:54]** and then this part of the object combined together

**[130:54 -> 130:56]** to create faces.

**[130:56 -> 131:00]** And if you remember, I already showed you something like that,

**[131:00 -> 131:05]** because this is exactly what our modern didn't our network

**[131:05 -> 131:10]** do when they extract features out of the images.

**[131:10 -> 131:14]** The compositional nature of a model,

**[131:14 -> 131:16]** so the fact of having multiple layer,

**[131:16 -> 131:18]** and the fact that one layer inherit

**[131:18 -> 131:21]** what the other layer has already extracted,

**[131:21 -> 131:26]** is practically mimicking exactly the nature itself

**[131:26 -> 131:30]** of the structural data where we have hierarchy

**[131:30 -> 131:31]** and compositionality.

**[131:33 -> 131:37]** So all these characteristics are there in the data.

**[131:37 -> 131:39]** And again, we are trying to find a way to exploit

**[131:39 -> 131:44]** these characteristics to be able to simplify an network.

**[131:44 -> 131:48]** And indeed, what we can do is to pass,

**[131:48 -> 131:51]** so by exploiting this logic of hierarchy,

**[131:51 -> 131:54]** compositionality, self-similarity,

**[131:54 -> 131:56]** shift in variant patterns,

**[131:56 -> 132:01]** We can pass from a network, which is fully connected.

**[132:01 -> 132:03]** So with layers where all the input are connected

**[132:03 -> 132:07]** with all the output to something which is instead

**[132:07 -> 132:09]** exploiting specific kind of layers,

**[132:09 -> 132:12]** which are called convolutional layers.

**[132:12 -> 132:14]** And so this leads us to something

**[132:14 -> 132:16]** which is called convolutional network.

**[132:16 -> 132:21]** So these information about the structure in the data

**[132:21 -> 132:21]** will guide us.

**[132:21 -> 132:26]** So we'll work as a prior to define

**[132:26 -> 132:29]** how the architecture has to be done.

**[132:29 -> 132:34]** So in practice, what we do is that rather than having

**[132:35 -> 132:39]** fully connected layers where every element of the output

**[132:39 -> 132:42]** depends on every element of the input,

**[132:42 -> 132:45]** we will have layers where, I mean,

**[132:45 -> 132:48]** the structure is that of a convolution

**[132:48 -> 132:51]** and we will see what convolution means.

**[132:51 -> 132:54]** But now let's look at this figure already.

**[132:54 -> 132:55]** So rather than having an output

**[132:55 -> 132:58]** that depends on all the elements of the input,

**[132:58 -> 133:00]** we might have an output

**[133:00 -> 133:03]** that depends only on a subset of the input.

**[133:03 -> 133:07]** And if you see here is like a window shifting.

**[133:07 -> 133:11]** So these three elements generate this output.

**[133:11 -> 133:15]** Then you move and the three elements here

**[133:15 -> 133:17]** generate this output and so on and so forth.

**[133:17 -> 133:20]** So it's like a window moving them.

**[133:20 -> 133:25]** So let's say every element of the output is obtained

**[133:26 -> 133:30]** so the responsibility for that element of the output

**[133:30 -> 133:35]** is just due to a subset of the elements of the input.

**[133:38 -> 133:41]** So what is convolution?

**[133:41 -> 133:46]** The concept of convolution comes from signal theory.

**[133:46 -> 133:50]** And I just want to provide you with a brief overview

**[133:50 -> 133:52]** of where this concept comes from.

**[133:52 -> 133:56]** So just then you understand how we actually apply it.

**[133:56 -> 133:57]** Okay.

**[133:57 -> 133:58]** So we might have two functions

**[133:58 -> 134:00]** and convolving a function.

**[134:00 -> 134:02]** I mean, the executing the convolution

**[134:02 -> 134:05]** is this kind of thing that we're looking at here.

**[134:05 -> 134:06]** So here we are,

**[134:06 -> 134:11]** the thing about dealing with square waves, okay.

**[134:13 -> 134:16]** And the function app is a square wave

**[134:16 -> 134:20]** and I want to convolve a square wave with itself.

**[134:20 -> 134:23]** What I'm doing is that one of the wave is fixed

**[134:23 -> 134:25]** and the other is moving.

**[134:25 -> 134:28]** And what we calculate with this integral

**[134:28 -> 134:31]** is the area of the overlap.

**[134:31 -> 134:34]** So the integral is usually calculating an hour.

**[134:34 -> 134:36]** So this is what we do.

**[134:36 -> 134:38]** We take a function, I mean, one of the squared function

**[134:38 -> 134:41]** is fixed, the other is moving, the wave is the other is moving,

**[134:41 -> 134:44]** and we calculate the overlapping area.

**[134:44 -> 134:48]** And then it gets to the maximum and then it gets out.

**[134:48 -> 134:49]** it reduces again.

**[134:49 -> 134:53]** And so this is the effect of the convolution.

**[134:53 -> 134:54]** Okay.

**[134:54 -> 134:58]** You can also have a lower triangular wave and a square wave.

**[134:58 -> 134:59]** And then it's the same.

**[134:59 -> 135:01]** So first of all, what do we have to do?

**[135:01 -> 135:04]** If you look at this function here, the first thing,

**[135:04 -> 135:08]** so if this is F and this is G,

**[135:08 -> 135:13]** so we need to and the integral here is respect to DT

**[135:13 -> 135:15]** and T appears with the minus in front.

**[135:15 -> 135:18]** So we need to invert the triangle.

**[135:18 -> 135:19]** So this is what we are doing.

**[135:19 -> 135:24]** So it's just changing the direction of the triangle.

**[135:24 -> 135:28]** And then we move the triangle over the square wave.

**[135:28 -> 135:30]** And this is the effect that we have calculating

**[135:30 -> 135:31]** the overlapping area.

**[135:31 -> 135:34]** So this is the concept of convolution

**[135:34 -> 135:37]** when we deal with, let's say signal theory.

**[135:38 -> 135:43]** And usually, yeah, this is called kernel.

**[135:43 -> 135:48]** then you are convolving F with a kernel, okay, the kernel G,

**[135:48 -> 135:51]** and the output is usually called feature map.

**[135:51 -> 135:53]** And this name feature map would be exactly the same

**[135:53 -> 135:56]** that we will use for our deep network,

**[135:56 -> 135:58]** in particular for the convolutional.

**[136:00 -> 136:01]** Right?

**[136:01 -> 136:04]** So the convolution is commutative, right?

**[136:04 -> 136:09]** So F convolved by G is equal to G convolved by F,

**[136:09 -> 136:11]** I mean it's commutative.

**[136:11 -> 136:14]** It's also shift the covariance,

**[136:15 -> 136:18]** practice equality is respected,

**[136:18 -> 136:22]** you can shift F and a combo with G,

**[136:22 -> 136:26]** or you can do the convolution over the shifted data.

**[136:26 -> 136:27]** And if you see here,

**[136:27 -> 136:30]** I mean, you start looking at this kind of

**[136:30 -> 136:35]** mathematical properties, which indeed,

**[136:35 -> 136:38]** I mean, resemble what we want to do with our data

**[136:38 -> 136:41]** and the nature of the data themselves.

**[136:41 -> 136:43]** So for instance, I mean dealing with data, right,

**[136:43 -> 136:46]** we discussed about the translation environment

**[136:46 -> 136:47]** for the semantics, right?

**[136:47 -> 136:50]** So think about this, you can shift the object

**[136:50 -> 136:53]** and then convolve, think about a filter

**[136:53 -> 136:56]** to enhance the edges of the object, right?

**[136:56 -> 136:59]** So now I mean, I'm using the work convolve

**[136:59 -> 137:02]** to think about the fact that I'm applying a filter

**[137:02 -> 137:07]** to make the edge appear more strong in the image.

**[137:07 -> 137:13]** So you can shift the object and convolve, or you can convolve and shift the object.

**[137:13 -> 137:14]** And the results will be the same.

**[137:14 -> 137:20]** So you start seeing that this logic of applying a mathematical function somehow

**[137:20 -> 137:26]** respects the priors that we would like to have and the nature of the data we are dealing with.

**[137:26 -> 137:31]** So it makes sense, right, to use this logic of the convolution.

**[137:31 -> 137:43]** And we see that this is just adding more properties about the, yeah, this is just sort of, you can write down the convolution as a linear operator.

**[137:43 -> 137:51]** So if you have convolution over two function is just like a linear operator or applied over every single function.

**[137:51 -> 137:54]** there is again this logic of translational covariance.

**[137:54 -> 137:59]** Yeah, this is just showing the same logic of the two waves one over the other,

**[137:59 -> 138:03]** but rather than dealing with a continuous function,

**[138:03 -> 138:06]** is what happens when you are dealing with discrete function.

**[138:06 -> 138:07]** The logic is the same.

**[138:07 -> 138:10]** It's like the multiplication in the area,

**[138:10 -> 138:13]** as we saw before, before there was an integral.

**[138:13 -> 138:16]** Now there is a summation because you are dealing with discrete function.

**[138:17 -> 138:21]** But now I mean, okay, so convolution will like it.

**[138:21 -> 138:26]** it seems to fit well also with structural data.

**[138:26 -> 138:28]** And when we deal with images,

**[138:28 -> 138:32]** since we know that we are dealing with discrete objects,

**[138:32 -> 138:33]** because usually they are represented,

**[138:33 -> 138:37]** I mean, with magicians as pixels, right?

**[138:37 -> 138:41]** Then we can indeed think about applying this logic

**[138:41 -> 138:46]** and elaborate the images with this idea of convolution.

**[138:46 -> 138:53]** And what does it mean to report this idea of convolution over an image?

**[138:53 -> 139:01]** It is like thinking about a kernel, which is in this case you can think about it as a window, okay?

**[139:01 -> 139:05]** That moves over the image, okay?

**[139:05 -> 139:07]** So this is what we will do.

**[139:07 -> 139:10]** And what will be this kernel?

**[139:10 -> 139:12]** What will be this window?

**[139:12 -> 139:21]** This window would be our linear part of the network, of each layer.

**[139:22 -> 139:31]** So the window will contain weights. Remember W, remember B, this window will contain the weights,

**[139:31 -> 139:37]** the weights that we will need to optimize for our model. And what is the linear operation?

**[139:37 -> 139:45]** The linear operation is multiplying the content of this window with the

**[139:45 -> 139:52]** content of the image. So think about this window here as containing W1, W2, W3 in

**[139:52 -> 139:56]** every single pixel you have a weight and then you multiply the weight with the

**[139:56 -> 140:02]** value of the X. So the value of the pixel that is behind that that window.

**[140:02 -> 140:04]** Okay, this will be your linear operation

**[140:05 -> 140:09]** W I mean the window that the weight part that is applied

**[140:10 -> 140:18]** linearly applied means just multiply on the data on your X and then what you do you move the window

**[140:18 -> 140:24]** Okay, and then you move the window and the same weights are applied on a different part of the data and

**[140:25 -> 140:28]** You do it for all your data itself and you will search

**[140:28 -> 140:37]** I mean, of course you will do many data and this will be just a linear part on which you will apply an own linearity and that will build your model.

**[140:37 -> 140:39]** So what are we doing here?

**[140:39 -> 140:51]** We are getting back to model that rather than being done like this, it's actually, I mean, yeah, sorry, it's, it's better to go. It's practically representing this.

**[140:51 -> 140:58]** Okay. So now we will search for a model that works like this rather than being like this,

**[140:58 -> 141:04]** fully connected. We will work with windows that will contain our models.

**[141:04 -> 141:10]** These windows will move over the data. So the whole input is this, right? So our x is composed

**[141:10 -> 141:15]** of all these elements, but we will manage these elements just by looking at sub-part of it.

**[141:15 -> 141:23]** Okay, so and this is the logic of applying the convolution on the model.

**[141:23 -> 141:30]** So rather than having this network with all the full connection, the number of connection

**[141:30 -> 141:37]** here will be reduced a lot, because this rule, what are we doing that we are reusing the same weights.

**[141:37 -> 141:42]** Okay, we look at part of the data and then we search for that subset of weights.

**[141:42 -> 141:46]** And it will be always the same reapplied over the image.

**[141:46 -> 141:46]** Why?

**[141:46 -> 141:49]** Because we have sub-similarity.

**[141:49 -> 141:51]** So the same set of weights will be useful also

**[141:51 -> 141:53]** in many other parts of the image.

**[141:53 -> 141:56]** So there's no need to have a weight for every single pixel.

**[141:56 -> 141:59]** We will just look at patches and elaborate over them.

**[141:59 -> 142:02]** And the weights will be assigned to this sub-part

**[142:02 -> 142:04]** of the image itself.

**[142:04 -> 142:08]** And moreover, apart from reducing the, say,

**[142:08 -> 142:12]** this disconnection here.

**[142:12 -> 142:17]** Yeah, so we'll deal with the small data in this sense.

**[142:17 -> 142:21]** We will also apply other kind of layers

**[142:21 -> 142:25]** that will allow to progressively reduce

**[142:25 -> 142:26]** the amount of value.

**[142:26 -> 142:30]** So at every layer, we will practically

**[142:30 -> 142:36]** pool the information to reduce the weights that we will need

**[142:36 -> 142:37]** in the next layer.

**[142:37 -> 142:42]** And so we have the linear part, we have the non-linearity,

**[142:43 -> 142:45]** and then we can apply a pulling that reduces the dimensionality

**[142:45 -> 142:48]** such that what enters in the next layer

**[142:48 -> 142:52]** requires less parameter with respect to what we had before.

**[142:52 -> 142:54]** Okay, so there are many strategies

**[142:54 -> 142:58]** that combined together will define our convolution network.

**[142:58 -> 143:03]** And the goal is that of reducing the amount of parameters

**[143:03 -> 143:04]** that our network needs.

**[143:04 -> 143:07]** and why we did it like this,

**[143:07 -> 143:11]** because we are dealing with a specific data that has a structure,

**[143:11 -> 143:15]** and structural data allow us to be treated in this way.

**[143:15 -> 143:20]** So it's a prior knowledge that guides the way in which you define our network.

**[143:20 -> 143:24]** So in practice,

**[143:24 -> 143:29]** so these are the W we will search for.

**[143:29 -> 143:34]** That would be the contents of our small windows.

**[143:34 -> 143:39]** And we've had many of them, W1, W2, W3.

**[143:39 -> 143:41]** And once the network is straight,

**[143:41 -> 143:44]** if we look at what this window has learned,

**[143:44 -> 143:47]** because you can try to visualize these weights,

**[143:47 -> 143:48]** then the model has optimized,

**[143:48 -> 143:51]** will be the content of these more windows,

**[143:51 -> 143:52]** you can visualize them, right?

**[143:52 -> 143:54]** And what do you visualize, especially in the very first

**[143:54 -> 143:59]** layer, is that the model understood

**[143:59 -> 144:03]** that I need a kernel that focuses on, I don't know,

**[144:03 -> 144:13]** 45 degree edge and my window will detect always only that kind of pattern. Then I will have another

**[144:13 -> 144:19]** window that will focus on a changing of color from the bottom to the top. So horizontal edge

**[144:19 -> 144:26]** with this change of color. Then I will have maybe another kind of edge. So the weights that we learn

**[144:26 -> 144:29]** it really represents some structure,

**[144:29 -> 144:33]** small structure inside the image.

**[144:33 -> 144:36]** And indeed, when they, so this is,

**[144:36 -> 144:38]** what I did is that I trained my model

**[144:38 -> 144:41]** and then I'm looking back at what the model learned.

**[144:41 -> 144:43]** So I'm looking inside these weights

**[144:43 -> 144:46]** that the model optimized and I'm trying to visualize them.

**[144:46 -> 144:49]** And indeed now, I posteriori know that they behave like this.

**[144:49 -> 144:53]** So what was this, let's say window doing?

**[144:53 -> 144:55]** Every time it passes over the image,

**[144:55 -> 145:00]** it will highlight all the places in the image

**[145:00 -> 145:03]** where I had that particular kind of edge.

**[145:03 -> 145:07]** And this other window will highlight the region

**[145:07 -> 145:11]** where I have an almost more part of the image.

**[145:11 -> 145:14]** These will highlight different kind of edges.

**[145:14 -> 145:17]** So the effect of applying this filter over the image

**[145:17 -> 145:18]** you see here.

**[145:19 -> 145:23]** And what is this W is what a model has learned.

**[145:23 -> 145:28]** So again, I provided the model with lots of data.

**[145:28 -> 145:30]** I asked the model, for instance,

**[145:30 -> 145:34]** like in the image red classification challenge,

**[145:34 -> 145:36]** the one that were really this kind of model

**[145:36 -> 145:37]** demonstrated their duty.

**[145:37 -> 145:42]** So let's say 10,000 images,

**[145:42 -> 145:45]** I asked the model, they passed through the network.

**[145:45 -> 145:47]** I need to minimize the loss function that says,

**[145:47 -> 145:52]** these images have to be classified in 1,000 classes.

**[145:52 -> 145:55]** And then the model is optimized for this goal

**[145:55 -> 145:56]** to minimize the loss,

**[145:56 -> 145:59]** to be able to classify the images correctly.

**[145:59 -> 146:01]** Then once my model is trained,

**[146:01 -> 146:03]** so I optimize the parameter,

**[146:03 -> 146:06]** I go back to understand what the model has learned.

**[146:06 -> 146:09]** I look inside the parameters

**[146:09 -> 146:11]** that in the very first layer,

**[146:11 -> 146:13]** I really can visualize them, right?

**[146:13 -> 146:15]** They are the small windows

**[146:15 -> 146:18]** and they are windows that are capturing edges.

**[146:18 -> 146:21]** If I go into more the intermediate layers,

**[146:21 -> 146:24]** I will see that these kind of windows

**[146:24 -> 146:25]** will become a little larger,

**[146:25 -> 146:28]** and we'll look at the larger region of the image,

**[146:28 -> 146:29]** and so on and so forth,

**[146:29 -> 146:31]** until I get to the, I mean,

**[146:31 -> 146:35]** one of the latest, I mean, the farthest,

**[146:36 -> 146:39]** in depth inside the network layer,

**[146:39 -> 146:41]** and there it's really starting to capture

**[146:41 -> 146:45]** a whole semantic of an object, okay?

**[146:45 -> 146:46]** So how does it work?

**[146:46 -> 146:48]** So we are talking about filters

**[146:48 -> 146:50]** that move over the image.

**[146:50 -> 146:51]** We said, what is this W?

**[146:51 -> 146:55]** So in this case, this table here, I repeat it again,

**[146:55 -> 146:58]** because it might sound strange.

**[146:58 -> 147:02]** It's a sort of window that moves over the image.

**[147:02 -> 147:05]** And this window now contains the parameters

**[147:05 -> 147:06]** that you want to optimize.

**[147:06 -> 147:09]** It's your W.

**[147:09 -> 147:10]** Right?

**[147:10 -> 147:11]** Right?

**[147:11 -> 147:16]** And so a filter that initially you can initialize

**[147:16 -> 147:18]** with random values, maybe just 0, 1.

**[147:18 -> 147:20]** This is what exactly you are doing.

**[147:20 -> 147:22]** you are initializing your dabbles, right?

**[147:22 -> 147:24]** So you initialize in the network.

**[147:24 -> 147:26]** And then you have an input data, right?

**[147:26 -> 147:30]** Now I'm putting everything as very simple matches

**[147:30 -> 147:32]** with very simple numbers.

**[147:32 -> 147:37]** So now the filter is applied over the input data.

**[147:37 -> 147:41]** This is just the linear part of the model.

**[147:41 -> 147:44]** It's the W multiplied by the input

**[147:44 -> 147:47]** and provides you with the feature model.

**[147:47 -> 147:51]** So what is happening here?

**[147:51 -> 147:53]** Well, let's see.

**[147:53 -> 147:59]** So this filter, now it's applied in a very specific way

**[147:59 -> 148:03]** because it's applied with the row and the column outside.

**[148:03 -> 148:08]** So sorry, it might be confusing, let me draw it somehow.

**[148:08 -> 148:12]** So you have the image, put it like this.

**[148:12 -> 148:15]** So you're using it like this.

**[148:15 -> 148:19]** So, just one column and one row is set outside,

**[148:19 -> 148:21]** then you have the other two inside.

**[148:22 -> 148:24]** So, one column of this is outside.

**[148:24 -> 148:29]** So, this column and this row, they are outside this matrix.

**[148:29 -> 148:32]** So, they are applied a little bit with a margin outside.

**[148:32 -> 148:35]** So, you're using only this one, one, one and zero, zero.

**[148:35 -> 148:38]** And when you apply it here, okay,

**[148:38 -> 148:41]** it's one multiplied by three,

**[148:41 -> 148:44]** plus one multiplied by three,

**[148:44 -> 148:48]** plus 0 multiplied by 3 plus 0 multiplied by 3 is 6.

**[148:48 -> 148:53]** So I'm really just multiplying the content of the filter

**[148:54 -> 148:56]** with the content of the input data

**[148:56 -> 148:58]** by starting a little bit with the margin

**[148:58 -> 149:02]** and just involving now this part of the filter

**[149:02 -> 149:04]** and this part of the image.

**[149:04 -> 149:07]** The content is 6 and I put it here.

**[149:07 -> 149:11]** Then I move, move the window, apply again,

**[149:11 -> 149:13]** how could the value put it there?

**[149:13 -> 149:14]** Do it like this, okay?

**[149:14 -> 149:17]** Just shifting with the filter,

**[149:17 -> 149:20]** which is applied to the input data.

**[149:20 -> 149:23]** And once I've done it, I also have another layer

**[149:23 -> 149:26]** that operates a pooling.

**[149:26 -> 149:29]** And it's, as we said, reducing the output

**[149:29 -> 149:34]** of this previous step to be able to manage,

**[149:34 -> 149:37]** now a smaller amount of elements

**[149:37 -> 149:38]** and then be able to go ahead

**[149:38 -> 149:41]** with a limited lower amount of parameters.

**[149:41 -> 149:43]** So what is this step doing?

**[149:43 -> 149:45]** What I call pooling?

**[149:45 -> 149:46]** It's a particular case.

**[149:46 -> 149:49]** I'm showing the case of max pooling.

**[149:49 -> 149:51]** How does max pooling work?

**[149:51 -> 149:53]** It takes again, windows.

**[149:53 -> 149:55]** Now I'm just dividing the feature map,

**[149:55 -> 150:00]** the output of this step in subparts, all equal to by two.

**[150:02 -> 150:04]** And then I'm taking the maximum out of this.

**[150:04 -> 150:07]** So for this window here, I take 13,

**[150:07 -> 150:10]** for this window here I take 10.

**[150:11 -> 150:15]** for this window here at the top two, please turn off the microphone

**[150:18 -> 150:24]** from the audience. Okay, so, okay. And why are we doing this? Of course, is to reduce the

**[150:24 -> 150:31]** dimensionality and then be able to manage less parameters, but also because it is like

**[150:31 -> 150:36]** like zooming out from the image.

**[150:37 -> 150:42]** Because you see, I mean, this 10,

**[150:43 -> 150:45]** it was not touching the two, right?

**[150:45 -> 150:47]** So this two somehow, let me call them pixel,

**[150:47 -> 150:49]** although they are not pixel anymore,

**[150:49 -> 150:52]** because this is a feature map after the elaboration.

**[150:52 -> 150:55]** But this value here was far away from the two.

**[150:55 -> 150:57]** So now after I do the pulling,

**[150:57 -> 151:00]** now these two values, they touch each other.

**[151:00 -> 151:02]** So it's like really zooming out.

**[151:02 -> 151:06]** I lose the details, but I keep the maximum.

**[151:06 -> 151:11]** So I'm looking in practice at larger region in the image.

**[151:11 -> 151:14]** So the more I go inside the network, the more I zoom out.

**[151:14 -> 151:16]** So I see larger and larger region

**[151:16 -> 151:19]** and I start capturing information

**[151:19 -> 151:22]** about not only the local structure,

**[151:22 -> 151:26]** but more and more semantic parts of the image.

**[151:26 -> 151:33]** Okay. So yeah, so what was before a non-local interaction, then it becomes a local interaction.

**[151:33 -> 151:42]** So again, I mean, this is what we are doing. We are reducing in practice, the amount of per meter and just focusing on windows.

**[151:42 -> 151:49]** Rather than having a W that has to take care of all the connection, I have a W that only takes care of small region.

**[151:49 -> 151:53]** Okay. Of my input in this window.

**[151:53 -> 151:57]** Right and this is exactly what I think we already saw in one of our previous slide

**[151:58 -> 151:59]** so the

**[151:59 -> 152:01]** Windows that I get at the beginning of the

**[152:02 -> 152:10]** Network will capture this blob of colors then more and more structure and then going to the semantics of the image

**[152:11 -> 152:13]** so a

**[152:13 -> 152:16]** convolution on our network usually has this structure

**[152:17 -> 152:19]** So at the beginning we have the inputs

**[152:19 -> 152:21]** Then we have

**[152:21 -> 152:28]** And we know that linear combination linear combination is again linear function and this is not what we want.

**[152:28 -> 152:33]** So among the layers that are of course also known as linear function.

**[152:33 -> 152:35]** So, we have a solution and layers which are of this type here.

**[152:35 -> 152:40]** middle there are nonlinearities because the operation that we saw are practically all linear,

**[152:41 -> 152:46]** and we know that linear combination, linear combination is again linear function and this

**[152:46 -> 152:52]** is not what we want. So among the layers that are of course also nonlinearities,

**[152:54 -> 153:00]** and then towards the end of the network, only towards the end of the network, we keep

**[153:00 -> 153:03]** both fully connected layers.

**[153:03 -> 153:06]** So there is a big part of the network

**[153:06 -> 153:11]** that is dedicated to sort of what we call feature extraction,

**[153:11 -> 153:15]** feature learning, and then the ending part of the network

**[153:15 -> 153:18]** is dedicated to the model itself.

**[153:18 -> 153:21]** So it's performing classification, regression,

**[153:21 -> 153:24]** with a network of this kind.

**[153:24 -> 153:27]** So the initial part of the network has this form,

**[153:27 -> 153:28]** it's convolutional.

**[153:28 -> 153:31]** The ending part of the network is that fully connected.

**[153:33 -> 153:36]** So you remember we saw that figure

**[153:37 -> 153:40]** where we said we might invest.

**[153:40 -> 153:42]** So you remember we were talking about the iris,

**[153:42 -> 153:43]** the flowers, right?

**[153:43 -> 153:47]** So you can either invest on the representation of data

**[153:47 -> 153:49]** or you can invest on improving the model.

**[153:49 -> 153:53]** Deep network do the two things at the same time.

**[153:53 -> 153:55]** There is an initial part of the network

**[153:55 -> 153:58]** that learns to extract the features.

**[153:58 -> 154:00]** And then there is an ending part of the network

**[154:00 -> 154:05]** that is executing the task itself.

**[154:05 -> 154:07]** So we are doing it in cascade.

**[154:07 -> 154:11]** So initially we extract the feature with convolutional layers,

**[154:11 -> 154:13]** and then we have the fully connected part

**[154:13 -> 154:16]** that makes the predictions.

**[154:16 -> 154:19]** Compositionality is exploited by the convolutional network

**[154:19 -> 154:21]** as we did, translation invariance,

**[154:21 -> 154:24]** all this information, or the structure of the data

**[154:24 -> 154:27]** guided the way which we apply this,

**[154:28 -> 154:31]** and we define the convolutional filters, okay?

**[154:31 -> 154:34]** So yeah, this is the convolutional part,

**[154:34 -> 154:36]** this is the fully connected part.

**[154:37 -> 154:42]** So let's see, when I deal with the fully connected layer,

**[154:43 -> 154:46]** and let's say that I only want to use this kind of layer,

**[154:46 -> 154:49]** so only the fully connected layers.

**[154:49 -> 154:54]** So I say that as star from an image, an RGB image,

**[154:54 -> 154:58]** which is 32 pixels by 32 pixels by three

**[154:58 -> 155:01]** because you have RG and BE, right?

**[155:01 -> 155:03]** So three colors.

**[155:03 -> 155:06]** Then what you need to do, well, fully connected layers

**[155:06 -> 155:09]** are only able to manage vectors.

**[155:09 -> 155:13]** Okay, they cannot capture structure inside the data.

**[155:13 -> 155:15]** They only manage vectors.

**[155:15 -> 155:17]** They have to be playing vectors.

**[155:17 -> 155:19]** So what you need to do is to take an image

**[155:19 -> 155:22]** and stretch it into a long vectors

**[155:22 -> 155:25]** of 3,000, more than 3,000 elements.

**[155:25 -> 155:27]** So this is your vector.

**[155:27 -> 155:30]** Then you have the linear part with a W

**[155:30 -> 155:33]** that multiplies all the elements of the vector.

**[155:33 -> 155:37]** And then you get the, let's say the feature map

**[155:37 -> 155:39]** at the output, right?

**[155:39 -> 155:43]** And if you have, you remember,

**[155:43 -> 155:46]** I mean, we discussed about the fact that

**[155:46 -> 155:48]** you can have the W function.

**[155:48 -> 155:52]** every row has a same dimensionality of the input,

**[155:52 -> 155:54]** but then depending on how many rows you have,

**[155:54 -> 155:56]** you will have as many outputs, right?

**[155:56 -> 156:00]** So now we are thinking about a W of dimension 10 rows.

**[156:00 -> 156:02]** So we have 10 rows, each of the row

**[156:02 -> 156:04]** has the same dimensionality of X.

**[156:04 -> 156:08]** And so we have a vector as an output which has 10 elements,

**[156:10 -> 156:13]** so one number for every multiplication of one row

**[156:13 -> 156:17]** of the W by X, okay?

**[156:17 -> 156:19]** Now, in a convolutional layer,

**[156:19 -> 156:22]** we have a different kind of approach.

**[156:22 -> 156:25]** We have an image and we keep it with the structure.

**[156:25 -> 156:27]** So, you do by 32 by three.

**[156:28 -> 156:30]** Hide, wait and death.

**[156:30 -> 156:32]** The death is three RGB, right?

**[156:32 -> 156:34]** So, we have three modules of three colors.

**[156:34 -> 156:37]** Okay, so now we can preserve this partial structure.

**[156:37 -> 156:40]** And what we do is that we take a filter,

**[156:40 -> 156:42]** or we call kernel, or,

**[156:42 -> 156:44]** and let's say it's up to us.

**[156:44 -> 156:47]** Now it's the designer of the network that chooses

**[156:47 -> 156:50]** the dimensionality of this filter.

**[156:50 -> 156:55]** Now, I mean, we decided to take a filter dimension

**[156:55 -> 156:57]** five by five by three.

**[156:57 -> 157:02]** Now note that five by five is something that we decide,

**[157:02 -> 157:07]** but three, the depth should be the same as the input.

**[157:07 -> 157:09]** Unless we go in more complex model,

**[157:09 -> 157:11]** we can find a different strategy.

**[157:11 -> 157:14]** But for us, let's keep it as a rule.

**[157:14 -> 157:19]** The depth of the filter has to be the same of the input.

**[157:19 -> 157:21]** Five by five is something you can choose,

**[157:21 -> 157:24]** but three, we keep it fixed depending on the input.

**[157:24 -> 157:29]** So now we take this filter and we convolve it over the image.

**[157:30 -> 157:33]** So what we need to do, we have to multiply this

**[157:33 -> 157:34]** with the input.

**[157:34 -> 157:35]** Okay.

**[157:35 -> 157:44]** So, in every position where we apply the filter, we produce one value.

**[157:44 -> 157:46]** It's a dark product.

**[157:46 -> 157:48]** It's just a scalar value.

**[157:48 -> 157:57]** You multiply every element of your filter, which contains your W's, with every element of your input.

**[157:57 -> 158:03]** right? And you obtain a value, it's just a scalar because you do the multiplication and you sum

**[158:03 -> 158:10]** all the values and you get one value. This is the effect of the linear part. Now of course,

**[158:10 -> 158:15]** I'm saying that this window contains only the W but of course you can

**[158:15 -> 158:25]** accompany, let's say, combine every filter with also an extra bias value B, right? Such that your

**[158:25 -> 158:30]** filter now contains 5 by 5 by 3 values W plus the B.

**[158:30 -> 158:35]** Okay, this will be the parameters and this is just operating the linear part of the model.

**[158:36 -> 158:38]** Okay, so executing the dot product plus the bias.

**[158:41 -> 158:47]** Now, then what you do is that you move this window over the input and you obtain every time

**[158:47 -> 158:52]** you obtain a value, then you start the values properly. Of course, this depends on the dimension,

**[158:52 -> 158:57]** The dimension of the output will depend on the dimension of the input and of the filter.

**[158:57 -> 159:02]** And then the way we just start, if you start the little bit outside or you start in the middle,

**[159:02 -> 159:05]** I'm not in the middle, but exactly at the margin or not.

**[159:06 -> 159:13]** And you can have many filters, okay, not only one. So as we saw before, we can have multiples,

**[159:13 -> 159:21]** more Ws, multiples, more kernels. So you can have, let's say, let's call it a blue filter,

**[159:21 -> 159:26]** Then it can have a green filter. I'm just calling it by color. But of course, each of them will

**[159:26 -> 159:31]** capture a different thing. You guys, we saw before, it can be an edge, it can be a blob of color.

**[159:31 -> 159:36]** So each of them will focus on something, right? And you don't know, every only. It will be your

**[159:36 -> 159:43]** network to decide what is the thing that will be included in that filter. By optimizing the network,

**[159:44 -> 159:50]** you will fill in these filters with values with W, with the optimal W. And then when looking back,

**[159:50 -> 159:55]** then you understand what the model is, let's say captured. For the moment it's just a mathematical

**[159:55 -> 160:02]** operation, you are applying the filter over the input and you obtain different outputs.

**[160:02 -> 160:09]** Let's say you applied, I don't know, six filters and then you obtain, I mean, a new feature map

**[160:09 -> 160:18]** that will have dimensionality six in terms of the depth. I remember about it. The number of filters

**[160:18 -> 160:23]** that you apply will decide the depth of the output.

**[160:23 -> 160:26]** And the depth, so this output will be the input

**[160:26 -> 160:28]** of the next layer, right?

**[160:28 -> 160:32]** So the depth of the output piece will depend

**[160:32 -> 160:36]** on how many filters you applied on the input.

**[160:36 -> 160:40]** Then of course, 28 by 28, so this specific dimension

**[160:40 -> 160:43]** will depend on the regional dimensionality,

**[160:43 -> 160:46]** will depend on the size of the kernel,

**[160:46 -> 160:50]** 5 by 5 in our case, and will depend on how you started,

**[160:50 -> 160:53]** so the position where the filter was applied in the first place.

**[160:54 -> 160:59]** So we have six filters and also six values of the bias.

**[160:59 -> 161:02]** So how many parameters do we have?

**[161:02 -> 161:05]** Well, 5 by 5 by 3 by 6.

**[161:05 -> 161:09]** So this is all these filters contain parameters,

**[161:09 -> 161:11]** plus the six dimensional bias values.

**[161:12 -> 161:15]** Okay, so this will be the number of parameters of your layer.

**[161:15 -> 161:18]** if you shape it like this.

**[161:18 -> 161:19]** If you design it like this,

**[161:19 -> 161:21]** then this will be the number of parameters of your model,

**[161:21 -> 161:23]** five by five by three,

**[161:23 -> 161:26]** content of each of these kernel by six,

**[161:26 -> 161:28]** plus the corresponding bias.

**[161:30 -> 161:31]** Okay?

**[161:31 -> 161:34]** But, and actually, so every time you end up

**[161:34 -> 161:37]** producing a feature map,

**[161:37 -> 161:39]** then this feature map will become the,

**[161:39 -> 161:42]** let's say the input for the next layer.

**[161:42 -> 161:44]** And after the convolution,

**[161:44 -> 161:47]** what you do is that usually apply a nonlinearity.

**[161:47 -> 161:51]** So over the output of this linear part,

**[161:51 -> 161:52]** then you apply a nonlinearity.

**[161:52 -> 161:54]** So you might apply a value, right?

**[161:54 -> 161:58]** So if the product produced you somehow a negative value,

**[161:58 -> 162:00]** then it will be moved to zero.

**[162:00 -> 162:03]** If it is positive, it will be capped as it was.

**[162:03 -> 162:06]** This would be the effect of applying nonlinearity

**[162:06 -> 162:08]** as a value function.

**[162:08 -> 162:10]** The shape, of course, will remain the same.

**[162:10 -> 162:12]** It will be applied, let's say, pointwise

**[162:12 -> 162:14]** over the matrix.

**[162:15 -> 162:17]** And then you do it again.

**[162:17 -> 162:19]** So the output of your first layer

**[162:19 -> 162:21]** will become the input of the next layer,

**[162:21 -> 162:22]** and so on and so forth.

**[162:22 -> 162:23]** And every time you have a linear part,

**[162:23 -> 162:26]** which is the convolution and the application

**[162:26 -> 162:27]** of non-linearity.

**[162:28 -> 162:32]** And so then when you go and look at these filters backward,

**[162:32 -> 162:36]** then you can understand what did they actually learn,

**[162:36 -> 162:38]** guys, so which kind of concept they captured.

**[162:40 -> 162:41]** Okay?

**[162:41 -> 162:43]** Yeah, this is just a different visualization,

**[162:43 -> 162:45]** what we had before.

**[162:45 -> 162:48]** The window will start from a matrix seven by seven

**[162:48 -> 162:50]** and a filter three by three.

**[162:50 -> 162:52]** I just progress it, they have to move it.

**[162:52 -> 162:54]** And so it also can obtain,

**[162:54 -> 162:56]** clearly what is the dimension of the object, right?

**[162:56 -> 163:01]** So if I start like this and I move just one pixel at a time,

**[163:01 -> 163:03]** I have three five moves.

**[163:03 -> 163:06]** And so I have five values, right, as output.

**[163:06 -> 163:10]** And then I go one pixel down and I do it like this again.

**[163:10 -> 163:14]** And so I expect so five, or it's also in five vertical,

**[163:14 -> 163:17]** and my output will be five by five, right?

**[163:17 -> 163:18]** As simple as this.

**[163:18 -> 163:20]** And indeed, there is also a formula

**[163:20 -> 163:23]** to get automatically written and doing it by hand.

**[163:23 -> 163:26]** There is a formula that you can apply

**[163:26 -> 163:29]** to understand what will be the dimensionality of the output.

**[163:29 -> 163:33]** So n is the dimensionality of the input.

**[163:33 -> 163:37]** F is the dimensionality of the filter or the kernel.

**[163:37 -> 163:42]** And then divide it by stride, what is stride?

**[163:42 -> 163:45]** The stride is the step you take.

**[163:45 -> 163:49]** It can be of one pixel, it can be of two pixel,

**[163:49 -> 163:50]** so on so forth.

**[163:51 -> 163:54]** And again, the dimensionality of the filter,

**[163:54 -> 163:56]** as well as the dimensionality of the stride

**[163:56 -> 164:00]** is up to the machine learner designer.

**[164:00 -> 164:03]** So who designed the network?

**[164:03 -> 164:06]** Also decided these values that will depend

**[164:06 -> 164:07]** on the kind of data that you have

**[164:07 -> 164:09]** do it and then on the kind of task that you have.

**[164:09 -> 164:12]** But as someone already asked me,

**[164:12 -> 164:15]** there are some backbone architecture

**[164:15 -> 164:18]** that formalizes these choices.

**[164:18 -> 164:21]** And then we can reuse these choices, right?

**[164:21 -> 164:23]** So now we're talking about five by five,

**[164:23 -> 164:24]** we can have three by three,

**[164:24 -> 164:26]** and there are architecture that we use that kind of shape.

**[164:26 -> 164:30]** And then I mean, this has been formalized

**[164:30 -> 164:34]** and we don't have to really think about them from scratch.

**[164:34 -> 164:38]** we can just use choices that have been done in the past.

**[164:38 -> 164:42]** Now, what we have is that the dimensionality

**[164:42 -> 164:46]** by proceeding in this way, we started from seven by seven,

**[164:46 -> 164:50]** we get that five by five, the dimensionality per sale,

**[164:50 -> 164:52]** already the dimensionality of the data shrink,

**[164:52 -> 164:54]** plus we said we want to apply a Boolean.

**[164:54 -> 164:56]** So we have to pay a little bit of attention

**[164:56 -> 165:00]** because we don't want this information to shrink too fast.

**[165:00 -> 165:03]** And to avoid that, we cannot decide

**[165:03 -> 165:06]** to change the stride, so not using one,

**[165:06 -> 165:08]** but using for instance two.

**[165:08 -> 165:12]** So this will allow to have, let's say,

**[165:12 -> 165:13]** a different dimensionality.

**[165:13 -> 165:15]** So of course this goes in the wrong direction,

**[165:15 -> 165:17]** this is shrinking even more.

**[165:17 -> 165:19]** But another thing that you can do

**[165:19 -> 165:21]** will take it back next time.

**[165:21 -> 165:25]** So this will be the last concept I asked you today,

**[165:25 -> 165:27]** because I know you're tired and it's quite late.

**[165:27 -> 165:32]** So one thing that you can do is to add a sort of a frame

**[165:33 -> 165:41]** around the image, right? Full of zeros. And in this case, you will do what we said before,

**[165:41 -> 165:45]** like starting a little bit outside. So you have a sort of margin around the image

**[165:46 -> 165:52]** that helps you to avoid your model to shrink the information too fast. Okay, so there are things

**[165:52 -> 166:01]** that you can decide in this sense. This is called padding. Okay, so when I ask you, what are the

**[166:01 -> 166:10]** choices that one has to make to design a convolutional layer, what are the choices?

**[166:10 -> 166:18]** Dimensionality of the filter, stride and padding mainly, right? So what is the dimensionality of

**[166:18 -> 166:25]** the filter? How it moves and if it starts from the margin or somehow it will be outside.

**[166:25 -> 166:33]** And the margin, I mean this padding can be of one row and one column or it can be of two rows and two columns and so on and so forth.

**[166:33 -> 166:37]** And we can also have the, let's say, formal out of the cloud play it includes.

**[166:37 -> 166:41]** Okay, so we stop here and we will start again next time.

**[166:41 -> 166:49]** This is God's plans.

**[166:49 -> 166:54]** You

