# Lecture Transcription

- **Source**: `temp_audio_83841.wav`
- **Model**: `base.en`
- **Device**: `mps`

---

**[00:00 -> 00:21]** Advanced

**[00:21 -> 00:38]** Okay, so the Zoom classroom should be on the microphone is on, everything is working.

**[00:38 -> 00:42]** So we can start.

**[00:42 -> 00:43]** And we can start.

**[00:43 -> 00:46]** So we will start exactly what we left last time.

**[00:46 -> 00:50]** So we are talking about what does it mean to become a martial learner.

**[00:50 -> 00:54]** And we have seen this high level, let's say, procedure.

**[00:54 -> 00:58]** First of all, we need to understand the domain prior knowledge and goal.

**[00:58 -> 01:04]** So we have to manage also information about the data, which kind of information do we

**[01:04 -> 01:05]** have?

**[01:05 -> 01:10]** So what is the main experience that we have, right?

**[01:10 -> 01:12]** So the experience is in the data.

**[01:12 -> 01:16]** Then we want to define the task.

**[01:16 -> 01:19]** So what we are doing this data?

**[01:19 -> 01:22]** We learn the model, we will run the model,

**[01:22 -> 01:24]** we will interpret the results,

**[01:24 -> 01:27]** we will understand what these results are telling us,

**[01:27 -> 01:32]** and then we'll get back to the definition of the model

**[01:32 -> 01:33]** and possibly improve it.

**[01:33 -> 01:35]** So I think if I'm not wrong,

**[01:35 -> 01:37]** this is where is the last slide we saw last time.

**[01:39 -> 01:42]** So, and becoming a machine learner,

**[01:42 -> 01:45]** that means really being able to understand

**[01:45 -> 01:48]** what's going on behind the scenes.

**[01:48 -> 01:51]** So not just steering the data or changing the data

**[01:51 -> 01:54]** or torturing the data as much as we want

**[01:54 -> 01:58]** until they tell us what we want them to say, right?

**[01:58 -> 01:59]** That doesn't work like this.

**[02:00 -> 02:05]** Okay, so, and we discuss about somehow the history

**[02:06 -> 02:09]** of artificial intelligence, how we actually arrive

**[02:09 -> 02:12]** to what we defined today as AI.

**[02:12 -> 02:15]** So with statistical learning, with machine learning,

**[02:15 -> 02:17]** with deep learning, which is a subpart

**[02:17 -> 02:19]** of machine learning overall.

**[02:19 -> 02:23]** And what actually happened in 2010

**[02:23 -> 02:27]** when there was this somehow revolution

**[02:27 -> 02:29]** in the way in which AI was defined

**[02:29 -> 02:31]** at the last, let's say, revolution

**[02:31 -> 02:34]** with the introduction of deep neural network

**[02:34 -> 02:38]** is that there was a sort of perfect storm

**[02:38 -> 02:40]** where we had the availability of data,

**[02:40 -> 02:42]** larger probability of data,

**[02:43 -> 02:46]** the cost of the storage and of computation.

**[02:46 -> 02:49]** So storage interval memory and computation

**[02:49 -> 02:53]** thanks to the GPUs, so computing power.

**[02:53 -> 02:55]** So the cost of storage went down

**[02:55 -> 02:58]** and the computing power were up practically, right?

**[02:58 -> 03:02]** So a perfect storm combination of data, memory, cost, low

**[03:02 -> 03:05]** and the high computational capacity.

**[03:05 -> 03:09]** So this perfect storm allows to actually enter

**[03:09 -> 03:11]** into this new era of AI.

**[03:11 -> 03:13]** And the first element is data, right?

**[03:13 -> 03:18]** So what we're looking at here is sort of overview

**[03:18 -> 03:23]** of the availability of digital data.

**[03:24 -> 03:28]** Are you able to see or should I turn on some lights

**[03:28 -> 03:31]** that are more or less visible?

**[03:31 -> 03:33]** I don't know if the situation can improve,

**[03:33 -> 03:34]** but we tried.

**[03:35 -> 03:37]** So we know about.

**[03:43 -> 04:03]** Unfortunately, the first road hour, so let me look darker, but I hope you can see better.

**[04:03 -> 04:04]** Okay.

**[04:04 -> 04:10]** So, certainly we need to extract knowledge from the data, right?

**[04:10 -> 04:22]** For years, knowledge where there in music was in specific records and CDs, and then the text was in books.

**[04:22 -> 04:27]** Then with the digital revolution, all the information, all the data became digital.

**[04:27 -> 04:30]** All this information is available online.

**[04:30 -> 04:38]** Now, of course, you can wonder, is it legal or even ethical to just take everything which is on the web and use it to train a model?

**[04:38 -> 04:43]** not really, but no, there are some things you can do for research purposes.

**[04:43 -> 04:44]** So knowledge is there.

**[04:44 -> 04:48]** So unless you have to do something bad, interior, if you're used,

**[04:48 -> 04:51]** you are able to exploit this knowledge.

**[04:51 -> 04:53]** And actually, this is what happened for the last year.

**[04:53 -> 04:59]** So all the information that is on the web has been used to train the learning model.

**[04:59 -> 05:02]** And data, so it's particularly relevant.

**[05:02 -> 05:07]** Now, first of all, first basic rule, you have to observe the data.

**[05:07 -> 05:15]** the data. So do not trust any of your colleagues that came into your room and say we have to solve

**[05:15 -> 05:20]** a problem with your knowledge of machine learning. Just use the data and providing you. It's everything

**[05:20 -> 05:26]** inside this directory. Don't waste time to open it up, but just fit it to your model. It doesn't

**[05:26 -> 05:32]** work like this. If you want to become a good machine learner and an expert, what you have to do is to

**[05:32 -> 05:36]** open the directory, look the data in the eyes.

**[05:36 -> 05:39]** And summarize the uncertainty of this data.

**[05:39 -> 05:42]** Don't trust the statistics provided by someone else.

**[05:42 -> 05:45]** And let me provide you some examples.

**[05:45 -> 05:50]** So you see here we can have a set of data that actually

**[05:50 -> 05:53]** amin appear nicely behaved.

**[05:53 -> 05:57]** So in this case, we are sampling for a subset of data

**[05:57 -> 06:02]** from a certain kind of one-on event.

**[06:02 -> 06:08]** And we see that they actually behave similarly according to, I mean, they can be approximated

**[06:08 -> 06:13]** by a straight line, so they can be fitted by a straight line. And they have similar statistics.

**[06:13 -> 06:20]** And till now, I mean, this behaves nicely. But if we look at these other set of points,

**[06:20 -> 06:25]** I mean, you see they are distributed completely different, right? But they have the same statistics.

**[06:25 -> 06:29]** And you could try to fit a line on them.

**[06:29 -> 06:31]** You will have the same kind of line.

**[06:31 -> 06:35]** Although in practice, their real distribution

**[06:35 -> 06:37]** show different patterns, right?

**[06:37 -> 06:40]** So you have really to look at the data.

**[06:40 -> 06:42]** And now of course, you might wonder,

**[06:42 -> 06:44]** well, but I might have data that are,

**[06:44 -> 06:46]** I don't know, 1,000 dimensional.

**[06:46 -> 06:48]** How can I look at them?

**[06:48 -> 06:51]** Well, you have instruments, right?

**[06:51 -> 06:53]** So last time we mentioned PCA,

**[06:53 -> 06:55]** you are super expert about it, right?

**[06:55 -> 06:57]** So please welcome Paul and analysis

**[06:57 -> 06:58]** is something that you manage.

**[06:58 -> 07:00]** So you can do something like that.

**[07:00 -> 07:03]** And you will see that there are many other kind of techniques

**[07:03 -> 07:06]** that we will talk about also in the deep learning part

**[07:06 -> 07:09]** that help you to visualize features

**[07:09 -> 07:11]** and try to understand how the data distributed.

**[07:11 -> 07:15]** So this kind of expertise is something super relevant,

**[07:15 -> 07:19]** which means that you have to look at the data.

**[07:19 -> 07:22]** First rule, look at the data, okay?

**[07:22 -> 07:27]** which means again that if you come at the exam

**[07:27 -> 07:30]** and we ask you, which data set did you use?

**[07:30 -> 07:35]** You have to know what was inside the data sets.

**[07:36 -> 07:40]** Okay, so of course, many of the data that we will use

**[07:40 -> 07:44]** are just very standard, very well-known,

**[07:44 -> 07:47]** but questions like which kind of object categories

**[07:47 -> 07:49]** do they contain because for the most of them

**[07:49 -> 07:53]** would be an image classification or action

**[07:53 -> 07:56]** recognition, which kind of action are in there.

**[07:56 -> 08:00]** How many of them do you think that if you do or know

**[08:00 -> 08:03]** an analysis on subgroups of these categories,

**[08:03 -> 08:04]** you would see different kind of results.

**[08:04 -> 08:09]** I mean, you have to acknowledge about which data you are using.

**[08:09 -> 08:13]** And we'll do these experiences also for paper presentations.

**[08:13 -> 08:15]** So understanding which data I'm presenting

**[08:15 -> 08:18]** or referring to the data that the paper was using

**[08:18 -> 08:24]** super relevant. This is another extreme, right? This is the data sounds data sets. So it's a set

**[08:24 -> 08:33]** of points that have all the same statistics, okay? Same mean, sum of deviation, and you see correlation

**[08:33 -> 08:45]** till the second decimal character, I mean, that's a conditional let's say, so 0.03, so 83.26,

**[08:45 -> 08:49]** all of them have the same, but they are completely different.

**[08:49 -> 08:54]** Okay, so again, never trust summary statistics by themselves.

**[08:54 -> 08:56]** Right?

**[08:56 -> 09:02]** And so this is all the first part, let's say, of this group of how to deal with data.

**[09:02 -> 09:08]** And then there is also how to represent the data because,

**[09:08 -> 09:13]** And I mean, this is connected to what we have been seeing now

**[09:13 -> 09:16]** because the representation of the data and the model

**[09:16 -> 09:20]** that you use to make sense and to make prediction

**[09:20 -> 09:22]** on the data are super relevant.

**[09:22 -> 09:26]** So let's stop for a minute on find the model

**[09:26 -> 09:27]** to explain the data.

**[09:27 -> 09:28]** So the last point here, right?

**[09:28 -> 09:31]** So before passing to representing the data.

**[09:33 -> 09:36]** So summarize uncertainty is already what we said.

**[09:36 -> 09:39]** statistics is okay, but better to look at the data.

**[09:39 -> 09:42]** Then search for construction,

**[09:42 -> 09:44]** for construction and variances,

**[09:44 -> 09:46]** and we will talk about prior knowledge now,

**[09:46 -> 09:48]** then find the model to explain the data.

**[09:48 -> 09:52]** So let me tell you what I mean with these expressions.

**[09:54 -> 09:56]** So now let's look at this set of points, right?

**[09:56 -> 09:58]** So we have three examples.

**[09:59 -> 10:02]** Each point is a bit dimensional point.

**[10:02 -> 10:04]** So I've just X and Y, right?

**[10:04 -> 10:06]** It's two coordinates.

**[10:06 -> 10:11]** And we would like to define a model that map from x to y, right?

**[10:11 -> 10:17]** Everything is super simple, specifically for the first plot is just,

**[10:17 -> 10:23]** I mean, we can draw a line, right, that approximately fits the points.

**[10:23 -> 10:27]** We can define a parabola for the second case, and

**[10:27 -> 10:33]** we can define a binomial of degree 3 for the third case, okay?

**[10:33 -> 10:38]** So this is first of all sort of definition that we introduce.

**[10:38 -> 10:42]** So we need to search for a function that connect x and y.

**[10:42 -> 10:44]** And depending on the data I'm facing,

**[10:44 -> 10:47]** I can start putting some kind of prior, right?

**[10:47 -> 10:49]** Because I looked at the data,

**[10:49 -> 10:53]** I kind of choose the kind of function

**[10:53 -> 10:55]** I want to use to describe the data.

**[10:55 -> 10:56]** So the first case would be,

**[10:56 -> 10:58]** pulling number degree one,

**[10:58 -> 11:00]** second, pulling number degree two,

**[11:00 -> 11:02]** the third case pulling number degree three.

**[11:02 -> 11:05]** Good, so this is already my choice, right?

**[11:05 -> 11:06]** Because I was able to look at the data.

**[11:09 -> 11:14]** Now, I might have some extra knowledge.

**[11:14 -> 11:17]** So let's look at the third what.

**[11:17 -> 11:21]** If someone tells me that the data actually come

**[11:21 -> 11:24]** from a periodic kind of procedure, I don't know,

**[11:24 -> 11:28]** we are collecting data from some industrial process

**[11:28 -> 11:30]** that it's periodic, right?

**[11:30 -> 11:34]** And so rather than using a polynomial of degree three,

**[11:34 -> 11:39]** I can choose to use a assigned function to define,

**[11:39 -> 11:41]** I mean the connection between x and y.

**[11:41 -> 11:43]** Again, it's my choice, depending on the fact

**[11:43 -> 11:45]** that I have some prior knowledge

**[11:45 -> 11:48]** about where the data from.

**[11:48 -> 11:50]** And I'm able to formalize

**[11:50 -> 11:53]** then the this function for my own goal.

**[11:55 -> 11:59]** Now, this connects to what we said before.

**[11:59 -> 12:03]** So choosing a model to connect to X and Y, in this case,

**[12:03 -> 12:06]** is specifically choosing the function, the kind of function,

**[12:06 -> 12:10]** the family of function that I want to use.

**[12:10 -> 12:13]** We'll see, for instance, that for deep learning,

**[12:13 -> 12:16]** we will specifically search for modular function

**[12:16 -> 12:19]** that combine each other because they

**[12:19 -> 12:21]** have some specific properties that

**[12:21 -> 12:23]** combines linearity and nonlinearity.

**[12:23 -> 12:27]** So there's all science behind these choices.

**[12:27 -> 12:32]** And we said deep learning revolution happened with images

**[12:32 -> 12:34]** and the structure of this architecture

**[12:34 -> 12:36]** where they find like this,

**[12:36 -> 12:40]** because images have different kind of information.

**[12:40 -> 12:42]** They have local information, which are just patterned

**[12:42 -> 12:44]** and they combine the structure,

**[12:44 -> 12:46]** that they combine in semantics.

**[12:46 -> 12:48]** So this modular kind of choice

**[12:48 -> 12:50]** and the function is related to the kind of data

**[12:50 -> 12:51]** we want to describe.

**[12:51 -> 12:54]** We'll see and we'll talk about it multiple times,

**[12:54 -> 12:57]** compositional neural networks were really, I mean,

**[12:57 -> 12:58]** that the way in which they were defined

**[12:58 -> 13:01]** were driven by the kind of data

**[13:01 -> 13:03]** that were needed to manage.

**[13:05 -> 13:07]** So the kind of data, first part of the knowledge

**[13:07 -> 13:09]** and prior knowledge, right?

**[13:09 -> 13:12]** Someone that in this specific case of the examples

**[13:12 -> 13:15]** told me, look, these data are coming

**[13:15 -> 13:17]** from a periodic kind of process.

**[13:17 -> 13:20]** And so I choose to use the sinusoidal function.

**[13:20 -> 13:23]** Now let me provide you some extra example

**[13:23 -> 13:26]** of what do I mean with prior knowledge?

**[13:27 -> 13:30]** Prior knowledge, sorry, I closed the door.

**[13:30 -> 13:32]** Otherwise I killed the person.

**[13:41 -> 13:44]** Okay, so what does it mean prior knowledge?

**[13:44 -> 13:47]** It means knowing something that can guide

**[13:47 -> 13:50]** the definition of my model and all the function later on.

**[13:53 -> 14:00]** Yeah, I turned it off and I mean what?

**[14:00 -> 14:07]** What is mute?

**[14:07 -> 14:09]** Okay.

**[14:09 -> 14:10]** Good.

**[14:10 -> 14:11]** Okay.

**[14:11 -> 14:15]** So I want to go here to this slide.

**[14:15 -> 14:19]** like, providing an example of what do I mean with prior knowledge.

**[14:19 -> 14:23]** Prior knowledge is something that can really guide the definition of my model and

**[14:23 -> 14:26]** my training process, my learning procedure.

**[14:27 -> 14:30]** I don't know if you watch this movie, which is called The Imitation Game.

**[14:30 -> 14:35]** It's a movie that tells the story of Alan Turing building the machine that actually cracked.

**[14:35 -> 14:46]** the same impression that were used by the Enigma machine during the Second World War

**[14:46 -> 14:50]** to pass messages among Germans.

**[14:50 -> 14:57]** And there is a specific part in the movie in which Turing realizes how to guide the machine

**[14:57 -> 15:03]** to find a new solution and in practice what they realized was that there were some messages

**[15:03 -> 15:05]** that we're starting always with the same word.

**[15:05 -> 15:08]** So, I mean, maybe one of the person that was

**[15:08 -> 15:11]** must be sending the messages rather than following

**[15:11 -> 15:16]** the rules of changing this initial word

**[15:16 -> 15:17]** that was in the movie.

**[15:17 -> 15:20]** They should have changed in that week or day

**[15:20 -> 15:22]** or every certain amount of hours.

**[15:22 -> 15:24]** It was just using always the same.

**[15:24 -> 15:27]** And so, to remember, Stood, of course,

**[15:27 -> 15:30]** is a dramatized version of the reality.

**[15:30 -> 15:33]** But understood that it could use that as a,

**[15:33 -> 15:42]** reference to reduce the space in which it should have searched for the solution of the decryption of the code.

**[15:42 -> 15:50]** So, if you watch the movie, the machine is huge, right? They have several parts of the machine, each of it has to select.

**[15:50 -> 15:59]** I mean, the transitional one character into, I mean, the other characters of the transitional the encryption, right? So the decryption.

**[15:59 -> 16:01]** And rather than letting all the machine work,

**[16:01 -> 16:05]** so all the parts that we're just asking practicalists

**[16:05 -> 16:08]** to represent the sub-part or the sub-set

**[16:08 -> 16:09]** of the encryptions are said,

**[16:09 -> 16:11]** they didn't have to wait so much time

**[16:12 -> 16:16]** and they could decrypt the messages later on.

**[16:16 -> 16:18]** So in practice prior knowledge, in this sense,

**[16:18 -> 16:19]** what does it mean?

**[16:19 -> 16:23]** Reducing the space in which you search the kind of function

**[16:23 -> 16:26]** that you want to use to model the data.

**[16:26 -> 16:30]** So, prior knowledge is kind and you rather than say, okay,

**[16:30 -> 16:32]** I could use any function in the world, like,

**[16:32 -> 16:35]** you look at the data, I could use also polynomial

**[16:35 -> 16:39]** of degree nine also to describe my first plot, right?

**[16:39 -> 16:43]** But since I know the data, I use a polynomial of degree one.

**[16:43 -> 16:45]** And here I use a sinosoid, right?

**[16:45 -> 16:47]** It's my choice, it's restricting the space of function

**[16:47 -> 16:50]** in which I search for my solution.

**[16:50 -> 16:53]** This is what prior knowledge means.

**[16:53 -> 16:57]** And so this replicates in this kind of example.

**[16:57 -> 17:01]** And in general, prior wood is super relevant

**[17:01 -> 17:02]** when you don't have one pump,

**[17:02 -> 17:06]** when you want to optimize for time and for computation.

**[17:06 -> 17:09]** So you want to reduce the amount of time you need to,

**[17:09 -> 17:12]** to do your model and to the final model.

**[17:12 -> 17:15]** Because of course, the other extreme is

**[17:15 -> 17:18]** I have millions, billions of data.

**[17:18 -> 17:21]** I don't care, I don't put any, I'm in the constraint.

**[17:21 -> 17:25]** I let the model understand by itself what it has to find,

**[17:25 -> 17:28]** which is usually the general rule.

**[17:28 -> 17:31]** But if you manage to reduce a little bit of space

**[17:31 -> 17:35]** and put some constraint, extra condition in the laws,

**[17:35 -> 17:38]** extra condition in the model itself,

**[17:38 -> 17:40]** then you will waste less time

**[17:40 -> 17:43]** and you will waste less computation, right?

**[17:43 -> 17:45]** So you're just guiding better your model.

**[17:45 -> 17:48]** So that's some experience that you might get

**[17:48 -> 17:50]** and can be useful when you design your model.

**[17:52 -> 17:57]** And regarding the computational capacity

**[17:57 -> 18:00]** and needs of your model, of course,

**[18:00 -> 18:04]** is again, on the basis of the choice of the machine learner,

**[18:04 -> 18:06]** so who defines the model,

**[18:06 -> 18:10]** to understand how many parameters the model should contain.

**[18:10 -> 18:13]** And again, the formulation of the model is guided

**[18:13 -> 18:15]** by this choice,

**[18:15 -> 18:18]** because I can have a general function

**[18:18 -> 18:24]** linear function as in the case of the left plot or I can choose a parametric curve. The parametric

**[18:24 -> 18:31]** curve needs four parameters, a x, a y, the x, b y, in the linear function which just have two

**[18:31 -> 18:41]** coefficient a and b, right? So again, in the right case you have to find a way to fit four parameters

**[18:41 -> 18:46]** in the first way, you have to fit just two. So it's up to the capacity of your model. So four

**[18:46 -> 18:53]** weights or two weights, same here in the case of the problem, right? But then there are also other

**[18:53 -> 18:59]** cases in which, well, you can even look at the data and then you say, yes, I would like to have

**[18:59 -> 19:09]** a simplified function, but I don't have an explicit formula to do that. And here is the place where

**[19:09 -> 19:17]** again, smart machine learner puts its experience because the point is really I need to optimize this.

**[19:17 -> 19:24]** I have to find a solution. Well, let's just change the point of view. I don't want to use the standard

**[19:24 -> 19:32]** reference, the Cartesian axis x and y. What do I do is that I move my center in the center of the

**[19:32 -> 19:35]** the data and I start describing it in four or four days.

**[19:35 -> 19:40]** And if I do it like that, I have one variable as input,

**[19:40 -> 19:43]** which is the angle theta, and one variable as output,

**[19:43 -> 19:45]** which is very useful in the functionality,

**[19:45 -> 19:48]** the magnitude of the radius, and my parameter is a.

**[19:48 -> 19:52]** So it's just I have, again, to fit one v,

**[19:52 -> 19:55]** and I have a linear function again.

**[19:55 -> 20:00]** So it is your expertise that guides the way

**[20:00 -> 20:02]** which you define the model, okay?

**[20:04 -> 20:06]** Yes, so this is the layer.

**[20:06 -> 20:11]** Okay, so this, let's say that somehow provides you example,

**[20:12 -> 20:14]** what do I mean with this first four points

**[20:14 -> 20:16]** that we have here in the list?

**[20:16 -> 20:19]** And then we go to represent the data.

**[20:19 -> 20:23]** So let's see what do I mean.

**[20:23 -> 20:26]** So I see that there is a people chart.

**[20:30 -> 20:37]** Okay, so what is the difference between a normal function and a parametric curve?

**[20:37 -> 20:41]** Well, it's just a different way to parametrize the function itself.

**[20:41 -> 20:42]** Right?

**[20:42 -> 20:47]** So, it's a different way in which you communicate to your computer how the calculation has

**[20:47 -> 20:49]** to be done.

**[20:49 -> 20:53]** Nothing too complicated.

**[20:53 -> 21:04]** No, we, our goal is not to compute one from the other.

**[21:04 -> 21:05]** It's not that.

**[21:05 -> 21:07]** It's just too different from allization.

**[21:07 -> 21:11]** Oh, this is clear.

**[21:11 -> 21:12]** Okay.

**[21:12 -> 21:13]** Good.

**[21:13 -> 21:14]** We can go ahead.

**[21:14 -> 21:16]** So represent the data.

**[21:16 -> 21:19]** Now.

**[21:19 -> 21:33]** Standard machine learning kind of solution, which means let's say all good support vector machine, all good salicy learning around the 80s and 90s, right?

**[21:33 -> 21:40]** So something that for us seems to be a very long time ago, but it's actually a machine learning.

**[21:40 -> 21:43]** What was the procedure?

**[21:43 -> 21:45]** So we have some data.

**[21:45 -> 21:51]** For instance, we want to classify images of iris,

**[21:51 -> 21:55]** two families of flowers, family one,

**[21:55 -> 21:57]** which is the one on the left, family two,

**[21:57 -> 21:59]** which is the one on the right.

**[21:59 -> 22:03]** And you, what you do is that,

**[22:03 -> 22:06]** well, you are not an expert of flower.

**[22:06 -> 22:13]** flower, you go to someone who knows it better and you ask what are the features that you expect

**[22:13 -> 22:18]** to make the difference here and the expert tells you, well, you should measure the

**[22:19 -> 22:24]** petal length and the sepal length. These are the two relevant features and then you plot them

**[22:26 -> 22:32]** to the mesh on space and you will see, I mean, you can invest in a super vector machine that

**[22:32 -> 22:36]** that provides you a line that separates these two groups.

**[22:36 -> 22:38]** So what are we doing here?

**[22:38 -> 22:42]** Well, I'm supposing that I'm not providing the data directly

**[22:42 -> 22:43]** to the model.

**[22:43 -> 22:45]** I'm first passing through a human,

**[22:45 -> 22:49]** so through an expert, that summarizes and tells me

**[22:49 -> 22:53]** what are the relevant features I should extract

**[22:53 -> 22:58]** from the data to be able to do my classification model.

**[22:58 -> 23:01]** So there is a part here which is somehow a handcrafted

**[23:01 -> 23:05]** provided you by an expert, which is the representation,

**[23:05 -> 23:09]** that then brings this information into a two dimensional plot

**[23:09 -> 23:14]** in which I can then execute and run my model,

**[23:14 -> 23:19]** that will consume the two dimensional points, right?

**[23:19 -> 23:24]** So just take use, minimum metrics with the thing used,

**[23:24 -> 23:28]** and then we'll predict the linear classifier.

**[23:28 -> 23:33]** But then, I mean, the consequence is that for a new sample,

**[23:33 -> 23:36]** depending on the fact that it happens to be on one side

**[23:36 -> 23:37]** or the other of the line,

**[23:37 -> 23:41]** you can make the predictions, family one or family two.

**[23:41 -> 23:42]** But there are some cases in which your data

**[23:42 -> 23:46]** is much more complexly organized, right?

**[23:46 -> 23:50]** So, and in this case, you can do several things.

**[23:52 -> 23:56]** The first one would be that you might go back

**[23:56 -> 24:07]** to your expert and ask whether there is a third or fourth feature you can focus on.

**[24:07 -> 24:13]** So you can invest more on finding a better representation or you can invest more

**[24:13 -> 24:16]** in finding a better classification model.

**[24:16 -> 24:20]** And the people who really are aware of us,

**[24:20 -> 24:21]** perfect the machine or other approaches,

**[24:21 -> 24:24]** you know that there are no linear solutions, right?

**[24:24 -> 24:28]** so that go behind just predicting a line.

**[24:28 -> 24:30]** So maybe you can define a complex,

**[24:30 -> 24:33]** I mean hyper-parameter or hyper-play in a number of parameters,

**[24:33 -> 24:36]** hyper-play in our complex curves somehow,

**[24:36 -> 24:38]** that divides these two groups, right?

**[24:38 -> 24:41]** So a version, more complex version

**[24:41 -> 24:43]** of the classification model that solved the task.

**[24:43 -> 24:45]** You can invest on that.

**[24:45 -> 24:47]** But as we said, we can also invest in the representation.

**[24:47 -> 24:51]** So maybe find a new one, a new axis,

**[24:51 -> 24:54]** that eventually when it is introduced in this discussion,

**[24:54 -> 24:57]** I also separated to Bruce,

**[24:57 -> 25:00]** because practically we're looking at them as projected

**[25:00 -> 25:03]** in the same plane, but now they're disentamble

**[25:03 -> 25:05]** once you add the third axis.

**[25:07 -> 25:09]** Okay, so, and this is, of course,

**[25:09 -> 25:12]** the representation part is relevant

**[25:12 -> 25:15]** because there are cases in which you actually need

**[25:15 -> 25:18]** to expand the dimensionality

**[25:18 -> 25:23]** and possibly this helps you to make the model easier.

**[25:24 -> 25:26]** And there are some other cases in which instead,

**[25:26 -> 25:29]** you want to reduce the dimensionality, right?

**[25:29 -> 25:32]** So choosing the representation is something again relevant

**[25:32 -> 25:34]** because depends again on the task.

**[25:34 -> 25:35]** So if you want to visualize,

**[25:35 -> 25:37]** let someone visualize your data,

**[25:37 -> 25:40]** maybe rather than having 100 dimensionality,

**[25:40 -> 25:43]** you want to project into a lower dimensional space.

**[25:43 -> 25:44]** And this is what you would do

**[25:44 -> 25:47]** with principal component analysis, for instance,

**[25:47 -> 25:49]** especially when you have data that apparently

**[25:49 -> 25:51]** leak in three-dimensional.

**[25:51 -> 25:54]** But actually, they can easily summarize

**[25:54 -> 25:55]** by just a hyperplane.

**[25:55 -> 25:58]** And when you have data that might appear very complex,

**[25:58 -> 26:01]** they organize in a three-dimensional space.

**[26:01 -> 26:03]** Maybe by looking at the data themselves,

**[26:03 -> 26:06]** you can understand that the set of data can be unrolled,

**[26:06 -> 26:10]** again, just in one simple plane.

**[26:10 -> 26:15]** So investing on the representation is super relevant

**[26:15 -> 26:23]** because practically to do ahead, then what we want to do and what actually deep learning model do

**[26:24 -> 26:31]** is that they combine together an optimization of the representation and of the model. So they do

**[26:31 -> 26:40]** it jointly. Okay, so ideally we would like to let a model to be able to understand at the same time

**[26:40 -> 26:44]** What are the relevant features to be extracted from the data?

**[26:44 -> 26:49]** And what is the best way to represent the model and to optimize the model to execute the task?

**[26:51 -> 26:54]** Let me provide you then again this example.

**[26:54 -> 26:58]** So it is that we want to invest on both of them at the same time.

**[26:58 -> 27:06]** And what deep networks do, so what modern AI do task, is to put in these two pieces one

**[27:06 -> 27:13]** after the other. So we don't ask a human to provide us features and

**[27:13 -> 27:18]** corrupted features to describe data. We just feed the model, I mean,

**[27:18 -> 27:23]** we just feed the model to the data to the model itself as they are.

**[27:23 -> 27:28]** The case of images is just fixed so why is we provide them everything.

**[27:28 -> 27:33]** Then we have a part of the model that shows which representation to use,

**[27:33 -> 27:37]** So which features to extract out of the image?

**[27:37 -> 27:39]** And the following part of the network

**[27:39 -> 27:42]** that understand how these features should be combined

**[27:42 -> 27:45]** to be able to make prediction.

**[27:45 -> 27:47]** So this is the reason why the model become deep,

**[27:47 -> 27:51]** because you need many layers and many stages

**[27:51 -> 27:54]** to be able to do it.

**[27:54 -> 27:58]** And yeah, so at that point, once this is strained,

**[27:58 -> 28:01]** you provide it with a new data and will tell you

**[28:01 -> 28:03]** which family of the two you're looking at.

**[28:04 -> 28:08]** And this might seem, I mean, strange,

**[28:08 -> 28:09]** but actually this is what we want to do.

**[28:09 -> 28:11]** So we want really to provide both the data,

**[28:11 -> 28:13]** don't rely on human knowledge,

**[28:13 -> 28:17]** at least in this, let's say, high level kind of procedure,

**[28:17 -> 28:19]** because you can easily think about it.

**[28:19 -> 28:21]** I mean, the data themselves,

**[28:22 -> 28:25]** they can bring certain amount of knowledge,

**[28:25 -> 28:27]** but the knowledge that you need,

**[28:27 -> 28:31]** depend on the task that you want to solve.

**[28:31 -> 28:33]** It's like when you play cards.

**[28:33 -> 28:36]** So it's the color and the seeds, they are always the same,

**[28:36 -> 28:41]** but you might play poker, you can play another kind of game,

**[28:41 -> 28:43]** and they have a different role.

**[28:43 -> 28:46]** Okay, so the data is the same,

**[28:46 -> 28:47]** but the kind of features,

**[28:47 -> 28:51]** so of information that you want to extract from the data

**[28:51 -> 28:54]** depend on the task that you want to solve.

**[28:54 -> 28:57]** And that's the reason why it makes a lot of sense

**[28:57 -> 29:02]** to let the computer, the machine, understand by itself

**[29:02 -> 29:05]** what has to be extracted from data.

**[29:05 -> 29:07]** So representation of the feature is

**[29:07 -> 29:08]** left by the model itself.

**[29:08 -> 29:13]** And then, let's say, M to M model

**[29:13 -> 29:15]** that is optimized both to extract the feature

**[29:15 -> 29:19]** and to execute the classification.

**[29:19 -> 29:24]** So the most clear, let's say way to describe the difference

**[29:26 -> 29:30]** between shallow machine learning models

**[29:30 -> 29:34]** and deep machine learning models

**[29:34 -> 29:37]** is that shallow machine learning models

**[29:37 -> 29:40]** usually do not have this part.

**[29:40 -> 29:45]** The representation is formalized by hand

**[29:45 -> 29:50]** by hand or is provided by a different part

**[29:50 -> 29:53]** and a different system or a personal differences

**[29:53 -> 29:55]** is not end-to-end.

**[29:55 -> 29:57]** Deep learning model are end-to-end in this sense.

**[29:57 -> 30:02]** Extract representation executing the model itself,

**[30:02 -> 30:04]** the task for the model.

**[30:04 -> 30:05]** Okay.

**[30:05 -> 30:09]** And then when you look inside the representation,

**[30:09 -> 30:14]** so what features are extracted from the data,

**[30:14 -> 30:21]** We will refer lots of time to one specific dataset, which is ImageNet.

**[30:21 -> 30:32]** ImageNet is the database that is still available today that was used for the challenge in 2010,

**[30:32 -> 30:38]** the international challenge, in which the first architecture that was called AlexNet,

**[30:38 -> 30:43]** actually won, first of the learning architecture won.

**[30:43 -> 30:48]** This database contained 1,000 object categories,

**[30:49 -> 30:52]** and the task was indeed being able to classify them.

**[30:52 -> 30:56]** Okay, so the images were, there was a training phase,

**[30:56 -> 30:58]** the images were provided to the model,

**[30:59 -> 31:02]** and then the output was the labels,

**[31:02 -> 31:05]** so plus one, two, three, two, plus 1,000.

**[31:05 -> 31:08]** So this image length, the taskifier,

**[31:08 -> 31:11]** is exactly the one that is used here.

**[31:11 -> 31:14]** And what I'm doing is that I'm showing you the features

**[31:14 -> 31:16]** that the model extracted.

**[31:16 -> 31:20]** So if I have to go back to the site,

**[31:20 -> 31:24]** I'm trying to dig in these part of the model,

**[31:24 -> 31:27]** because previously, I mean, we had a human

**[31:27 -> 31:29]** telling us what to measure.

**[31:29 -> 31:33]** Now, since we left the model understand by itself

**[31:33 -> 31:38]** what to extract, I would like, once the model is trained,

**[31:38 -> 31:41]** to look back inside it and trying to make sense

**[31:41 -> 31:44]** of which kind of features have been instructed.

**[31:44 -> 31:47]** And in the case of ImageNet,

**[31:47 -> 31:49]** and exactly for the logic that I told you

**[31:49 -> 31:53]** that the model is ironic or structural modular

**[31:53 -> 31:56]** multiple layers, in practice,

**[31:56 -> 31:59]** the model is at the first layers,

**[31:59 -> 32:01]** extracting just lines,

**[32:01 -> 32:04]** so different angles,

**[32:04 -> 32:10]** blob of colors, which are very basic components of images.

**[32:10 -> 32:16]** Then these kind of features are combined together

**[32:16 -> 32:21]** to start forming some structure, like the part of a wheel of a car,

**[32:21 -> 32:27]** or I don't know, yeah, some other kind of more complex pattern.

**[32:27 -> 32:33]** And then towards the end, before entering the classification part,

**[32:33 -> 32:49]** These features are combined together to form already a part of objects like here there is a big hover bird or again, I mean, the visible part of a wheel or this is the base of a cut and so on.

**[32:49 -> 32:57]** So internally, the network is extracting this kind of information and combining them together

**[32:57 -> 33:03]** before providing them the representation to the ending part of the network that is taking

**[33:03 -> 33:08]** the decision on the label.

**[33:08 -> 33:09]** Okay.

**[33:09 -> 33:14]** So now we can make a lot of efforts in defining,

**[33:17 -> 33:20]** starting the data, representing them,

**[33:20 -> 33:23]** combining everything together, choosing a model,

**[33:23 -> 33:26]** exploiting our prior knowledge, right?

**[33:26 -> 33:28]** We can try to follow, I mean, at the best,

**[33:28 -> 33:31]** because we can all these items of rules.

**[33:31 -> 33:35]** But there is one important final thing

**[33:35 -> 33:38]** that we have to check is that we need

**[33:38 -> 33:41]** to avoid data bias.

**[33:41 -> 33:43]** Okay, data bias, what does it mean?

**[33:43 -> 33:48]** It means that my data contains some spurious correlation

**[33:49 -> 33:54]** that will be inevitably used by the model

**[33:54 -> 33:56]** to take the decision.

**[33:56 -> 34:01]** So for instance, some years ago,

**[34:01 -> 34:06]** one of the computer vision task that was in study

**[34:06 -> 34:14]** trained was trying to define the kind of job that the person is doing, I mean the job of a person,

**[34:14 -> 34:20]** by just looking at the picture right at the photo. Well, you expect that what make the

**[34:20 -> 34:25]** difference is what the person is wearing, right? So if you have a helmet, if an

**[34:25 -> 34:33]** aren't wearing some specific kind of suit or so on. Well, especially by looking at the results of

**[34:33 -> 34:35]** of these models, what they discover

**[34:35 -> 34:40]** is that for instance, to separate a doctor from a nurse,

**[34:40 -> 34:43]** they were looking at the face with the goal

**[34:43 -> 34:46]** of separating women from men.

**[34:46 -> 34:49]** Okay, men, doctor, women, nurses.

**[34:49 -> 34:50]** Why?

**[34:50 -> 34:53]** Because the data on which the model was trained

**[34:53 -> 34:58]** and has a clear unbalance between a male and female

**[34:58 -> 35:01]** in the different roles, right?

**[35:01 -> 35:04]** So there might be some bias in the data.

**[35:04 -> 35:06]** So this is a kind of spurious correlation

**[35:06 -> 35:10]** between gender and the specific job.

**[35:10 -> 35:13]** That is inevitably used by the model.

**[35:13 -> 35:16]** So as I told you also in the previous lecture,

**[35:16 -> 35:21]** if the goal of the model is trying to maximize its utility,

**[35:22 -> 35:24]** minimize the number of errors,

**[35:24 -> 35:27]** really optimize the output such that it produces

**[35:27 -> 35:30]** the maximum accuracy, it will do it.

**[35:30 -> 35:32]** it's optimized for that goal.

**[35:32 -> 35:36]** And even the middle, it finds a shortcut

**[35:36 -> 35:40]** to be able to do it, it will inevitably do.

**[35:40 -> 35:42]** So if the data is dirty for some reason,

**[35:42 -> 35:47]** there is some level noise, there is some bias and this sense,

**[35:47 -> 35:49]** it will be used to make the prediction.

**[35:49 -> 35:52]** It's a shortcut, it's easy to use that information

**[35:52 -> 35:54]** to make the prediction, since I know

**[35:54 -> 35:56]** that there's a strong correlation, right?

**[35:56 -> 35:59]** So this is just an extra context

**[35:59 -> 36:03]** that is telling you that you have garbage data as input,

**[36:03 -> 36:07]** you will have garbage prediction as output.

**[36:07 -> 36:09]** You can do whatever you want with your data.

**[36:09 -> 36:13]** I mean, maybe of course, if you run a proper sub-centling

**[36:13 -> 36:16]** and rebalancing, yes, it can help.

**[36:16 -> 36:18]** But what is written in the comics

**[36:18 -> 36:20]** that rather than summing you multiplies

**[36:20 -> 36:24]** for not providing the solution, right?

**[36:24 -> 36:27]** So, and data usually are biased, okay?

**[36:27 -> 36:29]** So again, that's the reason, again,

**[36:29 -> 36:31]** why you need to open up those directory

**[36:31 -> 36:33]** and try to understand what's happening.

**[36:33 -> 36:35]** So in the data themselves as a first stage,

**[36:37 -> 36:41]** especially because AI models are everywhere

**[36:41 -> 36:44]** and many AI models might,

**[36:44 -> 36:46]** the decision that they provide,

**[36:47 -> 36:50]** they can influence some political decision

**[36:50 -> 36:52]** or some justice decision

**[36:52 -> 36:57]** or some other kind of highly relevant societal decision,

**[37:01 -> 37:03]** for instance, a few years ago,

**[37:03 -> 37:06]** there was this sort of scandal in the USA

**[37:06 -> 37:11]** where an AI model was used to score people

**[37:11 -> 37:14]** where they are called in court.

**[37:14 -> 37:18]** And so they are evaluated, if they committed a crime

**[37:18 -> 37:19]** or they did something wrong,

**[37:19 -> 37:23]** then there is a first evaluation that considers

**[37:23 -> 37:25]** if the person has to be kept in jail

**[37:25 -> 37:27]** in the period of the evaluation

**[37:27 -> 37:30]** or if it can hear, shake and go home.

**[37:30 -> 37:34]** So this algorithm was trained on historical data

**[37:34 -> 37:37]** where practically it was a standard practice

**[37:37 -> 37:40]** you just put in jail after all American people.

**[37:40 -> 37:42]** So it was clearly biased, right?

**[37:42 -> 37:46]** And the score was inevitably providing a higher risk

**[37:46 -> 37:50]** to Afro-American rather than white people.

**[37:50 -> 37:52]** But then I mean, the risk of real fun

**[37:52 -> 37:55]** was actually practically higher for white people.

**[37:55 -> 37:57]** So there was this, I mean, of course,

**[37:57 -> 38:00]** this algorithm that was called Compass,

**[38:00 -> 38:02]** it is not used anymore.

**[38:02 -> 38:06]** And but taking into consideration that in Europe

**[38:06 -> 38:11]** from August of this year, there is the AI Act

**[38:11 -> 38:14]** that is practically regulating this kind of event.

**[38:14 -> 38:16]** So AI model cannot be used for justice

**[38:16 -> 38:21]** without a human intervention or without human supervision.

**[38:21 -> 38:24]** The AI Act does not hold in the USA or in other countries.

**[38:24 -> 38:28]** So the AI act works only for European.

**[38:28 -> 38:29]** So no specific rules.

**[38:29 -> 38:31]** Of course, US has different kinds of rules.

**[38:31 -> 38:36]** And anyway, they acknowledge that this kind of flag cannot happen.

**[38:36 -> 38:40]** So but in general, the point is that AI is influencing our life.

**[38:40 -> 38:42]** So we have to make sure about how it is used.

**[38:42 -> 38:47]** So we have to have a critical look on how AI is adopted.

**[38:47 -> 38:49]** Okay, not just trust, well,

**[38:49 -> 38:52]** charge you with the clodogenin I tell you, right?

**[38:52 -> 38:54]** Don't trust them.

**[38:54 -> 38:55]** You have to verify,

**[38:55 -> 38:58]** especially when you have done a specific kind of decision.

**[38:58 -> 39:01]** And in general, the bias can appear

**[39:01 -> 39:03]** and also different other for now.

**[39:03 -> 39:05]** So the bias of the data, of course,

**[39:05 -> 39:07]** we said it's a spurious correlation,

**[39:07 -> 39:09]** but more in general,

**[39:09 -> 39:12]** the issue is that in many cases,

**[39:12 -> 39:16]** You might find yourself to train a model on specific data

**[39:16 -> 39:19]** and then test it on a different kind of data.

**[39:20 -> 39:24]** So we will see that in practice,

**[39:24 -> 39:25]** there's no free lunch theorem for that.

**[39:25 -> 39:29]** So there's no way to provide a complete

**[39:29 -> 39:32]** at 100% guarantee that your model gives you

**[39:32 -> 39:36]** the right decision when there is this big shift

**[39:36 -> 39:38]** between what you have been training on

**[39:38 -> 39:41]** and what you want to test on.

**[39:41 -> 39:45]** And so there are several examples in this case here.

**[39:45 -> 39:48]** So now, I mean, this is standard in robotics

**[39:48 -> 39:52]** because we train on synthetic data simulations

**[39:52 -> 39:54]** and then we want to apply in real life.

**[39:54 -> 39:56]** So what is called seem to real gap

**[39:56 -> 40:00]** is something super relevant nowadays.

**[40:00 -> 40:02]** It's largely studied because of course,

**[40:02 -> 40:05]** we cannot let robots to be trained in the real world.

**[40:05 -> 40:09]** They might break objects, they might break themselves.

**[40:09 -> 40:11]** So we need to train them in simulation.

**[40:11 -> 40:14]** And then they have to be adopted and be used in real life.

**[40:14 -> 40:17]** So there is this gap that we might need to close

**[40:17 -> 40:19]** and try to find a better way to the best way

**[40:19 -> 40:21]** to generalize in this sense.

**[40:21 -> 40:23]** And also this kind of example here.

**[40:24 -> 40:28]** So you might decide to train your model

**[40:28 -> 40:31]** for autonomous car navigation in Rome

**[40:31 -> 40:35]** and in perfect sunny lights, I mean, during the day.

**[40:35 -> 40:38]** But then you want to use your model in China

**[40:38 -> 40:41]** during nights or when it is snowing,

**[40:41 -> 40:43]** so it will never work, right?

**[40:43 -> 40:46]** So if there is a big domain shift,

**[40:46 -> 40:48]** your model training one domain will not work

**[40:48 -> 40:50]** in a different one.

**[40:50 -> 40:54]** And now there are foundation models nowadays

**[40:54 -> 40:56]** that are trained on millions and billions of data

**[40:56 -> 41:00]** and this issue is less evident.

**[41:00 -> 41:04]** But the sub areas of research and referring here

**[41:04 -> 41:06]** is a particular one.

**[41:06 -> 41:10]** So, I was driving and in general, let's say,

**[41:10 -> 41:14]** European-owned recognition and segmentation

**[41:14 -> 41:16]** for navigation in the real world

**[41:18 -> 41:22]** is something that maybe Google with their own car

**[41:22 -> 41:27]** can afford to collect millions and millions of data, right?

**[41:27 -> 41:29]** But many other companies, they don't.

**[41:29 -> 41:33]** And what they do is that they rely on synthetic data.

**[41:33 -> 41:36]** So what you're looking at here is not a real image,

**[41:36 -> 41:41]** is a radical visualization of a urban street.

**[41:41 -> 41:43]** And you know where does it come from?

**[41:43 -> 41:46]** It comes from GTA 5 or 6 or 7.

**[41:48 -> 41:50]** There are millions of people that are working

**[41:50 -> 41:53]** on how to make knowledge extracted from games

**[41:53 -> 41:55]** to be applied in real world.

**[41:55 -> 41:59]** Because they are cheap, because they are synthetic.

**[41:59 -> 42:02]** They don't need a human to annotate them.

**[42:02 -> 42:05]** they are pre-emnotated because they were synthesized.

**[42:05 -> 42:08]** So again, seem to real gap.

**[42:08 -> 42:11]** Of course, simulation is becoming better and better,

**[42:11 -> 42:12]** closer and closer to the real world,

**[42:12 -> 42:17]** more 3D realistic, but it's not the real life.

**[42:17 -> 42:19]** And the model trained there might still have a gap

**[42:19 -> 42:21]** to be used in real life.

**[42:21 -> 42:23]** And for us, as human, that's standard

**[42:23 -> 42:25]** because we are trained in situations.

**[42:25 -> 42:28]** I mean, that the pilots are trained to,

**[42:28 -> 42:32]** they learn how to drive an airplane just with simulators.

**[42:32 -> 42:34]** For us, it's normal.

**[42:34 -> 42:37]** I mean, human are able to generalize.

**[42:37 -> 42:40]** Machines still not be able to generalize

**[42:40 -> 42:45]** unless they see millions or billions of data.

**[42:45 -> 42:47]** For us, as human, you're still able to adapt

**[42:47 -> 42:50]** to new condition, generalize knowledge,

**[42:50 -> 42:52]** reuse knowledge for a completely different area

**[42:52 -> 42:55]** to be applied on a new task.

**[42:55 -> 42:57]** Adaptation, continual learning,

**[42:57 -> 43:00]** these are areas where there is big gap of research

**[43:00 -> 43:03]** because it's still not clear a solution in this sense.

**[43:03 -> 43:05]** Deep learning models also the most modern AI

**[43:05 -> 43:07]** is not efficient at all.

**[43:07 -> 43:09]** Our brain is super efficient.

**[43:09 -> 43:13]** So, I mean, we are still far from AI

**[43:13 -> 43:16]** that will meet humans in this sense, just to assure you.

**[43:17 -> 43:23]** But yeah, so this was actually the last slide.

**[43:23 -> 43:26]** I was supposed to get to the last lecture

**[43:26 -> 43:30]** And we are getting to it now today.

**[43:30 -> 43:32]** So we went through the course,

**[43:32 -> 43:36]** we went to a high level definition of artificial intelligence

**[43:36 -> 43:38]** and she learned even deep learning.

**[43:38 -> 43:41]** How does it mean to build a model at least at high level?

**[43:41 -> 43:43]** How do we deal with data?

**[43:43 -> 43:45]** What is representing the data?

**[43:45 -> 43:46]** What does it mean?

**[43:46 -> 43:49]** What does it mean deep learning when we combine

**[43:49 -> 43:52]** representation learning and models at the same time?

**[43:52 -> 43:54]** And what are the risks of data bias

**[43:54 -> 43:57]** and it involves unfairness, right?

**[43:57 -> 44:00]** And again, what I really would like him to become

**[44:00 -> 44:03]** is a real machine learner, not just someone who plays

**[44:03 -> 44:05]** with tools that someone has built for you

**[44:05 -> 44:08]** and you didn't know absolutely anything about it

**[44:08 -> 44:13]** and they, the inherent wide function, okay?

**[44:13 -> 44:17]** But to do that, there is an important part

**[44:17 -> 44:21]** to be expert on which is probabilistic reasoning.

**[44:21 -> 44:23]** I know I'm sorry,

**[44:23 -> 44:24]** improbability is boring,

**[44:24 -> 44:26]** statistics is boring,

**[44:26 -> 44:28]** but we need a bit of mathematics

**[44:28 -> 44:31]** because all the decision that

**[44:31 -> 44:34]** our model will do are based on statistics.

**[44:34 -> 44:36]** Nothing more than that.

**[44:36 -> 44:38]** Probability is statistics,

**[44:38 -> 44:42]** so we have to manage at least a bit of the basics.

**[44:42 -> 44:45]** In theory, I mean this bit of basics,

**[44:45 -> 44:46]** you are supposed to have them from

**[44:46 -> 44:49]** high school or previous courses,

**[44:49 -> 44:54]** but I prefer to refresh them here. I mean just to focus on what is relevant for our goals.

**[44:56 -> 45:04]** Okay, so I would say that I now pass to the next slide, unless there are questions. I mean,

**[45:04 -> 45:07]** I will pass anyway and also take questions if you need.

**[45:19 -> 45:21]** you

**[45:49 -> 45:56]** Okay.

**[45:56 -> 45:59]** So we'll go ahead for another half an hour.

**[45:59 -> 46:04]** Then I'll take a break, a serious break.

**[46:04 -> 46:08]** Okay.

**[46:08 -> 46:10]** So this was just five minute break.

**[46:10 -> 46:12]** Which, what is this?

**[46:12 -> 46:14]** Oh, busted.

**[46:14 -> 46:15]** Here.

**[46:15 -> 46:16]** Okay.

**[46:16 -> 46:17]** Here.

**[46:17 -> 46:18]** Okay.

**[46:18 -> 46:27]** So, as we said, we need some basic knowledge about probability because machine learning

**[46:27 -> 46:29]** is all about making predictions.

**[46:29 -> 46:33]** And you see here some examples.

**[46:33 -> 46:43]** So when you need to, I mean, have a diagnosis in practice from data, from medical data,

**[46:43 -> 46:46]** you want to make a prediction on the basis of the, for instance, herd attack,

**[46:49 -> 46:54]** medical records. And so when you make the prediction, you're actually making it with a probability,

**[46:54 -> 47:00]** right? So we are saying you have probability higher than 80% that you will have an R to tag

**[47:00 -> 47:07]** due to agency. So the feature that you started on the data. Another detection is the same. So

**[47:07 -> 47:18]** you want to assess how likely is that some measurement from an urban jet engine would indicate that

**[47:18 -> 47:25]** the engine is working in normal condition or not. Anomaly detection is there's a lot of

**[47:25 -> 47:33]** research and application in this kind of area, not only for time series or sequences of information

**[47:33 -> 47:37]** and like in the case of the airplane recordings,

**[47:37 -> 47:39]** but also videos because you want to,

**[47:39 -> 47:42]** for instance, again, autonomous application,

**[47:42 -> 47:45]** autonomous driving, you want to detect that,

**[47:45 -> 47:48]** an animal is crossing the streets and you want to break,

**[47:48 -> 47:52]** that there is an almost object that should not be

**[47:52 -> 47:56]** in a specific place, airports, you want to identify

**[47:56 -> 47:57]** anomalies, both in terms of objects,

**[47:57 -> 47:59]** in terms of action of people,

**[47:59 -> 48:03]** in reinforcement learning again, right?

**[48:03 -> 48:05]** So we've mentioned about reinforcement learning

**[48:05 -> 48:09]** as the kind of learning strategy you would use for robots, right?

**[48:09 -> 48:14]** So you want your agents to act intelligently in an environment.

**[48:14 -> 48:18]** And this means that it needs to think about the probability

**[48:18 -> 48:24]** of getting a higher reward under each of the available actions.

**[48:24 -> 48:26]** So it has to make a move, right?

**[48:26 -> 48:29]** So each of the possible move creates

**[48:29 -> 48:32]** and expectation, what would be the reward, right?

**[48:32 -> 48:35]** And so then it will take as a next decision

**[48:35 -> 48:38]** the one that will bring to the highest the world possible.

**[48:38 -> 48:40]** Or if these are the recommended system,

**[48:40 -> 48:43]** like the example here, there's an example of books,

**[48:43 -> 48:48]** but it's the same that we mentioned for Netflix, right?

**[48:48 -> 48:53]** So suggesting the new movie to some client, right?

**[48:54 -> 48:57]** The next movie he or she has to watch.

**[48:57 -> 49:01]** And this means providing something and providing a new movie

**[49:01 -> 49:04]** with that you expect to have a high probability

**[49:04 -> 49:06]** that the person would like.

**[49:06 -> 49:08]** OK, so everything is based on probability,

**[49:08 -> 49:12]** even because we are managing data.

**[49:12 -> 49:17]** If data are usually noisy, so the real life data are noisy.

**[49:17 -> 49:19]** Some of them can be missing.

**[49:19 -> 49:22]** The knowledge in general is uncertain

**[49:22 -> 49:25]** because there might be multiple causes that

**[49:25 -> 49:27]** into the same effect.

**[49:27 -> 49:32]** Yeah, so there can be different condition.

**[49:32 -> 49:36]** Think also about translating from one language to another.

**[49:36 -> 49:39]** So if you want to do the example of the language.

**[49:39 -> 49:42]** So there's not one single way to evaluate the sentence.

**[49:42 -> 49:45]** So there's not one single way to those

**[49:45 -> 49:48]** later single word in different languages.

**[49:48 -> 49:51]** So it's everything in a matter of probabilities.

**[49:51 -> 49:59]** what GPT does is that it reads what you wrote, it reads the prompt, and then it provides you

**[49:59 -> 50:07]** in an outer regressive way the next word, each of them with the highest probability given the

**[50:07 -> 50:14]** words that it's so before. So the answer is actually just going ahead producing words on the basis of

**[50:14 -> 50:21]** the prompt or the question that you provided. So everything is based on probability and

**[50:21 -> 50:26]** they can also answer them outputs because of course I mean they can be a different condition

**[50:26 -> 50:31]** where you have a level of uncertainty. So everything is based on probability which allows

**[50:31 -> 50:39]** to summarize the uncertainty of the world. So what is the sample space? It's just here we call it

**[50:39 -> 50:46]** omega is the set of possible outcomes of a solar problem experiments. So you roll a dice and you

**[50:46 -> 50:52]** might have six numbers. You flip a coin and you can have had a tape, right? So you flip a coin

**[50:52 -> 50:56]** three times and then you have to enumerate all the possibilities that you can have,

**[50:57 -> 51:05]** have in terms of had or tape. Then you can have probabilities where the sample space is discrete,

**[51:05 -> 51:11]** like in these cases or the condition in which the sample space is continuous. So you have

**[51:11 -> 51:19]** like a person age, positive integer, person age, positive reals and so on and so on and then event

**[51:19 -> 51:26]** is a subset of the sample space, right? So what we search generally is the probability of a particular

**[51:26 -> 51:34]** event. So out of this space of all the possibilities, we are searching for the probability of a certain

**[51:34 -> 51:41]** subset of the space, so a certain event to happen. And of course, you know, I mean, the probability

**[51:41 -> 51:46]** here starting to draw something in terms of visualization, we have the sample space,

**[51:46 -> 51:51]** we have subset of the sample space, which is the event we mentioned before. And you know that

**[51:51 -> 51:56]** probability is an alert between 0 and 1, right? It's just a continuous variable that expressed

**[51:56 -> 52:05]** the fact that that's an event is kind of core with the significant frequency much higher with

**[52:05 -> 52:10]** respect to others for instance and so we have higher probability that gets to one or probably

**[52:10 -> 52:17]** the zero if the event cannot happen. So you see we have the event space that whose area is totally

**[52:17 -> 52:23]** one and then we have a subset of the event whose area is lower beta within 0 and 1.

**[52:26 -> 52:32]** And these are the first let's say axiom. Of course the probability cannot go as more than 0 or higher

**[52:32 -> 52:40]** than 1. So the n to set is 0 for the data that we think of the whole space is 1. And we can draw

**[52:40 -> 52:46]** the event diagram and discuss about the probability of two events happening together.

**[52:46 -> 52:54]** So, event A and event B, the union of this two events, how is the kind of probability

**[52:54 -> 53:03]** of the present jointly is the probability of A plus the probability of B minus the probability

**[53:03 -> 53:05]** of the intersection, right?

**[53:05 -> 53:12]** Because if you don't subtract the intersection, practically you are counting the overlapping

**[53:12 -> 53:13]** parts twice.

**[53:13 -> 53:15]** So at least you remove it once.

**[53:15 -> 53:20]** So you have the union of the probability of A and B.

**[53:20 -> 53:22]** So these are three axioms.

**[53:22 -> 53:25]** There are other ways in which probability can be defined.

**[53:25 -> 53:26]** There is fuzzy logic.

**[53:26 -> 53:29]** There is no monotonic reasoning.

**[53:29 -> 53:31]** I mean, there are other kind of way

**[53:31 -> 53:33]** which we can define probabilities,

**[53:33 -> 53:37]** but that's the standard axiom we usually rely on.

**[53:37 -> 53:40]** And for sure, I mean, as the theory was saying,

**[53:40 -> 53:43]** if you gamble using them,

**[53:43 -> 53:45]** you can be unfairly exploited by an opponent

**[53:45 -> 53:47]** using another system among the others

**[53:47 -> 53:49]** that are most listing, right?

**[53:49 -> 53:52]** So it means that they are reliable, we can trust them.

**[53:52 -> 53:56]** So these are our axioms, very simple ones.

**[53:58 -> 54:01]** Then I mean, some more visualization

**[54:01 -> 54:04]** and formalization in terms of random variables.

**[54:04 -> 54:07]** So random variable is a function.

**[54:07 -> 54:11]** So real value random variable is just X,

**[54:11 -> 54:15]** which means the function that breaks from the space

**[54:15 -> 54:16]** to a value,

**[54:16 -> 54:21]** which the value represent our co-opability in practice.

**[54:21 -> 54:24]** And so you see in just the example below,

**[54:24 -> 54:25]** random variable examples

**[54:25 -> 54:28]** where the omega sort of space is discrete.

**[54:29 -> 54:33]** So X of W here is true if a random,

**[54:33 -> 54:37]** if a random person from a certain class is female,

**[54:37 -> 54:39]** or I mean, you can see this example in the sense.

**[54:39 -> 54:41]** So when we refer to random variable,

**[54:41 -> 54:44]** it's just this function that brings from the space

**[54:44 -> 54:49]** of the events to the real data that represents the probability.

**[54:49 -> 54:55]** Now, so we can do this class completely starting

**[54:55 -> 54:58]** to talk about the Gaussian distribution, the Poisson

**[54:58 -> 55:02]** distribution, and looking at the formulas of this distribution

**[55:02 -> 55:05]** and saying, OK, and maybe you've heard about that.

**[55:05 -> 55:07]** But also, that's just the formulation

**[55:07 -> 55:08]** of the probability distribution.

**[55:08 -> 55:12]** And then we say, all our data belong according

**[55:12 -> 55:15]** to this distribution, and we set both points out of that.

**[55:15 -> 55:17]** Which means that someone told us

**[55:17 -> 55:19]** that the data were behaving according

**[55:19 -> 55:21]** to those distribution.

**[55:21 -> 55:23]** Thus, I mean, this kind of description

**[55:23 -> 55:26]** is what I would call the Bayesian kind of approach, right?

**[55:26 -> 55:28]** So it's like really, I mean,

**[55:29 -> 55:31]** going into the theory of probability,

**[55:31 -> 55:34]** formalization of the probability distribution,

**[55:34 -> 55:36]** will be a little bit more practical.

**[55:36 -> 55:39]** So we'll go to the frequentist approach.

**[55:39 -> 55:41]** So we just want to look at the data,

**[55:41 -> 55:45]** observe what we have in our dataset,

**[55:45 -> 55:47]** and draw to make sense out of this data

**[55:47 -> 55:49]** and try to obtain probabilities

**[55:49 -> 55:52]** out of this observation that we do.

**[55:52 -> 55:56]** So like probabilities from events in these cases, right?

**[55:56 -> 56:01]** So I have to draw two numbers between one and four

**[56:02 -> 56:05]** and the random variable I'm focusing on,

**[56:05 -> 56:14]** want to consider is their sum. So I have to extract two numbers between 1 and 4. So I

**[56:14 -> 56:20]** saw doing some experiments and I consider what I observed. So these are all the possibilities

**[56:20 -> 56:27]** I can get. So I can get 1, 1, so the two numbers, 1, 2, 1, 3, 1, 4, 2, 1, 2, 3, so I try to see

**[56:27 -> 56:32]** all of them. And then in practice, so these are all the possible pairs and then I sum them

**[56:32 -> 56:35]** because my random variable is their sum.

**[56:35 -> 56:42]** So, one plus one is two, one plus two is three, one plus three is four.

**[56:42 -> 56:45]** So this is the random variable and focusing on.

**[56:45 -> 56:50]** And then I say, okay, what's the probability of this specific event of finding a two?

**[56:50 -> 56:55]** Well, out of all the possibilities, two appears only once.

**[56:55 -> 57:00]** So out of the 16 possibility, I listed here, two is one over 16.

**[57:00 -> 57:05]** three appears twice, one here and one here.

**[57:06 -> 57:09]** So, well, it's two over 16, right?

**[57:09 -> 57:13]** So this is what we are doing.

**[57:13 -> 57:17]** It's just obtaining from the data some ratios,

**[57:17 -> 57:20]** some fraction that then is immediately translated

**[57:20 -> 57:23]** into the sense of probability, right?

**[57:23 -> 57:25]** So very simple, just observation on time.

**[57:25 -> 57:31]** So this is the strategy we take.

**[57:31 -> 57:34]** And so when we talk about probability distribution

**[57:34 -> 57:37]** for us is tables is not the function of the Gaussian.

**[57:37 -> 57:39]** So on support, but it's just a table.

**[57:39 -> 57:41]** So the probability of temperature,

**[57:41 -> 57:43]** well, now we are simply fine.

**[57:43 -> 57:45]** We are considering just two possibilities

**[57:45 -> 57:47]** or just a pattern in kind of description.

**[57:47 -> 57:49]** It can be a whole of cold and the probability

**[57:49 -> 57:53]** of once you do some observations, half of.

**[57:53 -> 57:57]** The weather, probability of the weather can be now surviving in four groups,

**[57:57 -> 58:01]** sun, rain, fog, and meteor, and you have the corresponding probability.

**[58:01 -> 58:05]** Now, of course, if you never observed one of the possibilities,

**[58:05 -> 58:07]** then the probability is zero.

**[58:07 -> 58:13]** And what you expect is that the summation of all these numbers brings you to one, right?

**[58:13 -> 58:20]** So the sum is the covering whole space, so it has to be one.

**[58:20 -> 58:25]** So yeah, we are just managing tables.

**[58:25 -> 58:29]** And we can also have the joint probabilities, right?

**[58:29 -> 58:33]** So if you want to consider two variables at the same time,

**[58:33 -> 58:35]** then you have a table with more colors.

**[58:35 -> 58:37]** Okay, that's it, nothing more than that.

**[58:39 -> 58:44]** So then we observe this table

**[58:44 -> 58:47]** and we try to answer some question.

**[58:47 -> 58:52]** So if I have these joint probability,

**[58:52 -> 58:55]** okay, for temperature and weather

**[58:55 -> 58:58]** and this is the probability I get,

**[58:58 -> 59:01]** then my question is, what is the probability

**[59:01 -> 59:04]** that is hot and sunny?

**[59:05 -> 59:07]** This is for you.

**[59:07 -> 59:08]** I want to hear a number.

**[59:12 -> 59:15]** What is one?

**[59:15 -> 59:15]** Why?

**[59:17 -> 59:23]** Now the probability that is hot and sunny is written in the table.

**[59:23 -> 59:27]** 0 is the first line.

**[59:27 -> 59:29]** What is the probability to see how they're signing together?

**[59:29 -> 59:31]** It's the first form.

**[59:31 -> 59:36]** 0 is the probability that is hot?

**[59:36 -> 59:40]** 0 is the number.

**[59:40 -> 59:42]** Tell me just the number.

**[59:42 -> 59:44]** 0 is the number.

**[59:44 -> 59:56]** the summation of the first two rows. Okay, so 0.4 plus 0.1. And what is the probability that is hot or sunny? So, or sunny.

**[59:56 -> 60:08]** Correct. Is the sum of the first three rows, right? Because you are also admitting the possibility that is sunny but not hot.

**[60:08 -> 60:09]** Okay.

**[60:09 -> 60:10]** Good.

**[60:10 -> 60:19]** So that's the way which we reason on probabilities, right?

**[60:19 -> 60:21]** Looking at the tables.

**[60:21 -> 60:29]** And when you want to go from a joint distribution to the distribution of only one of the variables,

**[60:29 -> 60:33]** then it's a matter of extracting the information out of the table.

**[60:33 -> 60:37]** And this is generally said to marginalize.

**[60:37 -> 60:42]** And what we are calculating, so Planck-Bouglot joint to these probabilities here, these are

**[60:42 -> 60:44]** called the marginals.

**[60:44 -> 60:46]** So this is a joint probability.

**[60:46 -> 60:50]** This is the marginal distribution for each of the variables.

**[60:50 -> 60:55]** And they are cool like this because usually, this decision we're writing notes at the

**[60:55 -> 60:56]** margin of the book.

**[60:56 -> 60:58]** So they are the marginals.

**[60:58 -> 61:05]** And so in practice it consists of just summing up what you have in the table here, right?

**[61:05 -> 61:09]** So hard to your pipe and close your pipe and structure.

**[61:09 -> 61:12]** Very simple.

**[61:12 -> 61:16]** And now the conditional distribution.

**[61:16 -> 61:19]** So we can have two events, one condition by the other.

**[61:19 -> 61:26]** So the probability of adding A given B, so for video observing A given the fact that

**[61:26 -> 61:34]** observed the B is equal to the joint probability of A and B divided by the marginal B.

**[61:35 -> 61:39]** So we will see that this is part of an important part of the Bayesian theorem,

**[61:39 -> 61:45]** but for the moment, let's just consider this, that connect conditional probability with marginal

**[61:45 -> 61:51]** and joint probability. How do I use it? Well, if you look again at the table, the probability

**[61:51 -> 61:57]** that the weathery sun, given the fact that the temperature is cold, then we have the

**[61:57 -> 62:04]** joint probability. So the two present together, cold and sun, which was the serial tool. And the

**[62:04 -> 62:12]** marginal that we said is obtained by summation of the two joint distribution in this case of,

**[62:12 -> 62:17]** so here we are actually marginalised right from the joint probability to the marginal.

**[62:17 -> 62:20]** So this is obtained by 0 to 5 and then you do the calculation.

**[62:22 -> 62:29]** Now this rule is, and this calculation here is exactly the same I'm showing you here in a

**[62:29 -> 62:35]** small font. So even if you don't read it, don't, you can look at the PDF later on.

**[62:35 -> 62:40]** But I'm just telling you that it's just repeating what we saw before for two different variables.

**[62:40 -> 62:45]** What I want to do here is tell you how to, I mean, perform exactly the same calculation,

**[62:45 -> 62:52]** but just looking at the table, it might be easier because you can take this marginal,

**[62:52 -> 63:01]** you can look at the subset of the marginal subset of the joint where you focus only on cold, for instance, right?

**[63:01 -> 63:10]** And then you see that this is 0.2 and 0.3, but the conditional distribution with the conditional probability is a probability per se,

**[63:10 -> 63:15]** which means that all its possibility has to sum up to 1.

**[63:15 -> 63:16]** So what does it mean?

**[63:16 -> 63:19]** Is that when you extract this type of table,

**[63:19 -> 63:21]** then you have to renormalize.

**[63:21 -> 63:22]** That's it.

**[63:22 -> 63:25]** So you can do it through this calculation we saw before,

**[63:25 -> 63:28]** or you can do it just by looking at the table.

**[63:28 -> 63:35]** And yeah, so this is just a practical strategy.

**[63:35 -> 63:41]** And so what we are doing in practice

**[63:41 -> 63:43]** is that when we make a prediction,

**[63:43 -> 63:45]** what we're doing is really calculating

**[63:45 -> 63:49]** the conditional probability solution, right?

**[63:49 -> 63:52]** Because given the fact that we saw those data,

**[63:52 -> 63:55]** what's the probability that for this new sample,

**[63:55 -> 64:00]** the label is cut or the label is done, right?

**[64:00 -> 64:03]** So what we do is actually in the prediction,

**[64:03 -> 64:09]** what we're doing is computing condition probabilities. The probability to be on time given the fact that

**[64:09 -> 64:16]** the data is not aboard any accident, so we observe the data themselves and so on and so forth. So,

**[64:16 -> 64:22]** of course, the more condition you have, then they can be stopped, I mean, here in the right part

**[64:22 -> 64:25]** of your probability and so you have to calculate this condition.

**[64:25 -> 64:35]** Well, just to check if you are awake, what is the probability of winter?

**[64:35 -> 64:48]** We are just, so the point of W here is just, yeah, summing up the right book, the world

**[64:48 -> 64:49]** winter is there, right?

**[64:49 -> 64:51]** So we just have to sum these, these.

**[64:51 -> 64:54]** But yeah, so it's a marginal.

**[64:54 -> 64:57]** But then what's the probability of sun?

**[64:57 -> 64:59]** Here I'm just providing some extra examples.

**[64:59 -> 65:06]** So here is considering where sun is and I'm summing them up.

**[65:06 -> 65:09]** Probate of rain.

**[65:09 -> 65:12]** Now you can do the same exercise.

**[65:12 -> 65:16]** So you go through a table, look only at rain,

**[65:16 -> 65:17]** but you can do also the other way around.

**[65:17 -> 65:20]** Once you have observed the data and you

**[65:20 -> 65:22]** realize that the weather is,

**[65:22 -> 65:28]** you decided that someone provided you the data in this form and the weather has only two possible

**[65:28 -> 65:35]** behaviors. So, sun and rain, then you can express the probability of rain as 1 minus the probability of

**[65:35 -> 65:43]** sun. The probability of winter of W in general, I mean given the fact that this winter is hot,

**[65:44 -> 65:50]** you can, I leave them here just as an exercise because of course, as we said before, you can

**[65:50 -> 65:52]** and extract them from the table,

**[65:52 -> 65:54]** but then you have to renormalize.

**[65:54 -> 65:57]** Same here, you have to renormalize.

**[65:57 -> 65:59]** It's nothing too complicated.

**[65:59 -> 66:02]** And what we saw before,

**[66:02 -> 66:05]** so expressing the conditional probability

**[66:05 -> 66:09]** as the ratio between the probability,

**[66:09 -> 66:11]** the joint probability and the marginal,

**[66:11 -> 66:14]** can also be written in a different way.

**[66:14 -> 66:17]** So rather than putting the marginal at the denominator,

**[66:17 -> 66:22]** you can take the margin and bring it on the left of the equation,

**[66:22 -> 66:26]** and you have that the joint probability is a multiplication

**[66:26 -> 66:30]** between the margin and probability and the conditional probability.

**[66:30 -> 66:34]** So if someone provides you with these two tables,

**[66:34 -> 66:40]** then you can get the joint by just doing the useful

**[66:40 -> 66:44]** probability on the basis of the goal.

**[66:44 -> 66:50]** And if you have many variables, you can always decompose them

**[66:50 -> 66:52]** by using the chain pool.

**[66:52 -> 66:54]** So you can have the probability of the first,

**[66:54 -> 66:57]** multiplied by the probability of the second, given the first,

**[66:57 -> 66:58]** and so on and so forth.

**[66:58 -> 67:01]** And so yes, you have this high level general pool.

**[67:01 -> 67:04]** Now, all these are practically parts

**[67:04 -> 67:10]** of what we call the bias rule or bias theorem.

**[67:10 -> 67:12]** So I was spending some negative word

**[67:12 -> 67:16]** before to the bias and interpretation of probability.

**[67:16 -> 67:20]** But the truth is that the bias rule,

**[67:20 -> 67:23]** bias theorem is one of the most important one

**[67:23 -> 67:27]** for statistics and for making prediction in our case.

**[67:27 -> 67:30]** So a reverend bias, if you never saw him,

**[67:30 -> 67:35]** is the library, formulated the equation we are looking at here,

**[67:35 -> 67:39]** which is in practice just rewriting the same thing

**[67:39 -> 67:42]** we saw before into different order.

**[67:42 -> 67:44]** So the joint probability,

**[67:44 -> 67:48]** minus and y can be written as the probability of x

**[67:48 -> 67:51]** given y, multiplied by the probability of y

**[67:51 -> 67:53]** and the probability of y given as

**[67:53 -> 67:57]** multiplied by the marginal and x, so purex.

**[67:57 -> 67:59]** And so we can just divide and obtain this expression.

**[68:01 -> 68:04]** And that's the core, one of the core rules

**[68:04 -> 68:08]** because in practice, I mean, what we have generally

**[68:08 -> 68:10]** is observation, evidences,

**[68:10 -> 68:15]** And we want to predict, make a prediction.

**[68:15 -> 68:18]** And generally, the relation between the cause

**[68:18 -> 68:23]** and the effect of observation and hypothesis,

**[68:23 -> 68:25]** one of the two is easier to measure.

**[68:25 -> 68:28]** The other has to be estimated in general.

**[68:28 -> 68:31]** So that's exactly what we have.

**[68:31 -> 68:35]** So the fact that we can switch between x and y

**[68:35 -> 68:40]** and use the rule is super important.

**[68:40 -> 68:45]** And in general, what we have is that we don't really

**[68:45 -> 68:49]** use the whole bias rule.

**[68:49 -> 68:51]** We use a subpart of it.

**[68:51 -> 68:55]** Because rather than recalculating the probability,

**[68:55 -> 68:58]** we use this rule to produce scores.

**[68:58 -> 69:03]** And then we compare the scores among each other.

**[69:03 -> 69:04]** Look at this.

**[69:04 -> 69:08]** So now we remove the denominator.

**[69:08 -> 69:13]** And rather than having an equality, we have a proportionality.

**[69:13 -> 69:16]** This is the symbol of proportionality.

**[69:16 -> 69:19]** So now this is not the probability anymore.

**[69:19 -> 69:24]** So by its definition, all the events do not sum up to 1.

**[69:24 -> 69:27]** It becomes a score because we are removing the denominator.

**[69:27 -> 69:30]** This is usually called posterior.

**[69:30 -> 69:32]** This is usually called likelihood.

**[69:32 -> 69:35]** And this is usually called prior.

**[69:35 -> 69:41]** And it goes back to prior knowledge somehow, because if you know how the data are distributed,

**[69:42 -> 69:48]** you will need less data to reliably make this scoring evaluation. We'll get back there.

**[69:48 -> 69:55]** But this is indeed connected to what I called before prior knowledge. You know something about

**[69:55 -> 70:02]** from where the data were extracted, and the phenomena that generated it, and so the probability of x of

**[70:02 -> 70:03]** of the data themselves.

**[70:06 -> 70:08]** So this is how we use it, right?

**[70:08 -> 70:11]** So practical application,

**[70:11 -> 70:14]** we have this kind of prediction, right?

**[70:14 -> 70:18]** We want to predict the probability of a certain hypothesis

**[70:18 -> 70:20]** given the fact that we have some evidence

**[70:20 -> 70:23]** like diagnostics application, right?

**[70:23 -> 70:28]** So I have an eddy and I want to understand if I have the flu.

**[70:28 -> 70:31]** So what you do is that you go to consider

**[70:31 -> 70:33]** What is the probability that the population,

**[70:33 -> 70:35]** people can have a headache?

**[70:35 -> 70:37]** The probability that the population can have a flu,

**[70:37 -> 70:39]** and the probability that you get a headache,

**[70:39 -> 70:42]** considering the fact that you have a flu, right?

**[70:42 -> 70:44]** That's, I mean, kind of description

**[70:44 -> 70:46]** that you can easily measure.

**[70:46 -> 70:47]** You know you have the flu

**[70:47 -> 70:50]** because you have a metric to evaluate your temperature.

**[70:50 -> 70:52]** And then as an effect, you feel,

**[70:52 -> 70:55]** I mean, your feeling is that of having a headache.

**[70:55 -> 70:58]** And now you can try to do, I mean, calculate the other

**[70:58 -> 71:07]** conditional because then you can measure about a heavy probability that tells you that you have a flu given the fact that you have a

**[71:07 -> 71:08]** night.

**[71:08 -> 71:13]** Same here, I mean, there's another calculation for the case of

**[71:14 -> 71:20]** Manugitis and CIP link how do you affect the codes connected to each other here? It is provided with a

**[71:20 -> 71:26]** I mean, intermediate step because then you need to calculate the denominator.

**[71:26 -> 71:34]** So this marginal here, you have to obtain from the calculation between the condition

**[71:34 -> 71:35]** of the marginal.

**[71:35 -> 71:41]** And so in practice, since the data provided in this form, you can use it to make this

**[71:41 -> 71:42]** calculation.

**[71:42 -> 71:47]** But it's nothing more again than the application of the bias rule.

**[71:47 -> 71:52]** Now, the biased rule can seem something that, again,

**[71:52 -> 71:54]** it's very theoretical, it's written in book.

**[71:54 -> 71:58]** Of course, you can use it for some simple exercises,

**[71:58 -> 72:03]** but it's, again, something very, very lively, right?

**[72:04 -> 72:08]** So think about the fact that you want to go to the casino

**[72:08 -> 72:10]** and play poker with money, right?

**[72:10 -> 72:13]** So you want to count the card if you are able to do that

**[72:13 -> 72:15]** and fast enough.

**[72:15 -> 72:18]** And indeed, this is what, again, I'm providing an example

**[72:18 -> 72:20]** of a movie, another movie.

**[72:20 -> 72:23]** This movie is called 21.

**[72:23 -> 72:25]** And there is a professor of statistics

**[72:25 -> 72:28]** teaching their students just the basic of statistics.

**[72:28 -> 72:30]** And then in practice, they form a team

**[72:30 -> 72:33]** and they go to Las Vegas and they win a lot of money.

**[72:33 -> 72:36]** And they use the bias rule, practically.

**[72:36 -> 72:37]** I mean, one of their tools.

**[72:37 -> 72:39]** And there is a part of the movie

**[72:39 -> 72:41]** where the professor is explaining,

**[72:41 -> 72:45]** or at least is providing a game to the students.

**[72:45 -> 72:48]** a game that can be easily sold on the base of the price for.

**[72:48 -> 72:51]** So the game is a multi-o game show problem.

**[72:51 -> 72:54]** How does it work?

**[72:54 -> 72:57]** Well, there's a TV game show where a contestant select

**[72:57 -> 73:01]** one out of three doors behind one of the door,

**[73:01 -> 73:04]** there is a price, and behind that, the two,

**[73:04 -> 73:06]** there are no prices, right?

**[73:06 -> 73:09]** So the contestant selects a door,

**[73:09 -> 73:13]** and then the game show host opens one of the two remaining

**[73:13 -> 73:19]** doors and reveals that there's no price behind it, behind the one that he opened.

**[73:19 -> 73:27]** Then the host asked the contestant whether he or she and me, they want to switch to the

**[73:27 -> 73:34]** other door that is still closed or they want to keep their original choice.

**[73:34 -> 73:44]** And so it is possible to calculate the probability of having the price behind the already chosen

**[73:44 -> 73:47]** door or the new one on the basis of the bias rule.

**[73:47 -> 73:50]** It's just a matter of formalizing it well.

**[73:50 -> 73:53]** And these will tell you what is the right choice.

**[73:53 -> 73:57]** And the right choice is actually to switch.

**[73:57 -> 73:58]** And you can formulate it.

**[73:58 -> 74:02]** I'm just started here to help you to formalize the problem.

**[74:02 -> 74:04]** I think there is the last slide in the deck

**[74:04 -> 74:06]** that tells you the solution.

**[74:06 -> 74:10]** But in practice, you have the price being the under A

**[74:10 -> 74:13]** is the under A, which is the one selected by the contestant

**[74:13 -> 74:16]** and under B is the price is behind the big

**[74:16 -> 74:20]** and the one who remains closed or the price is behind the receipt

**[74:20 -> 74:22]** which is the one opened by the host

**[74:22 -> 74:24]** and then the host opens right door C.

**[74:24 -> 74:27]** So we know that in mind that there's no price.

**[74:27 -> 74:30]** And so you have to calculate the probability of A.

**[74:30 -> 74:35]** So the price is in A, given the fact that the door has been open

**[74:35 -> 74:38]** and the probability of the price being in B,

**[74:38 -> 74:41]** given the fact that the door C has been open.

**[74:41 -> 74:44]** And you will see that the probability is higher for switching,

**[74:44 -> 74:46]** and so it's better to switch.

**[74:48 -> 74:53]** Okay, some more basic concept in the bandits.

**[74:53 -> 74:58]** Well, we saw joint probability for two random variables,

**[74:58 -> 75:01]** But if the two-bar random variables do not really depend

**[75:01 -> 75:04]** among each other, well, then their joint probability

**[75:04 -> 75:07]** is just the multiplication between the two margin

**[75:07 -> 75:08]** also, X and Y.

**[75:08 -> 75:10]** And the conditional at this point

**[75:10 -> 75:12]** is only the marginal for the first.

**[75:12 -> 75:15]** So if X does not depend on Y,

**[75:15 -> 75:18]** the conditional probability is just the probability of X.

**[75:18 -> 75:22]** Now, you can win on the left, this week and next week,

**[75:22 -> 75:27]** these are completely unrelated and independent events.

**[75:27 -> 75:44]** If you want to play the Russian lids, I don't advise you to do that, but you have one bullet or a six position, and if you're fired and you are still alive, because it's you didn't get the bullets, then the next time you have a higher rule, you need to get the bullets right because the number of possibility.

**[75:44 -> 75:47]** I mean, the number of position becomes five, not six.

**[75:49 -> 75:50]** So they are not in the body.

**[75:50 -> 75:54]** And of course, you can also have conditional independence.

**[75:54 -> 75:59]** So if you have toothache, cavity and catch,

**[75:59 -> 76:02]** the fact that you have the cavity and the probability

**[76:02 -> 76:07]** that your dentist catches the cavity,

**[76:07 -> 76:12]** I mean, this does not depend on whether I feel pain.

**[76:12 -> 76:15]** So if I feel the toothache or not, right?

**[76:15 -> 76:18]** So the probability of catching the cavity,

**[76:18 -> 76:21]** given the fact that you have the parity and you have to eight,

**[76:21 -> 76:25]** that's not dependent on the target I feel today.

**[76:25 -> 76:28]** And saying, I mean, concept by extent, very clear.

**[76:30 -> 76:34]** Yeah, so again, also the conditional independence,

**[76:34 -> 76:37]** two random variables can be conditional independent

**[76:37 -> 76:41]** given the fact that a third event happened.

**[76:41 -> 76:44]** So the raw video ends up wide given z.

**[76:44 -> 76:47]** Actually, if this condition dependent happened,

**[76:47 -> 76:51]** It means that this probability is just a multiplication

**[76:51 -> 76:54]** between the probability of x given z

**[76:54 -> 76:56]** and the probability of y given z.

**[77:00 -> 77:03]** And knowing this z,

**[77:03 -> 77:06]** and which makes a difference between having or not

**[77:06 -> 77:08]** the initial independence is not for free.

**[77:08 -> 77:13]** So sometimes again, you have to discover it from your data

**[77:13 -> 77:15]** if this is a correct or not relation.

**[77:15 -> 77:19]** And here I was providing this example where some years ago

**[77:19 -> 77:24]** in practice in London, they were almost approving a law

**[77:26 -> 77:30]** that was forcing taxi drivers to not wear coats

**[77:30 -> 77:35]** because they were observing relation between the fact

**[77:35 -> 77:38]** that the taxi driver were wearing a coat

**[77:38 -> 77:40]** and the fact that there were some accident.

**[77:40 -> 77:44]** But then the discord that practically the real culprit

**[77:44 -> 77:48]** is the fact of what makes a difference in the fact that it is raining or not.

**[77:48 -> 77:52]** So, I mean, it's a different way of expressing the probability, right?

**[77:52 -> 77:56]** So, it's the fact that there's a rain that makes a difference, not percating the fact

**[77:56 -> 77:59]** of the coast, not the far percaging, there is a goat.

**[77:59 -> 78:05]** Okay, so this is just to tell you that we are playing with probabilities, but, and it

**[78:05 -> 78:11]** seems nothing really fancy, but then it might have serious consequences than in practical

**[78:11 -> 78:12]** life.

**[78:12 -> 78:15]** And there is people that are actually doing that job

**[78:15 -> 78:17]** for our goal learners.

**[78:17 -> 78:19]** There's really mathematicians and people

**[78:19 -> 78:20]** that are doing this kind of job

**[78:20 -> 78:23]** and then helps people to take the decision.

**[78:23 -> 78:28]** So at this point, I would like to go back

**[78:28 -> 78:33]** to our classifiers and our models and our function

**[78:33 -> 78:37]** which is again, taking X as our data,

**[78:37 -> 78:40]** having a Y as an output and having a function

**[78:40 -> 78:44]** and connects them to Y.

**[78:44 -> 78:47]** This is what we said since the beginning of every machine

**[78:47 -> 78:49]** learning model should do.

**[78:49 -> 78:52]** And I want to provide an example with probabilities.

**[78:52 -> 78:56]** So the very first, let's say, classifier for this class

**[78:56 -> 78:59]** formalized on the base of the logical probability

**[78:59 -> 79:01]** that we saw, which is the naive bias classifier.

**[79:01 -> 79:04]** Most probably already saw it, but it's just

**[79:04 -> 79:07]** to start everybody on the same page.

**[79:07 -> 79:10]** So we define what is a naive bias classifier.

**[79:10 -> 79:14]** But I would say that we take a break here now,

**[79:14 -> 79:17]** so 15 minutes, and then we get back to this.

**[80:40 -> 80:42]** you

**[81:10 -> 81:12]** you

**[81:40 -> 81:42]** you

**[82:10 -> 82:12]** you

**[82:40 -> 82:42]** you

**[83:10 -> 83:12]** you

**[83:40 -> 83:42]** you

**[84:10 -> 84:12]** you

**[84:40 -> 84:42]** you

**[85:10 -> 85:12]** you

**[85:40 -> 85:42]** you

**[86:10 -> 86:12]** you

**[86:40 -> 86:42]** you

**[87:10 -> 87:12]** you

**[87:40 -> 87:42]** you

**[88:10 -> 88:12]** you

**[88:40 -> 88:42]** you

**[89:10 -> 89:12]** you

**[89:40 -> 89:42]** you

**[90:40 -> 90:42]** you

**[91:10 -> 91:12]** you

**[91:40 -> 91:42]** you

**[92:10 -> 92:12]** you

**[92:40 -> 92:42]** you

**[93:10 -> 93:12]** you

**[93:40 -> 93:42]** you

**[94:10 -> 94:12]** you

**[94:40 -> 94:42]** you

**[95:10 -> 95:12]** you

**[95:40 -> 95:42]** you

**[96:10 -> 96:12]** you

**[96:40 -> 96:42]** you

**[97:10 -> 97:12]** you

**[97:40 -> 97:42]** you

**[98:10 -> 98:12]** you

**[98:40 -> 98:42]** you

**[99:10 -> 99:12]** you

**[99:40 -> 99:42]** you

**[100:10 -> 100:12]** you

**[100:40 -> 100:58]** Okay, so we are restarting and we are talking about probabilities.

**[100:58 -> 101:06]** Now we want to formalize our first classifier where the learning parameters are actually

**[101:06 -> 101:12]** probabilities, right? So a formulation of the function that brings us from x to y,

**[101:12 -> 101:20]** where the function in practice is defined by probabilities. So let's see what we are talking about.

**[101:22 -> 101:29]** So we said that learning beings starting from the experience, you have a metric that evaluates

**[101:29 -> 101:38]** how to do more in relation. So task, experience, and don't be magic. And we want to improve your

**[101:38 -> 101:44]** prediction ability the more experience you have. So the more dependent. Now, what kind of data

**[101:44 -> 101:52]** we're talking about are we looking at very simple tables where every instance, so every

**[101:52 -> 102:01]** data is actually a vector containing values. So you have practically a matrix. Each row

**[102:01 -> 102:10]** is one of your data elements. Every data element is described by D features. Usually our D

**[102:10 -> 102:18]** numbers. In this case, very simple formulation. We say that each element is described by this

**[102:18 -> 102:25]** categories we are considering. So, sun, may, or raining, warm up cold, normal up high, so humidity,

**[102:26 -> 102:33]** so it's a sky temperature, humidity, wind, water forecast. And what we want to predict

**[102:33 -> 102:42]** is whether a certain picnic spot, which is described by this attribute, is enjoyable or not.

**[102:42 -> 102:52]** very simple binary classification. Okay, so our answer is yes or no. And so we

**[102:52 -> 102:58]** have N data, right? So N samples, each of them is represented by a row, and D are

**[102:58 -> 103:06]** the features, okay, which describe each element. Now, how do we do the prediction?

**[103:06 -> 103:15]** Well, we exploited the bias rule and specifically we use just a numerator of the bias rule as we said.

**[103:15 -> 103:21]** So we discard the denominator. We consider only the likelihood of the prior.

**[103:21 -> 103:35]** And in practice, what we have is that there are some part of this expression of the probability that are easy to estimate directly from the data and other that are limited.

**[103:35 -> 103:38]** other that are going to be more complicated.

**[103:38 -> 103:42]** So the probability that in general, in a certain region,

**[103:42 -> 103:44]** you can find an enjoyable spot.

**[103:44 -> 103:47]** And so in this particular case, the probability of y,

**[103:47 -> 103:50]** the probability of our label, is something

**[103:50 -> 103:52]** that we can easily measure.

**[103:52 -> 103:55]** And then from the measure, as usual, marginal,

**[103:55 -> 103:57]** it's practically going to table.

**[103:57 -> 104:00]** From observation, we can somehow estimate the probability

**[104:00 -> 104:01]** of y.

**[104:01 -> 104:04]** It is emitting the probability of x, given y,

**[104:04 -> 104:10]** is not that easy because it's the probability of each of these features given why.

**[104:11 -> 104:19]** And these features, actually, they are not independent among each other. So x1, x2, x3, xd,

**[104:19 -> 104:24]** so this guy and the temperature are information that actually are related among each other.

**[104:24 -> 104:29]** So depending on how the sky is, you have a certain temperature, also the humidity, the wind.

**[104:29 -> 104:37]** So in general, this feature are not independent, but we can make a simplification for the purpose

**[104:37 -> 104:45]** of defining our very first simple classifier. So we suppose that all these features are

**[104:46 -> 104:53]** independent, specifically conditional independent. So they are independent given the label.

**[104:53 -> 105:05]** such that we can write these expressions. You see here we have an x which is bold and usually this notation is because x is a vector.

**[105:05 -> 105:11]** Indeed it is composed by multiple elements, right? So x is a vector composed by multiple elements.

**[105:11 -> 105:15]** And here I'm just exposing the components of this vector.

**[105:15 -> 105:26]** And what I'm expressing here is that the probability of these vectors or all its components can be written as the product of the single, of the probability of the single element given y.

**[105:26 -> 105:34]** So, I'm simplifying my life and saying that the features are conditional in the band and given y.

**[105:34 -> 105:40]** Okay, so I'll write it down like this. This provides me a way to simplify this expression

**[105:40 -> 105:47]** and possibly obtain this, which would be a score, right? And this score at the end, what

**[105:47 -> 105:53]** do I need to do? Well, if I have, think about it, the probability of y equal yes, and the

**[105:53 -> 105:59]** probability of y equal no. Now it's not the probability of a score, if I describe it

**[105:59 -> 106:06]** the numerator. So the score of yes and the score of no, then I can just compare it to

**[106:06 -> 106:10]** go. And if the score of yes is higher, then my prediction will be that the picnic spot

**[106:10 -> 106:17]** is enjoyable. If the no is higher, the probability that the picnic spot is not enjoyable will

**[106:17 -> 106:24]** win. And so this will be my prediction. Now, this simplification that I'm doing by adopting

**[106:24 -> 106:28]** this is called naive bias exactly for this reason,

**[106:28 -> 106:31]** and we're making a naive kind of decision

**[106:31 -> 106:34]** because it's not of course really representing reality,

**[106:34 -> 106:38]** which is more complex due to the interaction

**[106:38 -> 106:38]** between these elements,

**[106:38 -> 106:41]** but we are just making the simplification.

**[106:41 -> 106:42]** But it's really have an effect

**[106:42 -> 106:45]** on the number of calculation I need to do

**[106:45 -> 106:50]** because here each of these column is taking two values,

**[106:51 -> 106:53]** so each of them is binary.

**[106:53 -> 106:57]** And if I have to consider really this probability

**[106:57 -> 107:01]** in the right way, then I have to consider

**[107:01 -> 107:02]** how many cases work.

**[107:02 -> 107:06]** Two to the power of D, because D is the number of features,

**[107:06 -> 107:11]** multiplied by K, which is how many class labels I have.

**[107:11 -> 107:14]** That again, here is just binary, it's just a two,

**[107:14 -> 107:17]** but the problem can be eventually more complex.

**[107:17 -> 107:20]** While with this naive assumption,

**[107:20 -> 107:22]** I just need to consider two,

**[107:22 -> 107:24]** the right-by-D, right-by-key cases, right,

**[107:24 -> 107:29]** that combines the separate features with the label,

**[107:29 -> 107:32]** which is in this case is just enjoyable spot here.

**[107:33 -> 107:36]** Okay, so we're making a simplification.

**[107:36 -> 107:37]** This is our data.

**[107:37 -> 107:40]** We know what's the prediction we want to get.

**[107:40 -> 107:42]** Enjoyable spot, yes or no.

**[107:42 -> 107:47]** Now, so in practice, what we want to do

**[107:48 -> 107:51]** is just to make this calculation, right?

**[107:51 -> 107:56]** So since this is, let me go back, P of y,

**[107:56 -> 107:59]** and then we have just the numerator, P of x, given y.

**[107:59 -> 108:03]** We express P of x, given y with these multiplications,

**[108:03 -> 108:05]** how we need to calculate this.

**[108:05 -> 108:08]** So the gas prior, we can obtain it,

**[108:08 -> 108:10]** this is simplified, and then we make the prediction

**[108:10 -> 108:12]** of the posterior.

**[108:12 -> 108:16]** For each possible label, we'll do this calculation,

**[108:16 -> 108:18]** and then we compare them, right?

**[108:18 -> 108:24]** Now again, I underline and highlight that these are not probabilities, right?

**[108:24 -> 108:29]** This is a score because we are discarded with denominator.

**[108:29 -> 108:31]** So this is just a numerator of the virus rule.

**[108:31 -> 108:34]** So it's not really probability is a score.

**[108:34 -> 108:42]** It does not hold anymore that the summation between these two values that will get sum up to 1.

**[108:42 -> 108:42]** Okay.

**[108:42 -> 108:44]** So what is the name bias?

**[108:44 -> 108:45]** Is your rule?

**[108:45 -> 108:50]** our prediction, so the function that will bring us from x to the prediction

**[108:50 -> 108:58]** expense with y-heads. So our predicted y will be written in this way. We will try

**[108:58 -> 109:04]** to find the value of y that really maximizes this product. So it's just the

**[109:04 -> 109:09]** argmax of the expression that we got with simplification of this conditional

**[109:09 -> 109:14]** dependence just written in this way, right? And this kind of expression is what we

**[109:14 -> 109:17]** we'll see over and over and over,

**[109:17 -> 109:21]** maximizing something to obtain our relation.

**[109:21 -> 109:23]** Now in this particular case,

**[109:23 -> 109:26]** is just everything formulated in the base of probabilities.

**[109:26 -> 109:29]** Later on, we'll see function,

**[109:29 -> 109:31]** or linearity is,

**[109:31 -> 109:34]** we'll see how this maximization is obtained

**[109:34 -> 109:36]** with gradients and so on.

**[109:36 -> 109:38]** But for the moment,

**[109:38 -> 109:39]** everything is super simple,

**[109:39 -> 109:42]** just written in form of probabilities.

**[109:42 -> 109:49]** So to look at the practical examples, just changing the example itself,

**[109:49 -> 109:50]** but logic is the same.

**[109:50 -> 109:54]** It's not anymore the enjoyable spot for picnic, but good day or not,

**[109:54 -> 109:59]** or good place or not for playing tennis is just the logic at the end.

**[109:59 -> 110:06]** So here we have 14 days where there has been some measure on the outlook,

**[110:06 -> 110:08]** the temperature, your median width.

**[110:08 -> 110:10]** And then we have playing tennis yesterday.

**[110:10 -> 110:15]** So a human or a set of humans provide a disannotation.

**[110:15 -> 110:16]** OK.

**[110:16 -> 110:19]** So now we want to apply our name bias classifier.

**[110:19 -> 110:22]** What do we have to do?

**[110:22 -> 110:23]** We manage tables.

**[110:23 -> 110:28]** So we start from this table, which is just reported here.

**[110:28 -> 110:31]** I have 14 days.

**[110:31 -> 110:34]** And now, first of all, I try to calculate the marginal.

**[110:34 -> 110:37]** So the probability of playing equal yes,

**[110:37 -> 110:41]** Since I have 14 cases, I just count.

**[110:41 -> 110:43]** There are nine yes, out of 14.

**[110:43 -> 110:46]** So it's a fraction nine over 14.

**[110:46 -> 110:49]** The no is five over 14.

**[110:49 -> 110:51]** Okay, it's just the remaining points.

**[110:51 -> 110:53]** And then nine bias.

**[110:53 -> 110:56]** So we reason on every single features.

**[110:56 -> 111:01]** And then I consider a sub table for every single column.

**[111:02 -> 111:07]** So outlook, they combine with play yes

**[111:07 -> 111:15]** they know. So out of the nine cases where the place is yes, how many times the algo

**[111:15 -> 111:21]** is sunny, how many times it's overcast, how many times it's ready. Just have to count it out from

**[111:21 -> 111:30]** the state and write it here in the this sub table. And I do it for outlook, I do it for temperature,

**[111:30 -> 111:35]** I'll do it for wind, I'll do it for humidity. Very simple, just from observation. Now,

**[111:36 -> 111:44]** this I'm daring to call it a learning base because I'm looking at the data and I'm trying to learn

**[111:44 -> 111:50]** what in this particular case I'm the parameter of my model and what I need to make prediction.

**[111:51 -> 111:55]** What we will call really learning phase with the parameter of a deep network,

**[111:55 -> 112:01]** move is slightly different but anyway we will have a learning phase and a deployment phase.

**[112:01 -> 112:07]** So my learning phase in this case is just collecting the information that I have from the data just

**[112:07 -> 112:17]** rewriting them in a different way. Okay, so I put down these tables and then what I need to do is

**[112:17 -> 112:24]** If I have a new sample, new sample that is described as sunny, cool, high, and strong

**[112:24 -> 112:30]** with a full column, I just have to take them and recover from the tables, the numbers.

**[112:31 -> 112:38]** So, I would look sunny when it plays yes. So sunny when it plays yes. Temperature cool when

**[112:38 -> 112:46]** playing yes. Humidity high when playing yes. Wind strong when playing with yes. And just

**[112:46 -> 112:53]** copy them from the table, put them down in this column here. Same for no. And once I've done this,

**[112:53 -> 113:00]** just collect the information, I did a multiplication. So all the conditionals and the multiplied for

**[113:00 -> 113:08]** the marginal, yes, all the conditional and then multiplied by the marginal, no. Now the score

**[113:08 -> 113:13]** for no is higher than the score for yes.

**[113:14 -> 113:18]** And then my prediction is that this place here

**[113:18 -> 113:21]** or the environment is not enjoyable for playing times, right?

**[113:21 -> 113:26]** I would not, my advice would be to not play times.

**[113:27 -> 113:29]** So very, very simple, simple one.

**[113:29 -> 113:32]** I mean, things just full in the logic.

**[113:34 -> 113:38]** So, many players classifier is very fast per se.

**[113:38 -> 113:43]** Of course, you have a reasonable amount of data, so it's a super huge table, it can take a little time.

**[113:44 -> 113:47]** The training per se is just looking at the data.

**[113:47 -> 113:52]** The classification is linear in the number of attributes, as we said, because we're using this

**[113:52 -> 113:56]** night hypothesis, so it's not exponential, right? So it's just linear.

**[113:58 -> 114:04]** And the condition of independence, independence assumption among the attribute is quite heavy,

**[114:04 -> 114:10]** because in real life, these attributes really are not separated.

**[114:10 -> 114:16]** But generally, it provides you with a good approximation.

**[114:16 -> 114:19]** It's really a spanishometric decision, right?

**[114:19 -> 114:22]** If you have to do it very quickly, very fast,

**[114:22 -> 114:26]** and into data somehow respect the condition we saw,

**[114:26 -> 114:29]** then we can use knife bias.

**[114:29 -> 114:32]** So moderate or large frame sets with instances

**[114:32 -> 114:34]** represented by large number of activities

**[114:34 -> 114:36]** usually in the condition where you will choose it.

**[114:38 -> 114:43]** But there are some cases where this kind of strategy

**[114:43 -> 114:46]** might provide you, I mean, not really a failure,

**[114:46 -> 114:49]** but some corner cases.

**[114:49 -> 114:52]** Because look here, I mean, it's a different table,

**[114:52 -> 114:56]** but logic is the same way yes or no.

**[114:56 -> 114:58]** And there is one cases from this table

**[114:58 -> 115:02]** where actually when the sky is sunny,

**[115:02 -> 115:05]** It's never related to play no.

**[115:05 -> 115:07]** So it's always sunny, sunny, sunny, sunny,

**[115:07 -> 115:09]** and sunny is always connected with yes.

**[115:09 -> 115:13]** The only case with a no is raining here.

**[115:13 -> 115:15]** So it means that here you have a zero.

**[115:16 -> 115:19]** And when this happens, when then you want to make

**[115:19 -> 115:21]** a prediction, then you have to multiply

**[115:21 -> 115:24]** and if there is a zero in this multiplication,

**[115:24 -> 115:25]** all that's called becomes zero.

**[115:26 -> 115:31]** So is it becoming zero because really that score is now?

**[115:31 -> 115:36]** or because you didn't have enough data to really represent reality.

**[115:37 -> 115:39]** So maybe this set of data is not enough

**[115:39 -> 115:41]** and you are missing some cases

**[115:41 -> 115:45]** and your prediction becomes not really reliable.

**[115:45 -> 115:47]** So again, it depends on the data

**[115:47 -> 115:48]** on which you are building your model.

**[115:48 -> 115:51]** That's the reason why you have to open it up a little bit.

**[115:53 -> 115:57]** There is a correction to this,

**[115:57 -> 116:01]** which is called Laplace Mothing.

**[116:01 -> 116:07]** and consists in, rather than having this conditional probability that we saw before,

**[116:07 -> 116:15]** was practically taking only these parts of CV divided by the summation of CV, where

**[116:15 -> 116:21]** C is the count of training instances where that specific value for that specific attribute and

**[116:21 -> 116:26]** that specific place, the classes holding, right? So remember, in the sub tables, we were actually

**[116:26 -> 116:30]** collecting these information, these fractions. What LaBlas

**[116:30 -> 116:33]** moving is saying is that we have to add plus one and we have

**[116:33 -> 116:40]** an add denominator, the cardinality of the random variable

**[116:40 -> 116:43]** x of the actual index. So how many values that actually

**[116:43 -> 116:48]** would take? Okay, so if we're talking about sky and it can

**[116:48 -> 116:51]** be sunny or rainy, then it's two possibilities, right, for

**[116:51 -> 116:56]** instance. And so you can correct it a bit.

**[116:56 -> 117:01]** And so if you do it in this particular case,

**[117:01 -> 117:04]** you don't have the zero gets removed, right?

**[117:04 -> 117:07]** So this helps you to avoid that zero

**[117:07 -> 117:10]** that was actually happening just because

**[117:10 -> 117:14]** the set of data you have access to is was not enough.

**[117:14 -> 117:16]** You didn't have the opportunity to,

**[117:16 -> 117:20]** so during what you should do is go out in the world

**[117:20 -> 117:22]** and go get more observation,

**[117:22 -> 117:24]** but there are some cases in which you cannot do it.

**[117:24 -> 117:27]** So you try to adjust your data to let your model work.

**[117:29 -> 117:31]** And why do we use it?

**[117:31 -> 117:34]** Because we want our model,

**[117:34 -> 117:37]** we want to avoid that our model freakouts.

**[117:37 -> 117:40]** So they should not, I mean lose completely

**[117:40 -> 117:42]** their ability to predict, right?

**[117:42 -> 117:46]** So if a robot, now here I'm just joking about,

**[117:46 -> 117:50]** if a robot knows that the sunrise is always at 6 a.m.

**[117:50 -> 117:52]** But then the season change.

**[117:52 -> 117:55]** And at that time, the sun does not rise anymore.

**[117:55 -> 117:58]** Well, the system breaks completely.

**[117:58 -> 118:01]** It doesn't, is not able to do anything anymore.

**[118:01 -> 118:03]** It's not what we want.

**[118:03 -> 118:07]** We want to provide some reliability and robustness

**[118:07 -> 118:11]** to possible variation in the world.

**[118:11 -> 118:14]** And of course, this specific example is the fact that,

**[118:14 -> 118:17]** I mean, the robot didn't have enough,

**[118:17 -> 118:20]** didn't collect it enough information over more season

**[118:20 -> 118:23]** to be able to do the pitch, right?

**[118:23 -> 118:28]** So this Laplace smoothing is specific for nine-by-classifier.

**[118:28 -> 118:31]** Later on, when we talk about deep learning,

**[118:31 -> 118:33]** we talk about labels smoothing.

**[118:33 -> 118:36]** That is not the difference in the goal,

**[118:36 -> 118:40]** because rather than having a label, one-hot label

**[118:40 -> 118:44]** where on five classes, you have all zero,

**[118:44 -> 118:46]** and you put a one only for the corresponding labor

**[118:46 -> 118:48]** of your class, right?

**[118:48 -> 118:51]** This is really putting a peak on one single class.

**[118:51 -> 118:55]** Labus Moody says, well, you should have a peak there,

**[118:55 -> 118:56]** but just smooth it down.

**[118:56 -> 118:59]** So don't have zero, zero, zero, zero, zero,

**[118:59 -> 119:00]** no, no, no, no, no, no, no, no, no,

**[119:00 -> 119:03]** it's a five, a 10 depending on how many classes you have.

**[119:03 -> 119:06]** And it was one more encoded, but it just make, I don't know,

**[119:06 -> 119:09]** that zero becomes zero dot 80,

**[119:09 -> 119:14]** and then you diffuse the information on the other labels, right?

**[119:14 -> 119:15]** Still the peak remains there,

**[119:15 -> 119:17]** but you're providing to the other classes

**[119:17 -> 119:21]** the possibility to be there is not really at zero.

**[119:21 -> 119:23]** And your prediction is not anymore discrete.

**[119:23 -> 119:27]** It becomes a continuous probability of the other process.

**[119:27 -> 119:30]** So you see, I mean, again, I'm providing examples

**[119:30 -> 119:33]** of some people with probability, but my goal is just

**[119:33 -> 119:42]** to pave the way for something that then is used in modern AI.

**[119:42 -> 119:47]** Just to conclude on the last move thing,

**[119:47 -> 119:51]** we were adding plus one and plus the cardinality

**[119:51 -> 119:54]** of the attributes, right, at the denominator.

**[119:54 -> 119:56]** But rather than one, we can have a general k.

**[119:56 -> 120:00]** So k can be one, but can be also a higher number.

**[120:01 -> 120:03]** So think about the k's, you have a bucket

**[120:03 -> 120:05]** and inside it you have three balls,

**[120:05 -> 120:07]** two are red and one is blue, right?

**[120:07 -> 120:10]** Then you have to pick one on the ball

**[120:10 -> 120:13]** and you have two or three, the probability to get a red

**[120:13 -> 120:16]** and one over three, the probability of a blue, right?

**[120:16 -> 120:20]** But if k, you put a k which is equal to one,

**[120:20 -> 120:23]** then the fraction becomes three over five

**[120:23 -> 120:27]** because here, here is something plus one at the numerator

**[120:27 -> 120:29]** and in the denominator you have to sum plus two

**[120:29 -> 120:31]** because the color can be red or blue, right?

**[120:31 -> 120:33]** So two possibilities.

**[120:33 -> 120:36]** So you have three over five and two over five.

**[120:36 -> 120:39]** And if k grows and becomes 100,

**[120:39 -> 120:41]** then you have this kind of fraction.

**[120:41 -> 120:46]** Now what happens is that here, I mean, they're very distinct,

**[120:46 -> 120:50]** But then here, they almost become half half.

**[120:50 -> 120:54]** So the bigger is K, the more the two possibilities

**[120:54 -> 120:56]** tend to overlap among each other.

**[120:56 -> 120:59]** So it becomes less a distinction between the two cases.

**[120:59 -> 121:02]** So it's up to you how strong you want to put,

**[121:02 -> 121:04]** I mean, the strength of this prior

**[121:04 -> 121:07]** that again comes from what you expect

**[121:07 -> 121:11]** about how reliable is your data.

**[121:11 -> 121:13]** So if you want to put a little bit more margin

**[121:13 -> 121:15]** on the prediction that you have,

**[121:15 -> 121:17]** or you want to stay strict on the observation

**[121:17 -> 121:19]** that you get from your data.

**[121:23 -> 121:26]** Okay, so usually it's like,

**[121:27 -> 121:29]** I find it a little bit confusing in the sense

**[121:29 -> 121:31]** that I want to introduce some concept.

**[121:31 -> 121:34]** Let's see if I'm able to do it properly.

**[121:35 -> 121:37]** Because here you see this creaminess

**[121:37 -> 121:39]** in the generative model.

**[121:39 -> 121:41]** When you talk about this kind of keywords,

**[121:41 -> 121:43]** people immediately say generative,

**[121:43 -> 121:46]** Okay, charge it with the generic duration, text, language.

**[121:46 -> 121:48]** It's generating new images,

**[121:48 -> 121:52]** not what I'm trying to refer you like this here.

**[121:52 -> 121:57]** So I'm trying to use this term in a different way,

**[121:57 -> 122:02]** connected to the concept of frequentist approach

**[122:02 -> 122:04]** and by easy an approach,

**[122:04 -> 122:07]** I was referring to before for the probabilities

**[122:07 -> 122:11]** because sometimes we want to just observe the data

**[122:11 -> 122:14]** and take decisions on the basis of frequencies.

**[122:14 -> 122:16]** And we don't know absolutely anything

**[122:16 -> 122:20]** about Gaussian distribution, Poisson distribution,

**[122:20 -> 122:24]** or something else that our mathematician friends

**[122:24 -> 122:25]** can invite for us.

**[122:25 -> 122:27]** And in some other cases, instead,

**[122:27 -> 122:30]** we want to rely on the formulas of this distribution

**[122:30 -> 122:31]** that can be helpful.

**[122:32 -> 122:36]** So in practice, there are two families

**[122:36 -> 122:40]** of kind of approach to deal with these problems.

**[122:40 -> 122:42]** discriminative of generative,

**[122:42 -> 122:44]** frequently sub-biasing,

**[122:44 -> 122:48]** and also the way which we make the predictions, right?

**[122:48 -> 122:52]** When our goal is only estimated

**[122:52 -> 122:54]** plate of y given x,

**[122:54 -> 122:57]** which is what we saw from the null bias, right?

**[122:57 -> 123:01]** I want to predict the probability of a label given the data.

**[123:01 -> 123:03]** That is usually going into the direction

**[123:03 -> 123:06]** what we call discriminative learning.

**[123:06 -> 123:09]** Some might provide us the data.

**[123:09 -> 123:14]** just observe them and we try to fit a model and to find a line something that

**[123:14 -> 123:18]** separates the two groups of data and then depending on where the object is on the

**[123:18 -> 123:20]** left or on the right on the right on the right on the right on the right on the

**[123:20 -> 123:27]** prediction I will take my decision right. So these only care about estimating the

**[123:27 -> 123:32]** conditional probability and usually when I have

**[123:32 -> 123:39]** Let's say I don't know where the data come from, just a billions of data.

**[123:39 -> 123:42]** This is the approach they use.

**[123:42 -> 123:48]** I explained the fact that they have many data and can directly go to this kind of prediction.

**[123:48 -> 123:51]** But there are some other cases in which maybe I have less data.

**[123:51 -> 123:58]** And in that case, I need to ask the help of my decision and mathematician expert to have

**[123:58 -> 124:04]** an idea, more solid idea about how the data and eventually also the label are distributed.

**[124:04 -> 124:11]** So I cannot maybe directly evaluate P of Y and also the denominator of the Bayesian rule

**[124:11 -> 124:18]** of P of X directly. So I need a little bit of help. So if someone tells me as a prior

**[124:18 -> 124:25]** that the data behave according to a certain distribution, a formula distribution, then

**[124:25 -> 124:31]** And that can help me because I can then compose the prediction and I'm also able to predict

**[124:31 -> 124:37]** I mean to define how the joint probability is defined and this will provide me with a

**[124:37 -> 124:40]** different way of strategy to make the prediction.

**[124:40 -> 124:44]** This calls more because more into the direction of genetic learning.

**[124:44 -> 124:46]** So look at this figure.

**[124:46 -> 124:54]** What I mean here is that if I want to follow that direction, then what I do is that I look

**[124:54 -> 125:03]** at the data, I asked someone what could be the distribution from which those data were

**[125:03 -> 125:09]** generated. So this data are distributed like this, right? So maybe I can fit the Gaussian

**[125:09 -> 125:16]** out of there, right? So maybe it's the right thing to do. And if I fit the Gaussian, then first of

**[125:16 -> 125:21]** all, then I have an understanding of how the data distributed, then I look at this to maybe two,

**[125:21 -> 125:25]** Let's say modes, it's not just one motion one mode,

**[125:25 -> 125:27]** it's a multi-gauchute, right?

**[125:27 -> 125:29]** Multi-model.

**[125:29 -> 125:31]** And then it puts a classifier in the middle.

**[125:31 -> 125:35]** But it first passed through the distribution, okay?

**[125:35 -> 125:37]** Not, I don't know if I had directly the data,

**[125:37 -> 125:39]** so I used the data to make an estimate

**[125:39 -> 125:43]** of which kind of distribution they come from,

**[125:43 -> 125:44]** and then I take the decision

**[125:44 -> 125:48]** about the prediction for the normal data, okay?

**[125:48 -> 125:53]** So this is the way in which I'm trying to express this difference between

**[125:53 -> 125:55]** discriminative versus geologic learning.

**[125:55 -> 126:01]** And usually, generative learning or this kind of approach is adopted when you

**[126:01 -> 126:02]** don't have enough data.

**[126:02 -> 126:06]** So better to have some prior knowledge, more so in prior knowledge or something

**[126:06 -> 126:11]** that tells me where the data are coming from, because then I can at least rely on

**[126:11 -> 126:15]** a high level description of the distribution, although I have a limited amount of

**[126:15 -> 126:23]** sample. And if I know from where the data are extracted, then I can eventually use the distribution

**[126:23 -> 126:29]** to synthesize new data. And that's also why I'm a school generative. So I can enlarge.

**[126:29 -> 126:32]** So if I know from where this data are coming from, I have the Gaussian distribution, I

**[126:32 -> 126:38]** continue sampling more data out of it. And I can synthesize more of them. Right? So that's

**[126:38 -> 126:48]** reason why I need prile and orange in the cells. Okay, and indeed this leads to two different

**[126:48 -> 126:54]** families of way of approaching both of the prediction, right? So you might have heard about

**[126:54 -> 127:02]** maximum oposteriori and maximum likelihood, which is practically the two things and presenting here.

**[127:02 -> 127:09]** So maximum oposteriority is practically exploiting what we just saw with the

**[127:09 -> 127:16]** naive bias, right? Nothing more than that. So the final score predicting the

**[127:16 -> 127:22]** posterior given the likelihood of the prior while in maximum likelihood, well

**[127:22 -> 127:32]** Yeah, it's you are considering just the procedure and you consider the prior's uniform.

**[127:33 -> 127:37]** So just two different levels of method, but just to let you know what are the names.

**[127:38 -> 127:44]** And in the middle, there is this line referring to independent and identical distributed identity.

**[127:45 -> 127:51]** I'm inserting it here, but actually there's a concept that will reuse later on and

**[127:51 -> 127:53]** and we define that you're gone.

**[127:53 -> 127:55]** You remember that before I told you that

**[127:57 -> 127:59]** a model to be able to work,

**[127:59 -> 128:02]** well, actually a model is able to work

**[128:02 -> 128:05]** on making a prediction when the data

**[128:05 -> 128:08]** it will find that the deployment time

**[128:08 -> 128:12]** is the same kind of data it observed at training time.

**[128:12 -> 128:14]** If there is a big shift,

**[128:14 -> 128:16]** then you don't have really guarantees

**[128:16 -> 128:19]** on the ability of the method to make the prediction.

**[128:19 -> 128:24]** And so this hypothesis, which is called ILD,

**[128:25 -> 128:29]** is exactly there to say that we suppose

**[128:29 -> 128:32]** for our machine learning model that our data

**[128:32 -> 128:36]** are independent and identically distributed.

**[128:36 -> 128:39]** And so the data are independent.

**[128:39 -> 128:42]** So at the time we'll observe independent data

**[128:42 -> 128:43]** same as training time,

**[128:43 -> 128:46]** but they are identically distributed according

**[128:46 -> 128:47]** to a fixed distribution.

**[128:47 -> 128:51]** we might not know which distribution is that,

**[128:51 -> 128:53]** but this is the needed hypothesis

**[128:53 -> 128:56]** on which all the machine learning model work, okay?

**[128:56 -> 128:59]** Because if I don't have these hypothesis,

**[128:59 -> 129:03]** then I mean, whatever I plan for a trade now or not,

**[129:03 -> 129:06]** so the data that I observed during training

**[129:06 -> 129:08]** will provide with some dollars

**[129:08 -> 129:09]** that will not apply at this time,

**[129:09 -> 129:12]** because the distribution I will see at this time

**[129:12 -> 129:14]** will be completely different.

**[129:14 -> 129:18]** So the IID assumption is one of the most important assumption

**[129:18 -> 129:22]** which let's say all our machine learning model are based.

**[129:22 -> 129:26]** Of course, there are tricks to, let's say,

**[129:26 -> 129:29]** make models also be able to adapt

**[129:29 -> 129:32]** and reduce the domain gap or the main shift

**[129:32 -> 129:34]** with the trading and test.

**[129:34 -> 129:37]** But, and then you have the guarantee

**[129:37 -> 129:39]** of the ability of the model to generalize it.

**[129:39 -> 129:41]** I mean, you cannot really write down a theory.

**[129:41 -> 129:46]** you can, but it's really bounded in the sense of the,

**[129:46 -> 129:48]** there are three we can have,

**[129:48 -> 129:50]** and it's the correctness of the prediction.

**[129:52 -> 129:53]** Okay, so just remember IAD,

**[129:53 -> 129:55]** because this thing will come over and over

**[129:55 -> 129:57]** and over and in the next section.

**[129:59 -> 130:03]** And yeah, so this is just to summarize what we saw,

**[130:03 -> 130:08]** and this was the solution of the Montiouc game show

**[130:08 -> 130:09]** I was mentioning before.

**[130:09 -> 130:15]** Okay, so at this point, I will go to the next step of slides.

**[130:15 -> 130:21]** And so I have just a couple of minutes. If you have a question, just raise your hand.

**[130:21 -> 130:26]** Just change.

**[130:39 -> 130:41]** you

**[131:09 -> 131:11]** Okay.

**[131:15 -> 131:17]** Yes. Okay. So

**[131:18 -> 131:26]** With the nine bias classifier, we actually saw our very first example of

**[131:26 -> 131:31]** model based on probabilities, right?

**[131:31 -> 131:35]** So how to make prediction from the data, everything was

**[131:35 -> 131:37]** finalized in terms of probability,

**[131:37 -> 131:40]** we were maximizing the certain score

**[131:40 -> 131:44]** to describe the fact that we can have one output or another

**[131:44 -> 131:49]** in a very simple binary case.

**[131:49 -> 131:52]** But then, let's take one step forward.

**[131:52 -> 131:55]** So what we want to do in the future

**[131:55 -> 132:01]** will be always the same thing, the same logic. We have a function that should bring us from

**[132:01 -> 132:12]** our input to the output and the function is full of parameters. So this data here is there to

**[132:12 -> 132:18]** indicate that there's a lot of parameters that are there that should be fitted on the data to be

**[132:18 -> 132:21]** be then able to make a prediction.

**[132:21 -> 132:22]** Okay.

**[132:22 -> 132:30]** But then, I mean, which guarantees do we have that the model is going to provide us with

**[132:30 -> 132:33]** a good prediction?

**[132:33 -> 132:39]** This, of course, to be able to answer this question, we have to understand how we are

**[132:39 -> 132:45]** setting up the problem and all our training, procedure, and so on.

**[132:45 -> 132:51]** And so let me consider one case, so an example, practical example.

**[132:51 -> 132:57]** So want to make a good prediction in terms of eating, I mean, choosing the avocado and

**[132:57 -> 132:58]** the supermarket.

**[132:58 -> 133:05]** Now, the avocado is quite complex fruit in the sense that there is one specific time

**[133:05 -> 133:11]** range in its life where it's good to be eaten, otherwise we've gotten too soft or the other

**[133:11 -> 133:13]** side is too hard.

**[133:13 -> 133:17]** So it's not easy to understand if it's ripe or not.

**[133:17 -> 133:22]** So what do you do is that you create your expertise.

**[133:22 -> 133:25]** So you go to the supermarket, you buy several times,

**[133:25 -> 133:27]** and you start to understand that maybe the color,

**[133:27 -> 133:31]** and maybe I'm touching it, and you can estimate

**[133:31 -> 133:34]** if it's ripe or not, maybe it's melting it.

**[133:34 -> 133:38]** So you're collecting data, right?

**[133:38 -> 133:39]** And then what you want to do with it,

**[133:39 -> 133:46]** So you internally create a model to make prediction on new level cardels, right?

**[133:46 -> 133:51]** So you train yourself for something that you buy and that you bring at home and then you

**[133:51 -> 133:54]** eat even if it's not perfect.

**[133:54 -> 133:58]** But then in the future, then the next time you go to the supermarket, you would like

**[133:58 -> 134:00]** to have your model being brewed, right?

**[134:00 -> 134:07]** So the avocado that you choose is a little better with respect to the previous times.

**[134:07 -> 134:10]** So in practice, you have your trading data.

**[134:10 -> 134:12]** And so your expertise on which you build a model.

**[134:12 -> 134:15]** And then you want to make a prediction on a new sample.

**[134:15 -> 134:18]** So next time you build a super pilot.

**[134:18 -> 134:20]** So you build on your expertise, but you

**[134:20 -> 134:22]** want to make prediction on the future.

**[134:22 -> 134:25]** And that's, again, why it's important to have data which

**[134:25 -> 134:26]** are IAD.

**[134:26 -> 134:28]** Because if in the future your data comes

**[134:28 -> 134:30]** from a completely different distribution,

**[134:30 -> 134:33]** so if you, I don't know.

**[134:33 -> 134:35]** Now, I'm not an expert in avocados.

**[134:35 -> 134:39]** But if you, I mean, your supermarket, those of your house

**[134:39 -> 134:42]** sell at Zabokadas, which come only from one country,

**[134:42 -> 134:43]** and then you go to a different supermarket,

**[134:43 -> 134:45]** then they have a counter for a different country,

**[134:45 -> 134:48]** then the model that you built maybe doesn't work perfectly,

**[134:48 -> 134:49]** right?

**[134:49 -> 134:52]** So you want your avocados to be IID

**[134:52 -> 134:53]** and be extracted from the same issue.

**[134:57 -> 135:01]** So now, we minimize our trading errors.

**[135:01 -> 135:03]** So we have built a model on the expertise

**[135:03 -> 135:05]** that we have on the training data,

**[135:05 -> 135:09]** but actually we care about the test theorem.

**[135:09 -> 135:11]** So what happened in the future?

**[135:11 -> 135:13]** So now the question is, is it always possible

**[135:13 -> 135:17]** to get 100% accuracy and what are the important parameters

**[135:17 -> 135:20]** that characterize the learning problem in this sense?

**[135:20 -> 135:22]** So sorry, in this first lecture,

**[135:22 -> 135:24]** again, there is a little bit of mathematics,

**[135:24 -> 135:26]** but it's a basis, right?

**[135:26 -> 135:29]** It's just telling you why this model are working,

**[135:29 -> 135:32]** and which guarantees we can provide.

**[135:32 -> 135:36]** I don't know that from days two after you passed the exam,

**[135:36 -> 135:40]** you will completely forget about this, and it's a pity.

**[135:40 -> 135:43]** But if someone else doesn't ask you,

**[135:43 -> 135:45]** and now it's starting to happen,

**[135:45 -> 135:48]** then together with the accuracy of a model,

**[135:48 -> 135:51]** I want the range of guarantees.

**[135:51 -> 135:55]** So what is the probability that this output

**[135:55 -> 135:58]** will change of plus one or minus one,

**[135:58 -> 136:00]** you have to be able to do it.

**[136:00 -> 136:03]** I don't know to explain why you expect that the range is

**[136:03 -> 136:06]** smaller or big and why you expect that this model is really

**[136:06 -> 136:10]** able to provide that kind of, let's say,

**[136:10 -> 136:15]** reliability when something changed at this time eventually.

**[136:15 -> 136:19]** So let's try to understand what is behind the scene.

**[136:19 -> 136:24]** So we have our input space X, we have our output space Y.

**[136:24 -> 136:27]** And again, you output space, I mean,

**[136:27 -> 136:31]** This particular case can be of k possible classes,

**[136:31 -> 136:33]** binary or model two class,

**[136:33 -> 136:37]** k equal two is simply binary, so we'll do the documentation.

**[136:37 -> 136:41]** And yes, x represent the description measurement

**[136:41 -> 136:45]** of your data of your object and y is the category

**[136:45 -> 136:46]** to which the object below.

**[136:46 -> 136:49]** This is just very basic notation.

**[136:49 -> 136:51]** In typical case of binary,

**[136:51 -> 136:54]** you have labels to charge zero one or plus one minus one.

**[136:54 -> 136:59]** And you assume that your data come from a distribution,

**[137:00 -> 137:04]** D.D., you don't know what is the distribution D.D.,

**[137:04 -> 137:08]** but there is a distribution and you expected the same

**[137:08 -> 137:11]** for data training time and a test sign.

**[137:11 -> 137:16]** And I mean, ideally you have a core glabbling function,

**[137:16 -> 137:19]** at least you don't have it, but you supposedly exist.

**[137:19 -> 137:23]** I function Y, I mean that's all a function F,

**[137:23 -> 137:25]** that is really able to connect X and Y

**[137:25 -> 137:29]** and providing always 100% the correct answer.

**[137:31 -> 137:34]** So we define something which is called loss,

**[137:35 -> 137:37]** which is the loss of the classifier

**[137:37 -> 137:40]** and specifically we call it loss function,

**[137:40 -> 137:43]** which is a function measure the errors

**[137:43 -> 137:45]** that your model is going to do.

**[137:45 -> 137:49]** So you call your model, I mean, you make an hypothesis.

**[137:49 -> 137:53]** So your model will be what you build from the data

**[137:53 -> 137:57]** will be the model defined by H is your hypothesis.

**[137:57 -> 138:00]** Then when takes the data X provides an output,

**[138:01 -> 138:04]** F is the ground truth.

**[138:04 -> 138:08]** So Y F produces Y, which is the ground truth.

**[138:08 -> 138:11]** Your model produces something that we call,

**[138:11 -> 138:14]** you can call Y hat for Y tilde, right?

**[138:14 -> 138:16]** It's your prediction.

**[138:16 -> 138:18]** And you are comparing this to,

**[138:18 -> 138:20]** Now here is a very simple case.

**[138:20 -> 138:22]** We have a 0, 1 loss.

**[138:22 -> 138:25]** You count 1 when you make a mistake,

**[138:25 -> 138:28]** and you count 0 when you don't make a mistake.

**[138:28 -> 138:32]** So if your prediction is correct, you're not losing anything.

**[138:32 -> 138:34]** So your loss is 0.

**[138:34 -> 138:37]** If you are making a mistake, your loss, in this case,

**[138:37 -> 138:40]** a very simple one is 1.

**[138:40 -> 138:43]** So this is the loss function.

**[138:43 -> 138:46]** So the loss function is the function that

**[138:46 -> 138:50]** measures, wherever, between the assigned prediction

**[138:50 -> 138:53]** and the prediction of the correct level function.

**[138:53 -> 138:57]** And we call the true risk of your classifier.

**[138:57 -> 139:01]** What is the true risk of a classifier

**[139:01 -> 139:05]** is the probability that it does not predict

**[139:05 -> 139:10]** the correct label on a test random data,

**[139:10 -> 139:14]** which is extracted from the same distribution D

**[139:14 -> 139:17]** from which you would start the training data.

**[139:17 -> 139:19]** So the distribution D is the same

**[139:19 -> 139:22]** for the training and test data.

**[139:22 -> 139:25]** So the true risk of the classifiers, this one,

**[139:25 -> 139:29]** is the probability that you make a mistake.

**[139:30 -> 139:31]** And so your prediction is different

**[139:31 -> 139:33]** from the ground truth one.

**[139:33 -> 139:38]** And the true risk is the expected value of the loss.

**[139:38 -> 139:41]** So the loss is something that you've measured,

**[139:41 -> 139:45]** the data that you can observe,

**[139:45 -> 139:48]** the true risk is something that I'd hire them.

**[139:48 -> 139:52]** If I had the possibility to access the distribution D

**[139:52 -> 139:55]** from which the data are instructed,

**[139:55 -> 140:00]** then the expected value of the loss,

**[140:00 -> 140:02]** according to for X,

**[140:02 -> 140:04]** distributor according to D,

**[140:04 -> 140:07]** is exactly what we call true risk.

**[140:07 -> 140:09]** This true risk is also called

**[140:09 -> 140:12]** and I'd say connected to a joint position function,

**[140:12 -> 140:15]** because it's practically, you see,

**[140:15 -> 140:17]** what does mean expected value means,

**[140:17 -> 140:20]** a summation over a probability, nothing more than that.

**[140:20 -> 140:23]** And the function is multiplied by the probability itself.

**[140:23 -> 140:25]** And the probability we are considering

**[140:25 -> 140:28]** is the joint probability of x and y.

**[140:28 -> 140:32]** So this is just expressing what we mean with expectation,

**[140:32 -> 140:36]** right, so mathematical statistics doing,

**[140:36 -> 140:39]** calculating the expectation means considering

**[140:39 -> 140:42]** of the integral if you have a previous value or the summation

**[140:42 -> 140:45]** over all the possible probability of the function

**[140:45 -> 140:47]** multiplied by the probabilities.

**[140:47 -> 140:49]** So this is just to write a new term.

**[140:50 -> 140:55]** The true risk is something we don't have access to, right?

**[140:55 -> 140:57]** Because we would like to minimize the true risk,

**[140:57 -> 140:59]** but we don't have the full distribution D.

**[140:59 -> 141:02]** So it's something that we don't have access to.

**[141:03 -> 141:06]** And so what we have access to is only,

**[141:06 -> 141:08]** I mean, the calculation of the observation

**[141:08 -> 141:12]** the real loss, not the expected value.

**[141:12 -> 141:17]** So yeah, in practice, we end up back to the bias classifier.

**[141:18 -> 141:22]** So we would like to find the hypothesis edge,

**[141:22 -> 141:27]** the edge that maximizes the prediction from x to y, right?

**[141:27 -> 141:29]** So this is the probability of the errors.

**[141:29 -> 141:34]** This is what we will report here using the probability,

**[141:35 -> 141:38]** not the joint probability, but just the marginal mix.

**[141:38 -> 141:43]** Any practice you want to minimize the probability of the errors,

**[141:43 -> 141:45]** which means maximizing the,

**[141:45 -> 141:49]** so one minus the probability of doing the correct prediction.

**[141:49 -> 141:52]** So yeah, minimizing the error means

**[141:52 -> 141:54]** maximizing the correct prediction.

**[141:54 -> 141:55]** We have the ends,

**[141:55 -> 141:57]** we are doing this kind of prediction here.

**[141:57 -> 142:00]** So we are trying to maximize the y that we

**[142:00 -> 142:04]** assigned to the label x on the basis of the conditionals,

**[142:04 -> 142:06]** which again brings back to what we saw with

**[142:06 -> 142:11]** the real basic assignment, we were simply trying to get to the many biases.

**[142:11 -> 142:17]** But yeah, so the H star is, let's say,

**[142:17 -> 142:25]** the correct solution of the model that we would get by following these principles.

**[142:25 -> 142:34]** So this theoretical logic of bias risk and the advice rule and

**[142:34 -> 142:37]** the true risk, it was defined before, right?

**[142:38 -> 142:43]** So the true, so if I able to practice the true risk,

**[142:45 -> 142:48]** so here is a true risk for any age,

**[142:48 -> 142:50]** but if I follow the bias logic,

**[142:50 -> 142:53]** I would find better solutions

**[142:53 -> 142:55]** so the risk becomes smaller.

**[142:55 -> 142:58]** Now, here we are fetching a ghost, right?

**[142:58 -> 143:00]** Because we are talking about theory,

**[143:00 -> 143:03]** but how we put this on the ground.

**[143:03 -> 143:05]** So how do we realize it?

**[143:05 -> 143:08]** And specifically, what is the bias risk?

**[143:08 -> 143:11]** I mean, okay, we can write it down in formula,

**[143:11 -> 143:13]** but what is this age style?

**[143:13 -> 143:15]** So it's just a reference, right?

**[143:15 -> 143:18]** So we are trying to formalize it in the right way,

**[143:18 -> 143:20]** according to theory.

**[143:20 -> 143:22]** But then in practice, what does it mean?

**[143:22 -> 143:25]** Well, we can follow what Andrew Gueh,

**[143:25 -> 143:28]** which is, I told you, is the founder of Coursera

**[143:28 -> 143:30]** and one of the famous Stanford professor.

**[143:30 -> 143:34]** you are saying that per se the bias risk can be estimated

**[143:34 -> 143:36]** with the human performance, right?

**[143:36 -> 143:39]** So we have what we call the ground truth,

**[143:39 -> 143:42]** what a human would do, which kind of prediction

**[143:42 -> 143:43]** the human would do, right?

**[143:43 -> 143:45]** So that would be the ground truth

**[143:45 -> 143:48]** and we'll try to get closer with the machine prediction

**[143:48 -> 143:51]** to what we have as a ground truth produced by you.

**[143:52 -> 143:55]** Now, behind this sentence,

**[143:55 -> 143:58]** there are long studies about,

**[143:58 -> 144:04]** Yeah, so cognitive science, how human brain works.

**[144:04 -> 144:07]** And the fact that our human brain is

**[144:07 -> 144:11]** henarrantly wide to work according to the bias, right?

**[144:11 -> 144:15]** So it's not that, I mean, it's a big thing.

**[144:15 -> 144:16]** It's the other way around.

**[144:16 -> 144:19]** Also the Bayes rule comes from the way in which

**[144:19 -> 144:22]** we reasonably make prediction.

**[144:22 -> 144:25]** And everything comes up also matches with reality

**[144:25 -> 144:29]** when you do the, to obtain reasonable scores

**[144:29 -> 144:30]** in terms of probabilities.

**[144:31 -> 144:36]** Okay, so at the end, we do not know F,

**[144:36 -> 144:39]** which is this absolute ground truth.

**[144:39 -> 144:42]** We need to estimate the hypothesis H

**[144:42 -> 144:44]** and we want to do this prediction.

**[144:44 -> 144:48]** But then, yeah, so what we want to have is an H

**[144:48 -> 144:51]** that work well in future example,

**[144:51 -> 144:56]** But our loss is calculated, so the function, right,

**[144:56 -> 144:59]** that tells us how many mistakes we are doing

**[144:59 -> 145:03]** is calculated on the training data.

**[145:04 -> 145:08]** So we train our model and to train our model,

**[145:08 -> 145:11]** we look at the ground truth and we collect experience

**[145:11 -> 145:14]** and we look how many times we make the wrong

**[145:14 -> 145:16]** avocado prediction, right?

**[145:16 -> 145:17]** So our mistake.

**[145:17 -> 145:20]** We compare and then we try to optimize our model.

**[145:20 -> 145:23]** But this is our training experience, right?

**[145:23 -> 145:26]** But actually we would like to be correct on future examples.

**[145:26 -> 145:28]** And then here comes the idea again,

**[145:28 -> 145:32]** because D has to be shared between training and test.

**[145:32 -> 145:35]** And this is an absolutely important condition.

**[145:35 -> 145:39]** Okay, the assumption is, this assumption is the connection

**[145:39 -> 145:41]** between what we have seen in the past

**[145:41 -> 145:44]** and what we expect to see in the future.

**[145:44 -> 145:46]** Without these, most of machine learning

**[145:46 -> 145:48]** what was completely break.

**[145:48 -> 145:51]** It's very complicated to provide guarantee.

**[145:52 -> 145:55]** So the only thing we have access to

**[145:55 -> 145:58]** is the empirical risk, not the true risk.

**[146:00 -> 146:04]** The only thing we can get is how many mistakes we do.

**[146:04 -> 146:07]** Okay, so this one is just the function

**[146:07 -> 146:10]** that counts one every time we make a mistake

**[146:10 -> 146:11]** in the data function.

**[146:11 -> 146:13]** And here is the number of samples

**[146:13 -> 146:16]** that we have in our training set.

**[146:16 -> 146:17]** And so they're just averaging.

**[146:17 -> 146:18]** So just counting at the end,

**[146:18 -> 146:23]** how many mistakes we are doing out of the m samples

**[146:23 -> 146:25]** that we have in our trading set.

**[146:27 -> 146:30]** So this is the only thing we have access to,

**[146:30 -> 146:32]** this is the empirical risk.

**[146:32 -> 146:37]** So the theoretical risk is the expected value on the loss

**[146:38 -> 146:40]** calculated on the basis of the distribution.

**[146:40 -> 146:42]** When considering all the possible data

**[146:42 -> 146:45]** I've started from the distribution D,

**[146:45 -> 146:46]** we don't have access to that.

**[146:46 -> 146:49]** we only have access to the appeal purpose.

**[146:49 -> 146:53]** And then in practice, every model

**[146:53 -> 146:56]** can only be probably correct.

**[146:56 -> 147:01]** So we cannot hope to find the true risk keyboard to zero.

**[147:01 -> 147:05]** So even if we had photo completely, the Bayesian logic

**[147:05 -> 147:08]** and we get to do that H-star and then followed by its rule,

**[147:08 -> 147:12]** well, we only were only able to manage the appeal

**[147:12 -> 147:14]** because risk not that you would want.

**[147:14 -> 147:19]** And this depends on the fact that reality is complex.

**[147:20 -> 147:23]** It's nuanced and it's noisy.

**[147:23 -> 147:26]** And so it depends on the data itself on the world.

**[147:26 -> 147:29]** Because think about it, so this claim can be proven

**[147:29 -> 147:32]** just by providing a practical example.

**[147:32 -> 147:36]** So let's say that I can take,

**[147:36 -> 147:39]** I have a random variable that it can take two values,

**[147:39 -> 147:41]** X, Y and X, two, right?

**[147:41 -> 147:46]** And I can have, let's say that I suppose the probability

**[147:46 -> 147:50]** of observing X2 is defined by epsilon.

**[147:50 -> 147:53]** And the probability of observing X1 is one-man's epsilon.

**[147:53 -> 147:56]** There are only two possibilities, right?

**[147:56 -> 147:57]** For this random variable.

**[147:57 -> 147:59]** It's either X1 or X2.

**[147:59 -> 148:01]** So if the probability of X2 is epsilon,

**[148:01 -> 148:05]** then the probability of the other is one-man's X.

**[148:05 -> 148:10]** But if I take M examples out of this distribution,

**[148:10 -> 148:15]** There's always a possibility that I don't see X2 at all.

**[148:16 -> 148:17]** Right?

**[148:17 -> 148:20]** You remember when we did the example of the Laplace

**[148:20 -> 148:22]** smoothing, we said, well, there can be cases

**[148:22 -> 148:25]** where one attribute, you don't observe it

**[148:25 -> 148:27]** and then you have a zero

**[148:27 -> 148:29]** and then you have to find the work around.

**[148:29 -> 148:32]** We are practically in the same condition.

**[148:32 -> 148:36]** The date that we have, even though, I mean,

**[148:36 -> 148:39]** the probability can be small, but it can happen,

**[148:39 -> 148:42]** the specific attribute you never observed

**[148:42 -> 148:45]** because your training set may be small

**[148:45 -> 148:49]** or even if you go on collecting more data,

**[148:49 -> 148:52]** the probability of that particular event is so small

**[148:52 -> 148:55]** that it's a rare event and then it can happen

**[148:55 -> 148:56]** that you never observed it.

**[148:56 -> 148:58]** And so what does it mean?

**[148:58 -> 149:03]** Well, it means that the probability to not see X2

**[149:03 -> 149:06]** among M examples, how do I get it?

**[149:06 -> 149:11]** is this probability multiplied by itself, m times.

**[149:12 -> 149:15]** So I observed one sample, then another, then another,

**[149:15 -> 149:17]** then another, I'm just multiplying the probability

**[149:17 -> 149:19]** of each of the samples,

**[149:19 -> 149:23]** and it's one minus epsilon raised to the power of m.

**[149:23 -> 149:24]** This is the property.

**[149:24 -> 149:27]** If I use a Taylor expansion, I can write it down like this.

**[149:27 -> 149:30]** It's an approximation, but I can do it.

**[149:30 -> 149:33]** And if epsilon is very, very small,

**[149:33 -> 149:36]** then practically we never see extos,

**[149:36 -> 149:38]** which is a very real kind of event.

**[149:38 -> 149:43]** And so it means that we can never get to get this

**[149:44 -> 149:47]** through risky, but to zero, right?

**[149:47 -> 149:51]** So we will be happy to obtain a risk

**[149:51 -> 149:54]** that is closer to a smaller than epsilon,

**[149:54 -> 149:58]** where epsilon is specified by a user, right?

**[149:58 -> 150:01]** So we are trying to define this sentence.

**[150:01 -> 150:06]** So in practice, any model can only be probably correct.

**[150:06 -> 150:11]** On the basis of a threshold that is user specified.

**[150:11 -> 150:14]** And we see that depends on the data in the next slides.

**[150:15 -> 150:17]** So there are two parts of this theory.

**[150:17 -> 150:20]** What we are trying to formalize here

**[150:20 -> 150:22]** is what is called the pack learning theory.

**[150:22 -> 150:27]** So in practice, every model is can only be probably

**[150:27 -> 150:29]** and approximately correct.

**[150:29 -> 150:31]** There's no freelance theorem.

**[150:31 -> 150:34]** You cannot guarantee that the model is always working

**[150:34 -> 150:36]** in every situation.

**[150:36 -> 150:38]** So again, I should learn about it,

**[150:38 -> 150:43]** who to deal with are probably and approximately correct.

**[150:44 -> 150:46]** So the risk can be,

**[150:46 -> 150:50]** I mean, we expect it to be smaller than a certain threshold.

**[150:51 -> 150:55]** And then the other part, approximately correct.

**[150:55 -> 150:58]** So the data is of course, again,

**[150:58 -> 151:00]** maybe can be run a majority,

**[151:00 -> 151:02]** the world is complex, as we said, it's noisy.

**[151:02 -> 151:05]** So there's always a very more small chance

**[151:05 -> 151:09]** that we are actually looking always in the same example.

**[151:09 -> 151:13]** No algorithm can really guaranteed for sure,

**[151:13 -> 151:16]** guaranteed these, what was the previous slide for sure.

**[151:16 -> 151:19]** The best that we can do is have algorithm

**[151:19 -> 151:23]** that fail with the probability delta,

**[151:23 -> 151:26]** where delta is again, used, specified.

**[151:26 -> 151:30]** And the probability we expect it to be over,

**[151:30 -> 151:32]** so it depends on the examples again.

**[151:32 -> 151:37]** So the overall formulation of the path learning theory,

**[151:37 -> 151:40]** this one is this.

**[151:40 -> 151:42]** So this is what we can state

**[151:42 -> 151:44]** for our machine learning model.

**[151:44 -> 151:48]** The probability that the risk is,

**[151:48 -> 151:50]** we want that the probability of the risk

**[151:51 -> 151:55]** slower than epsilon, we can state it practically

**[151:55 -> 151:58]** only to be larger than one-month delta.

**[151:58 -> 152:01]** So this is the condition which we are working.

**[152:01 -> 152:02]** Right?

**[152:02 -> 152:05]** So and it's a quite complex theory.

**[152:05 -> 152:07]** I don't go into the demonstration of the theorems,

**[152:07 -> 152:10]** but in practice, that's the best that we can state

**[152:10 -> 152:12]** for machine learning models.

**[152:12 -> 152:13]** Right?

**[152:13 -> 152:17]** So that the probability of the probability

**[152:17 -> 152:19]** is larger than more minus delta

**[152:21 -> 152:23]** of having the risk global maximum.

**[152:23 -> 152:26]** The raw video having the least lower than epsilon

**[152:26 -> 152:29]** should be larger than one step.

**[152:29 -> 152:32]** And epsilon and delta are user specified in which sense.

**[152:32 -> 152:36]** Well, epsilon and delta depends on the samples

**[152:36 -> 152:38]** you're looking at.

**[152:38 -> 152:41]** So the learning algorithm will run and will be trained

**[152:41 -> 152:44]** on m examples.

**[152:44 -> 152:47]** And these are user specified in the bounds of the data

**[152:47 -> 152:48]** themselves.

**[152:48 -> 152:52]** This m, so the data is called sample complexity.

**[152:52 -> 152:56]** It's just a definition, but this is again to tell you

**[152:56 -> 153:01]** that I cannot trust deep learning algorithm 100%.

**[153:03 -> 153:06]** There's no way, I mean, that's really the theorem

**[153:06 -> 153:09]** and the theory on which our models are based.

**[153:09 -> 153:12]** There are conditions that are threshold.

**[153:12 -> 153:13]** We can provide some guarantees,

**[153:13 -> 153:15]** but till there's really limits.

**[153:15 -> 153:16]** Okay.

**[153:18 -> 153:30]** And now, even if you have a lot of data, okay, and even if, I mean, you are respecting the, let's say,

**[153:30 -> 153:34]** the condition we said before, things can go wrong.

**[153:34 -> 153:40]** And these can go wrong because it depends on how you are defining your model.

**[153:40 -> 153:44]** So we go back to the choices of the machine learner.

**[153:44 -> 153:51]** So here I'm trying to define some concept and we'll get back to the loss function that we mentioned before

**[153:51 -> 153:54]** and that's the best that we can do.

**[153:54 -> 153:56]** So let me just somewhere else.

**[153:56 -> 154:01]** We define what is the loss function, which is what we can measure out of our training

**[154:01 -> 154:04]** samples, so the number of errors that we can do.

**[154:04 -> 154:08]** The loss function is connected to the empirical risk.

**[154:08 -> 154:14]** Okay, the empirical risk is what we can measure on our training samples.

**[154:14 -> 154:19]** The true risk would be the expected value of the loss,

**[154:19 -> 154:22]** but we don't have access to the full distribution of the data.

**[154:22 -> 154:25]** So we cannot calculate it.

**[154:25 -> 154:32]** And with this starting point, we try to optimize the empirical risk.

**[154:32 -> 154:38]** And now our model can only be probably an approximately correct.

**[154:38 -> 154:40]** That's the best that we can do.

**[154:40 -> 154:48]** And the values that define this path you remember to show

**[154:48 -> 154:51]** depend on how many data you have on the sample complexity

**[154:51 -> 154:53]** that you can exploit.

**[154:53 -> 154:56]** All this information are connected to that.

**[154:56 -> 154:58]** And even if you do your best and try

**[154:58 -> 155:02]** to have your model the more correct possible,

**[155:02 -> 155:05]** any way things can go wrong.

**[155:05 -> 155:09]** So again, it's just a sort of way up

**[155:09 -> 155:17]** code to not trust your model, especially if it's a model that has been trained from someone by someone

**[155:17 -> 155:25]** that doesn't know what machine learning means. So it was trained by me, right? So this can move

**[155:25 -> 155:32]** on. What do I mean with that? Well, we have some data and we go back to the idea of formalizing

**[155:32 -> 155:38]** and function of described this data, right? So it's similar. So either you have a function that

**[155:38 -> 155:42]** tries to make a prediction or you have a function that tries to describe the data,

**[155:42 -> 155:49]** more or less, I mean, you have the same condition. And for instance, here you are trying to fit

**[155:50 -> 155:55]** these points, right, with a function. And hopefully, what you want to do it is because

**[155:55 -> 156:00]** if you have a new X, maybe you can also say what is the Y, right? So it can be helpful to fit the

**[156:00 -> 156:06]** data to make a prediction. So maybe someone provides you a new X here. So if you fitted this

**[156:06 -> 156:12]** curve, then you can make the prediction and say, well, yes, it's y would be more less

**[156:12 -> 156:13]** here.

**[156:13 -> 156:16]** So now we are doing what is called a regression, right?

**[156:16 -> 156:21]** Because now we have this amount, but I continue to fail.

**[156:21 -> 156:27]** So we have this function y, I have an x, and I have my parameters that I have to estimate

**[156:27 -> 156:32]** by fitting the data, which are this type of data.

**[156:32 -> 156:38]** So my function is just a linear combination of the x's,

**[156:38 -> 156:43]** where the x's have a specific kind of formulation,

**[156:43 -> 156:46]** because it's linear in terms of the weights,

**[156:46 -> 156:48]** but it's not linear in terms of the x's,

**[156:48 -> 156:51]** because now I'm writing this as a polynomial function

**[156:51 -> 156:52]** of degree m, right?

**[156:52 -> 156:57]** So there's x, x squared, till x to the power of n.

**[156:57 -> 157:00]** So this is the real function that generated the data,

**[157:00 -> 157:01]** which I don't have access to.

**[157:01 -> 157:05]** I'm just observing the point and try to fit them.

**[157:05 -> 157:10]** Now, depending on the degree that I choose

**[157:10 -> 157:14]** to define my model, I can make some mistake.

**[157:14 -> 157:19]** So if the degree is zero, so I just choose a constant,

**[157:19 -> 157:23]** the way which I'm repeating today is very poor force

**[157:23 -> 157:25]** and this is not good.

**[157:25 -> 157:30]** I can raise the degree and have a one.

**[157:30 -> 157:31]** In this case, I have a line.

**[157:31 -> 157:34]** Again, it's not fitting the data very well.

**[157:34 -> 157:38]** With three, I started to fit the data good.

**[157:38 -> 157:42]** And then I can go over and have an end, which is very large.

**[157:42 -> 157:47]** And then surely my model is fitting the data perfectly.

**[157:49 -> 157:51]** It's passing through all of them.

**[157:51 -> 157:53]** What does it mean?

**[157:53 -> 157:58]** It means that when I measure the loss, my loss is zero.

**[157:58 -> 157:59]** It's perfect.

**[157:59 -> 158:03]** On the training samples, the function that they find,

**[158:03 -> 158:06]** the model that they find is perfectly able

**[158:06 -> 158:08]** to make the correct prediction.

**[158:10 -> 158:13]** This sound strange, it starts smelling bad.

**[158:13 -> 158:17]** We said that it's strange and the model is so perfect, right?

**[158:17 -> 158:19]** And indeed what's happening here

**[158:19 -> 158:22]** is that we are practically overfitting the model, right?

**[158:22 -> 158:26]** So we are defining a model that is memorizing

**[158:26 -> 158:32]** the training set and it will not be able to make a good prediction for the next data.

**[158:32 -> 158:40]** So look here, the next time I take an X and I want to make the prediction, the true output

**[158:40 -> 158:46]** should be this value here, so the height should be this, let me put it here, but instead my

**[158:46 -> 158:51]** model will predict this point, so wrong one.

**[158:51 -> 158:55]** So that's an issue that depends on the way

**[158:55 -> 158:56]** and formalizing the problem.

**[158:58 -> 159:03]** So I suppose the manual you have already heard is turned,

**[159:03 -> 159:07]** but I'm just repeating it just for basic concept.

**[159:07 -> 159:09]** What has been overfitting?

**[159:09 -> 159:11]** It means that you have a model

**[159:11 -> 159:15]** which is memorizing the training samples.

**[159:15 -> 159:20]** The loss on the training set is zero or it's very small.

**[159:20 -> 159:26]** But then when you go to the test, the error starts growing.

**[159:26 -> 159:34]** So here I'm showing it, showing the error when increasing the capacity of a model,

**[159:34 -> 159:42]** which for deep models can be having 100,000 layers.

**[159:42 -> 159:46]** So because you're increasing the amount of parameters you want to add.

**[159:46 -> 159:50]** And indeed, if you go back here, what are we doing?

**[159:50 -> 159:54]** When we have a value which is very high,

**[159:54 -> 159:57]** we are increasing the,

**[159:58 -> 160:01]** and say the degree of the polynomial.

**[160:01 -> 160:04]** But at the same time, we are increasing the amount

**[160:04 -> 160:08]** of parameters because this w is the parameter

**[160:08 -> 160:09]** and need to fit.

**[160:09 -> 160:13]** And if I have to get two power nine,

**[160:13 -> 160:15]** I also have nine weights.

**[160:15 -> 160:18]** And it's exactly what I'm doing.

**[160:18 -> 160:21]** I'm increasing the capacity of the model.

**[160:21 -> 160:25]** But increasing the capacity of the model might lead to a training

**[160:25 -> 160:28]** error, which is very small.

**[160:28 -> 160:31]** And the test error or evaluation error,

**[160:31 -> 160:35]** what we call generalization error, that starts growing back.

**[160:35 -> 160:40]** I mean, at the beginning, it seems that not only my model fits

**[160:40 -> 160:42]** well in training data, but it also

**[160:42 -> 160:48]** works well on a test data, on a validation set that is separated from the training set.

**[160:48 -> 160:57]** When it starts, my model is overfitted. I just memorized the training samples, and my model will

**[160:57 -> 161:04]** start making a lot of mistakes on the plot at the blind and time, so on new test samples.

**[161:05 -> 161:11]** So here it is underfitting zone. This is the overfitting zone. Now, overfitting is quite clear,

**[161:11 -> 161:16]** right? So it means that we have too many parameters. We exaggerate it in the way which we define the

**[161:16 -> 161:22]** model. But there's also the underfitting zone. And the underfitting zone was this case here.

**[161:23 -> 161:33]** So m0 is not enough, m1 is not enough, and 3 is fine, and 9 serves a bit much. So the underfitting

**[161:33 -> 161:37]** is when instead your model could have the potential

**[161:37 -> 161:41]** to be increased, right, to be improved,

**[161:41 -> 161:42]** to have more parameters,

**[161:42 -> 161:45]** and you're actually not providing it the possibility

**[161:45 -> 161:47]** to express correctly.

**[161:47 -> 161:50]** So here, maybe you could do better, right,

**[161:50 -> 161:53]** with different model or different way to formalize it.

**[161:53 -> 161:55]** So here's under 30, and here's over 50,

**[161:55 -> 161:58]** in the middle, I mean, more or less you are doing that.

**[161:58 -> 162:09]** Okay, so overfitting is when a predictor has excellent performance on the training sets,

**[162:09 -> 162:16]** but it's the performance at deployment time on the true world is very, very poor.

**[162:16 -> 162:20]** Queen, so overfitting is not about, and yeah, let me handle it.

**[162:20 -> 162:26]** It's not about the noise or about having just a training error equal to zero, but it's about

**[162:26 -> 162:34]** the fact we only have access to the empirical risk to the error that we can obtain from

**[162:34 -> 162:39]** the training data. The training error, which is not the true error, it's not the true risk,

**[162:39 -> 162:47]** we don't have access to that. Our approximation of modeling of the data comes from the training

**[162:47 -> 162:56]** samples and that's the only thing we are access to. Okay. So only if we are in the IID condition,

**[162:56 -> 163:02]** we can expect that our vision to predict in the future will respect what we have seen during

**[163:02 -> 163:09]** training. And of course, it's not enough. You have to model the things correctly, so not exaggerating

**[163:09 -> 163:15]** them up or fitting. So what you do to avoid overfitting first of all is typical things. I think you're

**[163:15 -> 163:21]** already seen it multiple times. When someone provides you a deficit, you divide it in training

**[163:21 -> 163:28]** and testing. Testing is a part that you never look at. You train a model on a subpart, then

**[163:28 -> 163:35]** on the deficit, and you can do what is called cross validation. So you divide the training part

**[163:35 -> 163:43]** again in two parts, subparts, and training and the validation. So your model, you calculate the

**[163:43 -> 163:49]** loss here. So you select the parameters of your model on the training sets and then you see what

**[163:49 -> 163:55]** happens on the validation. And this allows you to choose the regime in which you want to work.

**[163:55 -> 164:01]** How many parameters? So if I have to make a model deeper or not, which degree of the polynomial,

**[164:01 -> 164:07]** right? This is how you choose your parameter set, your hyper parameter set, so the model itself.

**[164:07 -> 164:12]** And then once this is done, then you go to test and you evaluate your model.

**[164:12 -> 164:24]** If your training data is big enough, you can also decide to divide it in some parts.

**[164:24 -> 164:29]** Well, it's the other way around. If it's not enough big, then you can rather than dividing it like this,

**[164:29 -> 164:37]** you can divide it in multiple parts and then you train on three of them and test on the other

**[164:37 -> 164:43]** and you go like this and you do it in round, then you take the average, this is called careful cross

**[164:43 -> 164:52]** validation. And if the sample that you keep out, so this part that you keep out for validation,

**[164:52 -> 165:00]** It's just composed by one sample. So if you have n sample, you use n minus one to train and one,

**[165:00 -> 165:07]** you leave it out. This is called live one out cross validation. So that's just a specific case.

**[165:09 -> 165:15]** Okay, so at least the thing you have to do is that you always divided on the centering part

**[165:15 -> 165:22]** three training validation and test. If the number of sample, so of course the training

**[165:22 -> 165:27]** service should be big enough to let you take some choices, you violate it on the validation,

**[165:29 -> 165:35]** and you never have to use the test set, which is left separated, which is the ending phase in

**[165:35 -> 165:40]** which you really evaluate if you're model, that you train on training and validation

**[165:40 -> 165:48]** words well, of course, if the test is too small, your what you claim might not be statistically

**[165:48 -> 165:53]** strong enough, because if you just test one or two samples, maybe you cannot make a statement about

**[165:53 -> 166:01]** the real ability of your model. So always good to have a test which is, let's say, rich enough to

**[166:01 -> 166:06]** make some statistical evaluation and take care of random floptation that you can handle first time.

**[166:06 -> 166:13]** So what we call model selection in practice is exactly this procedure.

**[166:13 -> 166:20]** So we want to select the model and the selection of the model happens through cost validation.

**[166:20 -> 166:28]** When I say never use a test set for model selection is this kind of number.

**[166:28 -> 166:29]** Okay.

**[166:29 -> 166:30]** So never ever.

**[166:30 -> 166:35]** I know, unfortunately, some are practice on race,

**[166:35 -> 166:38]** then people when they want to publish a paper,

**[166:38 -> 166:41]** they tend to use a test set to demonstrate,

**[166:41 -> 166:44]** I mean, to include the test set in the training,

**[166:44 -> 166:45]** this is cheating.

**[166:45 -> 166:48]** You are choosing your model of the basis

**[166:48 -> 166:52]** on the particular kind of data which you want to test it.

**[166:52 -> 166:54]** It's cheating and it's not realistic.

**[166:54 -> 166:55]** It means that what you show,

**[166:55 -> 167:00]** Since the model is actually trained on the deployment time,

**[167:00 -> 167:04]** you're actually overestimating the capabilities of the model.

**[167:04 -> 167:06]** So the test set, we have to leave it out.

**[167:06 -> 167:12]** Okay. So I think that for today, we can end here.

**[167:12 -> 167:15]** We practically covered some of the concept,

**[167:15 -> 167:17]** relevant concept for machine learning.

**[167:17 -> 167:18]** Some of them you already knew,

**[167:18 -> 167:20]** but just to refresh the data.

**[167:20 -> 167:21]** And then we go on.

