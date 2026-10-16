# Lecture Transcription

- **Source**: `temp_audio_83843.wav`
- **Model**: `base.en`
- **Device**: `mps`

---

**[00:00 -> 00:29]** And over 15 means that the model is memorizing the training data. And so at that time, it will not be able to generalize. So the draining error, you will see that it goes down, right? But the foundation error, so the error that you measure on a new set of samples that you didn't see during training, might start growing.

**[00:30 -> 00:33]** if we provide too much capacity in the model.

**[00:33 -> 00:35]** So it has too much time to learn,

**[00:35 -> 00:39]** if it has only a limited amount of samples to learn on.

**[00:39 -> 00:43]** So it's really, so the limited amount of samples

**[00:43 -> 00:45]** and the big amount of parameters.

**[00:45 -> 00:47]** So this is the effect that we would see.

**[00:47 -> 00:50]** And of course, we would like to avoid it.

**[00:50 -> 00:52]** So we'll find out what you think.

**[00:52 -> 00:55]** And we said that one practical way in which you always

**[00:55 -> 00:59]** have to organize your data when you train a model

**[00:59 -> 01:02]** is that of starting from your deficit

**[01:02 -> 01:04]** and dividing it in three parts.

**[01:04 -> 01:08]** So you have really a cleaning part of the deficit

**[01:08 -> 01:12]** and the test part, which is, let's say set apart,

**[01:12 -> 01:14]** so you don't touch it.

**[01:14 -> 01:18]** And will be the very last part on which you will deploy

**[01:18 -> 01:21]** the model to verify its performance.

**[01:21 -> 01:25]** While the training set itself is generally divided

**[01:25 -> 01:27]** into parts, training and motivation.

**[01:27 -> 01:30]** So you train the model on this part of the data,

**[01:30 -> 01:34]** which means optimizing the parameters

**[01:34 -> 01:37]** to be able to fit where the data,

**[01:37 -> 01:42]** which means you try to minimize the loss, right?

**[01:42 -> 01:47]** So you want to make the minimum number possible mistakes.

**[01:47 -> 01:48]** And then while you're doing that,

**[01:48 -> 01:53]** you verify the performance on this validation cycle.

**[01:53 -> 01:55]** And it is the performance of this unitization

**[01:55 -> 01:59]** that also guides you to take some decision

**[01:59 -> 02:01]** on some hyperparameters of the model.

**[02:01 -> 02:05]** So you will see, say, multiple times.

**[02:05 -> 02:08]** So inside the model, you will have training parameters,

**[02:08 -> 02:10]** which are either one with your eyes.

**[02:10 -> 02:13]** But there are also some hyperparameters,

**[02:13 -> 02:16]** which are instead the ones that you set by hand

**[02:16 -> 02:18]** during the optimization.

**[02:18 -> 02:21]** And so you want to check how to set the spallinger

**[02:21 -> 02:23]** and do the sides on the wings of what you see,

**[02:23 -> 02:25]** the performance of the elevation.

**[02:25 -> 02:27]** And just a minute ahead.

**[02:29 -> 02:31]** Okay, so...

**[02:35 -> 02:37]** And we said how do we do that?

**[02:37 -> 02:41]** Well, we can just do it in the way we saw it here.

**[02:41 -> 02:47]** Or we can divide the phosphorylation part, so the training part in the southwards.

**[02:47 -> 02:52]** Training, for instance, in this case, and three of them, test the fourth, and then you do it in round.

**[02:52 -> 02:59]** and you might have your K-fold coordination, where K is a number of soft moves that you

**[02:59 -> 03:08]** created. And you can also, if you have N examples, you can also decide to train N-1 and test

**[03:08 -> 03:14]** your summer. And it is called really one-hour cross-dimensional force. And you usually put,

**[03:14 -> 03:21]** when do you expect to use leave one-hour cross-formation? So just keeping one sample out. Do you think

**[03:21 -> 03:23]** some specific conditions.

**[03:23 -> 03:26]** In the setting of your data, there

**[03:26 -> 03:30]** guides you to choose this kind of setting,

**[03:30 -> 03:32]** believing just one sample out.

**[03:38 -> 03:39]** When you have this number.

**[03:39 -> 03:43]** So we already said that this kind of setting

**[03:43 -> 03:44]** is when you have an each algorithm.

**[03:44 -> 03:48]** If you have enough data, that will keep one part, one

**[03:48 -> 03:51]** But if you have an significant amount of samples,

**[03:51 -> 03:54]** a better group, and if it's very few,

**[03:54 -> 03:56]** then you just keep one sample out.

**[03:56 -> 04:01]** And actually, these kind of settings,

**[04:01 -> 04:04]** so the error, yeah, I'm just single-tempered.

**[04:04 -> 04:06]** The outcome, the average and the error,

**[04:06 -> 04:12]** is an unbiased estimator of the generalization error

**[04:12 -> 04:13]** of the model.

**[04:13 -> 04:18]** So it gets really close to what we expect to see as two weeks.

**[04:18 -> 04:22]** So there are some, uh, teary-remy, demonstrate.

**[04:22 -> 04:26]** So this is a tool that we really want to be, uh,

**[04:26 -> 04:28]** as precise as possible or even, uh,

**[04:28 -> 04:32]** evaluating the, the abilities of your model to generalize

**[04:32 -> 04:33]** running cycles.

**[04:33 -> 04:35]** So even if you have a lot of sample,

**[04:35 -> 04:37]** you don't do that, but of course, you don't do that, right?

**[04:37 -> 04:41]** So it's time to keep time centered on it.

**[04:41 -> 04:43]** Okay, so, uh, this is, let's say, the procedure

**[04:43 -> 04:47]** that we, uh, find, um, yeah.

**[04:47 -> 04:52]** So of course, in general, if you keep a test set that is very, very small,

**[04:52 -> 04:58]** then when you finally deploy a model and just try to verify the performance there,

**[04:58 -> 05:01]** then you might not have to know the support of statistics.

**[05:01 -> 05:04]** So you might see that the error.

**[05:04 -> 05:09]** So you cannot really make a final statement about the model because it might be

**[05:09 -> 05:13]** something fluctuation without due to how to do something.

**[05:13 -> 05:17]** to better have a reasonable amount,

**[05:17 -> 05:20]** for example, here, so you can divide your data

**[05:20 -> 05:24]** into a particular thing in your list.

**[05:24 -> 05:27]** And in general, this procedure is also

**[05:27 -> 05:30]** called model selection, exactly because you are actually

**[05:30 -> 05:34]** selecting some hyperparameters.

**[05:34 -> 05:37]** Inside your model, so we said, what is a model, right?

**[05:37 -> 05:40]** So you have your delta, which is x.

**[05:40 -> 05:42]** You have your output, which is y.

**[05:42 -> 05:46]** You have a function that brings you from x to y.

**[05:46 -> 05:50]** And your function f, depends on some parameters.

**[05:50 -> 05:53]** And these are the parameters you want to optimize.

**[05:53 -> 05:56]** So these are, you train your model

**[05:56 -> 05:57]** to optimize your parameters.

**[05:57 -> 06:00]** But inside the model, there can be also

**[06:00 -> 06:03]** other set of parameters that you have to choose by n.

**[06:03 -> 06:05]** Those are called hyper parameters.

**[06:05 -> 06:08]** And those are the ones that you are selecting.

**[06:08 -> 06:11]** But you can also think at a more higher level.

**[06:11 -> 06:14]** So the function itself, so the shape of the function,

**[06:14 -> 06:16]** it might be the form of the function,

**[06:16 -> 06:19]** it's gonna be something you have to select, right?

**[06:19 -> 06:19]** Since that would be.

**[06:19 -> 06:22]** So even choosing the form of the function

**[06:22 -> 06:25]** is something that you can, let's say,

**[06:25 -> 06:27]** do through cross-validation.

**[06:27 -> 06:31]** I see that there are final questions on each other.

**[06:35 -> 06:37]** I don't know what's happening with the audio,

**[06:37 -> 06:39]** but I don't know.

**[06:41 -> 06:43]** Do I need a straight two-foot water?

**[06:43 -> 06:44]** Please.

**[06:48 -> 06:49]** Okay.

**[06:49 -> 06:50]** Okay.

**[06:54 -> 06:55]** Yeah.

**[06:55 -> 06:56]** Yeah.

**[06:56 -> 06:57]** Water?

**[06:57 -> 06:58]** Water?

**[06:58 -> 06:59]** Yeah.

**[06:59 -> 07:00]** Water?

**[07:00 -> 07:01]** Water?

**[07:01 -> 07:02]** Water?

**[07:02 -> 07:03]** Water?

**[07:03 -> 07:04]** Water?

**[07:04 -> 07:05]** Water?

**[07:05 -> 07:06]** Water?

**[07:06 -> 07:07]** Water?

**[07:07 -> 07:08]** Water?

**[07:08 -> 07:09]** Water?

**[07:09 -> 07:10]** Water?

**[07:10 -> 07:39]** I don't know if it's better now.

**[07:39 -> 07:41]** Okay, great.

**[07:41 -> 07:44]** Okay, so now we have just this.

**[07:44 -> 07:45]** Good.

**[07:45 -> 07:46]** Okay.

**[07:46 -> 07:47]** So.

**[07:47 -> 07:50]** And we said that.

**[07:50 -> 07:57]** Of course you might have your model which is quite complex.

**[07:57 -> 08:02]** You can increase the number of parameters that you are doing in your model.

**[08:02 -> 08:05]** she's quite complex.

**[08:05 -> 08:07]** You can increase the number of parameters

**[08:07 -> 08:09]** that you are in your model, and that makes your model

**[08:09 -> 08:12]** more complex.

**[08:12 -> 08:17]** But I think a complex model means that you have a higher risk

**[08:17 -> 08:18]** to repeat, right?

**[08:18 -> 08:21]** So you remember the plot.

**[08:21 -> 08:24]** And yeah, of course, this provides you, by the way,

**[08:24 -> 08:27]** to reduce the empirical risk.

**[08:27 -> 08:31]** But it doesn't mean that you get close to the true risk.

**[08:31 -> 08:34]** And in general, although you can be tempted,

**[08:34 -> 08:39]** you should never use the test set to select

**[08:39 -> 08:44]** or to adopt your model because that is really cheating.

**[08:44 -> 08:48]** It means that anyway, you are not estimating correctly,

**[08:48 -> 08:51]** estimating correctly the way in which the model is working

**[08:51 -> 08:54]** or the ability to generalize the model.

**[08:54 -> 08:55]** So never use the test set.

**[08:55 -> 08:58]** Always make sure to have a separate set

**[08:58 -> 09:00]** on which you're only after the model selection,

**[09:00 -> 09:03]** you show and you evaluate your sets

**[09:03 -> 09:05]** the performance of your model.

**[09:05 -> 09:10]** Now, we said you might increase the complexity of the model,

**[09:10 -> 09:11]** but increasing the complexity of the model

**[09:11 -> 09:13]** might be towards fitting.

**[09:13 -> 09:17]** And so one way to avoid it, we said,

**[09:17 -> 09:19]** do proper cross validation.

**[09:19 -> 09:23]** And the other thing you can do is

**[09:23 -> 09:26]** try to regularize the model to avoid the fitting.

**[09:26 -> 09:30]** So another solution to avoid this kind of issue.

**[09:30 -> 09:33]** And does it mean that we're going to rise a model?

**[09:33 -> 09:35]** It means trying to avoid it,

**[09:35 -> 09:38]** that the body itself has begun to complex.

**[09:38 -> 09:43]** And this is connected to what is called the Occam razor.

**[09:43 -> 09:47]** So Mr. William Hong Kong will say that a short explanation

**[09:47 -> 09:50]** is always preferred over a longer one.

**[09:50 -> 09:53]** It is generally remembered as the Occam razor,

**[09:53 -> 09:57]** but actually something that goes back to ancient laws

**[09:57 -> 09:59]** of verse much more important.

**[09:59 -> 10:02]** But in general, the idea is that we

**[10:02 -> 10:05]** want to have not only a good explanation,

**[10:05 -> 10:07]** so not only a good model, but a model

**[10:07 -> 10:09]** that at the same time is not too complex.

**[10:09 -> 10:13]** And this introduces, I mean, this condition that we are having,

**[10:13 -> 10:16]** it's, we can practically introduce

**[10:16 -> 10:17]** a penalization in the model, which

**[10:17 -> 10:19]** is called the realization.

**[10:19 -> 10:21]** So it's strategy to rewrite the model,

**[10:21 -> 10:24]** that avoid the complexity of the model to grow to match.

**[10:24 -> 10:29]** And so reduces the risk of over-fitting.

**[10:29 -> 10:34]** Okay, so let's see a practical way to introduce this

**[10:37 -> 10:38]** regularization.

**[10:38 -> 10:40]** There are many strategies to memorize a model,

**[10:40 -> 10:43]** but one, I mean, the immediate one is really just

**[10:43 -> 10:47]** to introduce something to penalize the activation process

**[10:47 -> 10:51]** and to guide the selection of the model

**[10:51 -> 10:54]** in terms of the parameters that can be there.

**[10:55 -> 10:58]** Okay, so let's see that we have a training set

**[10:58 -> 11:02]** with N samples, and we are searching for this model age

**[11:02 -> 11:04]** that will solve the task.

**[11:04 -> 11:06]** And we measure the empirical risk, right?

**[11:06 -> 11:09]** So which means out of the N model,

**[11:09 -> 11:11]** we've come how many errors we are

**[11:11 -> 11:15]** and when we stake the model is doing.

**[11:15 -> 11:19]** So prediction of our model will come from any times

**[11:19 -> 11:22]** it is different with respect to the ground truth.

**[11:22 -> 11:27]** So assigning the wrong label to the sample X.

**[11:27 -> 11:29]** And we actually, what we're doing is searching for the model

**[11:29 -> 11:33]** that minimizes this global loss and this cost term,

**[11:33 -> 11:39]** which is indeed the empirical risk minimization.

**[11:39 -> 11:42]** What we can do to summarize the model

**[11:42 -> 11:47]** is to add an extra term that takes under control

**[11:47 -> 11:50]** the complexity of the model, which

**[11:50 -> 11:53]** means that I will search for the model that not only

**[11:53 -> 11:56]** reduces the number of error on the training set,

**[11:56 -> 11:59]** but also has a low complexity.

**[11:59 -> 12:04]** And these two terms, they are combined in Arabic

**[12:04 -> 12:08]** with a weight here, that we call it lambda.

**[12:08 -> 12:13]** And this is the first example of what we can call hyperparameter.

**[12:13 -> 12:18]** Because inside here, we have a function H

**[12:18 -> 12:20]** that will depend on a set of parameters

**[12:20 -> 12:23]** that the model will try to optimize.

**[12:23 -> 12:24]** And the same was here.

**[12:24 -> 12:25]** It was H, rule of the bare known,

**[12:25 -> 12:27]** the same set of parameters.

**[12:27 -> 12:30]** But this thing we hear is something

**[12:30 -> 12:31]** that we usually set by hand,

**[12:31 -> 12:34]** and we can choose it on the basis of the performance

**[12:34 -> 12:36]** that we see on the validation

**[12:36 -> 12:38]** and through the cross-validation.

**[12:39 -> 12:41]** It only goes, I mean, these two terms

**[12:41 -> 12:44]** might not, might live in two different region of the space,

**[12:44 -> 12:44]** right?

**[12:44 -> 12:46]** So I mean, you can be, you know, the first term,

**[12:46 -> 12:48]** can be very big, the second term can be very small,

**[12:48 -> 12:51]** so you need something to revise the two parts.

**[12:51 -> 12:57]** So, yeah, so many cross-validation to choose this lambda.

**[12:57 -> 13:01]** But in practice, we are regularizing the model in this sense,

**[13:01 -> 13:07]** adding the to the loss, a term that quantifies the complexity of the model.

**[13:07 -> 13:11]** So now let's see a practical example of what does it mean.

**[13:11 -> 13:14]** I suppose that you'll know in your regression, right?

**[13:14 -> 13:19]** So regression, as we said, is different from classification.

**[13:19 -> 13:22]** what you have is a prediction of a continuous menu

**[13:22 -> 13:25]** rather than a new goal, right?

**[13:25 -> 13:27]** And in particular linear classification

**[13:27 -> 13:30]** that linear regression is the pure critical line

**[13:30 -> 13:32]** on the data, okay?

**[13:32 -> 13:34]** So, till now we have been talking

**[13:34 -> 13:36]** of classification problems,

**[13:36 -> 13:38]** but we can always have a regression

**[13:38 -> 13:41]** where the output is available in Q1

**[13:41 -> 13:44]** or in general it's in the real domain,

**[13:44 -> 13:46]** the use of the real domain.

**[13:46 -> 13:48]** And we want to measure and get the ability of this model

**[13:48 -> 13:49]** to make the correct prediction.

**[13:49 -> 13:54]** Now evaluating the error in this sense

**[13:54 -> 13:57]** doesn't make much sense in the regression context

**[13:57 -> 13:59]** because now the label itself,

**[13:59 -> 14:02]** so it's not just difference in the name,

**[14:02 -> 14:03]** it's not just the discrete name,

**[14:03 -> 14:06]** so doesn't mention thoughts

**[14:06 -> 14:08]** because what we need to do instead

**[14:08 -> 14:11]** is compare two continuous variable, right?

**[14:11 -> 14:14]** So the exact function of the loss

**[14:14 -> 14:17]** will not be any more at zero one loss

**[14:17 -> 14:21]** that's what we saw last time, but we'll have a different shape.

**[14:21 -> 14:23]** But when we are trying to do the same thing,

**[14:23 -> 14:26]** we want to minimize the loss, which we know,

**[14:26 -> 14:31]** and in theory, what we like to do is minimize the risk

**[14:31 -> 14:33]** that we don't have access to.

**[14:33 -> 14:34]** So we'll just focus on the loss itself.

**[14:34 -> 14:37]** So how do we write the loss?

**[14:37 -> 14:42]** It's not anymore these kind of loss, a 0, 1 loss.

**[14:42 -> 14:44]** But it will be something like this.

**[14:44 -> 14:47]** So a really continuous difference,

**[14:47 -> 14:49]** because these are two continuous values.

**[14:49 -> 14:53]** And this is a simple mean square error, right?

**[14:53 -> 14:56]** So we adjust the volume of the difference between two values

**[14:56 -> 14:58]** and taking it squared because then we

**[14:58 -> 15:01]** have always positive values and we like it more.

**[15:01 -> 15:05]** OK, so of course it's not only a possible choice.

**[15:05 -> 15:08]** We might have a different kind of formalization for the loss.

**[15:08 -> 15:12]** This is another two, but we might have an L1 and so on,

**[15:12 -> 15:15]** so our other kind of losses.

**[15:15 -> 15:17]** And in general, so this tells you

**[15:17 -> 15:21]** that the way in which I write the loss function,

**[15:21 -> 15:25]** so the cost of the mistake, will depend

**[15:25 -> 15:28]** on the task that I'm using, and then focusing on.

**[15:28 -> 15:34]** So this means that during the pre-representation,

**[15:34 -> 15:36]** if I tell you, if I ask you which loss

**[15:36 -> 15:40]** did the old reuse, you have to know, right?

**[15:40 -> 15:43]** So sometimes, in the paper, you will see something

**[15:43 -> 15:47]** We can cross-entropy laws or L2 laws,

**[15:47 -> 15:49]** but it's written out in text.

**[15:49 -> 15:51]** I want to see the laws in the article,

**[15:51 -> 15:55]** because I want you to look at which laws have been optimized.

**[15:55 -> 15:59]** So try to understand what does this law say?

**[15:59 -> 16:01]** What is this term?

**[16:01 -> 16:03]** What are the authors trying to minimize?

**[16:03 -> 16:04]** What is the objective?

**[16:04 -> 16:07]** It is an important part, because it tells you

**[16:07 -> 16:11]** what I'm really trying to obtain with my model.

**[16:11 -> 16:15]** So always search for this keyword and try to identify

**[16:15 -> 16:19]** what the authors are trying to minimize.

**[16:19 -> 16:22]** So that's the objective that guide my training,

**[16:22 -> 16:23]** the training woman of.

**[16:24 -> 16:28]** Okay, so now we have our training sample sets,

**[16:28 -> 16:30]** let's say a non-pointed N, but okay,

**[16:30 -> 16:34]** so this is the number of samples that I have.

**[16:34 -> 16:37]** And I'm supposing them, so this is,

**[16:37 -> 16:38]** let's say somehow my prior,

**[16:38 -> 16:42]** because I said I want to perform a linear regression,

**[16:42 -> 16:44]** that the model has this shape, right?

**[16:44 -> 16:46]** So it's a line.

**[16:46 -> 16:50]** So I will take the input x, and I will have two parameters,

**[16:50 -> 16:52]** which are the slope of the line,

**[16:52 -> 16:54]** and the point in which the line intercepts

**[16:54 -> 16:59]** and pass through the y-axis.

**[16:59 -> 17:04]** So this is a paramagnetic model, right?

**[17:04 -> 17:06]** It depends on the optimal mean.

**[17:06 -> 17:09]** Okay? And now, so now what do we have to do?

**[17:09 -> 17:11]** So we write down the loss function,

**[17:11 -> 17:14]** so which counts how many errors my model is doing.

**[17:14 -> 17:16]** And then trying to search for that when

**[17:16 -> 17:19]** the e- that really minimizes this loss.

**[17:19 -> 17:22]** So that's what linear regression is doing,

**[17:22 -> 17:23]** not more than that.

**[17:23 -> 17:26]** So we have this least square minimization.

**[17:26 -> 17:28]** So we're trying to minimize the critical loss,

**[17:28 -> 17:30]** because of the square loss,

**[17:30 -> 17:33]** so we will move it forward as we are to learn,

**[17:33 -> 17:36]** and we apply the implementation.

**[17:36 -> 17:38]** So this is very simple steps.

**[17:38 -> 17:40]** This is what I find to predict, right?

**[17:40 -> 17:45]** So my important is class is the family of lines,

**[17:45 -> 17:48]** defined by this set of parameters, right?

**[17:48 -> 17:54]** And, and yeah, in practice, I'm trying to read the line.

**[17:54 -> 17:56]** So these are my points.

**[17:56 -> 17:59]** I have for each of the small, I have x and I have the y,

**[17:59 -> 18:03]** and I minimize the loss such that they get a line,

**[18:03 -> 18:06]** that really minimizes this discrepancy between what I predict,

**[18:06 -> 18:08]** which, why, and the correct why.

**[18:08 -> 18:11]** So the prediction on the law of the values, of course,

**[18:11 -> 18:12]** this one, right?

**[18:12 -> 18:13]** And the product is this one.

**[18:13 -> 18:16]** So the first one on the y-axis.

**[18:16 -> 18:20]** And I'm trying to minimize this distance squared.

**[18:20 -> 18:23]** Such that, at that point, I will be

**[18:23 -> 18:27]** able to tell what is the correct corresponding

**[18:27 -> 18:30]** to why they do.

**[18:30 -> 18:33]** Of course, I mean, we can leave an two-dimensional space.

**[18:33 -> 18:35]** We can leave an higher dimensional space.

**[18:35 -> 18:40]** In case of 3D space, this depends on how many value the x

**[18:40 -> 18:43]** is composed of.

**[18:43 -> 18:45]** So x is my input.

**[18:45 -> 18:48]** And it can actually, it's a mode.

**[18:48 -> 18:49]** So it's a vector.

**[18:49 -> 18:52]** First, we're saying that it's just composed by one value,

**[18:52 -> 18:53]** exactly.

**[18:53 -> 18:57]** But it can also be composed of two values, the x1 and x2,

**[18:57 -> 19:00]** and the y's and the third axis and so on and so forth.

**[19:00 -> 19:05]** So here we have practically the vectors, so x is a vector,

**[19:05 -> 19:08]** and w, sort of a set of parameters we're searching for,

**[19:08 -> 19:12]** one of the parameters that is itself a vector.

**[19:12 -> 19:16]** So we are just a dot product, but this is two vectors,

**[19:16 -> 19:18]** and then we have a coefficient V.

**[19:18 -> 19:20]** OK, so this is what we're searching for.

**[19:20 -> 19:24]** My model depends on this set of parameters,

**[19:24 -> 19:26]** and I have to search for V and W

**[19:26 -> 19:29]** that minimizes the scree loss.

**[19:29 -> 19:30]** Perfect.

**[19:30 -> 19:35]** So yeah, this is what I'm trying to minimize.

**[19:35 -> 19:40]** And since it's a vector, we can write the equation down

**[19:40 -> 19:43]** in the total terms and in matrix terms.

**[19:43 -> 19:47]** So we have a set of data, right?

**[19:47 -> 19:51]** So n in the samples, we are stuck in the in- out matrix.

**[19:51 -> 19:55]** So one vector of the other, right?

**[19:55 -> 19:57]** And this is the corresponding y.

**[19:57 -> 20:00]** So we are just writing this, which was the last, right?

**[20:00 -> 20:04]** So y minus what my model predicts.

**[20:04 -> 20:07]** The square is just a summation.

**[20:07 -> 20:09]** We can write down a partial form.

**[20:09 -> 20:13]** So we are taking this vector here, minus.

**[20:13 -> 20:17]** And this is just a matrix where we are sucking a column of 1s

**[20:17 -> 20:20]** plus the x that is here.

**[20:20 -> 20:23]** And here I have a b at the beginning and just the down

**[20:23 -> 20:29]** back. Since I mean if you do it like this, the first column is 1x, you multiply by the

**[20:29 -> 20:34]** column bw, so you will have b and the value multiplied by the remaining part of the x.

**[20:34 -> 20:40]** So it's just a geometric way to calculate the problem.

**[20:40 -> 20:46]** And so at the end you end up writing it down like this, right? Because you can also rename

**[20:46 -> 20:53]** this function at least marked simply as x. And these you can simply call it w, okay?

**[20:53 -> 21:00]** So you are in, it's including b inside the w, including one inside the x. And you have

**[21:00 -> 21:07]** this very simple expression. It's a very simple expression which is convex. So if you

**[21:07 -> 21:12]** look at the formula itself, you can see that it's a parabola, right? Because I mean square,

**[21:12 -> 21:16]** squared, it's just different, it's very, very simple.

**[21:16 -> 21:19]** And whenever we have convex function,

**[21:19 -> 21:21]** we know that we can find a minimum.

**[21:21 -> 21:24]** So the base of the Jensen-Mian body,

**[21:24 -> 21:28]** we know that this is the shape of the convex function.

**[21:28 -> 21:30]** So we will always be able to find a minimum.

**[21:30 -> 21:34]** And this block we are trying to do with our utilization

**[21:34 -> 21:35]** of our series.

**[21:35 -> 21:36]** Now, pay attention.

**[21:36 -> 21:38]** This is very simple.

**[21:38 -> 21:39]** It's a convex function.

**[21:39 -> 21:43]** When we deal with these models, most of the cases

**[21:43 -> 21:45]** develop to a monthly complex.

**[21:45 -> 21:49]** And we'll need to hack our way through to find a minimum.

**[21:49 -> 21:52]** And generally, the function will have only one minimum,

**[21:52 -> 21:53]** like in this case.

**[21:53 -> 21:55]** There are many of them.

**[21:55 -> 21:58]** So you also have to understand if you really

**[21:58 -> 22:01]** got to a good minimum or not.

**[22:01 -> 22:02]** So it could be more complex.

**[22:02 -> 22:05]** Now, if everything's super simplified,

**[22:05 -> 22:08]** then just it will go through the procedure.

**[22:08 -> 22:12]** Okay, so this is a special, what you have to do with the minimum,

**[22:12 -> 22:14]** you just have to take the derivative,

**[22:14 -> 22:15]** and then I put the derivative, and then I put the derivative,

**[22:15 -> 22:19]** and I put the zero, and this ends up by just,

**[22:19 -> 22:22]** I mean, you can be solved in code four,

**[22:22 -> 22:24]** which means that just from the mathematics,

**[22:24 -> 22:27]** just putting inside the values of x and y,

**[22:27 -> 22:30]** you can find an optimal value.

**[22:30 -> 22:34]** So the one that produces the minimum for your function.

**[22:34 -> 22:37]** So the optimal, which provides you with the optimal classifier,

**[22:37 -> 22:40]** the optimal regressor in this case.

**[22:40 -> 22:43]** So it's just inverting these, putting it

**[22:43 -> 22:46]** on the middle of it, say it's just the inversion.

**[22:46 -> 22:48]** And you have an expression.

**[22:48 -> 22:50]** Of course, you can do it also explicitly

**[22:50 -> 22:52]** known as the enrollment ratio term.

**[22:52 -> 22:54]** And expression would be the same.

**[22:54 -> 22:57]** So now it's written, it's pleasingly with a summation

**[22:57 -> 23:02]** rather than being written in the moment ratio form.

**[23:02 -> 23:06]** And everything was the reason without the input in the B

**[23:06 -> 23:08]** and the one in the x, but when you put,

**[23:08 -> 23:13]** I mean, you re-exclusively expose the one in the B,

**[23:13 -> 23:16]** practical it's not changing that much.

**[23:16 -> 23:18]** So the W is expressed like this,

**[23:18 -> 23:22]** summation of xi yi divided by the summation of xi squared.

**[23:22 -> 23:25]** And if you get back to that, it's this expression

**[23:25 -> 23:30]** where you're practically subtracting to the yi,

**[23:30 -> 23:32]** a coefficient of w squared,

**[23:32 -> 23:35]** because you have another, it will be the B paper, right?

**[23:35 -> 23:39]** So it's a W vector plus a W0 from which corresponds

**[23:39 -> 23:42]** to what you want to search for the region.

**[23:42 -> 23:44]** OK, so this is just very monomeratic apart.

**[23:44 -> 23:46]** But at the end, what we have is that we are trying

**[23:46 -> 23:48]** to minimize this.

**[23:48 -> 23:52]** So now, my point is I want to regularize the model.

**[23:52 -> 23:55]** So we said we want you to do some polarization.

**[23:55 -> 23:56]** So what do we do?

**[23:56 -> 24:00]** Together with this loss, we add the null return.

**[24:00 -> 24:06]** We remember it was plus lambda, the complexity of the model.

**[24:06 -> 24:09]** And now in our case, the model is defined by wv.

**[24:09 -> 24:13]** We are just forgetting about v.

**[24:13 -> 24:16]** Let's say that all the parameters are inside the value.

**[24:16 -> 24:20]** So I want to minimize the complexity of the model.

**[24:20 -> 24:21]** What do I ask?

**[24:21 -> 24:27]** I ask that the vector w itself should have a more norm.

**[24:27 -> 24:31]** This is the way in which I'm introducing a regularization

**[24:31 -> 24:36]** term to avoid the model to be too complex.

**[24:36 -> 24:41]** So I say, you are searching for the model y equal dot

**[24:41 -> 24:42]** to x.

**[24:42 -> 24:44]** So it's simple in a model.

**[24:44 -> 24:46]** This dot will, I mean, this model.

**[24:46 -> 24:50]** Not only has to minimize the error on the training set,

**[24:50 -> 24:54]** but also on the constraint that the norm of the vector

**[24:54 -> 24:56]** W has to be small.

**[24:56 -> 24:57]** Because when I minimize this, I'm just

**[24:57 -> 25:01]** saying the L2 norm of that will is a term.

**[25:01 -> 25:04]** Has to be small, how can we minimize it?

**[25:04 -> 25:07]** So I'm just adding an extra term.

**[25:07 -> 25:10]** And this is called rich regression,

**[25:10 -> 25:14]** just the name that we assign when we add this condition

**[25:14 -> 25:16]** on the complex.

**[25:16 -> 25:19]** So it's just an explicit way to see what we mean

**[25:19 -> 25:21]** with the polarization.

**[25:21 -> 25:23]** And the solution will be the same.

**[25:23 -> 25:27]** In the end, you can still solve it with this extra curve.

**[25:27 -> 25:30]** And alpha will be a hyper parameter

**[25:30 -> 25:34]** that you need to optimize to choose from cross-frontation.

**[25:38 -> 25:42]** Now, the same logic can be applied

**[25:42 -> 25:45]** even if your model is not being linear,

**[25:45 -> 25:48]** but if you might have a polynomial.

**[25:48 -> 25:52]** Because I mean, the model itself in this case

**[25:52 -> 25:56]** will not be linear in terms of x.

**[25:56 -> 25:59]** But what we care about is the linearity

**[25:59 -> 26:00]** with respect to the fun here.

**[26:00 -> 26:03]** So the b and the dot.

**[26:03 -> 26:07]** With respect to then, which is what we are searching for,

**[26:07 -> 26:09]** the model is still linear.

**[26:09 -> 26:14]** So the function itself is f or h, f and b4.

**[26:14 -> 26:16]** It can be as complex as we want.

**[26:16 -> 26:21]** But in theory, we can still, this is our goal,

**[26:21 -> 26:25]** the regression, we can still apply the same logic

**[26:25 -> 26:27]** to so in the steps we saw before.

**[26:27 -> 26:29]** Because at the end, it's just a matter

**[26:29 -> 26:31]** of introducing a general function here,

**[26:31 -> 26:34]** and you see you can still treat the whole procedure

**[26:34 -> 26:37]** in what you're doing for, and so on and so forth.

**[26:37 -> 26:40]** And the goal will be always the same, right?

**[26:40 -> 26:42]** Anyways, searching for the doubt,

**[26:42 -> 26:46]** right, the second plan, and the third is something

**[26:46 -> 26:50]** you can see it's all the inkles for it.

**[26:50 -> 26:54]** OK, so yeah, so this was just summarizing

**[26:54 -> 26:57]** what is so deep here, so a pack, a product

**[26:57 -> 27:01]** that approximately I regret, what is overpitting and repeating,

**[27:01 -> 27:03]** what is cost of relation, and what does

**[27:03 -> 27:07]** mean to memorize the model by the example of the regression.

**[27:11 -> 27:15]** So now, this was just closing the depth of line

**[27:15 -> 27:16]** we saw last time.

**[27:16 -> 27:22]** So I hope that the concept of overfitting and underfitting,

**[27:22 -> 27:27]** the concept of loss, the concept of regularization

**[27:27 -> 27:28]** are clear.

**[27:28 -> 27:30]** If not, raise your hand.

**[27:30 -> 27:37]** Ask questions, because these are important concepts.

**[27:37 -> 27:39]** The kind of things I would generally always ask a big sound.

**[27:39 -> 27:42]** There is a loss, but I was poor looking,

**[27:42 -> 27:43]** and then on the people.

**[27:43 -> 27:45]** What does it mean to verbalize them all?

**[27:45 -> 27:48]** And now it's one way to verbalize them all,

**[27:48 -> 27:50]** by adopting the term of the false.

**[27:50 -> 27:51]** But there are other strategies.

**[27:51 -> 27:54]** And we will see that.

**[27:54 -> 27:56]** So I'll change that slide.

**[27:56 -> 27:57]** And meanwhile, if you have questions,

**[27:57 -> 27:58]** I'll answer them.

**[29:12 -> 29:18]** So there was a question here in the chart that the error could have a different form and not be always a problem, exactly.

**[29:18 -> 29:22]** So the last function that we wrote here was a very simple one.

**[29:22 -> 29:28]** And his complex, and it's very simple to minimize, but it's not always the case.

**[29:28 -> 29:35]** So when we will have more complex problems, the form of the loss will be much more complex and not necessarily complex.

**[29:35 -> 29:39]** So it will be more challenging to minimize.

**[29:39 -> 29:43]** We will start entering into this movie with an inspired

**[29:43 -> 29:45]** of the texture.

**[29:45 -> 29:48]** So I was answering the question in the chat.

**[29:54 -> 29:54]** Good.

**[29:54 -> 29:56]** So we go ahead now.

**[29:56 -> 30:01]** So we have been dealing with linear regression.

**[30:01 -> 30:06]** But then I want to understand if I could use a regression

**[30:06 -> 30:10]** model to perform classification.

**[30:10 -> 30:17]** And we will see where it brings this kind of task.

**[30:17 -> 30:22]** So because, of course, at the end, in many cases,

**[30:22 -> 30:25]** even if your prediction is a continuous value,

**[30:25 -> 30:27]** we might want to take a final decision,

**[30:27 -> 30:29]** maybe it's just a binary decision.

**[30:29 -> 30:33]** Like, is there a two more or not in this image,

**[30:33 -> 30:35]** medical, which is right?

**[30:35 -> 30:42]** So what you can do is try to apply some post processing.

**[30:42 -> 30:46]** So you look at the values and you put a threshold.

**[30:46 -> 30:49]** But this is not necessarily the optimal solution.

**[30:49 -> 30:52]** I mean, your model was a region optimized with regression.

**[30:52 -> 30:54]** Now you are applying something over it

**[30:54 -> 30:56]** to take a binary decision.

**[30:56 -> 30:59]** But instead, what we want to do is try to understand

**[30:59 -> 31:03]** if we can use a continuous prediction directly

**[31:03 -> 31:06]** to be optimized for a category called prediction on foot.

**[31:06 -> 31:13]** And I guess you can guess what is the logic here.

**[31:13 -> 31:15]** Think about binary prediction.

**[31:15 -> 31:19]** Then maybe the continuous value represents a probability.

**[31:19 -> 31:20]** So if it represents a probability,

**[31:20 -> 31:22]** then I can take it this year.

**[31:22 -> 31:26]** Maybe it's just optimized to have a probability which

**[31:26 -> 31:29]** is higher than 0, 5 if the number is there or not.

**[31:29 -> 31:33]** So this continuous behavior now we try to predict,

**[31:33 -> 31:38]** we would like it to behave as a probability.

**[31:39 -> 31:41]** Okay, so what can we do?

**[31:41 -> 31:45]** Well, we move towards what is called logistic regression.

**[31:45 -> 31:47]** So it's still regression,

**[31:47 -> 31:49]** we're still predicting a continuous behavior,

**[31:49 -> 31:53]** but now we change something.

**[31:53 -> 31:54]** What do we change?

**[31:54 -> 31:59]** Well, before we had H of X, right,

**[31:59 -> 32:03]** a generic function for classification for the regression.

**[32:03 -> 32:06]** Now we are explicitly writing it like this.

**[32:06 -> 32:08]** We have a linear part like before.

**[32:08 -> 32:10]** It was wx plus b.

**[32:10 -> 32:13]** Now it's written as a x plus b.

**[32:13 -> 32:14]** But you have a linear part.

**[32:14 -> 32:20]** And you are adding all the linear part and nonlinear function.

**[32:20 -> 32:22]** This, which is called sigma.

**[32:22 -> 32:25]** And sigma function.

**[32:25 -> 32:30]** And so the sigmoid function, you can look at it in the eyes.

**[32:30 -> 32:33]** This is the shape of the sigmoid function.

**[32:33 -> 32:36]** This is how it's written mathematically.

**[32:36 -> 32:40]** So it's just a function that squeeze every value

**[32:40 -> 32:44]** and provide as input into a value between student 1.

**[32:44 -> 32:46]** So you can run and select the value

**[32:46 -> 32:48]** in any point in the x-axis.

**[32:48 -> 32:52]** And then the output would be something between student 1.

**[32:52 -> 32:54]** When it is the value of the input,

**[32:54 -> 32:58]** that says it's very small, then you get the minus one.

**[32:58 -> 33:01]** If it's very big, it's a close to plus one.

**[33:01 -> 33:04]** And in the middle is more or less linear, right?

**[33:04 -> 33:05]** So you have the slope.

**[33:05 -> 33:08]** Now, of course, the choice of this parameter

**[33:08 -> 33:13]** will tell you how big is the slope.

**[33:13 -> 33:16]** But it's a combination of a linear function

**[33:16 -> 33:19]** with a nonlinear one, right?

**[33:19 -> 33:22]** So the sigma function is nonlinear, right?

**[33:22 -> 33:23]** So it's clearly nonlinear.

**[33:23 -> 33:26]** has this linear behavior in the middle, but the extreme,

**[33:26 -> 33:30]** they are just the corresponding particular one.

**[33:33 -> 33:36]** OK.

**[33:36 -> 33:40]** Yeah, so has the situation in fact that it marks between 0, 1

**[33:40 -> 33:44]** and sub weight at minus 1.

**[33:44 -> 33:50]** This function here, unfortunately, is no longer.

**[33:50 -> 33:51]** So we are trying to do this.

**[33:51 -> 33:54]** So if we are able to do this, I mean,

**[33:54 -> 33:56]** this logic of writing in them like this

**[33:56 -> 33:58]** goes into the direction of having a failure

**[33:58 -> 34:00]** that will represent the problem.

**[34:00 -> 34:03]** Really, we are combining getting a part with a new linear part

**[34:03 -> 34:06]** and the output behavior will be in a continuous value

**[34:06 -> 34:08]** between 0 and 1.

**[34:08 -> 34:10]** But this expression is non-contents.

**[34:10 -> 34:13]** So and here, of course, I'm supposing

**[34:13 -> 34:17]** it's the number of samples I can access at 20.

**[34:17 -> 34:22]** So since this is non-convex, how do I optimize it?

**[34:22 -> 34:26]** Well, first of all, we can try to understand if you can write

**[34:26 -> 34:29]** the same thing in a convex way.

**[34:29 -> 34:32]** So rather than using this expression,

**[34:32 -> 34:36]** we write down a cost function that is convex,

**[34:36 -> 34:40]** and that more or less behaves as what we saw before.

**[34:40 -> 34:41]** How do we do that?

**[34:41 -> 34:43]** Well, instead of the loss, now we write down

**[34:43 -> 34:46]** C as a general cost function.

**[34:46 -> 34:49]** And the cost function now is retail like this.

**[34:49 -> 34:52]** So it's minus the lower income of the sigmoid

**[34:52 -> 34:57]** of the BDR function when the label is one.

**[34:57 -> 34:59]** I mean, when I want to get, it's not the label.

**[34:59 -> 35:00]** The value gets to one.

**[35:00 -> 35:05]** Of course, we said our goal is to use a regression model

**[35:05 -> 35:06]** to perform a classification.

**[35:06 -> 35:08]** So this is the adaptation we're doing

**[35:08 -> 35:10]** in the mean, the middle, right?

**[35:10 -> 35:13]** So we still want a one zero prediction,

**[35:13 -> 35:16]** but we are predicting these continuous values.

**[35:16 -> 35:19]** So we are using the lower end of the sigmoid

**[35:19 -> 35:21]** of the linear function.

**[35:21 -> 35:24]** And in these other case, my mouss lower end of 1,

**[35:24 -> 35:28]** minus the sigmoid function of the linear function instead.

**[35:28 -> 35:31]** So why am I using this?

**[35:31 -> 35:35]** Well, first of all, am using this, the continuous function,

**[35:35 -> 35:37]** which is the lower end.

**[35:37 -> 35:38]** And let's see what can happen.

**[35:38 -> 35:45]** So if y is 1, and the output of the sigmoid here

**[35:45 -> 35:47]** is 1.

**[35:47 -> 35:52]** Now, we know that the logarithm of 1 is 0.

**[35:52 -> 35:57]** So then if the label is 1 and then predicting a 1,

**[35:57 -> 36:00]** I don't think any cost, which is going to be a good one.

**[36:00 -> 36:03]** So I, no mistake, no cost.

**[36:03 -> 36:09]** If the label is 1, but the prediction is 0,

**[36:09 -> 36:13]** then we know that the logarithm in 0 is minus infinity.

**[36:13 -> 36:16]** with the minus in front, it becomes anything.

**[36:16 -> 36:18]** So I'm paying an infinite cost.

**[36:18 -> 36:22]** If my prediction is one, so if my prediction is zero,

**[36:22 -> 36:24]** but the ground group was one,

**[36:24 -> 36:27]** I want my model to pay a huge cost

**[36:27 -> 36:28]** because this mistake should not happen.

**[36:28 -> 36:31]** So I'm guiding the model in this sense.

**[36:31 -> 36:33]** And if you read these lines,

**[36:33 -> 36:35]** practically the same the other way round, right?

**[36:35 -> 36:40]** So if the label is zero, but the prediction is one,

**[36:40 -> 36:42]** then one minus one is zero again,

**[36:42 -> 36:45]** minus logarithm of zero and it goes from fieldy.

**[36:45 -> 36:47]** And so it's the same.

**[36:47 -> 36:52]** So in general, if my prediction is correct, no cost.

**[36:53 -> 36:56]** If my prediction is wrong, I pay a cost,

**[36:56 -> 36:59]** which is huge, the infinite cost.

**[37:00 -> 37:04]** And this is the way which I define my loss

**[37:04 -> 37:05]** to train my loss.

**[37:05 -> 37:09]** And so to search for the optimal AMB of the model,

**[37:09 -> 37:16]** So now the parameters of the model are inside the linear function, which is also inside

**[37:16 -> 37:21]** and nonlinearity, which is a sub model.

**[37:21 -> 37:23]** Now, this is a combative function.

**[37:23 -> 37:30]** You can verify it and you can use the concept of the combination of combative functions

**[37:30 -> 37:31]** or combative functions.

**[37:31 -> 37:33]** So these two are separate combative.

**[37:33 -> 37:36]** And what I'm doing also is an extra step.

**[37:36 -> 37:43]** So, rather than writing it down as a system, I write down everything together.

**[37:43 -> 37:51]** It doesn't change everything because I'm putting a y from here, which means that when

**[37:51 -> 37:54]** y is equal to 1, this part holds.

**[37:54 -> 38:01]** And when y is equal to 0, this part holds because one case I have a y from it, in the

**[38:01 -> 38:03]** other case I have 1 minus 1 from it.

**[38:03 -> 38:10]** It's just a way to pass from the system to a single line of our equation.

**[38:10 -> 38:14]** Good. So this function is convex. Nice. Perfect.

**[38:14 -> 38:21]** So now I write it down as my loss function, and now I need to optimize it.

**[38:21 -> 38:26]** But they attention that the parameters we're searching for,

**[38:26 -> 38:30]** I decide this, let's say, a monophilostrophy,

**[38:30 -> 38:33]** because it's really near inside and only the reality.

**[38:33 -> 38:35]** So would not really have the feeling

**[38:35 -> 38:38]** that it would not be so easy to optimize it

**[38:38 -> 38:40]** or go for functions, unless.

**[38:41 -> 38:46]** So now I want to open just more brackets and parentheses

**[38:46 -> 38:48]** that connects what we just saw,

**[38:48 -> 38:52]** which is a regression, most probably you've heard about it,

**[38:52 -> 38:54]** but for people who maybe didn't hear about it

**[38:54 -> 38:59]** and maybe also have curiosity about super backup machines,

**[38:59 -> 39:02]** Well, what we saw is practically minute also

**[39:02 -> 39:03]** of its super vector machine.

**[39:03 -> 39:08]** So remember, super vector machine is defining a model

**[39:08 -> 39:08]** of this kind.

**[39:08 -> 39:11]** Start off from your titer, multiply by x,

**[39:11 -> 39:13]** see if the predict, so it's 1.

**[39:13 -> 39:17]** If this is positive, otherwise it's 0, remember searching

**[39:17 -> 39:18]** for a line.

**[39:18 -> 39:21]** So what is on the right is plus 1.

**[39:21 -> 39:23]** What is on the left is 0.

**[39:23 -> 39:25]** And ideally, would like my prediction

**[39:25 -> 39:29]** to be as big as possible and possibly bigger than 1,

**[39:29 -> 39:31]** such that the 1th A and the cos.

**[39:31 -> 39:36]** So the cos function for an SVM is a hinge loss.

**[39:36 -> 39:37]** It is written like this.

**[39:37 -> 39:40]** So it's the maximum between 0 and 1

**[39:40 -> 39:45]** minus the set of parameter tilde and 2 by by x if y is 1

**[39:45 -> 39:47]** and y is the other.

**[39:47 -> 39:52]** So you can look at them as these two curves here.

**[39:52 -> 39:58]** So in the case in which y is 1, I don't pay any cost.

**[39:58 -> 40:01]** And my prediction is higher than 1.

**[40:01 -> 40:06]** So if you're on this side here, very far away from the line.

**[40:06 -> 40:09]** So if your prediction is very big, you don't pay any cost,

**[40:09 -> 40:12]** because you're doing the correct prediction, you are far away.

**[40:12 -> 40:16]** And instead, if you go lower than 1,

**[40:16 -> 40:19]** then your cost starts to lower it.

**[40:19 -> 40:21]** And the same happens on the other side.

**[40:21 -> 40:25]** So this is what happens inside a super vector machine.

**[40:25 -> 40:26]** And if you look at the logistic regression

**[40:26 -> 40:28]** it's populated in the same.

**[40:28 -> 40:28]** Nothing works.

**[40:28 -> 40:31]** Just written in a different way.

**[40:31 -> 40:33]** But the logic is the same.

**[40:33 -> 40:41]** So you see that the red curve is the logistic one.

**[40:41 -> 40:44]** And even in the super vector machine,

**[40:44 -> 40:46]** I don't know if you saw the primal or the dual formulation.

**[40:46 -> 40:51]** But in practice, the loss you are trying to minimize this one.

**[40:51 -> 40:53]** here, sorry for the changing of notation,

**[40:53 -> 40:56]** but I'm going to explain the same if that now I'm

**[40:56 -> 41:00]** calling n number of samples, but it should be quite clear

**[41:00 -> 41:03]** from the notation.

**[41:03 -> 41:06]** n is another feature, so the dimensionality

**[41:06 -> 41:09]** of the vector x.

**[41:09 -> 41:10]** And what do I do?

**[41:10 -> 41:12]** I have my loss.

**[41:12 -> 41:14]** I add an extra 30.

**[41:14 -> 41:16]** So again, depending on the fact that you

**[41:16 -> 41:20]** saw the primal or the dual formulation,

**[41:20 -> 41:25]** There are lots of theorems that support the supervector machine in the logic.

**[41:25 -> 41:29]** But at the end, if you really look at what supervector machine is optimizing this,

**[41:29 -> 41:33]** it's a loss function plus a organizational term.

**[41:33 -> 41:41]** It tells you that the model, the L2 norm of the parameter of the model has to be small.

**[41:41 -> 41:42]** Nothing more than that.

**[41:46 -> 41:47]** I call it the prime.

**[41:47 -> 41:53]** So let's go back to our logistic regression problem, right?

**[41:53 -> 41:57]** So this is what those who are trying to minimize.

**[41:57 -> 42:00]** And I mean, minimize for the complex function

**[42:00 -> 42:05]** means taking the derivative and putting it equal to 0.

**[42:05 -> 42:08]** First, what is this theta here?

**[42:08 -> 42:10]** It's a set of parameters of the model.

**[42:10 -> 42:14]** So a and b, w and b, or how are they

**[42:14 -> 42:19]** want to call them and they are inside of the linear part for the function, right? So it's

**[42:19 -> 42:28]** a of b. So theta is overall the set of parameters of the model that we want to optimize. Okay.

**[42:28 -> 42:34]** So now I need to calculate the gradient of each term in the summation that we need to

**[42:34 -> 42:42]** And so I think the derivative, we respect the theta of the function.

**[42:42 -> 42:47]** And of course, I mean, why does not depend on theta?

**[42:47 -> 42:53]** So I can just bring it outside the derivative and say in this case,

**[42:53 -> 42:57]** because the dependence on the model is, I mean, this theta means a and b, right?

**[42:57 -> 43:00]** So I can just move it closer to the algorithm.

**[43:00 -> 43:04]** And now let's have fun to see how to derive it.

**[43:04 -> 43:07]** I mean again here we have a function of a functional function.

**[43:07 -> 43:12]** Right, so we have f of g of h, which depends on the table.

**[43:12 -> 43:18]** So we have to derive it and what we would do is we would apply it simply to the chain

**[43:18 -> 43:19]** rule.

**[43:19 -> 43:27]** So now the derivative of f of g of h depending on a, how do we do that?

**[43:27 -> 43:32]** We derive the function f of respect to g, the function g with respect to h and the function

**[43:32 -> 43:39]** So it's just combined in this, the partial derivatives.

**[43:39 -> 43:44]** And now what is the derivative of h with respect to a?

**[43:44 -> 43:47]** So h itself is the linear function, right?

**[43:47 -> 43:50]** So aa x plus e.

**[43:50 -> 43:53]** So the derivative of this is just x, right?

**[43:53 -> 43:58]** It's just removing a, the coefficient.

**[43:58 -> 44:04]** And now we have to pass to the derivative of G with respect to H.

**[44:04 -> 44:11]** What is G? G is the sigmoid of A x i plus B.

**[44:11 -> 44:17]** But now, I mean, it's the derivative of H with respect to H.

**[44:17 -> 44:21]** H is the whole thing, the whole A x i plus B.

**[44:21 -> 44:25]** So here I'm just, so you remember how is the sigmoid done, right?

**[44:25 -> 44:32]** right? It's like this. So in this exponent here, you have a xi plus b. And you have to take

**[44:32 -> 44:40]** the derivative with respect to the whole exponent. Okay. So, yeah. So the real value

**[44:40 -> 44:49]** of this, and this is the expression I have for the sigma i, and the derivative of course

**[44:49 -> 44:55]** You have to remember the fractions, you have the table, the label, the square, and the

**[44:55 -> 44:56]** whole step.

**[44:56 -> 44:58]** And this is what I have.

**[44:58 -> 45:04]** Now I might want to simplify a little bit of my life, so I do something that my definition

**[45:04 -> 45:10]** likes to do, so I try to split things enough and remove the same partition from the same

**[45:10 -> 45:11]** element.

**[45:11 -> 45:16]** So here I'm just separating these two parts, and I have them on the numerator, which is

**[45:16 -> 45:24]** here and then what I do is that I add the plus one minus one just seems strange

**[45:24 -> 45:30]** but you will see that it gets to something and it helps because now you can write it

**[45:30 -> 45:39]** like this I can have one here and then minus destruction again but this is

**[45:39 -> 45:46]** again the sigma. I see this is the sigma and we have the same shape of the original function

**[45:46 -> 45:50]** and this is the same shape of the original function. So I ended up with something like

**[45:50 -> 45:57]** this. Here theorectal spectra G and this part is the sigma multiplied by 1 minus the sigma

**[45:57 -> 46:07]** multiplied by x. Okay, so we are putting it here and then I have to take the dereal

**[46:07 -> 46:11]** The real demographic with respect to G, right?

**[46:11 -> 46:13]** But what is F?

**[46:13 -> 46:17]** F is the lower rhythm of then the C1.

**[46:17 -> 46:19]** But the real area of the lower rhythm

**[46:19 -> 46:22]** is 1 minus the argument of the lower

**[46:22 -> 46:24]** of the lower rhythm, right?

**[46:24 -> 46:27]** So it's just this one.

**[46:27 -> 46:29]** So now putting everything together,

**[46:29 -> 46:36]** I can simplify this two and I get a big expression.

**[46:36 -> 46:43]** And all this was just to take the derivative of all

**[46:43 -> 46:46]** our loss functions and the expression with respect

**[46:46 -> 46:50]** to partial derivative with respect to A.

**[46:50 -> 46:54]** And moreover, we were focusing on the first term of the loss,

**[46:54 -> 46:56]** not the second.

**[46:56 -> 47:01]** So yeah, a lot of effort to get to this result,

**[47:01 -> 47:04]** but in practice, we did just one part.

**[47:04 -> 47:06]** One partial derivative.

**[47:06 -> 47:10]** So during now, we have to do the same for the second turn,

**[47:10 -> 47:12]** and then we have to do the same for the B,

**[47:12 -> 47:13]** and so on and so forth.

**[47:13 -> 47:18]** So this procedure, you see it's quite long.

**[47:19 -> 47:22]** And the challenges due to the difficulty

**[47:22 -> 47:24]** is due to the fact that the parameter

**[47:24 -> 47:26]** are hidden inside the model.

**[47:26 -> 47:29]** So the parameter appear in the linear part,

**[47:29 -> 47:33]** but it's entangled with the non-linearities.

**[47:33 -> 47:38]** So this makes things more complex.

**[47:38 -> 47:44]** And what we get is that now we have, in practice,

**[47:44 -> 47:46]** we have to put my multiple equations

**[47:46 -> 47:49]** and to solve the task.

**[47:49 -> 47:54]** And solving this, so taking the full derivative

**[47:54 -> 48:01]** will require not a linear system and not even,

**[48:01 -> 48:05]** Let's say we don't have a closed form, right?

**[48:05 -> 48:10]** So you remember for the linear regression,

**[48:10 -> 48:15]** the loss force convex, the solution was simply least clear.

**[48:15 -> 48:20]** I just had to invert the matrix, and I had a formula

**[48:20 -> 48:22]** to find the left.

**[48:22 -> 48:25]** In this case, it's not possible.

**[48:25 -> 48:27]** In the case of logistic regression,

**[48:27 -> 48:29]** although the loss is convex, so we already

**[48:29 -> 48:32]** in a reasonably easy condition,

**[48:32 -> 48:36]** the optimization is highly known in error.

**[48:36 -> 48:40]** So it's a combo, it's a convoluted procedure.

**[48:41 -> 48:43]** They're dealing with trash and ventilation

**[48:43 -> 48:46]** that gets scared, trash and then domains only

**[48:46 -> 48:50]** that there is an export E of something, right?

**[48:50 -> 48:53]** Which makes things, I mean, the derivative of the,

**[48:53 -> 48:55]** it's one usually an easy, but it takes a little bit more time

**[48:55 -> 48:58]** to be calculated, so it's,

**[48:58 -> 49:04]** the computer itself is completely not that easy, so analytically it's fine but when

**[49:04 -> 49:09]** many of them all together it becomes more complex.

**[49:09 -> 49:16]** So you see in the case of logistic regression we are already entering a world where the

**[49:16 -> 49:23]** solution is not immediate anymore and what we have to do, we have to hack our way through

**[49:23 -> 49:28]** but this will be our everyday task with the good models.

**[49:30 -> 49:34]** Okay, so I was separating, I mean, different type of flight,

**[49:34 -> 49:37]** so we'll change again, and I'll just take the advantage

**[49:37 -> 49:40]** of the minute, take your question,

**[49:40 -> 49:42]** and then raise your hand.

**[49:53 -> 50:03]** So, g is no longer written.

**[50:03 -> 50:06]** Is that another, yeah, see here?

**[50:06 -> 50:07]** I'm not right.

**[50:07 -> 50:09]** So, f is no longer written.

**[50:09 -> 50:11]** So, I'm not kidding.

**[50:11 -> 50:12]** It's also changed.

**[50:12 -> 50:19]** Right.

**[50:19 -> 50:32]** Yes. So this derivative here is the derivative of g of h. But the variable here that we are

**[50:32 -> 50:43]** searching for, so the h is the whole thing, is the sigmoid of the whole thing of h. So

**[50:43 -> 50:50]** Yes, H is the inside of the right.

**[50:50 -> 50:57]** So what is the question?

**[50:57 -> 51:02]** Yeah, but this is the derivative for the logarithm.

**[51:02 -> 51:07]** So this is, so the logarithm of, sorry, of this thing here.

**[51:07 -> 51:12]** Since it's the logarithm of something, it's one over something.

**[51:12 -> 51:14]** That's the derivative.

**[51:14 -> 51:17]** And so here it becomes one homework,

**[51:17 -> 51:19]** the something which is what is inside the logarithm.

**[51:19 -> 51:20]** So which is the same one.

**[51:23 -> 51:27]** So this is just the logarithm of sigma and function

**[51:27 -> 51:28]** of something.

**[51:28 -> 51:33]** But the derivative of the logarithm is one over the,

**[51:33 -> 51:35]** yeah, I understand that.

**[51:35 -> 51:38]** So that's it.

**[51:38 -> 51:39]** OK.

**[51:39 -> 51:41]** Um

**[52:09 -> 52:10]** Okay.

**[52:10 -> 52:36]** So we said we have to have our way to be able to derivative and so optimize the even complex

**[52:36 -> 52:42]** function that eventually they are complex but I mean we need another strategy to

**[52:42 -> 52:47]** divide it not possible for all the chain rule and the logic that we just saw

**[52:47 -> 52:54]** because it's my take time and moreover thinking about the fact that it was

**[52:54 -> 53:00]** again a simple case because of course complex and preparing our self to try

**[53:00 -> 53:03]** we might deal with no complex function.

**[53:03 -> 53:08]** So let's just get ready to find a strategy for the optimization.

**[53:08 -> 53:09]** What will be the strategy?

**[53:09 -> 53:12]** It will be broad and descent.

**[53:12 -> 53:15]** So what do we have?

**[53:15 -> 53:20]** We're supposed to have a function, which is our loss function.

**[53:20 -> 53:24]** That is represented here by this landscape.

**[53:24 -> 53:29]** So it is shaped with multiple minima.

**[53:29 -> 53:33]** And in general, you can think about it as a function of here.

**[53:33 -> 53:39]** It's simply, I mean, visualize that a function of two

**[53:39 -> 53:43]** dimensions, because let's say you think you have x1, x2.

**[53:43 -> 53:47]** And then the y-axis here, the third axis,

**[53:47 -> 53:50]** is the value of the loss itself.

**[53:50 -> 53:54]** So x1, x2 are the parameters of your model.

**[53:54 -> 53:58]** And then the value of the loss is the output

**[53:58 -> 54:05]** that you get is the re-acalculation of the cost of the model when you use those parameters,

**[54:05 -> 54:08]** those values of X1 and X2.

**[54:08 -> 54:14]** So it's a function that in this visualization takes as input to the use for two things.

**[54:14 -> 54:19]** It's in two parameters of the model and predicts the loss function itself, so the cost that

**[54:19 -> 54:21]** you are playing.

**[54:21 -> 54:24]** And this is the overall landscape, so the overall shape of the loss.

**[54:24 -> 54:28]** Of course, again, it's a cartoonish visualization.

**[54:28 -> 54:31]** When we start from the data, we don't supposed

**[54:31 -> 54:34]** to be able to access every single point

**[54:34 -> 54:37]** of this distribution of this shape.

**[54:37 -> 54:41]** We just measure every choice of the syllable parameter,

**[54:41 -> 54:44]** the corresponding Gaussian parameter.

**[54:45 -> 54:47]** So what do we do is that, well,

**[54:47 -> 54:49]** let's suppose we start from a certain X1 and X2,

**[54:49 -> 54:53]** so a certain choice of the radius of the parameter,

**[54:53 -> 54:56]** And then we look around and say, OK,

**[54:56 -> 55:00]** so where is the direction I should move to minimize?

**[55:00 -> 55:01]** I mean, what is the step I should take

**[55:01 -> 55:03]** to go towards the minimum?

**[55:03 -> 55:06]** Like being on the top of a hill, and you want to go down,

**[55:06 -> 55:08]** and you try to go down as soon as possible,

**[55:08 -> 55:10]** and you try to search and figure out

**[55:10 -> 55:13]** best the rhythm, it will the highest growth to go down.

**[55:15 -> 55:19]** So, brand new sense follows exactly this logic.

**[55:19 -> 55:22]** So you start from some point, some seven four meters

**[55:22 -> 55:27]** see the one that we want me to say on this game in this case.

**[55:27 -> 55:29]** And then you look around and you say,

**[55:29 -> 55:33]** OK, the next step I want to take a little next set of values

**[55:33 -> 55:38]** I want to apply will be obtained by starting

**[55:38 -> 55:41]** the work where it was before it and moving

**[55:41 -> 55:45]** towards the direction of the negative domain.

**[55:45 -> 55:49]** So looking for where I have the steepest gradient,

**[55:49 -> 55:52]** such that they can move the direction and move faster.

**[55:52 -> 55:55]** And it's the gradient of what?

**[55:55 -> 55:57]** It's the gradient of the loss, right?

**[55:57 -> 55:59]** Because we are switching forward the direction.

**[55:59 -> 56:02]** We're going to move over the landscape.

**[56:02 -> 56:05]** So I asked this at the time of the exam,

**[56:05 -> 56:07]** and half of the students are answering.

**[56:07 -> 56:09]** And I said, the gradient of what?

**[56:09 -> 56:11]** I didn't know the loss.

**[56:11 -> 56:14]** We are trying to minimize the loss.

**[56:14 -> 56:18]** We are trying to minimize the number of errors within that.

**[56:18 -> 56:20]** So start for a point.

**[56:20 -> 56:28]** A new set of parameters will be equal to what I have before minus the derivative of the box.

**[56:28 -> 56:33]** And we have a parameter, so this is the negative gradient, fine,

**[56:33 -> 56:35]** how many lines there was function.

**[56:35 -> 56:41]** And we have a parameter in front here, which is called learning rate.

**[56:41 -> 56:49]** So the derivative tells me the direction, the alpha, so the learning rate tells me how big is the step

**[56:49 -> 56:52]** that I'm taking in that direction.

**[56:52 -> 56:56]** Of course, in the step I take, it also

**[56:56 -> 56:59]** function with the mark in the middle of the direction.

**[56:59 -> 57:02]** But this coefficient is an extra coefficient

**[57:02 -> 57:05]** to put a top, and it's a very important one,

**[57:05 -> 57:07]** and it's called the re-grained.

**[57:07 -> 57:09]** And ideally, the procedure is this.

**[57:09 -> 57:14]** You do step by step until you reach a minimum, which,

**[57:14 -> 57:17]** of course, you might not be 100% sure,

**[57:17 -> 57:21]** is the absolute minimum of the model that can be kind of them.

**[57:21 -> 57:23]** But it leads to gaps to a minimum.

**[57:26 -> 57:31]** And so, yeah, this is again our lowest landscape.

**[57:31 -> 57:36]** And we are looking at how it's done.

**[57:36 -> 57:38]** And you can also think about

**[57:41 -> 57:44]** defining some horizontal planes

**[57:44 -> 57:46]** that cut the landscape.

**[57:46 -> 57:49]** So the cut is a 3D shape.

**[57:49 -> 57:55]** And if you do that, you see these eyes aligns or levels set.

**[57:55 -> 57:58]** So every line, I mean, every curve

**[57:58 -> 58:03]** is representing a plane where the loss is equal, right?

**[58:03 -> 58:04]** It's flat.

**[58:04 -> 58:05]** It is the same.

**[58:05 -> 58:07]** And the value that you see here,

**[58:07 -> 58:09]** the image line, corresponding the value of the loss

**[58:09 -> 58:16]** at that level, which means the corresponding axis here.

**[58:16 -> 58:20]** And usually, I mean, if you are lucky, your loss

**[58:20 -> 58:22]** is also very smooth and very nice,

**[58:22 -> 58:25]** like what we are looking at here.

**[58:25 -> 58:29]** And this means that you can take one direction vector

**[58:29 -> 58:32]** in every single point, and you see,

**[58:32 -> 58:34]** and we are just enlarging it,

**[58:34 -> 58:38]** that these vectors are the relative,

**[58:38 -> 58:42]** straighten that point, and point from position

**[58:42 -> 58:44]** with higher value of the loss,

**[58:44 -> 58:46]** was a lower value of the loss.

**[58:46 -> 58:48]** So when you see here, it's a region

**[58:48 -> 58:50]** where you might have a local minimum

**[58:50 -> 58:53]** and the relative becomes over zero.

**[58:53 -> 58:55]** So it's, let's say, but it's on the same level,

**[58:55 -> 58:57]** so you can see and change.

**[58:58 -> 59:00]** But then in the direction itself,

**[59:00 -> 59:05]** it's always going from the higher value of loss

**[59:05 -> 59:07]** to lower values of the loss.

**[59:07 -> 59:17]** And of course, the gradient is orthogonal to the level curves, because we said, I mean,

**[59:17 -> 59:24]** the level curves are the position where the law is fixed, is only so is equal, like it's

**[59:24 -> 59:27]** we have a category, for example.

**[59:27 -> 59:34]** And so this contribution of the derivative in zero, right, because along the directional

**[59:34 -> 59:37]** the function, let's say, is the parameter

**[59:37 -> 59:40]** is the function along this curve does not change.

**[59:40 -> 59:42]** So that distribution is 0.

**[59:42 -> 59:45]** The gradient is actually orthogonal, right?

**[59:45 -> 59:47]** To give all the information on the right

**[59:47 -> 59:49]** and the other side of the orthogonal direction.

**[59:49 -> 59:52]** While the direction on the right is 0,

**[59:52 -> 59:53]** I want the error to work.

**[59:56 -> 60:04]** And so we say we need to calculate

**[60:04 -> 60:13]** with the derivatives, which means that the function we're dealing with,

**[60:13 -> 60:17]** so the loss, should be differentiable.

**[60:17 -> 60:21]** Which means that not only I should be able to derive it,

**[60:21 -> 60:26]** but it should also have a continuous gradient.

**[60:26 -> 60:31]** So again, in the theory world, to be able to take this derivative

**[60:31 -> 60:35]** in the proper way and apply rather than sense,

**[60:35 -> 60:38]** according to the logic we just described,

**[60:38 -> 60:43]** your function should respect some specific condition.

**[60:43 -> 60:46]** And so it has to be these characteristics.

**[60:46 -> 60:47]** It has to be nice and smooth.

**[60:47 -> 60:49]** You have to be able to play full derivatives

**[60:49 -> 60:52]** and the gradient should be continuous.

**[60:52 -> 60:56]** But this, again, will not always be the case.

**[60:56 -> 60:59]** We will deal with more, much more complex function,

**[60:59 -> 61:02]** eventually also with these continuities,

**[61:02 -> 61:04]** or the right of anyway.

**[61:04 -> 61:07]** So we made proof for solutions, because that's

**[61:07 -> 61:10]** been shown that anyway it brings us,

**[61:10 -> 61:14]** since anyway, we are dealing with a districtized world

**[61:14 -> 61:17]** that are not considered to be not the case

**[61:17 -> 61:21]** since we are using the bits.

**[61:21 -> 61:23]** We are not really, our model that really

**[61:23 -> 61:27]** happened to be exactly in the point of discontinuity.

**[61:27 -> 61:31]** So any way that could be calculated.

**[61:31 -> 61:36]** And there is this caveat, but we'll anyway you would derive.

**[61:36 -> 61:41]** But just to provide you, so what can be the issues?

**[61:41 -> 61:46]** So the function has to be differentiable at all points

**[61:46 -> 61:49]** to really be able to apply the incentive

**[61:49 -> 61:53]** proper way to radically guarantee the rate.

**[61:53 -> 61:56]** But yeah, when you deal with function, which are complex,

**[61:56 -> 61:57]** I mean, this might not happen.

**[61:57 -> 62:00]** So for instance, here is the visualization

**[62:00 -> 62:04]** of a loss landscape or a function landscape

**[62:04 -> 62:05]** that is done like this.

**[62:05 -> 62:09]** Have this shape everywhere except in zero

**[62:09 -> 62:11]** where it is forced to pass to the origin.

**[62:13 -> 62:18]** So now you already see that this kind of function

**[62:19 -> 62:21]** is has different derivative.

**[62:21 -> 62:24]** So depending on the fact that you're looking

**[62:24 -> 62:28]** along the x axis or along the y axis,

**[62:28 -> 62:33]** the derivative in zero have a different orientation.

**[62:34 -> 62:37]** So let's see if I manage to describe it.

**[62:37 -> 62:39]** So this function here,

**[62:39 -> 62:43]** let's say I want to calculate in the points function x

**[62:43 -> 62:46]** and y equals zero, okay?

**[62:46 -> 62:50]** So let's look at the denominator, right?

**[62:50 -> 62:53]** So here the middle grows faster

**[62:53 -> 62:55]** in terms of y, the spectral and wave of the denominator

**[62:55 -> 62:58]** have this base of the power of 2.

**[62:58 -> 63:03]** So when we focus on y equals 0, in practice,

**[63:03 -> 63:06]** this becomes 0 much faster than the numerator, this y.

**[63:06 -> 63:08]** So this is a remove of 2.

**[63:08 -> 63:11]** So think about that this will be practically canceled

**[63:11 -> 63:14]** very fast when you move in directional 0.

**[63:14 -> 63:19]** And you remain with x to square y divided by x2.

**[63:19 -> 63:21]** So this x to square gets removed.

**[63:21 -> 63:23]** and you get only the y.

**[63:23 -> 63:28]** And so, I mean, the, what I get is that

**[63:29 -> 63:33]** the derivative of this of y with respect to y is one.

**[63:34 -> 63:35]** Right?

**[63:35 -> 63:36]** So if this function goes to zero,

**[63:36 -> 63:40]** practically dA is as y.

**[63:40 -> 63:43]** So as y itself is a line,

**[63:43 -> 63:46]** then the derivative with respect to y is one.

**[63:46 -> 63:49]** So this is what this expression is telling me.

**[63:49 -> 63:51]** So when I take the derivative of the function,

**[63:51 -> 63:56]** with respect to y, close to y equals 0, I have a 1.

**[63:56 -> 64:00]** And this holds also, it holds in general for x different from 0.

**[64:00 -> 64:03]** If you do the same reasoning for the other part,

**[64:03 -> 64:09]** now it becomes immediately 0 because if x is 0,

**[64:09 -> 64:10]** now this numerator and the domain,

**[64:10 -> 64:12]** or they grow at the same time, and then

**[64:12 -> 64:15]** when they say the law seems to be both x squared,

**[64:15 -> 64:19]** so the numerator becomes 0 in practice.

**[64:19 -> 64:20]** And that's the most important term

**[64:20 -> 64:22]** because y is equal to 0.

**[64:22 -> 64:26]** So the numerator becomes 0, but the denominator does not.

**[64:26 -> 64:28]** And so then everybody is equal to 0,

**[64:28 -> 64:30]** and you go in the other direction.

**[64:30 -> 64:33]** And so you see that in the origin in practice,

**[64:33 -> 64:36]** you have two different derivatives.

**[64:36 -> 64:38]** So there is a discontinuity.

**[64:38 -> 64:41]** So in theory, this function cannot be derived in the origin.

**[64:41 -> 64:43]** So not only it's very visible from the shape,

**[64:43 -> 64:46]** but you can really calculate it and show

**[64:46 -> 64:48]** that the two directions are different.

**[64:48 -> 64:53]** So in practice, this function is not differentiable.

**[64:53 -> 64:55]** But in this case, as I told you,

**[64:55 -> 64:58]** we will anyway use the right-hand side.

**[64:58 -> 64:59]** And a high-level work.

**[64:59 -> 65:01]** But we know that the mind be balanced.

**[65:01 -> 65:02]** The mind be issues.

**[65:02 -> 65:03]** So we have to be prepared.

**[65:03 -> 65:05]** So if we see a certain condition where

**[65:05 -> 65:08]** your awareness starts behaving strangely,

**[65:08 -> 65:11]** then you might also ask yourself,

**[65:11 -> 65:14]** is it something happening to the heart of my loss?

**[65:14 -> 65:16]** It really badly behaved.

**[65:16 -> 65:19]** So this is the kind of question that might turn out to you

**[65:19 -> 65:22]** when you see some strange behavior in goodness.

**[65:24 -> 65:29]** Okay, so then what we are actually searching for,

**[65:32 -> 65:36]** we said at high level a minimum, right?

**[65:36 -> 65:38]** But in general it tends to be a specialary point.

**[65:38 -> 65:41]** So a point where the derivative proves the zero.

**[65:42 -> 65:45]** And here again, we have to be careful

**[65:45 -> 65:51]** because a special rate point can also not be a local minimum.

**[65:51 -> 65:54]** It can be what is called a saddle point,

**[65:54 -> 66:05]** which if you go back to this here,

**[66:05 -> 66:10]** I mean, these, for instance, these are a saddle point

**[66:10 -> 66:14]** because you have a minimum in a direction.

**[66:14 -> 66:18]** But if you look at it in the other direction, it's a monsoon.

**[66:18 -> 66:21]** So it is a stationary point because the derivative is 0.

**[66:21 -> 66:25]** But it's not a point of stable equilibrium.

**[66:25 -> 66:31]** Because if you put a goal there, you can't anyway hold on.

**[66:31 -> 66:36]** OK, so we know that we are searching for a minimum

**[66:36 -> 66:39]** by putting the derivative to 0.

**[66:39 -> 66:44]** but we know that it can be a set of points.

**[66:44 -> 66:48]** And of course, the minimum where we get

**[66:48 -> 66:52]** depends from where we start the process.

**[66:52 -> 66:57]** So if I start from here, I'll be attracted

**[66:57 -> 67:00]** to where these local remove, right?

**[67:00 -> 67:03]** But if I start from here, maybe I'll be attracted to low

**[67:03 -> 67:06]** and then another minimum of the landscape,

**[67:06 -> 67:09]** which is lower with respect to where I started from,

**[67:09 -> 67:11]** and I also end up, I mean,

**[67:11 -> 67:13]** I think they're careful to not end up inside the coin

**[67:13 -> 67:15]** because they're really point of

**[67:16 -> 67:19]** very unstable degree, but it's not what we like.

**[67:22 -> 67:27]** So we said that in this expression,

**[67:28 -> 67:30]** we are moving towards, I mean,

**[67:30 -> 67:33]** the direction of the minimum amount,

**[67:33 -> 67:35]** the base of the derivative of the loss,

**[67:35 -> 67:38]** and these those are the directions.

**[67:38 -> 67:41]** And we have this coefficient in front,

**[67:41 -> 67:42]** which is called the rate.

**[67:43 -> 67:45]** Usually we say that the step,

**[67:45 -> 67:48]** the dimensional step is guided by alpha,

**[67:48 -> 67:51]** but actually is guided by alpha and the momentum

**[67:51 -> 67:52]** of the green bit, of course.

**[67:54 -> 67:58]** And that's a very important parameter

**[67:58 -> 67:59]** all in the water.

**[67:59 -> 68:02]** But no, let me correct myself.

**[68:02 -> 68:04]** Is a hyperparameter.

**[68:04 -> 68:08]** is not the formulae of the model that you optimize

**[68:08 -> 68:10]** by minimizing the loss.

**[68:10 -> 68:14]** You know, I mean, F is a function that depends on the details

**[68:14 -> 68:17]** of the cell of family or it has inside.

**[68:17 -> 68:21]** Those are the parameters, so W, B, G, A, and B.

**[68:21 -> 68:24]** Those are the parameters of the model that you optimize

**[68:24 -> 68:29]** while this alpha here is not a parameter

**[68:29 -> 68:32]** in the hyper parameter of the model.

**[68:32 -> 68:41]** Of course, there are strategies to optimize the

**[68:41 -> 68:42]** time.

**[68:42 -> 68:50]** The way which is defined is actually a hyper parameter, something you would like to tune

**[68:50 -> 68:55]** through for instance cross-validation.

**[68:55 -> 68:57]** Now how do we choose it?

**[68:57 -> 68:59]** The best, I mean not best.

**[68:59 -> 69:02]** The most simple thing would be, well, I keep it fixed.

**[69:02 -> 69:05]** Fine, I keep it fixed.

**[69:05 -> 69:08]** But then, which videos do I put?

**[69:08 -> 69:13]** Because if I select a value, which is very small,

**[69:13 -> 69:15]** then I take very, very small steps

**[69:15 -> 69:18]** towards the minimum and can take forever

**[69:18 -> 69:21]** to get somewhere reasonable, okay?

**[69:21 -> 69:25]** On the other side, if I take step which are too big,

**[69:25 -> 69:28]** then I might have enough jumping here and there,

**[69:28 -> 69:33]** And I don't get to the minimum because I start oscillating

**[69:33 -> 69:36]** government and never gets to be meaningful to us.

**[69:36 -> 69:39]** So not too small, not too big.

**[69:39 -> 69:43]** There are things you can do as you said to also optimize

**[69:43 -> 69:47]** the alpha, something like the underlying search.

**[69:47 -> 69:50]** So in that case, what you do is that

**[69:50 -> 69:54]** besides the optimization for the parameter

**[69:54 -> 69:58]** which are inside f, you have another approximation.

**[69:58 -> 70:00]** So you take some step, you calculate the loss,

**[70:00 -> 70:03]** and then you write down this function,

**[70:03 -> 70:06]** not anymore as a function of the parameter being,

**[70:06 -> 70:10]** but as a functional alpha, and you try both of them.

**[70:10 -> 70:12]** So this is something you can do,

**[70:12 -> 70:14]** which is called linear search, okay,

**[70:14 -> 70:17]** for the parameter of the learning rate.

**[70:17 -> 70:19]** And what you observe in this case,

**[70:19 -> 70:22]** and that is that you tend to take as many steps

**[70:22 -> 70:27]** in a direction until you touch one of the isolines.

**[70:27 -> 70:32]** lines. And then when you touch it, you move into the orthogonal direction, of course, because

**[70:32 -> 70:38]** the status would be in the direction of the river that you move your carbon under that.

**[70:38 -> 70:44]** So this is the kind of effect you would see if you apply linear search. So every direction

**[70:44 -> 70:50]** is orthogonal with respect to one of the previous. But the logic is always the same, right?

**[70:50 -> 71:02]** Now I'm writing you like this, what you can read here very clearly is teta at step t plus 1 is equal to teta at step t.

**[71:02 -> 71:15]** It might not have the real feel back, where here you have the teta only, let's say we have the sound script, because n depends on the set of under teta.

**[71:15 -> 71:28]** Now we said, okay, you can set the learning rate as a fixed value, but you have to properly

**[71:28 -> 71:29]** choose it.

**[71:29 -> 71:38]** Or you can try to impose a change in learning rate, which is actually smart.

**[71:38 -> 71:39]** Why?

**[71:39 -> 71:46]** Because maybe at the beginning you would like to have a big step because you're far away from the minimum

**[71:46 -> 71:51]** And then progressively while you're training you want to reduce the dimensional over step

**[71:51 -> 71:55]** Right mark strategy. So you decrease alpha

**[71:56 -> 71:59]** According to maybe you can set the degree decay parameter

**[71:59 -> 72:06]** So you say okay, I start from alpha and zero that should be out of zero and then I want to get alpha

**[72:06 -> 72:09]** I define at the end of my procedure,

**[72:09 -> 72:10]** the training procedure,

**[72:10 -> 72:13]** I want to get to do an alpha that I call alpha 0.

**[72:13 -> 72:15]** Then I divide, let's say,

**[72:17 -> 72:19]** the changing procedure in steps.

**[72:19 -> 72:24]** I have T steps and at T0, I only have alpha 0.

**[72:25 -> 72:27]** While when T is equal to row, I only have alpha.

**[72:27 -> 72:31]** So I'm changing the alpha with stages,

**[72:31 -> 72:36]** which are defined by the row that I have.

**[72:36 -> 72:45]** Or you can have exponential decay or at least there are different ways to do that.

**[72:45 -> 72:50]** Linear schedule is financial schedule and this would be something you would use to practice

**[72:50 -> 72:53]** with the behavior in the optimization.

**[72:53 -> 72:59]** But again, there are some conditions where this kind of strategy is still not enough

**[72:59 -> 73:11]** because you want maybe also to improve the procedure in which you choose your learning rate parameter.

**[73:11 -> 73:15]** So what you can do, you can introduce something which is called moment.

**[73:15 -> 73:26]** So now in theory, what we've got before was that at T plus 1, we have a t, minus the derivative, right?

**[73:26 -> 73:32]** right minus r of fact the middle right. So now I think the term in the middle and this term is called

**[73:32 -> 73:42]** V and V changes in this way. V depends on another either parameter here that it will lambda, right.

**[73:42 -> 73:49]** Now if lambda is zero then Vd plus one is just equal to the derivative so we go back to standard

**[73:49 -> 73:56]** the difference that the momentum is provided is exactly the carbon we are disturbing here.

**[73:56 -> 74:04]** And what happens is that in time, so with multiple stages, the product accumulates,

**[74:04 -> 74:09]** because you keep the sort of memory when you respect to the V at the previous step.

**[74:09 -> 74:15]** And so it's called momento, which is a reminder of physics.

**[74:15 -> 74:19]** So, we'll also be biomassive and not long.

**[74:19 -> 74:23]** And the idea is that if the dragon in time

**[74:23 -> 74:27]** is always pointing to the same direction, then the dragon accumulates.

**[74:27 -> 74:33]** And it makes your changing, I mean, the learning rate,

**[74:33 -> 74:36]** the logic of the whole procedure, the learning rate still is out of it.

**[74:36 -> 74:39]** But the momentum provides you to go faster and faster.

**[74:39 -> 74:43]** So, if the dragon accumulates, if more steps go in the same direction

**[74:43 -> 74:50]** you are just accumulating and making the movement towards the minimum posture.

**[74:50 -> 74:52]** This is what we are doing.

**[74:52 -> 75:00]** If they are aligned, the sequence of gradients just, yeah, start up and the effect is accelerated.

**[75:00 -> 75:05]** And this is helpful because sometimes you start from the local minimum that you don't like.

**[75:05 -> 75:10]** You would like to move towards another minimum which is lower in the loss.

**[75:10 -> 75:15]** Okay, and so this helps you to somehow escape from a local demo.

**[75:16 -> 75:21]** And you see him in this behavior like in terms of moving balls,

**[75:21 -> 75:24]** that you have both as targets at a point.

**[75:24 -> 75:29]** Now you can read SGD as simple grab the sand,

**[75:29 -> 75:32]** although S is stochastic grab the sand

**[75:32 -> 75:36]** and we will discuss, so explain the next slide.

**[75:36 -> 75:40]** But read, you can look at the red path,

**[75:40 -> 75:44]** the movement of the bowl, just found that by the sun.

**[75:44 -> 75:47]** And then you can look at what happens with momentum.

**[75:47 -> 75:49]** I mean, with momentum, you get into a wrong minimum,

**[75:49 -> 75:53]** but then you go into, you escape from it

**[75:53 -> 75:55]** and go to another minimum.

**[75:55 -> 76:00]** Now, if there's something in this plot that tells us

**[76:00 -> 76:06]** that this minimum is greater than this one, yes,

**[76:06 -> 76:13]** There is some theory that explains that a flutter minimum is better than the spectra picked one.

**[76:13 -> 76:18]** And so it's better to get to something which is flutter, more stable,

**[76:18 -> 76:21]** with respect to something minimum which is very picked.

**[76:21 -> 76:26]** So that's the reason why in general I would like to get to these minimums rather than this one.

**[76:26 -> 76:30]** So you see, I have a function that I have many of, that many minimum,

**[76:30 -> 76:33]** and we want to get to a nice minimum.

**[76:33 -> 76:41]** Now, at the end, anyway, they are all law convenina of function, which are very complex.

**[76:41 -> 76:50]** And ideally, we would not even like to really get to the best possible minimum.

**[76:50 -> 76:55]** So the global minimum, it's not necessarily the best solution.

**[76:55 -> 76:58]** So I'm saying this.

**[76:58 -> 77:00]** Why do you think?

**[77:00 -> 77:05]** Why do you think, at the end, you say, OK, all of our models are trying to get to the

**[77:05 -> 77:12]** minimum costs, minimum of the loss, but maybe the absolute minimum of the loss function might

**[77:12 -> 77:15]** not necessarily be the best one.

**[77:15 -> 77:16]** Exactly.

**[77:16 -> 77:21]** So if you really go to the global minimum, you might end up overfitting, which means you

**[77:21 -> 77:24]** are perfectly memorizing your training samples.

**[77:24 -> 77:29]** Because indeed, again, everything is optimized as a training set.

**[77:29 -> 77:36]** and build a risk minimization. So if you optimize perfectly zero error on the training set,

**[77:36 -> 77:42]** possibly you are over 50. So you are memorizing the training set and then the model will not

**[77:42 -> 77:47]** be able to generalize. So any local minimum reasonable one, of course you always thought

**[77:47 -> 77:54]** to search really a little round, if you just don't, say you're not satisfied by the generally

**[77:54 -> 77:55]** but the first medium would be fine,

**[77:55 -> 77:59]** but you really, there are moving in that direction

**[77:59 -> 78:00]** is the right thing to do.

**[78:03 -> 78:05]** Yeah, so there are many other strategies.

**[78:05 -> 78:09]** I mean, this is just looking at the minimum in the eye,

**[78:09 -> 78:12]** so the momentum in the eye, I would say,

**[78:12 -> 78:14]** I mean, this is down there in the sand,

**[78:14 -> 78:16]** and there are just colors like to look at the mid,

**[78:16 -> 78:18]** the momentum.

**[78:18 -> 78:19]** So this is greater than the sand,

**[78:19 -> 78:21]** and you see already that greater than the center per se

**[78:21 -> 78:23]** accumulates guidance, right?

**[78:23 -> 78:25]** But when you do it with momentum,

**[78:25 -> 78:27]** rather than being like this,

**[78:27 -> 78:29]** you also have this term in front,

**[78:29 -> 78:33]** which enforces, let's say, make the movement faster

**[78:33 -> 78:35]** when the breathing is accurate.

**[78:35 -> 78:37]** And you might also have a more general form

**[78:37 -> 78:40]** because at the end, this is applying

**[78:40 -> 78:42]** one single coefficient somehow

**[78:42 -> 78:44]** to all the directional movements of the,

**[78:44 -> 78:47]** to all of the directional derivatives,

**[78:47 -> 78:49]** while this you might have,

**[78:49 -> 78:50]** you might have, you might have,

**[78:50 -> 78:52]** having the margins, right?

**[78:52 -> 78:57]** where that tells you that you have different strengths

**[78:57 -> 78:59]** and different, let's say, enforcement

**[78:59 -> 79:02]** of the acceleration, let's say, of the gradient

**[79:02 -> 79:04]** in different sub-directions.

**[79:04 -> 79:08]** And so there are several variants of the momentum logic

**[79:08 -> 79:12]** that you will play with them, the other, other, and so on.

**[79:12 -> 79:13]** And this is what we're doing.

**[79:13 -> 79:17]** It's just the optimization procedure that we adopt

**[79:17 -> 79:21]** and is related to how we are moving along the driving

**[79:21 -> 79:21]** direction.

**[79:22 -> 79:23]** Okay.

**[79:23 -> 79:33]** Yeah, so earlier, as you said, we are really interested in the global optimum because we

**[79:33 -> 79:36]** might handle the feeling.

**[79:36 -> 79:42]** And so, yeah, as usual, we get back to the fact that even though we're not too...

**[79:42 -> 79:48]** Okay, so we said, complex problem, they can in any way be complex.

**[79:48 -> 79:53]** So we saw the logistic regression that doesn't have a close formula.

**[79:53 -> 79:55]** Then you can apply dry the scent.

**[79:55 -> 79:59]** Of course, nothing prevent us to use dry the scent also for the dry the scent.

**[79:59 -> 80:01]** You can see through it.

**[80:01 -> 80:05]** Although you have a close formula, the logic of dry the scent is,

**[80:05 -> 80:10]** you see work can take a work value of editing this conference there.

**[80:10 -> 80:12]** And that's something, the goal is that you have efficient and

**[80:12 -> 80:14]** the medical institutions.

**[80:14 -> 80:15]** So yeah.

**[80:15 -> 80:16]** Yeah.

**[80:16 -> 80:17]** So.

**[80:17 -> 80:24]** So, anyway, we'll manage non-combat and also non-differentiable function, but we'll apply

**[80:24 -> 80:28]** one in the same way.

**[80:28 -> 80:29]** Okay.

**[80:29 -> 80:37]** I don't know, just one extra minute, then we will take the concept again.

**[80:37 -> 80:46]** So, the issue here is that anyway, the loss has to be completed over the old set of samples,

**[80:46 -> 80:49]** all the trade insert.

**[80:49 -> 80:53]** But this, considering the fact that the loss function

**[80:53 -> 80:55]** that have multiple terms, you might

**[80:55 -> 80:59]** take multiple partial derivatives,

**[80:59 -> 81:02]** high dimensionality of the x.

**[81:02 -> 81:05]** So these can be quite heavy to be calculated.

**[81:05 -> 81:08]** So both the number of centers and the number of parameters

**[81:08 -> 81:11]** that you have in the models of the dimension of this data

**[81:11 -> 81:14]** influence the calculation of this loss.

**[81:14 -> 81:17]** So one thing that one can do is to avoid

**[81:17 -> 81:20]** the data calculation over all the samples

**[81:20 -> 81:25]** and considering batches of samples rather than all of them.

**[81:25 -> 81:29]** So I take only a small representative subset

**[81:29 -> 81:31]** of my N examples.

**[81:31 -> 81:35]** I might consider only this summation over N,

**[81:35 -> 81:38]** where N is much smaller than all the training samples

**[81:38 -> 81:40]** at the same time.

**[81:40 -> 81:44]** And then I can repeat it multiple times in many batches

**[81:44 -> 81:51]** optimized for batch and I take another batch and we go on like this. These speed up the procedure a lot, okay,

**[81:52 -> 81:57]** for instance the case of the MNIST dataset which is the one with the digit and with the digit.

**[81:57 -> 82:04]** We have 60,000 samples, but I can get to smaller batches and work on that. This is called stochastic

**[82:05 -> 82:11]** So I managed to work on subsets from the whole string of samples

**[82:11 -> 82:20]** But of course I have to be very careful because every batch I work with, it has to be representative

**[82:20 -> 82:22]** of the old trading samples.

**[82:22 -> 82:27]** Think about the fact you have to make to produce a classifier and every batch, a classifier

**[82:27 -> 82:32]** on 10 classes and every batch could be examples only of class one.

**[82:32 -> 82:39]** Because it sees only the sample of class one, what should it classify?

**[82:39 -> 82:43]** So every batch should be representative of the whole.

**[82:43 -> 82:48]** If you do it like that, then working with this stochastic version

**[82:48 -> 82:54]** that just manages batches of data in sequences helps you to get to the good solution.

**[82:54 -> 82:59]** It also has a regularization effect because you are shuffling the data

**[82:59 -> 83:04]** and you are not looking at them at the same time and it helps you to avoid the fitting.

**[83:04 -> 83:08]** So it's helpful in this sense.

**[83:08 -> 83:12]** And this is just, I mean, the stochastic writers and version.

**[83:12 -> 83:16]** And once all the, you have seen all the patches

**[83:16 -> 83:20]** that complete the database, then you have completed the NEPA.

**[83:20 -> 83:22]** And so you have optimized a very NEPA.

**[83:22 -> 83:24]** And generally, a deep learning model

**[83:24 -> 83:26]** will optimize a little more to the NEPA.

**[83:26 -> 83:28]** So you start again, and you do it again.

**[83:28 -> 83:29]** Right?

**[83:29 -> 83:31]** So you search again for the set of parameters

**[83:31 -> 83:33]** that optimize the model.

**[83:33 -> 83:34]** OK.

**[83:34 -> 83:39]** So, yeah, of course, with the graphic editor,

**[83:39 -> 83:42]** you don't expect any more to see that very nice path

**[83:42 -> 83:45]** towards the middle, the application,

**[83:45 -> 83:48]** and the thing is based on the batch of the data,

**[83:48 -> 83:51]** but anyway, to get to the minimum and to see some observation

**[83:51 -> 83:53]** maybe around the minimum.

**[83:56 -> 83:58]** I think, yeah, it's ended, so just for good.

**[83:58 -> 84:03]** So, when I deal with histocastic randomisms,

**[84:03 -> 84:09]** The dependence of my model is related only on the dimension of the data, not on the number

**[84:09 -> 84:13]** of samples, because the cost of every batch should be all the same, right?

**[84:13 -> 84:16]** And it depends on the subset, not the load of some of trans samples.

**[84:16 -> 84:21]** But I would be able to get to a good optimal solution for an optimal map.

**[84:21 -> 84:26]** I mean, go to one of the good minimum, one of the good minimum.

**[84:26 -> 84:29]** And this, as you said, regularize a little bit of the model.

**[84:29 -> 84:31]** and so also have in generalization,

**[84:31 -> 84:36]** so being helpful to reduce the cost of the condition process.

**[84:37 -> 84:40]** And I would say that that's it in the sense

**[84:40 -> 84:42]** that this just summarizes whether or not

**[84:42 -> 84:44]** with privacy and that's so.

