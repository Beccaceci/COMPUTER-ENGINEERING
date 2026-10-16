# Lecture Transcription

- **Source**: `temp_audio_62414.wav`
- **Model**: `base.en`
- **Device**: `mps`

---

**[00:00 -> 00:29]** We'll need to initialize that somehow. And we discuss about the right decision, which is something that happened inside the network, right? So to summarize how the variability of the parameters, how the numbers inside the network can itself change. But we also know that we are providing a need for learning, and we might need also to maybe normalize the data itself, so we might need some data pre-processing, so we need to also focus on what we are providing,

**[00:30 -> 00:35]** to the network and possibly apply some sort of

**[00:35 -> 00:38]** normalization in a new state.

**[00:38 -> 00:46]** So, well, here we're looking at data, of course,

**[00:46 -> 00:47]** we're simplifying the little data

**[00:47 -> 00:49]** that's on the dimension.

**[00:49 -> 00:51]** And we see that we have managed with it

**[00:51 -> 00:59]** that actually has sort of principal axis, right,

**[00:59 -> 01:02]** which is not the virus,

**[01:02 -> 01:06]** which is clearly given more one direction than other.

**[01:06 -> 01:27]** And Nruga, the

**[01:27 -> 01:32]** of sine for the output in theta that was constant issue

**[01:34 -> 01:37]** to degrade them, then a similar issue

**[01:37 -> 01:42]** can originate also, but the fact that our data

**[01:42 -> 01:43]** is not zero centred.

**[01:44 -> 01:46]** So this, we discussed about this,

**[01:46 -> 01:50]** we were talking about the activation function,

**[01:50 -> 01:53]** right, so the signal that was not zero centred

**[01:53 -> 01:56]** and it was leaving to an issue.

**[01:56 -> 01:58]** Well, similar things can happen.

**[01:58 -> 01:59]** So, see where you should go now.

**[01:59 -> 02:04]** If we don't recognize, if we don't center our data.

**[02:05 -> 02:08]** So, the first thing that we have to think about

**[02:08 -> 02:11]** is really zero standard of data, okay?

**[02:11 -> 02:13]** And then eventually there are also other things

**[02:13 -> 02:14]** that people do.

**[02:14 -> 02:17]** Maybe they can think about widening for data.

**[02:17 -> 02:20]** So, I'm already significantly close

**[02:20 -> 02:24]** between moving in features that characterize them.

**[02:24 -> 02:27]** So in this case, we adjust the risk scheme because it's

**[02:27 -> 02:31]** very hard to see me on some how extension

**[02:31 -> 02:35]** in the principal's in directions.

**[02:35 -> 02:37]** Something that, of course, we can do

**[02:37 -> 02:40]** so we know by the best of evaluation.

**[02:40 -> 02:43]** So somehow, you can see this kind of stuff

**[02:43 -> 02:47]** as the normalization that we were doing inside the network.

**[02:47 -> 02:50]** Now we are actually also doing it at the beginning.

**[02:50 -> 02:52]** So all the manual inserts.

**[02:52 -> 02:59]** So we can center the data and then make sure that, you know, also why the data is recorded

**[03:03 -> 03:10]** in the future. Let's say that this kind of operation, not with a particular process in

**[03:10 -> 03:17]** the algorithm, so it's, nowadays that is more rare than just simply centering the algorithm.

**[03:17 -> 03:24]** So, centering the data is super important, applying some instead of widening or neglect

**[03:24 -> 03:31]** relation are a specific strategy that might be needed for particular kind of data, but

**[03:31 -> 03:34]** not this kind of data.

**[03:34 -> 03:36]** And why centering the data is relevant?

**[03:36 -> 03:45]** Well, you can extend the discussion that we did regarding what's happening inside where

**[03:45 -> 03:49]** of the network, but you can also think about, I mean,

**[03:49 -> 03:51]** very simple example, right?

**[03:51 -> 03:56]** So if you have, think about the fact that your model

**[03:56 -> 04:00]** is initialized with weights that are equal to zero.

**[04:00 -> 04:04]** Or at least, I mean, if you think about the linear model,

**[04:04 -> 04:09]** Wx plus B, you can say, okay, at least the B as I did zero.

**[04:10 -> 04:13]** Right, so the coefficient that indicates

**[04:13 -> 04:16]** where your line captures the y axis, right?

**[04:16 -> 04:18]** So it's that kind.

**[04:18 -> 04:21]** So if you think about initializing the line in sleep,

**[04:21 -> 04:25]** then you're lying in deep process of mooring.

**[04:25 -> 04:28]** And if your data is far away with respect

**[04:28 -> 04:31]** to the origin of your axis of your reference,

**[04:31 -> 04:38]** say, yeah, the base of the vector of your space,

**[04:38 -> 04:43]** then a small variation in this loop of this line

**[04:43 -> 04:47]** will lead to a significant variation in the prediction

**[04:47 -> 04:50]** because as more angle will have a big effect

**[04:50 -> 04:52]** if your data are far away, right?

**[04:52 -> 04:57]** Because although you have a more angle here

**[04:57 -> 04:58]** than that, you can call it somehow.

**[04:58 -> 05:01]** And this is something you don't want, right?

**[05:06 -> 05:11]** So since you expect that somehow you have a simple

**[05:11 -> 05:17]** the integration where the bias is zero or many of your parameters can be very small,

**[05:17 -> 05:21]** then at the same time you would like to use it as a big code of the origin,

**[05:21 -> 05:27]** so that's more variation of the stroke of the line, or not have a big effect on the variation.

**[05:27 -> 05:32]** So this is another motivation on how it tells you that centralizing the data,

**[05:32 -> 05:48]** So in general, what is the rule of thumb?

**[05:48 -> 05:53]** You can think about considering one of your limiters.

**[05:53 -> 05:57]** Well, you will see that different kind of architecture

**[05:57 -> 06:00]** adopt a different city kind of pre-fossed.

**[06:00 -> 06:04]** More or less, the basic logic of the same,

**[06:04 -> 06:08]** we want to center the data.

**[06:08 -> 06:11]** So centering can be done, for instance,

**[06:11 -> 06:16]** if you deal with images, you can just take the overall

**[06:16 -> 06:17]** texture that you find the image.

**[06:17 -> 06:22]** So 32 by 32 by 3, here I'm supporting it,

**[06:22 -> 06:25]** and considering site for 10 images

**[06:25 -> 06:29]** that are 32 of these two pixels by three.

**[06:29 -> 06:31]** Well, we have RGB.

**[06:31 -> 06:34]** And we can take the average image.

**[06:34 -> 06:36]** And then all the images in my data set,

**[06:36 -> 06:40]** what I do is just take each of them and there's a chart in view.

**[06:40 -> 06:43]** So in this way, I'm centering the data set.

**[06:43 -> 06:47]** This is something that is the standard kind of processing

**[06:47 -> 06:51]** we would apply for the very first kind of architecture

**[06:51 -> 06:56]** which are alexanate architecture, or this network that,

**[06:56 -> 07:01]** I think, this alexan or the architecture that won the first challenge

**[07:01 -> 07:06]** and actually demonstrated the possibility of this network to perform well

**[07:06 -> 07:10]** on the initial situation. And then in the years that many other

**[07:10 -> 07:14]** alexanate, you see that for instance, for this other architecture,

**[07:14 -> 07:19]** what you can do is not considering the average image,

**[07:19 -> 07:24]** but considering the mean per channel,

**[07:25 -> 07:28]** so you will have the mean red color,

**[07:28 -> 07:32]** the mean green color and green blue color,

**[07:32 -> 07:34]** and then everything will be used

**[07:34 -> 07:36]** to track this tree, they will follow them,

**[07:36 -> 07:39]** taking the average image roll.

**[07:40 -> 07:43]** Yeah, so you will consider this average per channel.

**[07:44 -> 07:49]** Yeah, and so I see that I view for more

**[07:49 -> 07:51]** reason kind of architecture.

**[07:51 -> 07:56]** So anyway, you have to apply at least a very simple strategy

**[07:56 -> 07:58]** to research your data.

**[07:58 -> 08:02]** Other kind of technique like an organization,

**[08:02 -> 08:07]** a wide- domain, an applying PCA as a wide order,

**[08:07 -> 08:10]** and a wide- domain, or other more complex strategies

**[08:10 -> 08:14]** of different relation, these are less common

**[08:14 -> 08:17]** in the manual specific kind of stuff.

**[08:17 -> 08:21]** But at least the centering is something

**[08:21 -> 08:23]** you have to think about.

**[08:23 -> 08:30]** And these can also create some, be the source of some bugs,

**[08:30 -> 08:33]** because maybe you have a lot of experience

**[08:33 -> 08:35]** of working on an architecture.

**[08:35 -> 08:39]** And the standard strategy is to pre-elaborate your data

**[08:39 -> 08:44]** with this logic here, as Alex and I moved into move,

**[08:45 -> 08:47]** and from this kind of architecture.

**[08:47 -> 08:50]** But then some other reason, it happens that you need to work

**[08:50 -> 08:52]** in a different architecture,

**[08:52 -> 08:56]** and you tend to code the import of the data

**[08:56 -> 08:57]** and you're processing the same way,

**[08:57 -> 09:01]** but that model, maybe you are narrating weights

**[09:01 -> 09:04]** from the freedom model that instead was managing

**[09:04 -> 09:06]** the centering in a different way.

**[09:06 -> 09:11]** So always pay attention to what is the strategy

**[09:11 -> 09:14]** that the author performs for the architecture

**[09:14 -> 09:17]** and in general how other researchers

**[09:17 -> 09:19]** are actually using that kind of model.

**[09:19 -> 09:21]** So there are some other strategies

**[09:21 -> 09:24]** and it's good to have a look at what is that

**[09:24 -> 09:25]** that the thinking to me is.

**[09:30 -> 09:35]** Okay, so, and we said that certainly

**[09:35 -> 09:39]** I mean, this idea of normalizing at the input level

**[09:39 -> 09:43]** is relevant, but the other aspect we want to focus on

**[09:43 -> 09:47]** is also how to maybe show the weights.

**[09:47 -> 09:51]** So what we discussed about grinding the sand,

**[09:51 -> 09:55]** you remember, we are saying that the new set of weights

**[09:55 -> 09:58]** would be equal to the weights at the previous step

**[09:58 -> 10:02]** minus the learning rate multiplied by the findings

**[10:02 -> 10:03]** of the losses, right?

**[10:03 -> 10:08]** But then, at the beginning, how do we initialize the weights

**[10:08 -> 10:11]** of this network?

**[10:11 -> 10:16]** Well, we can have a look at different cases.

**[10:16 -> 10:19]** So we're looking at a very small network.

**[10:19 -> 10:23]** And you see that here are different nodes,

**[10:23 -> 10:28]** so we're looking at the moving realities.

**[10:28 -> 10:29]** We're going to correspond in value,

**[10:29 -> 10:32]** and then have the alpha, the sigma.

**[10:32 -> 10:35]** We're doing just a binary presentation, for our point.

**[10:35 -> 10:38]** And this is the causes of the loss function,

**[10:38 -> 10:40]** what happens with the loss function,

**[10:40 -> 10:43]** the more you train the actor.

**[10:43 -> 10:46]** So it will initialize the network with weights

**[10:46 -> 10:49]** that are very small.

**[10:49 -> 10:52]** What happens is that at the beginning,

**[10:52 -> 10:55]** the loss function remains stable.

**[10:55 -> 10:58]** So we are not changing the weights,

**[10:58 -> 11:00]** so that the network is not really learning.

**[11:00 -> 11:04]** it takes quite some equal, so quite some certain number

**[11:04 -> 11:07]** of parts over the data to understand

**[11:07 -> 11:10]** what the right direction in which the rates should be

**[11:10 -> 11:14]** updated and moved, then be able to perform

**[11:14 -> 11:14]** the presentation.

**[11:14 -> 11:18]** So you'll have this kind of behavior that immediately

**[11:18 -> 11:21]** will tell you that the way in which you initialize the rates

**[11:21 -> 11:24]** is not ideal.

**[11:24 -> 11:27]** It is quite small, the way it's not covered in children.

**[11:30 -> 11:34]** So what happens is that if the weights are too large,

**[11:34 -> 11:37]** well, yeah, I mean, the network starts immediately

**[11:37 -> 11:40]** changing its weight, and you see that

**[11:40 -> 11:43]** the sort of situation and how the decision is taken.

**[11:43 -> 11:46]** The loss goes down, there is some oscillation

**[11:46 -> 11:50]** at the beginning, and it goes down,

**[11:50 -> 11:55]** but it tends to pull, and it doesn't go really toward zero.

**[11:55 -> 12:06]** So most probably what happened is that you are ending up in a minimum that is not really an ideal minimum.

**[12:06 -> 12:11]** There can be some better minimum where you want to go.

**[12:11 -> 12:16]** But with this kind of initialization, when the weights are too large,

**[12:16 -> 12:25]** then you're not really able to improve the optimization and to minimize furthermore your loss.

**[12:25 -> 12:31]** So, and moreover, at the end, the kind of classification you get is not that good.

**[12:31 -> 12:37]** That's the performance of the female circuit, is not what you expect.

**[12:37 -> 12:40]** So, it might get better.

**[12:40 -> 12:50]** So if the weights are just right, so if you're able to do a proper choice, you see immediately how the weights go.

**[12:50 -> 13:01]** So if it starts going down smoothly and it goes down down downward, maybe it's slowly, but it tends to really work zero.

**[13:01 -> 13:09]** So you don't have that kind of a plateau at the beginning that we have when the weights

**[13:09 -> 13:15]** were too small and not even the other kind of result when the weights are too high where

**[13:15 -> 13:19]** you plateau at the end but at the very end quite a high level.

**[13:19 -> 13:26]** So here everything is going down nicely and you see that the kind of decision that you get

**[13:26 -> 13:31]** So the kind of decision in terms of binary distribution

**[13:31 -> 13:38]** in more the task and the final performance

**[13:38 -> 13:41]** in terms of the task of the model.

**[13:41 -> 13:45]** OK, so no one to have these kinds of stuff.

**[13:45 -> 13:48]** So the initial decision is an important step,

**[13:48 -> 13:52]** and we need to find a strategy to properly assign

**[13:52 -> 13:55]** these weights of the beginning.

**[13:55 -> 14:01]** Well, as we mentioned before, well, we really don't know where to start from.

**[14:01 -> 14:08]** One possible hypothesis to say, well, let's just start from zero weights.

**[14:08 -> 14:12]** Now, zero weights have the factor.

**[14:12 -> 14:16]** So the network doesn't learn absolutely anything.

**[14:16 -> 14:24]** And the problem is not to say that the weights are too small or the factor they are zero.

**[14:24 -> 14:29]** The problem is that all weights are zero at the same time.

**[14:29 -> 14:37]** And so there's no direction and there's no indication of how these weights have to move.

**[14:37 -> 14:44]** So really the model is not able to understand the last landscape and where what is the minimum,

**[14:44 -> 14:45]** because everything is zero.

**[14:45 -> 14:52]** Again, it's not a matter that the weights are all equal, but they are all zeros to say.

**[14:52 -> 14:55]** but the fact that they are all equal.

**[14:55 -> 14:58]** So even if all the ways where all equal is more,

**[14:58 -> 15:00]** so at a certain constant, then fixed,

**[15:00 -> 15:03]** for an effort, that will create issues,

**[15:03 -> 15:06]** kind of not providing that to the network

**[15:06 -> 15:07]** that possible need to learn.

**[15:09 -> 15:14]** So, indeed, what we have when we fix everything to zero

**[15:15 -> 15:19]** is that we don't have what is called symmetry breaking.

**[15:19 -> 15:26]** So, since the beginning, what we said is that we are creating this network with different

**[15:26 -> 15:34]** modules and we expect these to help the network first to focus on small features, characteristics

**[15:34 -> 15:39]** which then are combined in larger structure and then become some semantic area.

**[15:39 -> 15:47]** So, we would like each neuron to focus on some physical, some specific attributes on some

**[15:47 -> 15:51]** the specific pattern that I show in the image is not going to be done.

**[15:51 -> 15:57]** But if we put everywhere the same weights, more weights and old equal,

**[15:57 -> 16:02]** well, we are not providing the natural, this ability to differentiate.

**[16:02 -> 16:08]** And providing each neuron the possibility to focus on some specific characters.

**[16:08 -> 16:12]** So all the neurons will be able to see this.

**[16:12 -> 16:15]** And so we have this issue of symmetry which is not broken,

**[16:15 -> 16:18]** which is instead what we would like to do.

**[16:18 -> 16:20]** And this is not an issue related to having the young

**[16:20 -> 16:25]** four zeros, but is related to having a constant

**[16:25 -> 16:26]** insulation.

**[16:26 -> 16:30]** This will certainly perform very poorly.

**[16:30 -> 16:34]** So we need to find another strategy.

**[16:34 -> 16:40]** And so because this, as you said,

**[16:40 -> 16:43]** we need to break this symmetry.

**[16:43 -> 16:48]** And yeah, so the initial point of the way

**[16:48 -> 16:51]** which we are initializing our network

**[16:51 -> 16:54]** might make a significant difference.

**[16:56 -> 17:01]** So usually what we can think about

**[17:01 -> 17:06]** is to define parameters that belong or are drawn

**[17:06 -> 17:09]** from a distribution very standard

**[17:09 -> 17:12]** generally stationary distribution, right?

**[17:12 -> 17:16]** But again, so how do we choose the solution?

**[17:16 -> 17:18]** So what fine mediums can be selected?

**[17:18 -> 17:24]** What which foundation would want to consider to then

**[17:24 -> 17:28]** start from the distribution and draw in fine years of width

**[17:28 -> 17:32]** to the initial value?

**[17:32 -> 17:32]** What can we do?

**[17:32 -> 17:36]** Well, we can think about a Gaussian.

**[17:36 -> 17:38]** The distribution is 0 to the woman.

**[17:38 -> 17:41]** And 0 to 0 wants some other deviation.

**[17:41 -> 17:45]** say that we start from this. And then we start selecting the phase,

**[17:45 -> 17:51]** going based on the distribution. What we need to do is to initialize our

**[17:51 -> 17:54]** value, right? So now let's forget for a minute about the

**[17:54 -> 18:01]** beam or think that these beams are even included inside W. And so our

**[18:01 -> 18:08]** matrix would be the dimension of the wave by the dimension of the output,

**[18:08 -> 18:12]** So you remember that we have to be down to write by x, right?

**[18:12 -> 18:16]** So and the number of rows will tell me how many elements

**[18:16 -> 18:21]** are we having the output, why the dimensional each row

**[18:21 -> 18:25]** should be the same of the dimensional x.

**[18:25 -> 18:28]** So we have this dimensionality that

**[18:28 -> 18:31]** sends the dimension of w.

**[18:31 -> 18:33]** And what I'm doing is that I'm taking this matrix

**[18:33 -> 18:37]** and I'm filling it with random values,

**[18:37 -> 18:42]** I'm going to extract it from a Gaussian distribution with 0 min and 0.0.0.

**[18:42 -> 18:46]** So I'm going to do this around n-natural, right?

**[18:46 -> 18:48]** Which is doing this, right?

**[18:48 -> 18:53]** I'm just selecting the dimension, I'm going to add to the sum of the division I want to do.

**[18:53 -> 19:01]** So this kind of choice, again, we are breaking the symmetry because not only do we go all equal,

**[19:01 -> 19:04]** we are selecting randomly.

**[19:04 -> 19:09]** And it's quite okay, let's see, when we're dealing with more math work.

**[19:10 -> 19:17]** But when the math work grows, these still provide us with some issues.

**[19:17 -> 19:20]** So we lost with some issues.

**[19:21 -> 19:33]** So let's think about an artwork where we have only simple and fully connected areas.

**[19:34 -> 19:39]** So, let's say that we have six layers plus the input,

**[19:39 -> 19:43]** and internally the dimensionality of the output of each one

**[19:43 -> 19:47]** is 2096, and we have a little set of areas at this time.

**[19:49 -> 19:53]** So, what we're doing is that this is our input,

**[19:53 -> 19:55]** so now I'm just performing, I have some data,

**[19:55 -> 19:58]** I'm done with the define.

**[19:58 -> 20:01]** I'm defining the dimensionality between and the out, right?

**[20:01 -> 20:06]** that has to respect the connectedly dimensional X.

**[20:06 -> 20:09]** And then, calculate V by W, in the way in which I defined

**[20:09 -> 20:10]** before.

**[20:10 -> 20:14]** And after, let's say, the linear part,

**[20:14 -> 20:18]** where I have W as multiplied by X,

**[20:18 -> 20:21]** I have my normal linearity, so the activation function.

**[20:21 -> 20:24]** So I have this, let's say, just a WX.

**[20:24 -> 20:28]** And then, I'm using the activation function on H.

**[20:28 -> 20:32]** Now we have discussed about the fact that the image is better,

**[20:32 -> 20:35]** the signal is not ideal.

**[20:35 -> 20:39]** The problem now is just to understand what's happening.

**[20:39 -> 20:42]** It's just a high level example.

**[20:42 -> 20:45]** And consider also that, in the younger time,

**[20:45 -> 20:47]** back then, the given this comes,

**[20:47 -> 20:50]** now that was actually the advantage.

**[20:50 -> 20:53]** So we're trying to analyze somehow how the story

**[20:53 -> 20:59]** of the wave utilization was resumpting.

**[20:59 -> 21:07]** Okay, so if we look at the output and we know that time age provides us with values between

**[21:07 -> 21:08]** minus 1 and 1.

**[21:08 -> 21:09]** Right?

**[21:09 -> 21:10]** So whatever we provide is good.

**[21:10 -> 21:20]** We look at the output of each layer and we just collect the surface.

**[21:20 -> 21:24]** So how many times you see between minus one, right?

**[21:24 -> 21:28]** So I think about inviting the space in the old things

**[21:28 -> 21:31]** and then just calculating the frequency

**[21:31 -> 21:33]** and looking at what happens in time.

**[21:35 -> 21:38]** So with this strategy, what we have is that in the beginning,

**[21:38 -> 21:41]** the babies are more or less from the beginning,

**[21:41 -> 21:45]** which is time, so it means that we have quite good viability.

**[21:45 -> 21:47]** But then the more we go inside and then for it,

**[21:47 -> 21:54]** more in draft is the value that we'll serve gets towards zero and the distribution strings.

**[21:54 -> 22:06]** But I mean in this kind of condition, so the value are zero and when we, every output

**[22:06 -> 22:13]** then multiply by the model and at the end everything is very cool to do.

**[22:13 -> 22:18]** This provides us with very low expressiveness.

**[22:18 -> 22:22]** So again, we have some limitation.

**[22:22 -> 22:25]** Everything is collapsing for zero,

**[22:25 -> 22:30]** and the method is not really able to learn properly,

**[22:30 -> 22:34]** like so, all zero, no worry.

**[22:34 -> 22:37]** And this, again, is a problem.

**[22:37 -> 22:40]** So we said this kind of decision makes sense

**[22:40 -> 22:45]** if you have more network block as far as you go,

**[22:45 -> 22:47]** at least even around six layers,

**[22:47 -> 22:49]** then you have this kind of issue in life.

**[22:50 -> 22:55]** Okay, so the legal issue is in the standardization

**[22:55 -> 22:59]** that we set in the beginning, then it was 0.01,

**[22:59 -> 23:02]** and then B equals two more.

**[23:02 -> 23:05]** So let's try to see what happens.

**[23:05 -> 23:08]** If instead, I consider 0.05.

**[23:08 -> 23:16]** Okay. Well, I end up in a similar condition. So, a similar, it's a different issue but

**[23:16 -> 23:23]** in a similar programmatic condition. Because what I have is that it's the values, I mean,

**[23:23 -> 23:29]** with the behavior of the output of the activation to off with an H, will bring, I mean, most of my

**[23:29 -> 23:34]** My data, again, there's this data chart of sparse around 0.

**[23:34 -> 23:38]** And then you have to speak towards 1, 1, where you know,

**[23:38 -> 23:41]** I mean, the non-H is flat there.

**[23:41 -> 23:44]** And no gradient in that region.

**[23:44 -> 23:47]** So you have data that are either close to 0,

**[23:47 -> 23:53]** or in practice, are close to region-wide agreement in 0.

**[23:53 -> 23:57]** And so even in this case, all the local gradients are 0,

**[23:57 -> 23:58]** no, they're not.

**[23:58 -> 24:05]** So, let's say that the strategy is okay.

**[24:05 -> 24:11]** So, because we are running the mindset, we are breaking symmetry, but the issue is we

**[24:11 -> 24:18]** need to choose the proper value of the original standardization of Gaussian formulae to draw

**[24:18 -> 24:21]** our values.

**[24:21 -> 24:34]** This idea of in a high level rule about how to select this video was studied by the Schabendjoe and Xavier Giro.

**[24:34 -> 24:45]** Back in 2010, that's where indeed trying to understand how to initialize a simple number.

**[24:45 -> 24:50]** And what they proposed is in this position of course,

**[24:50 -> 24:53]** takes the name of the first author,

**[24:53 -> 24:54]** called Sabine's

**[24:54 -> 24:55]** television.

**[24:55 -> 24:58]** And now on, I mean, I already mentioned Alex Knapp

**[24:58 -> 25:00]** that goes under the name of the first author,

**[25:00 -> 25:01]** which is Alex Knapp.

**[25:01 -> 25:04]** Because I mean, he's very cool to be pronounced.

**[25:04 -> 25:06]** So now we're looking at the examination

**[25:06 -> 25:09]** on the name of the first author of his favorite.

**[25:09 -> 25:13]** You know that Young Lecan signed his mentors

**[25:13 -> 25:16]** with the limit while the entire.

**[25:16 -> 25:17]** So now you will be the next slide.

**[25:17 -> 25:19]** So make sure to become famous,

**[25:19 -> 25:23]** and you'll only create the solutions

**[25:23 -> 25:26]** that everybody will remember about your name.

**[25:26 -> 25:29]** So what is this study and its elevation?

**[25:29 -> 25:32]** Well, it is saying that we need to choose properly

**[25:32 -> 25:38]** this variable here, and the strategy is to select

**[25:38 -> 25:42]** one over the square root of the dimensionality

**[25:42 -> 25:48]** the image. It seems like the magic rule is like a good day at the age of my grandmother

**[25:48 -> 25:56]** and it will work. Well, there is a reason of course, right? It's not just the magic of

**[25:56 -> 26:02]** the week. So we have to try to understand what's happening here. So first of all, let's see

**[26:02 -> 26:08]** the effect. Well, the effect is this one, right? So we have strange, maybe distribution

**[26:08 -> 26:12]** at the beginning, but more or less, all the layer remains alive.

**[26:12 -> 26:16]** So the distribution is not shrinking towards zero,

**[26:16 -> 26:19]** not even going to the maximum.

**[26:19 -> 26:22]** So it's behaving nicely.

**[26:22 -> 26:25]** And this is exactly what we want.

**[26:25 -> 26:28]** Now, this is the just right choice.

**[26:28 -> 26:30]** Like what we said, we have to apply the weight

**[26:30 -> 26:31]** in the right way.

**[26:31 -> 26:35]** And this seems to be the sum of the option.

**[26:35 -> 26:40]** And these discussions, in these, in terms of what we're providing here,

**[26:40 -> 26:44]** is for people who are natural, so only fully connected layers,

**[26:44 -> 26:48]** where we know that we are managing just one vector, right?

**[26:48 -> 26:52]** Or even if you're a mathematical, then a me-made-chair just comes over

**[26:52 -> 26:58]** and you're able to own vector, because we're going to be layers only able to manage vectors.

**[26:58 -> 27:03]** Then when you deal with it from usually layers, well, what would be the input

**[27:03 -> 27:07]** with the middle shire domain, but will be kernel size, right?

**[27:07 -> 27:11]** So your window that you're moving will be your dream, right?

**[27:11 -> 27:14]** So the kernel size is side by side.

**[27:14 -> 27:18]** So kernel size squared by the number of English numbers.

**[27:18 -> 27:22]** So this will be the begin that you would use in the case

**[27:22 -> 27:24]** in which you are applying this logic of weight

**[27:24 -> 27:28]** and celebration for a declaration.

**[27:28 -> 27:32]** But again, there is still this doubt of why this paper,

**[27:32 -> 27:38]** why Ben-Juan and Agistra, Sanya, were deciding from the state.

**[27:38 -> 27:43]** Well, the reason is that they want to keep the violence.

**[27:43 -> 27:45]** So what does it mean?

**[27:45 -> 27:50]** Well, we would really like that the violence of the output

**[27:50 -> 27:52]** is equal to the violence of the user.

**[27:52 -> 27:56]** So I want that one may modulate a lot for instance,

**[27:56 -> 27:59]** the violence of the output in the behavior that I had

**[27:59 -> 28:01]** should be analogous to the violence of the user.

**[28:01 -> 28:05]** And if I impose this condition or if I'm able to apply

**[28:05 -> 28:07]** this condition, then I have the defect.

**[28:07 -> 28:10]** So more or less, I'm able to keep

**[28:10 -> 28:15]** both the distribution of all the bases.

**[28:15 -> 28:20]** So here, this is just the linear part, right?

**[28:20 -> 28:22]** And we now need to express.

**[28:22 -> 28:26]** Now, the variance of y depends on the value of x.

**[28:26 -> 28:34]** And the best particular dimension of the x-ray.

**[28:34 -> 28:38]** And this is just a little bit back to the statistics

**[28:38 -> 28:41]** and to the IAD and both of the slides.

**[28:41 -> 28:46]** So you suppose that all the data are extracted IAD

**[28:46 -> 28:48]** from the same distribution.

**[28:48 -> 28:50]** And now, also down the right, there

**[28:50 -> 28:51]** should be a certain amount of distribution

**[28:51 -> 28:55]** in the fixed and beginning of the discussion.

**[28:55 -> 28:58]** And you can express the variance.

**[28:58 -> 29:02]** This is the, and if one we unvold it,

**[29:02 -> 29:04]** what does mean, stop and derive?

**[29:04 -> 29:06]** Is the expected value of a square?

**[29:06 -> 29:09]** Multiply the expected value of WI.

**[29:09 -> 29:13]** Minus expected value of X, raise to the power of 2.

**[29:13 -> 29:19]** Will be divided by the expected value of raise to the power of 2.

**[29:19 -> 29:21]** So it seems X and WI independent,

**[29:21 -> 29:23]** then you can be careful with these two bars.

**[29:23 -> 29:25]** we have in expression.

**[29:25 -> 29:30]** So this means that if the variance of the double

**[29:30 -> 29:34]** is one over the dimension of the input,

**[29:34 -> 29:37]** then we can get this condition that we are for.

**[29:37 -> 29:40]** So then the variance of what we obtain

**[29:40 -> 29:43]** after the module that we are plotting a pre-layer

**[29:43 -> 29:47]** is equal to the variance that we have at the beginning.

**[29:47 -> 29:51]** So this is just the reason why we are

**[29:51 -> 29:56]** and why the figure and the team wrote that paper

**[29:56 -> 29:58]** for proposing the solution and lead

**[29:58 -> 30:02]** which is the one that is largely used in the database.

**[30:02 -> 30:06]** So it's a very powerful kind of result.

**[30:09 -> 30:14]** Now, that pulls when we're dealing with that age.

**[30:16 -> 30:19]** And what happens when we're dealing with red?

**[30:19 -> 30:23]** So, randomly it's a different kind of manuality.

**[30:23 -> 30:27]** And we expect a different kind of behavior.

**[30:27 -> 30:32]** Well, it turns out that here, of course, you see now

**[30:32 -> 30:36]** that we have the right of the maximum between the linear 5

**[30:36 -> 30:40]** and 0, so there are ws and 0.

**[30:40 -> 30:43]** And using the series in addition is not ideal,

**[30:43 -> 30:46]** because what you see is that, again,

**[30:46 -> 30:51]** see this effect of shrinking on the distribution course to zero.

**[30:51 -> 30:56]** And it turned out that some of the formal up thinkers

**[30:56 -> 30:59]** five years after the previous one.

**[30:59 -> 31:03]** Another team from Microsoft Research,

**[31:03 -> 31:07]** and specifically from Microsoft Research Asia,

**[31:07 -> 31:13]** they discussed about how to change the skin cell infection.

**[31:13 -> 31:15]** So what they discover is that in practice,

**[31:15 -> 31:18]** in this situation, to introduce a tool

**[31:18 -> 31:22]** in a numerator of the value that you were passing before,

**[31:22 -> 31:25]** it was one over the square root of the,

**[31:25 -> 31:26]** I don't think you should have a link,

**[31:26 -> 31:29]** but these now are new, so I think

**[31:29 -> 31:32]** the square root of two over the E.

**[31:33 -> 31:34]** Why?

**[31:34 -> 31:37]** Because in practice, this tool is more or less

**[31:37 -> 31:39]** compensating for the fact that

**[31:39 -> 31:46]** that relu has a zero oblivion on one half of the space,

**[31:46 -> 31:50]** or a negative radius of the opposite.

**[31:50 -> 31:54]** And this too somehow helps to, here,

**[31:54 -> 31:59]** helps to compensate for this housing of the leading space of your data.

**[31:59 -> 32:04]** And what you get, and as simple as the solution means,

**[32:04 -> 32:09]** that you observe now at the nicer, nicer kind of situation.

**[32:09 -> 32:16]** Still you have zero on the left, but these is not peak as the one you get in the previous

**[32:16 -> 32:17]** case.

**[32:17 -> 32:24]** So indeed, the solution is called hanging and stabilization for the micro-doctorate which

**[32:24 -> 32:29]** angia and penetration.

**[32:29 -> 32:35]** So this case is just to, what's happening?

**[32:35 -> 32:37]** Okay.

**[32:37 -> 32:45]** So this is just the logic that we define for the implementation.

**[32:45 -> 32:49]** And this is an important part in such an after-the-advent work.

**[32:49 -> 32:58]** And we will see that several architectures will also have a particular kind of structure.

**[32:58 -> 33:03]** So, till now, we'll discuss about what we call people with architecture, right?

**[33:03 -> 33:06]** So, we have an input, the input passes through the network,

**[33:06 -> 33:12]** you calculate everything with the number, what we discuss about the computational graph, right?

**[33:12 -> 33:17]** So, you have the input, you calculate the steps, you pick forward information,

**[33:17 -> 33:24]** then you get the loss, and then from the loss, you do the back-to-the-back edition of the data collection, and so on.

**[33:24 -> 33:29]** And this is sort of, let's say, very clear directional

**[33:29 -> 33:33]** counter-computer with one path along the network.

**[33:33 -> 33:35]** But there's some architecture that

**[33:35 -> 33:38]** are called residual network, where you can see

**[33:38 -> 33:41]** these kind of connections.

**[33:41 -> 33:43]** These are residual connections,

**[33:43 -> 33:46]** or also called scheme connections.

**[33:46 -> 33:50]** That's, they affect the way they do.

**[33:50 -> 33:54]** Because in practice, we have an input here,

**[33:54 -> 33:57]** But, and we are elaborating the input of the rule

**[33:57 -> 34:01]** this to be is, and then here we get the output

**[34:01 -> 34:03]** of its elaboration of the input,

**[34:03 -> 34:06]** but we want to re-opt the input itself.

**[34:06 -> 34:10]** Because we expect that, yes, we gain some information here

**[34:10 -> 34:13]** from this elaboration, but we might also lose some things.

**[34:13 -> 34:17]** We want to bring it back, and then bring it over

**[34:17 -> 34:21]** into the next layer, we still have again our x.

**[34:21 -> 34:23]** So we have x, we are elaborating it,

**[34:23 -> 34:29]** So here we get the net of X, but then we also read out of the X.

**[34:29 -> 34:32]** So now, this kind of residual connection or skip

**[34:32 -> 34:36]** connection might create something

**[34:36 -> 34:38]** sure in this logic that we defined.

**[34:38 -> 34:40]** Because people always said that we want

**[34:40 -> 34:43]** that the variance of the output is the equal to the variance

**[34:43 -> 34:44]** of the input.

**[34:44 -> 34:46]** But now we have that, I mean, the output

**[34:46 -> 34:48]** has the input again.

**[34:48 -> 34:53]** So these might create some problems.

**[34:53 -> 34:56]** and we have a variance of practical growth at each block.

**[34:56 -> 35:00]** But we can, I mean, too later so can

**[35:00 -> 35:04]** hunt for us to be distracted with this particular kind of block.

**[35:04 -> 35:09]** And the princess can visualize the first revolution

**[35:09 -> 35:11]** with the micro-popherse-rich Asia.

**[35:11 -> 35:13]** And then they utilize the second revolution

**[35:13 -> 35:17]** in the zeros of these will help to obtain again

**[35:17 -> 35:21]** the scandalous strategy, which still

**[35:21 -> 35:25]** is the logic that we want to keep it right,

**[35:25 -> 35:29]** to avoid that our networks lose information

**[35:29 -> 35:33]** or have ways that you might be here in size.

**[35:34 -> 35:35]** Okay.

**[35:35 -> 35:37]** What is it that I'm talking about?

**[35:37 -> 35:42]** So, in general, proper insatization

**[35:43 -> 35:45]** is seanactive viral research.

**[35:45 -> 35:47]** So now I stopped in 2019,

**[35:47 -> 35:49]** but they are landing on the thing for a year

**[35:49 -> 35:54]** in 20-20 seconds, that the 20-20 scientists and other

**[35:54 -> 35:58]** later on, that still study what is the optimal way

**[35:58 -> 35:59]** to initialize an network.

**[35:59 -> 36:04]** And we will see that, I mean, here we are discussing

**[36:04 -> 36:07]** about the definition from scratch.

**[36:07 -> 36:11]** By someone who has the data, we want to design architecture,

**[36:11 -> 36:15]** and we want to train from scratch.

**[36:15 -> 36:21]** But we will see that for many of the more recent applications,

**[36:21 -> 36:23]** you actually don't start in French.

**[36:23 -> 36:25]** You start from a set of parameters that someone

**[36:25 -> 36:29]** will possibly, and then you go on and adjust to them.

**[36:29 -> 36:32]** So of course, it's a vision of a made relevant,

**[36:32 -> 36:35]** but it will be more a transfer language

**[36:35 -> 36:37]** from another set of parameters rather than

**[36:37 -> 36:39]** mainly starting in French.

**[36:39 -> 36:43]** And in any case, if you want to design a new part

**[36:43 -> 36:50]** network, then you will have new pieces, new residual block, new components, new layers,

**[36:50 -> 36:55]** and in that case, of course you have to start from scratch, so you have to visualize properly

**[36:55 -> 37:00]** that part of the way to your network.

**[37:00 -> 37:06]** Okay, question, doubts in the part?

**[37:06 -> 37:11]** Because here we are single, small pieces that are part of the logic of training our network.

**[37:11 -> 37:14]** We saw the components in terms of architecture,

**[37:14 -> 37:18]** pooling layer, batch of meditation layers,

**[37:18 -> 37:21]** activation function, pooling, and the layer, and so on.

**[37:21 -> 37:24]** But then, again, when you create an network,

**[37:24 -> 37:28]** you have to pay attention to how you initialize your data

**[37:28 -> 37:31]** for data processing and how you initialize the list.

**[37:32 -> 37:37]** And then, again, you know that,

**[37:37 -> 37:39]** although you try to do your best,

**[37:39 -> 37:43]** your network and your model anyway can't work either.

**[37:43 -> 37:47]** So remember, or fitting means memorizing your training

**[37:47 -> 37:50]** sample, and we want to avoid.

**[37:50 -> 37:54]** And we know that basic strategies of order

**[37:54 -> 37:59]** are thinking in introducing some regularization.

**[37:59 -> 38:01]** Regularization is a far many of sorts.

**[38:01 -> 38:04]** The far many of methods.

**[38:04 -> 38:09]** their goal again, instead of avoiding the working thing.

**[38:09 -> 38:13]** So what you would expect is that the training loss

**[38:13 -> 38:14]** goes down, right?

**[38:14 -> 38:18]** So it's what we kind of serve during the training process

**[38:18 -> 38:21]** by the day we were tri-collecting.

**[38:21 -> 38:25]** And the training loss, you want it to be nice way

**[38:25 -> 38:27]** to go down.

**[38:27 -> 38:29]** And at the same time, you also want

**[38:29 -> 38:32]** that your validation performance

**[38:34 -> 38:41]** So you don't want to see a very high accuracy on the training and a very low accuracy on the validation.

**[38:41 -> 38:51]** You can use that tracking and you can remember it on the training set, but you're not able to provide results on any set of samples.

**[38:51 -> 39:01]** So of course you expect a gap between what the model can do on training set and what the model can do on the validation.

**[39:01 -> 39:07]** that some people can expect, but you don't want this gap to be too big, and you don't

**[39:07 -> 39:13]** want your validation error to go between the accuracy of the validation to go down, which

**[39:13 -> 39:17]** would mean no more to people.

**[39:17 -> 39:24]** So we said that in general, regularization is a family of techniques, and the most basic

**[39:24 -> 39:29]** one is adding a third in the wash.

**[39:29 -> 39:33]** So, I'm the third in the law that says,

**[39:33 -> 39:37]** not only I want my model to perform well

**[39:37 -> 39:39]** on the training samples,

**[39:39 -> 39:42]** but this is a set of training samples, right?

**[39:42 -> 39:45]** This is just a simple hinge loss

**[39:45 -> 39:50]** where we are comparing the prediction for two classes

**[39:50 -> 39:53]** and saying that their difference should be larger than one.

**[39:53 -> 39:57]** If it doesn't happen, then you have a cost.

**[39:57 -> 40:02]** One is that if the prediction of the margin,

**[40:02 -> 40:04]** there is two classes,

**[40:04 -> 40:06]** it's like the one that you don't know about.

**[40:06 -> 40:09]** So this is just a simple hinge loss

**[40:09 -> 40:14]** to which you are adding some term that asks

**[40:14 -> 40:17]** your model to not have two complex weights.

**[40:17 -> 40:21]** You remember, we discussed about the ochre-brain

**[40:21 -> 40:24]** as well, exactly what's this logic here.

**[40:24 -> 40:26]** And the current overrealization,

**[40:26 -> 40:30]** can apply it is the old of course also for this method.

**[40:30 -> 40:34]** So for the model and the conclusion

**[40:34 -> 40:37]** and the kind of your law in the algorithm,

**[40:37 -> 40:41]** and what can be used law, well, it can be, for instance,

**[40:41 -> 40:44]** air through a realization or a boundary

**[40:44 -> 40:48]** or maybe a combination of the two.

**[40:48 -> 40:50]** The end through a realization, which

**[40:50 -> 40:54]** is just saying that you don't want your set of values

**[40:54 -> 40:56]** to be too big, right?

**[40:56 -> 41:00]** Because if you remember, we discussed in some lecture

**[41:00 -> 41:05]** go that you were just saying, once the W is a vector,

**[41:05 -> 41:08]** once the norm of this vector is not

**[41:08 -> 41:10]** to be big, we want to keep it small.

**[41:10 -> 41:14]** Well, here, in this network, the logic is the same.

**[41:14 -> 41:17]** It's applied on all your dot in the matrix.

**[41:17 -> 41:20]** And this logic, which is just introduced

**[41:20 -> 41:25]** the two-reverization is also called the weight decay.

**[41:25 -> 41:28]** So when you will see the favorites that they say

**[41:28 -> 41:30]** that they adopted the weight decay

**[41:30 -> 41:32]** and use that in practice, they are

**[41:32 -> 41:37]** introducing this reverization curve.

**[41:37 -> 41:39]** Why this code would decay?

**[41:39 -> 41:43]** Well, think about the, when you have these laws, right?

**[41:43 -> 41:46]** And now we are saying that the laws is composed by the,

**[41:46 -> 41:49]** some of the laws is counseling how many errors

**[41:49 -> 41:52]** the meaning of the training plus an extraction.

**[41:52 -> 41:56]** And when you go to take the reversion of the loss,

**[41:56 -> 41:58]** in practice, this third year,

**[41:58 -> 42:00]** which is just an L2 in my digestion,

**[42:00 -> 42:03]** provides you with this extra term,

**[42:03 -> 42:05]** which is linear in volume.

**[42:05 -> 42:08]** And then when you apply the rule,

**[42:08 -> 42:13]** like that says that the new W is equal to the old W,

**[42:13 -> 42:16]** minus the learning rate by the derivative of the loss,

**[42:16 -> 42:19]** which is the word and the value of this term,

**[42:19 -> 42:21]** you'll have this expression.

**[42:21 -> 42:24]** And you can just, let's say, collect the dot view

**[42:24 -> 42:28]** and then say this confusion that would be one minus

**[42:28 -> 42:31]** at some hour, but we're going to have to do it.

**[42:31 -> 42:33]** And so probably simply, you don't want the dot view,

**[42:33 -> 42:35]** but you are reducing the dot itself.

**[42:35 -> 42:37]** It's always one minus sum.

**[42:38 -> 42:40]** That's the reason why it's only the day.

**[42:40 -> 42:42]** Because the dot view is probably sitting

**[42:42 -> 42:44]** in the dot view is more than the other.

**[42:44 -> 42:48]** but I shrink, but the value of the countenance there,

**[42:48 -> 42:52]** right, or decay by a constant factor in itself.

**[42:52 -> 42:56]** So, if you have norm, then when you take the derivative,

**[42:56 -> 42:58]** it's asking the fact.

**[42:58 -> 43:01]** And so that's a reason why it's called theta.

**[43:05 -> 43:10]** Now, of course, what does it mean

**[43:10 -> 43:13]** that we walk over thinking?

**[43:13 -> 43:18]** It means that you see your validation loss

**[43:19 -> 43:22]** that at the beginning, so the training loss goes down

**[43:22 -> 43:24]** and maybe there's an attack on the control force

**[43:24 -> 43:28]** and what you hope is that this plateau is as low as possible.

**[43:28 -> 43:31]** So depending on the fact that your property

**[43:31 -> 43:34]** shows your weight in the sanitation,

**[43:34 -> 43:37]** then this will stop at a height of your lower,

**[43:37 -> 43:39]** smaller, smaller, smaller, smaller.

**[43:39 -> 43:42]** And so this is the kind of behavior expectancy

**[43:42 -> 43:45]** during training on your training later.

**[43:45 -> 43:46]** But what happens in the evaluation?

**[43:46 -> 43:49]** Well, you might still see in the beginning

**[43:49 -> 43:52]** that the validation loss goes down,

**[43:52 -> 43:54]** but then it can happen.

**[43:54 -> 43:56]** The measurement point starts going up again.

**[43:56 -> 43:59]** So here you think about having a more epoch.

**[43:59 -> 44:02]** You are training your moral moral more epochs.

**[44:02 -> 44:04]** And so this is the effect of your team.

**[44:04 -> 44:07]** And if this happens, so if you have a minimum

**[44:07 -> 44:11]** and a validation loss and you observe,

**[44:11 -> 44:16]** Well, what you should, so your reaction would be to

**[44:16 -> 44:21]** by looking at the square, to decide to stop the training.

**[44:21 -> 44:23]** Because here it's a sort of sweet spot.

**[44:23 -> 44:27]** After which your model starts to work.

**[44:27 -> 44:29]** And you don't want your algorithm, right?

**[44:29 -> 44:33]** So this strategy, which also has somehow

**[44:33 -> 44:35]** a sort of regularization effect,

**[44:35 -> 44:39]** you could avoid working, is called early something.

**[44:39 -> 44:42]** So we are stopping the training as soon as we see that

**[44:42 -> 44:44]** the violation laws start going up.

**[44:46 -> 44:50]** And indeed it's a way to invent the effective member

**[44:50 -> 44:51]** and flexing, right?

**[44:51 -> 44:54]** So of course this is somehow,

**[44:54 -> 44:57]** there's a little wire and pudding inside the list

**[44:57 -> 44:59]** across your regularization strategy.

**[45:01 -> 45:02]** So, exactly.

**[45:02 -> 45:05]** So that's in practice what you would expect to do.

**[45:05 -> 45:07]** You really are looking, you are babysitting your training

**[45:07 -> 45:11]** process, you're looking at what happens, you've got curves,

**[45:11 -> 45:14]** on the training plan, data, and on the evaluation data.

**[45:14 -> 45:18]** And when you see this, then you decide to start the process.

**[45:18 -> 45:24]** And another thing that you can do is if you're not really

**[45:24 -> 45:27]** babysitting the process step by step,

**[45:27 -> 45:30]** but you're just launching and it's going to take a copy

**[45:30 -> 45:31]** and then getting back.

**[45:31 -> 45:34]** And then you see that you're more ready to learn.

**[45:34 -> 45:37]** Then you would like to be able to get back to the position

**[45:37 -> 45:39]** where you have the information loss,

**[45:39 -> 45:42]** which means that you have to think,

**[45:43 -> 45:46]** let's say forward, since the beginning,

**[45:46 -> 45:48]** and so you have to code, you have to add some line,

**[45:48 -> 45:53]** your code that says, from time to time, save no waste.

**[45:53 -> 45:56]** Because you don't do this, then you might end up here,

**[45:56 -> 46:00]** and you don't have any more the status of your snapshot

**[46:00 -> 46:03]** and the snapshot of your model at that time.

**[46:03 -> 46:06]** So from time to time, saving, taking a snapshot

**[46:06 -> 46:09]** your model is to keep in the way.

**[46:13 -> 46:17]** Yeah, so somehow, that's this early stopping

**[46:17 -> 46:20]** that the similar behavior of the spectrum with the case.

**[46:20 -> 46:27]** So it keeps saying the weights, how it avoids

**[46:27 -> 46:29]** to make a model to conflict.

**[46:29 -> 46:32]** And so it stops before the training

**[46:32 -> 46:34]** as somehow the same logic of the way

**[46:34 -> 46:40]** to be repeated, verbalized by keeping the wind small.

**[46:40 -> 46:44]** And first say, gain the strategy that doesn't work

**[46:44 -> 46:48]** wide to think about hazard parameters.

**[46:48 -> 46:51]** And you're not practically changing anything

**[46:51 -> 46:53]** in the training pipeline.

**[46:53 -> 46:56]** It's just a matter of having the radiation set, of course,

**[46:56 -> 46:57]** really good.

**[46:57 -> 46:59]** And taking some time, time, time, time,

**[46:59 -> 47:00]** should be done.

**[47:00 -> 47:06]** saving the coffee of the model, but meters during the train process.

**[47:12 -> 47:18]** Now, we have seven years because this is the kind of behavior we would expect.

**[47:18 -> 47:29]** So naturally, you expect that your model, after a number of epochs, fits perfectly in training samples and memorize them.

**[47:29 -> 47:34]** and so it starts behaving badly on the object.

**[47:37 -> 47:40]** And remember that we saw this figure, right?

**[47:40 -> 47:42]** So the more you model becomes complex,

**[47:42 -> 47:45]** and maybe you provide with enough flexible,

**[47:45 -> 47:48]** you have a large amount of parameters,

**[47:48 -> 47:52]** the more it will be able to fit your training sample

**[47:52 -> 47:55]** in the perfect immunocirals, right?

**[47:55 -> 47:58]** So the common sense will tell us

**[47:58 -> 48:02]** that the number of parameters should be designed

**[48:02 -> 48:06]** taking into consideration how big is a data set.

**[48:06 -> 48:10]** Because otherwise, if your data set is passed away.

**[48:14 -> 48:18]** Okay, so if your data set is too small,

**[48:18 -> 48:22]** then your model will end up really memorizing very fast.

**[48:22 -> 48:28]** is too small, then your model will end up really memorizing very fast.

**[48:28 -> 48:31]** All the data, considering that the model can be huge.

**[48:31 -> 48:35]** Number, right, big number, millions or billions of particles.

**[48:35 -> 48:39]** This, which is something that we would expect,

**[48:39 -> 48:47]** has a, say, counterintuitive, in fact, behavior.

**[48:47 -> 48:52]** And when in the good world, to learn very deeply in models.

**[48:52 -> 48:55]** Because that, I mean, the experience

**[48:55 -> 48:58]** is visually what we observe is that big and bold

**[48:58 -> 49:01]** provide better results, even though we

**[49:01 -> 49:04]** have a not huge amount of data.

**[49:04 -> 49:07]** Which is tricky.

**[49:07 -> 49:10]** So this phenomenon is called, I mean,

**[49:10 -> 49:12]** what's happening behind the scenes.

**[49:12 -> 49:15]** It's a phenomenon that is called double sand.

**[49:15 -> 49:17]** that has been studied.

**[49:17 -> 49:22]** This is before the paper where we did not study.

**[49:22 -> 49:27]** And yeah, so what we observed to now is this kind of

**[49:27 -> 49:28]** being in the field.

**[49:28 -> 49:31]** So the training in the law goes down.

**[49:31 -> 49:33]** So the training error, let's say, goes down.

**[49:33 -> 49:36]** And the validation error gets towards all switch buttons

**[49:36 -> 49:39]** and then it starts under the work again.

**[49:39 -> 49:41]** And is where, was the point where we said,

**[49:41 -> 49:44]** okay, we have to stop and apply in the study.

**[49:44 -> 49:51]** But yeah, in modern nuclear network, it has been observed that going on with a train,

**[49:51 -> 50:00]** yes, we see this effect of the air or conditionary or wind-up, but then it gets to a maximum,

**[50:00 -> 50:03]** and it starts going down again.

**[50:03 -> 50:13]** So, yeah, so what's happening here is that we are going over the condition in which the model

**[50:13 -> 50:16]** model is perfectly able to feed the data.

**[50:16 -> 50:19]** We are going so much over that point

**[50:19 -> 50:23]** that in practice, the big amount of parameters that we have

**[50:23 -> 50:26]** starts to create multiple possible functions.

**[50:26 -> 50:28]** So they are all the solutions that fits well

**[50:28 -> 50:32]** the trade examples, but now starts to have enough flexibility

**[50:32 -> 50:36]** also to generalize for the validation.

**[50:36 -> 50:38]** So this indeed is just something that

**[50:38 -> 50:42]** has been observed because it's been a minute ahead.

**[50:42 -> 50:45]** per se, the evidence that the model was working well,

**[50:45 -> 50:47]** it was just a practical evidence.

**[50:47 -> 50:49]** So they tried to really understand what happens

**[50:49 -> 50:50]** at every single step.

**[50:50 -> 50:55]** And they observed this double and same kind of individual.

**[50:55 -> 50:57]** Yeah, so this point here is, again,

**[50:57 -> 51:01]** some of our other sweet spot where your model is perfectly

**[51:01 -> 51:03]** able to memorize the trade examples.

**[51:03 -> 51:04]** But now the number of parameters

**[51:04 -> 51:09]** so make that it is as if you can have many solutions.

**[51:09 -> 51:13]** all of them fit perfectly well with training panels.

**[51:13 -> 51:16]** But then, among these possible solutions,

**[51:16 -> 51:19]** many possible solutions, there may be a subset that

**[51:19 -> 51:21]** also works well for the evaluation.

**[51:21 -> 51:23]** And so on and so for a new data sample.

**[51:23 -> 51:25]** And so now your model starts learning again,

**[51:25 -> 51:27]** and it's able to provide with results

**[51:27 -> 51:29]** to generalize the test line.

**[51:29 -> 51:31]** So this has been started considering what happens

**[51:31 -> 51:36]** when you have multiple epochs, when you have multiple parameters.

**[51:36 -> 51:38]** So it's not just a matter of increasing

**[51:38 -> 51:44]** the number of famidos, you can also have a fixed number of famidos by the very long training

**[51:44 -> 51:49]** procedure, right? But still, this is kind of a behavior in the way that happens for a

**[51:49 -> 51:58]** couple of people. You need to have quite a amount of famidos, a much larger way to

**[51:58 -> 52:06]** respect your training center. So, yeah, there's of course something to keep in mind with,

**[52:06 -> 52:12]** and you might read the papers and it's a motivation by entering your big big model or not just

**[52:12 -> 52:19]** over 15, you know, maybe you might be an example but I'll add something more.

**[52:19 -> 52:20]** Okay.

**[52:20 -> 52:27]** Still we are somehow discussing about possible revitalization strategies.

**[52:27 -> 52:34]** And among them, we also have what is called dropouts.

**[52:34 -> 52:39]** So what is this dropout?

**[52:39 -> 52:45]** Well, in general, the idea is to introduce some noise into your model.

**[52:45 -> 52:52]** So if you remember, the batch summarization, we said that since it's

**[52:52 -> 52:56]** Since it's been aligning your data in batches,

**[52:56 -> 53:01]** and so every week we hope to have different batches,

**[53:01 -> 53:03]** and you are mixing the data in a new way,

**[53:03 -> 53:05]** you are introducing a little bit of noise,

**[53:05 -> 53:07]** and this helps your model to regularize.

**[53:07 -> 53:10]** So we discussed about it for batch recognition.

**[53:12 -> 53:14]** And we said that this is a very traditional thing.

**[53:14 -> 53:18]** See, immediately, we said about Tocac is a descent,

**[53:18 -> 53:21]** rather than with respect to global descent.

**[53:21 -> 53:24]** So, as we said, since the stochastic descent,

**[53:24 -> 53:25]** looking at some sort of data,

**[53:25 -> 53:28]** it's introducing the difference of the specific noise,

**[53:28 -> 53:32]** and this helps your model to evolve in a theory,

**[53:32 -> 53:34]** otherwise.

**[53:34 -> 53:36]** So the dropout strategy that is the thing

**[53:36 -> 53:38]** that we are looking at here,

**[53:38 -> 53:41]** has more or less the same high level of motion.

**[53:41 -> 53:43]** I'm introducing a little bit of noise,

**[53:43 -> 53:46]** but at this point, I'm introducing it

**[53:46 -> 53:51]** in the having neurons which are on for O.

**[53:51 -> 53:55]** So I'm deciding to turn off some of the units

**[53:55 -> 53:56]** with a certain probability.

**[53:56 -> 54:00]** It can be zero five for the unit units

**[54:00 -> 54:03]** and maybe zero one for the input node.

**[54:03 -> 54:06]** So it can change the number of the network

**[54:06 -> 54:07]** and each day in the hub.

**[54:07 -> 54:10]** But still you are somehow deciding that

**[54:10 -> 54:13]** there is a certain probability on the basis of which

**[54:13 -> 54:15]** one of the nodes is actually dead.

**[54:15 -> 54:16]** So it's not working.

**[54:16 -> 54:23]** And this, what happens is that during the training, it is like you are creating different

**[54:25 -> 54:32]** sub-matworks, you are training different sub-matworks, but then what you need to do somehow is to

**[54:32 -> 54:36]** average all the sub-matworks. So you can introduce this noise, but then you need to

**[54:36 -> 54:43]** average it out. So how does drop out work? Well, this is just simple for you to do

**[54:46 -> 54:50]** And then we just before we hear.

**[54:50 -> 54:54]** So here I am taking the,

**[54:54 -> 54:57]** it's just the linear part of my model,

**[54:57 -> 55:00]** like the W and the B, so the linear part.

**[55:00 -> 55:03]** And then maximum is just taking the maximum,

**[55:03 -> 55:05]** right, so this is just a very function.

**[55:06 -> 55:10]** And then what I do is that I consider the matrix

**[55:10 -> 55:12]** of the same shape of each one,

**[55:12 -> 55:14]** so whatever they're there.

**[55:14 -> 55:17]** I feel in this matrix we're from a million.

**[55:17 -> 55:19]** I mean, we got a million.

**[55:19 -> 55:22]** And then I checked if you're from a million,

**[55:22 -> 55:24]** that below is like who?

**[55:24 -> 55:28]** And if it happens, then it's like this.

**[55:28 -> 55:31]** Then it's like the use of the wing, which

**[55:31 -> 55:34]** I'm creating a sort of mask that decides which

**[55:34 -> 55:37]** will happen on a region of the year,

**[55:37 -> 55:39]** which way you're working on which

**[55:39 -> 55:42]** is that it should be below zero.

**[55:42 -> 55:47]** And then I apply this mask over my image line.

**[55:49 -> 55:51]** And then I do it again.

**[55:51 -> 55:53]** That is all the next layer, points of course.

**[55:53 -> 55:57]** And I'm just going to show you some of the results.

**[55:57 -> 56:01]** So this, while we're doing that,

**[56:01 -> 56:02]** as you said, we're introducing a little bit of noise.

**[56:02 -> 56:05]** It's like creating several sub-mentories.

**[56:06 -> 56:09]** And indeed what we want to do is that

**[56:09 -> 56:12]** avoid or move to perfectly memorizing data.

**[56:12 -> 56:16]** We know, we expect somehow that each neuron

**[56:16 -> 56:18]** or each separate of the language

**[56:18 -> 56:20]** focuses on some attributes,

**[56:20 -> 56:23]** back to our countenuses of our data.

**[56:23 -> 56:24]** So think about the other side,

**[56:24 -> 56:26]** the next being clean, blue,

**[56:26 -> 56:28]** but the bi animals, right?

**[56:29 -> 56:32]** And there are some neurons that focuses on

**[56:32 -> 56:34]** and on the ear, the tail,

**[56:34 -> 56:38]** the fur, or the kind of blue,

**[56:38 -> 56:46]** the eyes, but you don't want all of them to be activated jointly because what you expect

**[56:46 -> 56:55]** is that even if from a training time you see images of cats which are always vintarka.

**[56:55 -> 56:57]** So you see the low end bone.

**[56:57 -> 57:02]** At this time you might be, you might have cases where you look at only the tail or only

**[57:02 -> 57:07]** a part of the body or only some sub-part of what is here and still you want to be able

**[57:07 -> 57:09]** to recognize it, right?

**[57:09 -> 57:12]** So you don't want to enforce a co-activation

**[57:12 -> 57:15]** of all these features jointly.

**[57:15 -> 57:19]** So you might want to provide the network, the flexibility,

**[57:19 -> 57:24]** to also see a subset of them, and still be able to recognize

**[57:24 -> 57:28]** that the image it's looking at, it's better than that.

**[57:28 -> 57:30]** So that's the logic that we practice

**[57:30 -> 57:34]** when it's behind this negative profile.

**[57:34 -> 57:39]** And as I said, it's like if you are creating several sub-models,

**[57:39 -> 57:42]** several sub-mentory, then you need somehow

**[57:42 -> 57:45]** to bring them by them together.

**[57:45 -> 57:50]** Yeah, so this is just happens with a simple final mask

**[57:50 -> 57:54]** in this kind of simple model.

**[57:54 -> 57:57]** And of course, you cannot do it by hand.

**[57:57 -> 58:02]** But there are strategies to go by this dropout.

**[58:02 -> 58:08]** And moreover, the problem is that you need to linearize.

**[58:08 -> 58:11]** So yes, you like what you're doing.

**[58:11 -> 58:16]** So you like to drop some neurons into a large core core.

**[58:16 -> 58:19]** But then when you do the prediction,

**[58:19 -> 58:22]** you want to make sure that all these subnet works,

**[58:22 -> 58:24]** I mean, they work together.

**[58:24 -> 58:28]** And they recombine, so we recombine more than in terms

**[58:28 -> 58:30]** of an expedition time.

**[58:30 -> 58:34]** which means that now you have a function that does not depend only on the input,

**[58:34 -> 58:38]** the predict the output, but also depends on the random mask that you apply.

**[58:38 -> 58:42]** And in theory, at that time, you would like to average out

**[58:42 -> 58:46]** these randomness that you introduce.

**[58:46 -> 58:52]** And managing this integral, of course, you imagine that it's not trivial,

**[58:52 -> 58:56]** and we need to find a way to resolve it.

**[58:56 -> 59:02]** Here I was writing in the linted graph, but you can think also about the...

**[59:02 -> 59:08]** If you have a set of masks, I mean, you find a number of masks, it's just a summation

**[59:08 -> 59:12]** with a distribution of the noise that you have in every mask.

**[59:12 -> 59:19]** Yeah, so, but this, again, you might have an explanation of the terms, and this is intractable.

**[59:19 -> 59:23]** So how do we solve this? How do we reorganize this?

**[59:23 -> 59:26]** There are some strategies, which are called Monte Carlo

**[59:26 -> 59:31]** without that indeed try to sound using the specific number

**[59:31 -> 59:33]** of sound masks.

**[59:33 -> 59:36]** And they are very useful when you want to estimate

**[59:36 -> 59:39]** how uncertain is the network.

**[59:39 -> 59:42]** But they are very costly.

**[59:42 -> 59:45]** So we need to find, they require a lot of forward-part

**[59:45 -> 59:49]** of the model, so that's not exactly what we want to do.

**[59:49 -> 59:53]** So as usual, we hack our way through.

**[59:53 -> 59:57]** So we use an approximation that will not be perfect, but still

**[59:57 -> 60:01]** is helpful and we rely on that. So what does this mean?

**[60:01 -> 60:05]** Now let's look at what we need to solve this thing, right?

**[60:05 -> 60:09]** So we need to re-domimize and want to somehow approximate this

**[60:09 -> 60:13]** recombination of all that matter. Now let's consider a very simple case

**[60:13 -> 60:18]** where we have these two elements, z-foot, two nodes, the

**[60:18 -> 60:20]** and one more of the output.

**[60:20 -> 60:23]** And the connection is defined by the weights, W1,

**[60:23 -> 60:26]** and then N.

**[60:26 -> 60:28]** Now, at this time, what I would like to have

**[60:28 -> 60:32]** is an expected value for A, which depends on the combination

**[60:32 -> 60:34]** of W1 with X and W2.

**[60:34 -> 60:39]** So it's not a common X and Y, that's the two main groups.

**[60:39 -> 60:42]** And now, during training, we can have

**[60:42 -> 60:46]** and say that we apply this logical dropout.

**[60:46 -> 60:54]** And we say that either is the neuron axis of,

**[60:54 -> 60:57]** or the neuron y is of, or they are all together,

**[60:57 -> 60:59]** or they are all together.

**[60:59 -> 61:02]** So there are four possible cases.

**[61:02 -> 61:05]** And so what we do is that, so, my family

**[61:05 -> 61:07]** don't even just considering all four possible cases.

**[61:07 -> 61:10]** And I'll give you just a way to get them all together.

**[61:10 -> 61:14]** So either they are all, I mean, both on,

**[61:14 -> 61:19]** or one of them is off a young dog or the other round,

**[61:19 -> 61:21]** or the whole dog.

**[61:21 -> 61:23]** Another one you take is some,

**[61:23 -> 61:25]** well you get one half,

**[61:25 -> 61:29]** multiplied by W1x plus W.

**[61:29 -> 61:34]** So what we were doing here is that we were saying

**[61:34 -> 61:37]** each node or each connection is off

**[61:37 -> 61:38]** with a probability of 0.5,

**[61:38 -> 61:42]** but it can be either on or off with the local body.

**[61:42 -> 61:46]** So the probability that you are applying to dropout

**[61:46 -> 61:52]** is a simple number, four zero five at one hour.

**[61:52 -> 61:56]** And now it turns out that if you do the calculation properly,

**[61:56 -> 62:00]** in practice it is a big one.

**[62:00 -> 62:04]** You are using the network per se, with no dropout.

**[62:04 -> 62:09]** And then you put a zero five in front of the other.

**[62:09 -> 62:13]** So this provides us with a rule of thumb.

**[62:13 -> 62:16]** It's not perfect, because of course,

**[62:16 -> 62:18]** this hold will be very simple,

**[62:18 -> 62:22]** it might not hold perfectly in other fingers.

**[62:22 -> 62:25]** But still, we can adopt this kind of approximation

**[62:25 -> 62:29]** and say, if I decided to use as hyperparameter

**[62:29 -> 62:31]** for my draw-out, so here, the only parameter

**[62:31 -> 62:34]** and the only hyperparameter you have to choose

**[62:34 -> 62:38]** is the probability that you set your each node

**[62:38 -> 62:43]** that's on or off and we chose to be 0 to 5.

**[62:43 -> 62:46]** Then what you do when you want to make the bridge

**[62:46 -> 62:49]** is that you keep the letter as all the neurons were on.

**[62:49 -> 62:51]** You just do the bridge in that way.

**[62:51 -> 62:56]** And then you put depth probability in front of the bridge.

**[62:56 -> 62:59]** As simple as this.

**[62:59 -> 63:02]** You just multiply it by little pout probability

**[63:02 -> 63:05]** that you chose to make it.

**[63:05 -> 63:10]** So now, if I ask you, considering what I said,

**[63:10 -> 63:15]** if I ask you, does the dropout later,

**[63:15 -> 63:19]** because again, the dropout, the logit, the dropout logic,

**[63:19 -> 63:21]** right, that's quite like this,

**[63:21 -> 63:25]** does it need a hyperparameter?

**[63:25 -> 63:26]** What would be your answer?

**[63:30 -> 63:32]** So these are the kind of questions

**[63:32 -> 63:33]** that you don't expect to be done,

**[63:33 -> 63:34]** but they have to proceed, right?

**[63:34 -> 63:40]** So we said dropout to use it.

**[63:40 -> 63:42]** You need to set by hand something.

**[63:42 -> 63:44]** What is the parameter you have to set by hand?

**[63:48 -> 63:49]** The probability, OK?

**[63:49 -> 63:52]** So you decide what is the probability

**[63:52 -> 63:56]** that each of your element is all or not all, OK?

**[63:56 -> 64:00]** So dropout has a hyperbaric here,

**[64:00 -> 64:03]** which is the probability to set each of these elements

**[64:03 -> 64:11]** And that probability is exactly the thing that you use to make the prediction and to avoid

**[64:11 -> 64:17]** this difficulty of averaging out all the sub-ninth words that you created.

**[64:17 -> 64:29]** So, in practice, you just do the prediction as all the neurons were active and then you put the probability in front.

**[64:29 -> 64:34]** So that's the strategy I used.

**[64:34 -> 64:37]** And so if you're in training, you did something

**[64:37 -> 64:40]** that we did before, or you were ready for it before,

**[64:40 -> 64:42]** and then at that time you take the same thing

**[64:42 -> 64:46]** and you apply it on the opposite for each player.

**[64:46 -> 64:48]** So you apply the scaling at that time.

**[64:48 -> 64:50]** Not in the middle.

**[64:50 -> 64:57]** But as usual, you might afford to spend time training

**[64:57 -> 65:04]** because the training is generally an offline procedure, right?

**[65:04 -> 65:06]** It's something that you do behind the scenes.

**[65:06 -> 65:09]** But then, I mean, when you sell your product,

**[65:09 -> 65:12]** you sell it to someone that wants to use it as a employment plan.

**[65:12 -> 65:16]** So really, for someone taking a decision, I mean,

**[65:16 -> 65:18]** this decision has to be fast.

**[65:18 -> 65:22]** So you don't want to make the deployment time,

**[65:22 -> 65:26]** the test time, more heavy, more calculation.

**[65:26 -> 65:32]** So one thing that we can do is avoid this, right?

**[65:32 -> 65:36]** And again, there's another sort of approximation

**[65:36 -> 65:39]** rather than doing this, what we do is

**[65:39 -> 65:42]** that we divide during train.

**[65:42 -> 65:45]** So rather move the blind at the one time,

**[65:45 -> 65:51]** we add a division here in the fraction during train.

**[65:51 -> 65:54]** A approximation over the approximation, right?

**[65:54 -> 65:55]** By the word, right?

**[65:55 -> 66:00]** So this allurems who have the test time unchanged,

**[66:00 -> 66:03]** you don't have to be afraid of, I mean,

**[66:03 -> 66:07]** thinking about the probability that we use during training.

**[66:07 -> 66:10]** It's just a sort of strategy that helps the model

**[66:10 -> 66:11]** to roll around.

**[66:11 -> 66:14]** So it has a revolution effect.

**[66:14 -> 66:18]** It's a illusion of noise, and I keep it back.

**[66:18 -> 66:21]** So it's sort of inverted apart because we're just applying

**[66:21 -> 66:25]** the division directly at training.

**[66:25 -> 66:30]** Okay, so now what are we doing here is that we are dropping,

**[66:32 -> 66:34]** and we said some calculations,

**[66:34 -> 66:36]** avoiding some calculations.

**[66:38 -> 66:41]** The truth is that when you use dropouts,

**[66:41 -> 66:44]** since you are creating these several sub-network,

**[66:44 -> 66:48]** the training procedure might become a bit slower,

**[66:48 -> 66:50]** but you have this quality effect in terms of the

**[66:50 -> 66:53]** generation on problems of the model,

**[66:53 -> 67:07]** and this extra calculation might ask for a little bit of time in terms of training, running

**[67:07 -> 67:08]** the training.

**[67:08 -> 67:13]** And, Maruba, where would you apply Robow?

**[67:13 -> 67:22]** Well, we want Robowite where the cost in terms of number of parameters is higher, right?

**[67:22 -> 67:27]** Because as we said, yes, in terms of time, the calculation,

**[67:27 -> 67:29]** it might be a little bit more costly,

**[67:29 -> 67:31]** but what's happening in certain languages

**[67:31 -> 67:34]** is that we are dropping some of the parameters in practice.

**[67:34 -> 67:37]** And so we want to use it on the part of the network,

**[67:37 -> 67:40]** where the number of parameters are higher, is out there.

**[67:40 -> 67:43]** And we know that, I mean, you remember,

**[67:43 -> 67:47]** all the logic of using the convolutional layer

**[67:47 -> 67:51]** was exactly going in the direction of

**[67:51 -> 67:54]** reducing the amount of values of one.

**[67:54 -> 67:57]** So rather than upgrading all the input at once,

**[67:57 -> 68:00]** with a very big W matrix, we use the conclusion

**[68:00 -> 68:03]** that considers the small kernels,

**[68:03 -> 68:05]** the more of the image,

**[68:05 -> 68:06]** all its weight sharing,

**[68:06 -> 68:09]** because it's used in multiple places of the image,

**[68:09 -> 68:11]** but the dimension of the computer is smaller.

**[68:11 -> 68:12]** So all the logic of the conclusion,

**[68:12 -> 68:15]** the mathematical and the conclusion layer,

**[68:15 -> 68:17]** was exactly designed to reduce numbers of values.

**[68:17 -> 68:20]** And indeed, when you go and consider

**[68:20 -> 68:21]** in different kind of architecture,

**[68:21 -> 68:24]** and you come to the palmita that are there,

**[68:24 -> 68:27]** you see that the number of palmita is very small

**[68:27 -> 68:28]** in the convolutional layer,

**[68:28 -> 68:33]** with respect to what you have in the ending part of network,

**[68:33 -> 68:36]** where you still have standard neural network

**[68:36 -> 68:39]** and not convolutional layers, but just fully connected layer.

**[68:39 -> 68:42]** There, the number of palmita is very big,

**[68:42 -> 68:46]** and there is the place where you would use problem.

**[68:46 -> 68:50]** So it's more rare to see it in the convolutional layer.

**[68:50 -> 68:55]** It's much more frequent to see it on the polygranate

**[68:55 -> 68:58]** of the word number.

**[68:58 -> 69:00]** And then you will see that nowadays,

**[69:00 -> 69:04]** I mean, most modern networks tend to not even use

**[69:04 -> 69:07]** to apply more because they have other strategies

**[69:07 -> 69:11]** through about your fitting and individual utilization.

**[69:11 -> 69:14]** We discuss about global average pooling.

**[69:14 -> 69:17]** So we discussed about pooling.

**[69:17 -> 69:20]** We said, OK, we can also buy global average pooling

**[69:20 -> 69:22]** from the old down market.

**[69:22 -> 69:28]** I don't know how to put our module, right?

**[69:28 -> 69:33]** So that already allows to reduce the dimensionality.

**[69:33 -> 69:35]** And indeed, this is the kind of strategy

**[69:35 -> 69:39]** that is used by natural by Google and most recent kind

**[69:39 -> 69:40]** of architecture.

**[69:40 -> 69:44]** But the origin dropouts, it happens

**[69:44 -> 69:47]** that you read it in a paper and still can

**[69:47 -> 69:49]** do without the architecture, then you

**[69:49 -> 69:53]** know what is mean and how it works.

**[69:53 -> 69:54]** OK.

**[69:54 -> 70:00]** Now, we already mentioned residual connections, right?

**[70:00 -> 70:05]** And we discussed about the weight in the expression.

**[70:05 -> 70:10]** And in this, we are also listing the residual connection

**[70:10 -> 70:18]** here in the set of strategies that one wants to use for

**[70:18 -> 70:21]** revitalization.

**[70:21 -> 70:24]** So what are these residual connection doing, as we said,

**[70:24 -> 70:28]** is reporting the input of the module also at the output

**[70:28 -> 70:30]** level.

**[70:30 -> 70:35]** And what is the effect of this?

**[70:35 -> 70:38]** It also helps geolization.

**[70:38 -> 70:39]** Why?

**[70:39 -> 70:45]** Because in practice, it is smoothing out the law of landscape.

**[70:45 -> 70:49]** Because, I mean, you are not forget about the X,

**[70:49 -> 70:53]** and using only the elaboration of the X, the F of X.

**[70:53 -> 70:56]** But you're keeping back what you had in the community.

**[70:56 -> 71:02]** So you are letting your, say, model to better represent

**[71:02 -> 71:06]** the space of possibilities that the need for like this.

**[71:06 -> 71:12]** And also to try to describe the error that you would see

**[71:12 -> 71:16]** would define a loss landscape that would be much bigger.

**[71:16 -> 71:17]** OK, we'll skip the next slide.

**[71:17 -> 71:19]** This is a kind of loss landscape we

**[71:19 -> 71:22]** said we would look at in the case of the joke.

**[71:22 -> 71:25]** Don't use the connection.

**[71:25 -> 71:28]** OK, so in this sense, since now you

**[71:28 -> 71:31]** will have this smoother loss function,

**[71:31 -> 71:34]** then your model behaves nicely.

**[71:34 -> 71:37]** and it also helps in generalizing overall.

**[71:40 -> 71:43]** Yeah, of course you can have fours

**[71:43 -> 71:45]** then on residual connection, right?

**[71:45 -> 71:48]** So more can be done even complex.

**[71:48 -> 71:50]** And indeed, if you look at like this,

**[71:50 -> 71:52]** then this brings you back again,

**[71:52 -> 71:53]** the logic of drop-up.

**[71:53 -> 71:57]** It's like creating some sound networks

**[71:57 -> 71:59]** that were parts of the network,

**[71:59 -> 72:01]** speaks to each other.

**[72:01 -> 72:03]** And this can be helpful as the logic

**[72:03 -> 72:05]** of the dropout that we said.

**[72:07 -> 72:10]** So here is like, yeah, combining multiple

**[72:10 -> 72:12]** deep parts from shallows of northward,

**[72:12 -> 72:14]** and these have to be obtained.

**[72:14 -> 72:16]** These kind of laws.

**[72:19 -> 72:23]** So again, this is just a light to remind us

**[72:23 -> 72:25]** that what is realization doing?

**[72:25 -> 72:28]** Well, we saw with dropout this logic

**[72:28 -> 72:30]** of introducing some noise,

**[72:30 -> 72:34]** and the need of a normalizing doubt or the averaging

**[72:34 -> 72:36]** is this randomness out.

**[72:36 -> 72:38]** But in practice, as I've already mentioned,

**[72:38 -> 72:40]** the same logic of batch normalization

**[72:40 -> 72:41]** was going into the batch.

**[72:41 -> 72:44]** So we elaborate with batches.

**[72:44 -> 72:47]** And since this batch has changes and every sample, then,

**[72:47 -> 72:50]** I say, we look at every sample together

**[72:50 -> 72:55]** with the other subset of data, then this introduces some noise.

**[72:55 -> 72:58]** And this helps to generalize.

**[73:00 -> 73:02]** What else?

**[73:02 -> 73:07]** Okay, so we mentioned strategies to change the answer,

**[73:09 -> 73:14]** what happens inside of the network that can help you visualize.

**[73:14 -> 73:18]** We discussed about strategy that you can apply during training,

**[73:18 -> 73:20]** like early stopping.

**[73:20 -> 73:24]** And you're going to do something at the training time

**[73:24 -> 73:27]** with respect to the data.

**[73:27 -> 73:34]** So, one regularization approach is double notation.

**[73:34 -> 73:38]** It actually seems this one.

**[73:38 -> 73:40]** So what are we doing inside the network?

**[73:40 -> 73:42]** Well, we have our data set.

**[73:42 -> 73:45]** We look at our images, like in a supervised class,

**[73:45 -> 73:47]** so we have an image, which is legal.

**[73:47 -> 73:50]** Then the data passes through the network.

**[73:50 -> 73:52]** The network produces something as an output

**[73:52 -> 73:54]** and is compared with a round.

**[73:54 -> 73:58]** That's the basic logic of what we are doing.

**[73:58 -> 74:05]** So we might decide to introduce some extra variability

**[74:05 -> 74:06]** in the data.

**[74:06 -> 74:09]** Now, of course, what we're supposed to have

**[74:09 -> 74:14]** is a large amount of samples that already cover

**[74:14 -> 74:19]** the variability of the glass cap.

**[74:19 -> 74:22]** But in case we have a limited amount of samples,

**[74:22 -> 74:25]** or even if we have a big amount of samples,

**[74:25 -> 74:30]** we can still get some gain in terms of geolocation

**[74:30 -> 74:34]** by introducing by hand some viability,

**[74:34 -> 74:37]** extra viability in the data.

**[74:37 -> 74:39]** So we can transform the image,

**[74:39 -> 74:43]** which provides us with extra synthetic samples,

**[74:43 -> 74:47]** which are artificial samples that we are creating by hand

**[74:47 -> 74:49]** and providing them to them.

**[74:49 -> 74:55]** So this increases the amount of sample, then the same can't increase the viability, so

**[74:55 -> 74:58]** we are practically augmenting the training data.

**[74:58 -> 75:02]** Now note, this is something you do for the training samples.

**[75:02 -> 75:08]** So to increase the viability during the training of the process, but your foundation stays

**[75:08 -> 75:09]** the same.

**[75:09 -> 75:11]** Isolization is active to keep it the same.

**[75:11 -> 75:16]** So you don't extend the evaluation process.

**[75:16 -> 75:20]** So, well, if there can be lots of data

**[75:20 -> 75:26]** of relation strategy, so you can take just the mirroring

**[75:26 -> 75:29]** maybe, but the same version, translation,

**[75:29 -> 75:31]** just nation rotation.

**[75:31 -> 75:33]** You can change the brightness, the contrast,

**[75:33 -> 75:37]** you can add some noise, you can add a color shift,

**[75:37 -> 75:40]** and you can just use your creativity

**[75:40 -> 75:43]** to introduce this by a little bit.

**[75:43 -> 75:48]** Of course, they have to be meaningful by a meeting.

**[75:50 -> 75:55]** When can happen that the violin that you introduced

**[75:55 -> 75:59]** is not an important one?

**[75:59 -> 76:04]** Well, think about the case in which you change the data,

**[76:04 -> 76:07]** but this changing of the data causes a change

**[76:07 -> 76:11]** in the semantic of the class

**[76:11 -> 76:15]** So the label of the results, like in the case of digits,

**[76:15 -> 76:18]** if you take your six and you just rotate them with it,

**[76:18 -> 76:22]** then you're really practically introducing

**[76:22 -> 76:29]** an issue because then you end up mixing the classes.

**[76:29 -> 76:33]** Because this object, you keep it as a label six.

**[76:33 -> 76:38]** But then if you divide it to your training model,

**[76:38 -> 76:41]** and you drain them all with this, and you call it a six,

**[76:41 -> 76:44]** of course, it will create issue in the ability

**[76:44 -> 76:46]** of classification of the one.

**[76:46 -> 76:48]** So these, of course, you have to make sure

**[76:48 -> 76:52]** that the kind of documentation that you applied

**[76:52 -> 76:57]** does not create problem or change the semantics of the data.

**[77:02 -> 77:04]** Of course, there are some other cases

**[77:04 -> 77:08]** like elevation 180 degree elevation,

**[77:08 -> 77:11]** plus sometimes it's not very difficult to look,

**[77:11 -> 77:16]** but it's a good for instance, if you want to segment images,

**[77:16 -> 77:19]** like higher-level images, so it's in the south light,

**[77:19 -> 77:23]** okay? And for that sense, I mean, the orientation

**[77:23 -> 77:27]** or the clipping doesn't change anything in the semantics,

**[77:27 -> 77:29]** right? So in that case, something you can do.

**[77:29 -> 77:33]** So again, it's not just a matter of al-humanizing

**[77:33 -> 77:38]** process, there's always some grain of soil that you as one

**[77:38 -> 77:40]** on the first of this leading the experiment

**[77:40 -> 77:42]** is defining the thoughts and problems

**[77:42 -> 77:45]** where the body learner should be doomed.

**[77:45 -> 77:48]** And of course, even before getting

**[77:48 -> 77:50]** to be able to learn in the double scientist,

**[77:50 -> 77:54]** you know what you have to do as a preliminary layer of the fact

**[77:54 -> 77:56]** that that data has to be fed to me,

**[77:56 -> 78:00]** how are you going to model or any machine anymore.

**[78:00 -> 78:09]** And you have to pay attention because if you apply this transformation on the data,

**[78:09 -> 78:18]** then differently from the case of just, I mean, when you provide an overall label to the image,

**[78:18 -> 78:22]** depending on the task, you might also need to change the label.

**[78:22 -> 78:29]** So if you're goal, instead of segmenting the image and recognizing different buildings

**[78:29 -> 78:33]** different areas in this region, right?

**[78:33 -> 78:38]** So every color represents a kind of ground, let's say,

**[78:38 -> 78:44]** or a type of buildings or cultural area and so on,

**[78:44 -> 78:45]** by those streets.

**[78:45 -> 78:51]** Then if you change the data, you'll have to change the data.

**[78:51 -> 78:52]** And this is not a change in semantics.

**[78:52 -> 78:54]** So the semantics is still there.

**[78:54 -> 78:56]** But it is something that you have to pay attention to.

**[78:56 -> 78:59]** Because otherwise, you start training your model

**[78:59 -> 79:04]** with changing the data, but they will remain

**[79:04 -> 79:07]** unaligned with respect to the data and your model

**[79:07 -> 79:09]** does not understand it.

**[79:09 -> 79:11]** So these are the difficult things that happen.

**[79:11 -> 79:14]** I can assure you, you don't pay attention

**[79:14 -> 79:15]** to this kind of thing happens.

**[79:15 -> 79:17]** Then nothing works and you start thinking,

**[79:17 -> 79:22]** oh my god, there's something going wrong there.

**[79:22 -> 79:23]** Nothing related to that.

**[79:23 -> 79:26]** Neither the learning way or the waiting situation.

**[79:26 -> 79:28]** No reactational context of that.

**[79:28 -> 79:31]** You didn't properly manage your training samples.

**[79:34 -> 79:35]** Okay, what else you can do?

**[79:35 -> 79:39]** Well, you can also crop your image.

**[79:39 -> 79:43]** You can take several one squared region,

**[79:43 -> 79:46]** maybe to the four angle and the central one.

**[79:46 -> 79:49]** And so you can also use skills data.

**[79:50 -> 79:54]** And this logic you want to apply the test on.

**[79:54 -> 79:59]** And here, so if you somehow extract more crops

**[79:59 -> 80:02]** from your image or training time,

**[80:02 -> 80:04]** at test time you can do the same,

**[80:04 -> 80:05]** so the same start is,

**[80:05 -> 80:07]** if you take the four crops at the corner

**[80:07 -> 80:11]** and the central one, then you can do the same test time.

**[80:11 -> 80:14]** And in that case, then for every image,

**[80:14 -> 80:16]** then you have to, again, take a final decision

**[80:16 -> 80:18]** that recombines the region,

**[80:18 -> 80:20]** that you have all the pieces

**[80:20 -> 80:22]** that you have stuck there from the region.

**[80:24 -> 80:27]** but it's a typical kind of challenge that you do,

**[80:27 -> 80:30]** taking multiple patches or taking multiple scales,

**[80:30 -> 80:32]** so just rescaling the image

**[80:32 -> 80:35]** when you're making a prediction on different scales.

**[80:35 -> 80:39]** And then, of course, if you apply it to test time,

**[80:39 -> 80:42]** then you have to re-average back the predictions somehow

**[80:42 -> 80:44]** to provide a single lingual envelope.

**[80:48 -> 80:52]** Well, again, I mean, it's just your creativity

**[80:52 -> 80:53]** is believing here, right?

**[80:53 -> 80:57]** So things that, of course, you can apply, you can introduce

**[80:57 -> 81:00]** on color, G-cell, with a randomization,

**[81:00 -> 81:03]** or change in contrast, change in the brightness.

**[81:03 -> 81:04]** You can do something more complicated.

**[81:04 -> 81:07]** You can apply DCA, and RGB, and then you introduce

**[81:07 -> 81:10]** and do an color offset.

**[81:10 -> 81:13]** Again, there are many things you can do, translational,

**[81:13 -> 81:18]** patient stretching, or blemptus, or shunt, and more crazy.

**[81:18 -> 81:21]** Or, of course, you have to pay attention

**[81:21 -> 81:26]** what you're doing, but it's something that you do

**[81:26 -> 81:28]** consciously, you know what you're doing,

**[81:28 -> 81:31]** and you also have to know how to manage the best time.

**[81:35 -> 81:39]** Okay, so this was just a presentation,

**[81:39 -> 81:41]** that they said the least of strategy

**[81:41 -> 81:43]** in terms of the very decision I made,

**[81:43 -> 81:46]** so just some why they found them,

**[81:46 -> 81:48]** and in general, all of them are connected with either

**[81:48 -> 81:52]** we are all introducing them on the noise.

**[81:52 -> 81:56]** We mentioned dropout, but we can also have drop for length.

**[81:56 -> 82:00]** So rather than finding a probability to the node

**[82:00 -> 82:02]** if it's on or off, we can assign a probability

**[82:02 -> 82:06]** to the connection if it is on or off.

**[82:06 -> 82:08]** We can have max pooling, again,

**[82:08 -> 82:11]** drilling up some noise in this structure, max pool

**[82:11 -> 82:12]** in the difference.

**[82:12 -> 82:14]** So not just the fix that the dimensionality

**[82:14 -> 82:16]** will window that you look at, but it can change it.

**[82:16 -> 82:19]** and this creates this kind of effect.

**[82:19 -> 82:22]** You can have a stochastic depth,

**[82:22 -> 82:24]** so you can reduce skin connection

**[82:24 -> 82:27]** that changes really the depth of the network,

**[82:27 -> 82:29]** again introducing noise.

**[82:31 -> 82:34]** And you can also cut out some part of the image.

**[82:34 -> 82:38]** It's like introducing by hand some occlusion, right?

**[82:38 -> 82:41]** So it's like the kind of dropout

**[82:41 -> 82:44]** where you operate directly on the neurons

**[82:44 -> 82:45]** that focus on patterns.

**[82:45 -> 82:50]** you can put already on the data. So you can decide to put them in a square in the image

**[82:50 -> 82:57]** that covers a part of the image. You can just break and just run down and swam to the card

**[82:57 -> 83:01]** who are interested in this panelists. And there is one super crazy thing that you can

**[83:01 -> 83:09]** do that we take the break, I promise. So there is something crazy that you can do that in

**[83:09 -> 83:13]** And here it seems to go against what I said.

**[83:13 -> 83:19]** So avoiding that when you apply some data of rotation,

**[83:19 -> 83:24]** the semantics of your content of the image then get lost.

**[83:24 -> 83:29]** So here, this mix of strategy is saying

**[83:29 -> 83:35]** that I can create extra data by mixing the images

**[83:35 -> 83:38]** of different levels, or in front of the mix.

**[83:38 -> 83:45]** I'm mixing up these which is more dog than cat somehow.

**[83:45 -> 83:50]** 60% dog and 40% cat and I hope I don't know.

**[83:50 -> 83:54]** So why it's not wrong to do that?

**[83:54 -> 83:57]** Again, it's because I'm taking this kind of choice under control.

**[83:57 -> 84:01]** I know what I'm doing and what I'm doing is that I'm creating extra data

**[84:01 -> 84:06]** that now has a specific kind of label.

**[84:06 -> 84:13]** So I want to force my model to be able to not say only 100% cut or 100% dog.

**[84:13 -> 84:20]** I want my model to have the flexibility to also look at cases where I have percentage

**[84:20 -> 84:25]** combination and then we'll ask my model to really predict this.

**[84:26 -> 84:33]** So I'm keeping this under control so it's not creating a problem anymore because

**[84:33 -> 84:36]** because now I'm supervising the process.

**[84:36 -> 84:38]** I say yes, I'm mixing the data,

**[84:38 -> 84:41]** and I want that my network predicts exactly the mix

**[84:41 -> 84:43]** that I created.

**[84:43 -> 84:45]** So I created the mix like this,

**[84:45 -> 84:47]** and now I want the prediction.

**[84:47 -> 84:50]** So you know, I say that we have 10 classes, right?

**[84:50 -> 84:53]** So these 10 classes usually you have 10 days

**[84:53 -> 84:55]** as output and output elements.

**[84:55 -> 84:58]** And you expect to have 100, this is a one,

**[84:58 -> 85:01]** value one for the taskar,

**[85:01 -> 85:04]** I know the red zero or plus,

**[85:04 -> 85:06]** no prediction of one for a baby one for class dog.

**[85:06 -> 85:08]** I know the other zero, right?

**[85:08 -> 85:11]** In this case, I'm asking to have two pigs.

**[85:11 -> 85:14]** Okay, so I'll add zero dot six for the class dog,

**[85:14 -> 85:15]** zero four for the class to come.

**[85:15 -> 85:17]** And I'm supervising them.

**[85:17 -> 85:20]** So I'm looking at the loss that really has to respect.

**[85:20 -> 85:22]** So I'm calculating the loss,

**[85:22 -> 85:25]** minimize this kind of,

**[85:25 -> 85:27]** so the error on this kind of data.

**[85:27 -> 85:31]** And of course, what I avoid is to be in this situation.

**[85:31 -> 85:34]** So I don't want to have 50-50.

**[85:34 -> 85:36]** I want to have always a little bit more than one clock

**[85:36 -> 85:37]** and the other.

**[85:37 -> 85:38]** So still there is a sort of disagreement

**[85:38 -> 85:40]** that we will be able to have.

**[85:43 -> 85:46]** OK, so this is just a mix of logic.

**[85:46 -> 85:51]** And somehow this ends the part on regularization.

**[85:51 -> 85:53]** So we discussed about, again, weight

**[85:53 -> 85:57]** in transition, data processing, and regularization.

**[85:57 -> 85:58]** So now we stop here.

**[85:58 -> 86:14]** take 50 minutes break and then we will have the one time set up, meaning that we have

**[86:14 -> 86:17]** and we have a final architecture.

**[86:17 -> 86:22]** And now we look at the component of our architecture.

**[86:26 -> 86:29]** Look at the activation function.

**[86:29 -> 86:32]** We look at how to put from data,

**[86:32 -> 86:37]** look at the weight classification and the representation.

**[86:37 -> 86:41]** So everything that we've been discussing

**[86:41 -> 86:46]** But if now, it's where I go here the one time to talk.

**[86:46 -> 86:51]** But then, the other two take big steps

**[86:51 -> 86:54]** in this learning global network, the mission

**[86:54 -> 86:59]** of the training about the big network, the big model,

**[86:59 -> 87:05]** which is, first of all, focusing on training the nummies.

**[87:05 -> 87:08]** And then, once the training is done,

**[87:08 -> 87:12]** We can think about the things after the training.

**[87:12 -> 87:16]** Now we focus on the training terms,

**[87:16 -> 87:17]** so this second step.

**[87:19 -> 87:21]** And my first round is on.

**[87:21 -> 87:22]** The top of it.

**[87:22 -> 87:27]** Okay, so training dynamics means that

**[87:27 -> 87:29]** we need to babysit the learning problems.

**[87:29 -> 87:34]** So we said architecture, now we provide the data,

**[87:34 -> 87:39]** And we have to look at what happens at our loss function.

**[87:39 -> 87:41]** It could go down and how it goes down.

**[87:41 -> 87:44]** It could go down.

**[87:44 -> 87:48]** In general, we said that what the procedure, therefore,

**[87:48 -> 87:50]** we need to write in the sample slides.

**[87:50 -> 87:51]** And we have to do the loss.

**[87:51 -> 87:53]** And then we have to do the derivatives

**[87:53 -> 87:59]** and search for a reasonable minimum of these loss lines.

**[87:59 -> 88:06]** And one important parameter in the garden central is the learned way.

**[88:06 -> 88:13]** I think this parameter, the hyperbar root that we have in the problem we do,

**[88:13 -> 88:17]** we do it in the loss, and that we have to set.

**[88:17 -> 88:20]** So now the question is how do we set this data?

**[88:20 -> 88:22]** Well, of course, we know that there are different

**[88:22 -> 88:23]** information procedures.

**[88:23 -> 88:28]** we have the learning rate that I provide in the children.

**[88:30 -> 88:33]** And we can, depending on the learning rate,

**[88:33 -> 88:36]** we have often can see different kinds of factors.

**[88:38 -> 88:43]** So if we have a very small learning rate,

**[88:44 -> 88:47]** then the loss goes down,

**[88:47 -> 88:49]** but goes down very soon.

**[88:49 -> 88:53]** So we're making very cool steps for the middle.

**[88:53 -> 88:58]** And these invited a lot to clean the spot where it's going to be.

**[88:58 -> 89:01]** If we have a very high learning rate,

**[89:01 -> 89:04]** then we see that when the logs look down together

**[89:04 -> 89:08]** at the beginning, but then we start to go through them.

**[89:08 -> 89:11]** And again, it goes to a very high level.

**[89:11 -> 89:13]** So now, this kind of behavior is something

**[89:13 -> 89:15]** that we already saw when discussing about weight

**[89:15 -> 89:16]** in celebration.

**[89:16 -> 89:20]** So you can imagine that the learning rate of the storm

**[89:20 -> 89:21]** connects with weight in celebration

**[89:21 -> 89:25]** the way the decision, where you're starting, right?

**[89:25 -> 89:27]** And then the government's sense goes down,

**[89:27 -> 89:29]** but depending on where you started,

**[89:29 -> 89:30]** it'll not be further back.

**[89:30 -> 89:33]** And also the way that you choose your learning weight.

**[89:33 -> 89:35]** How do you learn the fact?

**[89:35 -> 89:38]** Now, super high learning weight can create issue,

**[89:38 -> 89:42]** or you can have a loss of the bird or a strange behavior

**[89:42 -> 89:45]** because maybe every one of you is too big

**[89:45 -> 89:49]** to provide the model the ability to really learn something.

**[89:49 -> 89:56]** But in general, what is the correct learning rate?

**[89:56 -> 89:58]** Well, you would like something of this kind,

**[89:58 -> 90:02]** so the red curve, that goes down continuously

**[90:02 -> 90:05]** and possibly gets to very, very little.

**[90:05 -> 90:08]** So you would like to see this kind of being of the loss

**[90:08 -> 90:12]** and the learning rate of course, influence this rate.

**[90:12 -> 90:14]** But now, what is the learning rate of the better one?

**[90:14 -> 90:16]** Do you, of course, in the red one,

**[90:16 -> 90:23]** one or how to find it, for the more or in a period. So one thing that we can do is rather

**[90:23 -> 90:31]** fix the loadability is to change it during the training process. So we can set it at

**[90:31 -> 90:36]** a certain day view and then progressively decrease it because you remember that when

**[90:36 -> 90:42]** we start, we might be far away from the minimums. So maybe at the beginning you want to take

**[90:42 -> 90:47]** But then when we start getting good, the minimum work takes more status.

**[90:47 -> 90:52]** Just these laws get into the, the oil bouncing here and there, right?

**[90:52 -> 90:57]** And then there's a border of our loss landscape and we'll be able to go.

**[90:59 -> 91:03]** So this is the effect of the actual column, sir.

**[91:03 -> 91:09]** When we have growth is changing at the level.

**[91:09 -> 91:16]** So maybe we train our world, still at the point, we are a third world language, and then we decide to decrease.

**[91:16 -> 91:27]** And the fact that we see is that the loss goes down, start going down quickly, and then again, again, together.

**[91:27 -> 91:35]** And so we can do it multiple times, right? So we can set a strategy, just a step start, for instance.

**[91:35 -> 91:40]** Let's say that we have learning weight and now zeros one at the beginning,

**[91:40 -> 91:47]** the upper third, the upper, and then it becomes, you know, a, a, a, a, a zeros, zeros, one,

**[91:47 -> 91:57]** and that zeros, one, zeros, zeros, after the, after the third, one, and so you want a zeros.

**[91:57 -> 92:01]** So this is just a set-wise degree of the learning rate.

**[92:01 -> 92:04]** on the basis of a strategy which is side from the beginning.

**[92:04 -> 92:08]** So you take the learning place and after about 36 and 90,

**[92:08 -> 92:11]** you look, you decide to do it by,

**[92:11 -> 92:13]** you know, a, moving,

**[92:13 -> 92:14]** or you do it by 10,

**[92:14 -> 92:16]** and then you can write it.

**[92:16 -> 92:19]** Okay, so this is one thing that you really know.

**[92:19 -> 92:23]** Or you can introduce a function that says,

**[92:23 -> 92:27]** I mean, I want to start from the same value of zero,

**[92:27 -> 92:30]** and then I design a function that goes down,

**[92:30 -> 92:38]** time. The T is a total amount of time set that I considered and instead of in that

**[92:38 -> 92:45]** scene is that the label is a new term for how the time is going on. This is a

**[92:45 -> 92:50]** maximum number of time set. And then you have a function that tells you how the

**[92:50 -> 92:55]** information progressively changes time. And so when you use it and the prediction

**[92:55 -> 92:59]** you see that the U-laws, rather than having the steps,

**[92:59 -> 93:02]** so it's going down the link.

**[93:02 -> 93:04]** So learning from the three changes

**[93:04 -> 93:08]** during the training process.

**[93:08 -> 93:12]** You can also have this just a cosine rule, cosine decay.

**[93:12 -> 93:15]** We can have a linear decay, just a simple,

**[93:15 -> 93:18]** that's the U-1, so maximum on that step,

**[93:18 -> 93:21]** and the index of the step is the taking.

**[93:21 -> 93:25]** Or you can have a inverse square rule like this.

**[93:25 -> 93:28]** So there are many studies you can adopt,

**[93:28 -> 93:31]** but in general the logic is that you start to believe you

**[93:31 -> 93:33]** and then you probably see me as a prison.

**[93:34 -> 93:39]** Okay, now again the basic choice

**[93:39 -> 93:41]** is that of setting the living weight and keeping the mix.

**[93:42 -> 93:44]** This is not a bad choice.

**[93:45 -> 93:50]** So again, I don't expect that my network

**[93:50 -> 93:52]** is fully enabled to converge

**[93:52 -> 93:56]** because of my choice of learning.

**[93:56 -> 93:59]** Usually, if you have a reasonable choice of learning

**[93:59 -> 94:02]** with your network converges,

**[94:02 -> 94:05]** so the fact that your network is completely broken

**[94:05 -> 94:10]** is not because you have chosen a bad learning rate you care.

**[94:12 -> 94:14]** But that's not the point.

**[94:14 -> 94:18]** So, this is not the culprit for not having root results.

**[94:18 -> 94:22]** Of course, the proper choice of the learn with schedule

**[94:22 -> 94:29]** can have higher coolness in the game and in the application.

**[94:33 -> 94:37]** Now, early stopping is something that we have mentioned.

**[94:37 -> 94:40]** So how long to return?

**[94:40 -> 94:43]** Well, this depends on what to look at what happens

**[94:43 -> 94:46]** at the validation set.

**[94:46 -> 94:49]** And we can decide to stop when we start seeing

**[94:49 -> 94:52]** that the foundation error goes down.

**[94:52 -> 94:56]** So that's always a good idea.

**[94:56 -> 94:58]** We know of the double descent now,

**[94:58 -> 95:02]** but if we start seeing the decrease,

**[95:02 -> 95:05]** unless we want to train them a very, very long time,

**[95:05 -> 95:09]** then they're stopped and keep the formula of your model

**[95:09 -> 95:12]** corresponding to that sweet spot where the validation

**[95:12 -> 95:15]** error starts increasing and the evaluation

**[95:15 -> 95:17]** has to be very important.

**[95:17 -> 95:24]** Okay. And so we discussed about the learning rate, which is of course the choice you have

**[95:28 -> 95:35]** to make. And then you also have, I mean learning rate is one of the high-level one years,

**[95:35 -> 95:42]** but you might have several of them. So if you remember before, we were saying that we

**[95:42 -> 95:46]** we are saying that we might introduce some regularization

**[95:46 -> 95:50]** in the model by introducing an extra term in the loss.

**[95:50 -> 95:54]** And we're going to do this, this strategy is going to wait

**[95:54 -> 95:57]** to begin because we are having an extra term in the loss

**[95:57 -> 96:00]** that was constraining the weight of your model

**[96:00 -> 96:04]** to become smaller and smaller in part.

**[96:04 -> 96:07]** The loss was composed of two parts.

**[96:07 -> 96:12]** The part that really calculates how many errors you are making

**[96:12 -> 96:16]** on the training set plus a coefficient

**[96:16 -> 96:19]** and the condition on the boundary.

**[96:19 -> 96:21]** So that could be the coefficient there.

**[96:21 -> 96:23]** Is a coefficient that takes the tradeoff

**[96:23 -> 96:27]** between the fact that you want to provide more importance

**[96:27 -> 96:30]** to the number of errors you're doing on the training set

**[96:30 -> 96:32]** and the fact that you want your model

**[96:32 -> 96:33]** to not become the boundary.

**[96:33 -> 96:36]** So you have a parameter there.

**[96:36 -> 96:39]** That parameter is a high parameter,

**[96:39 -> 96:43]** right, because it is something that you have to choose. It is not something on which your

**[96:43 -> 96:51]** model is optimized model. So, at least you have two hyperparameters, the learning rate

**[96:51 -> 96:59]** and the weight decay, that way that you put in front of the L2, no one, so you can see

**[96:59 -> 97:04]** that. And what you want to do is to choose this hyperparameter and usually you do it

**[97:04 -> 97:09]** by cross validation and looking at the performance of your model of validation. When you change

**[97:09 -> 97:11]** these stages, right?

**[97:11 -> 97:16]** And what you would sort of hyper-positive with them,

**[97:16 -> 97:19]** where you choose different values,

**[97:19 -> 97:23]** and you under different pairs of them,

**[97:23 -> 97:26]** like the final window in which each of these values

**[97:26 -> 97:28]** is changing them, and then you would

**[97:28 -> 97:30]** have taken pairs of them and then you see what happens.

**[97:30 -> 97:33]** So you might have a hyper-positive with it.

**[97:33 -> 97:38]** But what is networked is I also be helpful

**[97:38 -> 97:41]** not to just fix these set of hyperparameter,

**[97:41 -> 97:44]** but considering an old range,

**[97:44 -> 97:48]** and a full range in which your hyperparameter are changing,

**[97:48 -> 97:51]** rather than taking a precise green.

**[97:51 -> 97:52]** So you can see the old range,

**[97:52 -> 97:55]** and then you possibly also take randomly

**[97:55 -> 97:58]** the value inside this range.

**[97:58 -> 97:59]** Why?

**[97:59 -> 98:02]** Well, because, I mean, when you have,

**[98:02 -> 98:04]** when you choose a green,

**[98:04 -> 98:07]** now you're saying that somehow

**[98:07 -> 98:13]** you are scheduling right how you select the bay use for the two parameters, in this case

**[98:13 -> 98:19]** that weight decay in the learning field. And then you look at that in a regular group.

**[98:19 -> 98:27]** But it can happen that one of the two hyperparameters is more influential than the other to change

**[98:27 -> 98:34]** in these stuff and provide you with significant variation in the performance while changing the other

**[98:34 -> 98:37]** and you see that it provides you with a big.

**[98:37 -> 98:40]** Then if this happens, then I mean,

**[98:40 -> 98:43]** in front of you with this grid organization,

**[98:43 -> 98:46]** you're practically looking at specific points

**[98:46 -> 98:50]** where you might end up losing the region

**[98:50 -> 98:53]** while you really, really see the big.

**[98:54 -> 98:59]** So if possible, so if your competition really affords you

**[99:00 -> 99:04]** and you can afford it, it would be better to select

**[99:04 -> 99:09]** more points and more points that are not distributed in this way but are wrong

**[99:09 -> 99:16]** when you need to. In the range in which the values can change.

**[99:16 -> 99:22]** So now here is exactly the same number of nine points and just distributing the

**[99:22 -> 99:26]** bandwidth in range. But of course if you can take more it will be better.

**[99:26 -> 99:32]** And this allows you also to capture the part that some of the parameters are

**[99:32 -> 99:34]** more relevant to the other.

**[99:36 -> 99:38]** And now look at this.

**[99:38 -> 99:41]** So these are results that come from a paper,

**[99:42 -> 99:45]** a paper from America, it's among one,

**[99:45 -> 99:47]** where they were testing, I mean,

**[99:47 -> 99:52]** it's cross-validating different kind of architectures.

**[99:52 -> 99:55]** And you see, I mean, they're taking loads of ones.

**[99:55 -> 99:59]** They really densely observing the space

**[99:59 -> 100:01]** of the hyperbarometers,

**[100:01 -> 100:04]** And then you should be using the best one for the evaluation.

**[100:04 -> 100:07]** Now, we are not necessarily met up.

**[100:07 -> 100:09]** We might not have all the competition

**[100:09 -> 100:12]** to fill in the space so densely.

**[100:12 -> 100:15]** But still, I mean, the fact that you can do that

**[100:15 -> 100:20]** and avoid having just agreed might help you to realize,

**[100:20 -> 100:24]** really, what is the best combination of hydrophysics,

**[100:24 -> 100:27]** right, rather than having this very specific kind of group.

**[100:27 -> 100:37]** So, what is the procedure one expect to follow?

**[100:37 -> 100:44]** So, let's say that first of all, of course, you choose the hydrodynamic, so you have

**[100:44 -> 100:47]** this initial phase.

**[100:47 -> 100:57]** And so at least we start playing with the architecture.

**[100:57 -> 101:04]** But even before somehow choosing this hyper parameter,

**[101:04 -> 101:07]** one can try to run some sanity check on the model

**[101:07 -> 101:10]** to see that everything is being corrected.

**[101:10 -> 101:15]** And to do the sanity check, maybe what we want to do

**[101:15 -> 101:19]** It's too far just on the laws.

**[101:19 -> 101:21]** And in salivation, when you're planning

**[101:21 -> 101:25]** on the model, you're going to say.

**[101:25 -> 101:28]** And you might also decide at the beginning

**[101:28 -> 101:31]** to turn off the way you do it.

**[101:31 -> 101:32]** Why you want to turn off the way you

**[101:32 -> 101:37]** decay, because you don't want to memorize.

**[101:37 -> 101:39]** So now, at the very beginning, you

**[101:39 -> 101:43]** don't want to memorize why it seems counterintuitive.

**[101:43 -> 101:46]** But what you actually are asking your method to do

**[101:46 -> 101:49]** is to really overthink sound example.

**[101:49 -> 101:53]** So your model is to reach a parameters

**[101:53 -> 101:57]** that you should be able to memorize the frame examples.

**[101:58 -> 102:01]** So I start by removing some revolution

**[102:01 -> 102:04]** with the case model revolution, right, the subject.

**[102:04 -> 102:08]** So we avoid it and we let the network train on data

**[102:08 -> 102:11]** and memorize the frame set.

**[102:11 -> 102:13]** It should be able to do that.

**[102:13 -> 102:17]** If it's not able to memorize the training samples of lower fit,

**[102:17 -> 102:18]** there's already something wrong.

**[102:18 -> 102:23]** Maybe the how you roll the code or some bug there.

**[102:23 -> 102:27]** So first thing, try to work it on the training sample.

**[102:27 -> 102:32]** Remove the regularization pathogens

**[102:32 -> 102:34]** and do some sort of scientific check.

**[102:34 -> 102:37]** And the first scientific check is immediately on the law.

**[102:37 -> 102:40]** So idea, the answer to your network is random.

**[102:40 -> 102:43]** And you expect a normal prediction at the very first.

**[102:43 -> 102:47]** Then when you train, you should be able to move a thing.

**[102:47 -> 102:50]** But the very beginning, right?

**[102:50 -> 102:52]** Your loss is practically normal.

**[102:52 -> 102:57]** So if you have your, say, C class prediction,

**[102:57 -> 103:00]** and you remember, it is your soft map, right?

**[103:00 -> 103:02]** Remember we discussed about it.

**[103:02 -> 103:06]** Or physical regression, it's a cross-center belong,

**[103:06 -> 103:08]** it's just a binary percentage of the loss.

**[103:08 -> 103:13]** and then we discard the moon because where you have the soft mark,

**[103:13 -> 103:16]** and then the category of the entropy law of the properly

**[103:16 -> 103:18]** and the reason of this.

**[103:18 -> 103:22]** Now we know how the law is written.

**[103:22 -> 103:26]** And if I have, so let me see here.

**[103:26 -> 103:29]** So if I consider, think about the case

**[103:29 -> 103:32]** in which you are trying to train your model on a problem

**[103:32 -> 103:36]** with 10 classes, like a site with 10 is a typical database

**[103:36 -> 103:47]** you have 10 classes. Now the self-max loss is the negative low probability of the correct

**[103:47 -> 103:51]** loss on the sine block. But now you are assigning class of random

**[103:51 -> 103:56]** probability. So you have 10 classes for every sample, you expect that I mean every class

**[103:56 -> 104:03]** of as probability 0, 1, plus a 10 percent probability. So they are all the classes are

**[104:03 -> 104:10]** So if you look at the formula and you say this, it should be minus the logarithm of 1 over

**[104:14 -> 104:20]** 10 in targets, because you have equal probability through the process. And so this number should

**[104:20 -> 104:25]** be exactly that, that way, that's the minus the logarithm of 0 to 1, which is something

**[104:25 -> 104:32]** like 2 of 3. So you know what to expect. And that's what you check if your net is the

**[104:32 -> 104:39]** So that's the very first thing you can do, checking the loss, that's the first thing,

**[104:39 -> 104:42]** okay, so you can check that.

**[104:42 -> 104:49]** And then you should be able, while you go on training, you should be able to overfeed the

**[104:49 -> 104:52]** training samples and be able to move a good position, okay.

**[104:52 -> 105:01]** So check initial loss, then go ahead by removing all the regression strategies, and you should

**[105:01 -> 105:05]** to perfectly memorize your training center.

**[105:05 -> 105:09]** So you should expect a 100% training accuracy

**[105:09 -> 105:11]** on a small sample of training done

**[105:11 -> 105:13]** when you're set up in the batches.

**[105:13 -> 105:17]** So you play with the architecture with the learning rate.

**[105:17 -> 105:19]** Of course, your training optimization,

**[105:19 -> 105:21]** you should be able to see that you're more

**[105:21 -> 105:25]** producing 100% accuracy on the training center.

**[105:25 -> 105:26]** Okay?

**[105:26 -> 105:28]** So if the loss is not going down,

**[105:28 -> 105:30]** like maybe the learning rate is too low

**[105:30 -> 105:37]** you have a diamond sensation, it's about explodes, then maybe you learn why or you have that

**[105:37 -> 105:44]** sensation. So, I mean, you start making a diagnosis of what's happening on your back

**[105:44 -> 105:50]** to it, to put it on the right track, right? Otherwise, if these things are not happening,

**[105:50 -> 105:52]** there's something strange.

**[105:53 -> 105:58]** Okay, then at this point, you go back to your,

**[106:01 -> 106:02]** if we have a private research,

**[106:02 -> 106:05]** so now everything seems super-verged,

**[106:05 -> 106:08]** but maybe you can choose a better room rate

**[106:08 -> 106:10]** to improve the convergence.

**[106:10 -> 106:13]** And so you start playing with a very great,

**[106:14 -> 106:18]** if you're trying to convey the result of this on the screen,

**[106:18 -> 106:22]** you have more iteration.

**[106:22 -> 106:26]** So you start looking at how the law works on right.

**[106:26 -> 106:28]** So really, you're limiting the learning process,

**[106:28 -> 106:31]** really looking at what's happening.

**[106:32 -> 106:35]** And at the beginning, you have some more or less

**[106:35 -> 106:38]** an high level idea of learning rate.

**[106:38 -> 106:42]** Then you start creating maybe a course grid of values,

**[106:42 -> 106:46]** also way introducing the weight gain, right?

**[106:46 -> 106:50]** and try and find leaders to run the research that

**[106:50 -> 106:55]** is on the finish guide.

**[106:55 -> 106:57]** Then we'll define the grid.

**[106:57 -> 107:00]** The new train is a little longer.

**[107:00 -> 107:02]** And you go on like this.

**[107:02 -> 107:07]** Of course, I think no steps you look at the learning curves.

**[107:07 -> 107:10]** And what you expect to see is a lot of good sound,

**[107:10 -> 107:13]** training, accuracy, that goes up, validation

**[107:13 -> 107:16]** that does not go down because otherwise,

**[107:16 -> 107:19]** I think about really stopping and there's something

**[107:19 -> 107:22]** that's not going to be any more than a thinking, right?

**[107:22 -> 107:24]** So these are the nice things.

**[107:24 -> 107:31]** And usually, I mean, each of these steps take a little bit more time.

**[107:31 -> 107:34]** So at the beginning, it's quite fast because you're working

**[107:34 -> 107:38]** on just a subset of data and then you start leaving the network

**[107:38 -> 107:43]** and his job for longer set of books or longer of the other plans.

**[107:47 -> 107:50]** And when you look at the curves, well, again,

**[107:50 -> 107:52]** you can see some typical behavior

**[107:52 -> 107:54]** that you also saw when discussing about

**[107:54 -> 107:56]** the needs of reading observations, right?

**[107:56 -> 107:58]** So if at the beginning the loss is flat

**[107:58 -> 108:02]** and it takes quite a long time before it starts decreasing,

**[108:02 -> 108:05]** then probably the culprit is the answer to the question.

**[108:05 -> 108:14]** If the lowest pathos then again it can be an issue a different sensation but also to the learning rate.

**[108:14 -> 108:20]** You can start trying to change the learning rate.

**[108:20 -> 108:28]** If you start, if you see something like this, then this small step, then maybe you change the learning rate.

**[108:28 -> 108:35]** applying a lot of self-wise learning K or another strategy of learning K, but in doing

**[108:35 -> 108:36]** it too early.

**[108:36 -> 108:41]** So you should let the network go ahead a little bit more, would that learning way?

**[108:41 -> 108:47]** And then decide to change the living term.

**[108:47 -> 108:53]** In terms of accuracy, again what we expect to see is that training accuracy goes up and

**[108:53 -> 108:59]** validation of course it was up to we expect that there is some gap right

**[108:59 -> 109:03]** because again the training sample is the thing that we are really optimizing on

**[109:03 -> 109:08]** but that we see during the continuation. Well the validation is something that we test on

**[109:08 -> 109:12]** somehow I mean we don't see it during training right so it's just the set of

**[109:12 -> 109:17]** data which we validate our model so we expect that it will find a little word

**[109:17 -> 109:21]** But we don't want to see this kind of behavior, right?

**[109:21 -> 109:24]** Otherwise we don't know where to stop the dissolution,

**[109:24 -> 109:28]** and because here more of the way we can get it.

**[109:28 -> 109:32]** Well, this kind of behavior here is actually

**[109:32 -> 109:35]** saying that we are good at training,

**[109:35 -> 109:38]** and our validation is practically performing

**[109:38 -> 109:40]** similar as one general unfolding.

**[109:40 -> 109:44]** So maybe, I mean, the difference is more.

**[109:44 -> 109:46]** So maybe we can do something better in training,

**[109:46 -> 109:50]** to get the founder gap that we will expect.

**[109:50 -> 109:55]** So maybe this can be an indication that we are under-thinking.

**[109:55 -> 109:58]** So we can increase the number of parameters of a model,

**[109:58 -> 110:01]** or we can change something else.

**[110:01 -> 110:05]** So we can train longer or lose a bigger model

**[110:05 -> 110:09]** to increase the number of parameters.

**[110:09 -> 110:14]** So we look at the loss curves in this procedure.

**[110:14 -> 110:17]** And in practice, I mean, we go back to set five.

**[110:17 -> 110:20]** So we finally change something else.

**[110:20 -> 110:23]** And after a while, everything starts to stop.

**[110:23 -> 110:25]** It's a way to get to the results.

**[110:25 -> 110:26]** We get to accuracy.

**[110:26 -> 110:28]** We might be satisfied.

**[110:28 -> 110:31]** Well, usually when you think about producing a research paper,

**[110:31 -> 110:33]** you're another satisfied.

**[110:33 -> 110:36]** So you go to set five and then you take the performance

**[110:36 -> 110:38]** and you say, OK, you're going to want to do five percent more

**[110:38 -> 110:42]** of a course than you go back and then you're moving around.

**[110:42 -> 110:44]** is that thinking about having pieces in the network

**[110:44 -> 110:48]** or maybe removing pieces to improve efficiency.

**[110:48 -> 110:51]** And so this, of course, is a look.

**[110:51 -> 110:56]** And is a look that actually costs,

**[110:56 -> 111:00]** because besides choosing a texture,

**[111:00 -> 111:03]** then you have the choice of all the hyperparameter,

**[111:03 -> 111:06]** deciding if introducing the evaluation or not

**[111:06 -> 111:08]** and how much of it.

**[111:08 -> 111:11]** So it's like really, I mean, tweaking all this pattern

**[111:11 -> 111:14]** and triggers that might happen.

**[111:14 -> 111:17]** You have this complex console on the plate.

**[111:18 -> 111:20]** So it's really, I mean,

**[111:20 -> 111:24]** neuro-mentor practitioners spend a lot of their time

**[111:24 -> 111:26]** in this kind of job,

**[111:26 -> 111:29]** and during all these triggers and debutments.

**[111:31 -> 111:33]** And in the past, for these,

**[111:33 -> 111:37]** that was quite heavy kind of work,

**[111:37 -> 111:40]** provided you with figures and tables of these kind,

**[111:40 -> 111:47]** So we are looking at all the losses, the periods, and trying to make sense of it.

**[111:47 -> 111:54]** And the common center to get crazy nowadays are much better tools that you can use, like

**[111:54 -> 111:59]** the way the biases of the common one you need, that allow you to realize what's happening

**[111:59 -> 112:05]** in philanthropic and what's going on in the effect of cheering you have in the whole year.

**[112:05 -> 112:08]** But yeah, I mean in general anyway,

**[112:08 -> 112:13]** large part of your time in Opioid in network

**[112:13 -> 112:18]** is spent by looking at babysitting the training process

**[112:18 -> 112:20]** and trying to understand what it can be better

**[112:20 -> 112:21]** to let the network perform,

**[112:21 -> 112:23]** and then improve its performance.

**[112:27 -> 112:32]** Okay, so you can also track the way

**[112:32 -> 112:40]** which the weights change because what you expect is that at every update in your

**[112:40 -> 112:48]** start in the same step you expect that the abrasion is very varying than the

**[112:48 -> 112:55]** video of this time okay so around the one so you depend on it themselves that

**[112:55 -> 113:00]** every run is set step they do not change that much so you start seeing

**[113:00 -> 113:06]** strange behavior with very big jumps that again there is something wrong. So somehow

**[113:06 -> 113:12]** you can also pay attention to how much each of the weights or at least the

**[113:12 -> 113:18]** seven weeks is updated to control the ratio of the weight.

**[113:18 -> 113:25]** And so this somehow covers this part, right? Which actually takes a little time.

**[113:25 -> 113:29]** This is really the part where who designed the network

**[113:29 -> 113:32]** and try to think of work, think about new solutions,

**[113:32 -> 113:34]** spend a lot of time.

**[113:34 -> 113:38]** So doing research in this sense is super,

**[113:38 -> 113:40]** I mean, it needs a little bit hurt

**[113:40 -> 113:43]** because it's not just a matter of thinking about

**[113:43 -> 113:45]** the problem, the task.

**[113:45 -> 113:50]** So making sense of the data, thinking about the task,

**[113:50 -> 113:52]** trying to understand what you really need

**[113:52 -> 113:54]** to let this task work and be resolving.

**[113:54 -> 113:56]** then formalizing the architecture,

**[113:56 -> 113:59]** and then spot seeing the numbers.

**[113:59 -> 114:00]** But then the numbers, I mean, again,

**[114:00 -> 114:02]** you're never satisfied.

**[114:02 -> 114:05]** So you go back backwards and you say, okay,

**[114:05 -> 114:08]** but this, the way which I'm solving the task,

**[114:08 -> 114:09]** requires something else.

**[114:09 -> 114:11]** And then you think about how to formalize it

**[114:11 -> 114:13]** in the architecture and then you change the model

**[114:13 -> 114:15]** and then you spend, then there is the extra layer

**[114:15 -> 114:17]** of choosing all the higher parameters,

**[114:17 -> 114:20]** the engineering solution, right?

**[114:20 -> 114:23]** So that's the reason why usually when you see nowadays

**[114:23 -> 114:27]** a research paper, it's very rare to see research paper

**[114:27 -> 114:29]** when two or three overs.

**[114:29 -> 114:32]** There are 10 people there, because as far as some groups

**[114:32 -> 114:33]** that you're working on a part,

**[114:33 -> 114:35]** is that another subgroup is working on a part

**[114:35 -> 114:39]** and then they put each other and produce a good result.

**[114:39 -> 114:41]** On the other way around, when you see paper,

**[114:41 -> 114:44]** whether a few number of authors, well,

**[114:44 -> 114:46]** don't over all are super smart.

**[114:46 -> 114:47]** A good section.

**[114:47 -> 114:50]** There's something that really makes them different

**[114:50 -> 114:53]** with the perspective and range of a lot of publication,

**[114:53 -> 114:57]** where there is five, six, or 10 papers.

**[114:57 -> 115:00]** OK, so now this is about the training dynamic.

**[115:00 -> 115:03]** Let's see what happens after training.

**[115:03 -> 115:07]** So here I'm reporting model and sample and transfer learning.

**[115:07 -> 115:09]** So what we mean with model and sample?

**[115:09 -> 115:19]** Well, so we might decide to solve a task

**[115:19 -> 115:21]** with different architecture.

**[115:21 -> 115:23]** So different architecture and different logics provides

**[115:23 -> 115:25]** you with different solution.

**[115:25 -> 115:28]** And then you might want to just average the average

**[115:28 -> 115:31]** all the predictions of these models the way.

**[115:31 -> 115:32]** Because usually different models,

**[115:32 -> 115:37]** from a lot of different, provides you with different errors.

**[115:37 -> 115:38]** And then when you average down here,

**[115:38 -> 115:40]** you just get enough advantage.

**[115:40 -> 115:43]** So you can train multiple and you run a model.

**[115:43 -> 115:45]** And the first line you get an advantage there here.

**[115:45 -> 115:49]** I'm just estimating like 2% extra performance.

**[115:49 -> 115:50]** Why I'm telling it?

**[115:50 -> 115:54]** It's because, so we mentioned several times

**[115:54 -> 115:59]** that often there are these, let's say,

**[116:00 -> 116:03]** international challenges where some company

**[116:03 -> 116:06]** or search center provides that,

**[116:06 -> 116:10]** that asks interest in researchers who are by their model

**[116:10 -> 116:14]** and we know that that's a produce the best performance.

**[116:14 -> 116:15]** And we have these leaderboards,

**[116:15 -> 116:19]** those different groups competing to produce better results.

**[116:19 -> 116:24]** Well, one of the strategies that certainly provides you,

**[116:24 -> 116:26]** I mean, gain in this leaderboard,

**[116:26 -> 116:29]** is that you don't trade just one model.

**[116:29 -> 116:31]** It can be perfect, super good.

**[116:31 -> 116:32]** But rather than trading one model,

**[116:32 -> 116:34]** you're trying to work with your fight.

**[116:34 -> 116:35]** And you're having a problem.

**[116:35 -> 116:39]** And it did in the last years, in these international challenges,

**[116:39 -> 116:42]** most of the groups that win, that's the strategy

**[116:42 -> 116:43]** that they need.

**[116:43 -> 116:46]** Of course, every single of this model

**[116:46 -> 116:48]** has to be white, and they need to produce good results.

**[116:48 -> 116:51]** But then I mean, everything else, multiple models,

**[116:51 -> 116:53]** of course, gets you some extra performance.

**[116:55 -> 116:58]** So that's something you can always do.

**[117:00 -> 117:03]** But also requires that you have to train multiple models,

**[117:03 -> 117:04]** which it can be costly.

**[117:04 -> 117:07]** So again, it is a solution, but it's a solution

**[117:07 -> 117:12]** that can be afforded maybe by only a few groups,

**[117:12 -> 117:14]** few research groups, I mean.

**[117:14 -> 117:21]** And moreover, it means that you don't only have to spend time to train multiple models,

**[117:21 -> 117:26]** but also at test time, you have to run multiple inferences.

**[117:26 -> 117:29]** So this is not ideal in terms of electricians.

**[117:29 -> 117:38]** If you call it a result very quickly, faster, I'm saying this is not the real.

**[117:38 -> 117:47]** But besides training multiple models, one thing that you can think about is just taking one

**[117:47 -> 117:53]** single model and keeping several snapshots of your model during training.

**[117:53 -> 117:59]** Now again, we know that if during training our loss goes down, it means that the model

**[117:59 -> 118:04]** is fast in two different positions in our loss landscape, which are not ideal and then

**[118:04 -> 118:19]** progress will go to a minimum. True. But it can also happen that you can guide the training to let your network visit multiple minimas and then you keep a snapshot of your model, this multimulima and then you adjust them up.

**[118:19 -> 118:23]** You keep an ensemble of all these

**[118:23 -> 118:27]** an assumption of other people in the model.

**[118:27 -> 118:31]** Now to do that, you have to get crazy

**[118:31 -> 118:35]** a little bit with the study of how you set the learning rate.

**[118:35 -> 118:40]** Maybe you can have some very strange learning rate schedule,

**[118:40 -> 118:46]** right, that allow you to go here and there and jump on different points of the last landscape,

**[118:46 -> 118:53]** which again not necessarily brings you to just one optimal minimum, but let you visit, I mean,

**[118:53 -> 119:01]** explore the last landscape. So this is certainly something that you can do. Or you can,

**[119:01 -> 119:10]** yeah, this is just an average, so you can keep track of your planet Earth factors during the

**[119:10 -> 119:14]** training process and then we take another. So even though, I mean, at the beginning, the more

**[119:14 -> 119:19]** not to remove, but then you prove and you properly take this average of the fine

**[119:19 -> 119:24]** meter in time so rather than just rely on the next, from time to time you take the

**[119:24 -> 119:29]** average and then you use that to go on, pay off the fineers, then this can help your body.

**[119:29 -> 119:35]** So there are several trick and tricks, I mean in this sense that you can adopt and

**[119:35 -> 119:40]** then somehow go into the logical and sampling that can provide you with more

**[119:40 -> 119:45]** of accuracy.

**[119:45 -> 119:48]** And now there was also a graph on model ensemble.

**[119:48 -> 119:50]** What I'm adding here is also something

**[119:50 -> 119:53]** that I call transfer learning.

**[119:53 -> 119:55]** Now, what is transfer learning?

**[119:55 -> 119:59]** And why I'm putting it in the group of after training.

**[119:59 -> 120:01]** Because in practice, this transfer learning

**[120:01 -> 120:05]** substitute what we defined before as weighting solution.

**[120:05 -> 120:08]** So the idea is that we have a model

**[120:08 -> 120:11]** that rather than training from scratch,

**[120:11 -> 120:15]** it starts from the parameter that someone provides you

**[120:15 -> 120:19]** and that was the result of the training on an undersell.

**[120:20 -> 120:22]** Okay, so you want to train your model on the duck set

**[120:22 -> 120:26]** that you have, but someone else said,

**[120:26 -> 120:31]** okay, you know, I did the training of that architecture

**[120:31 -> 120:33]** in a master for another duck set.

**[120:33 -> 120:35]** So maybe you can renew my weight

**[120:35 -> 120:37]** and then go ahead in the training.

**[120:37 -> 120:40]** rather than starting from scratch.

**[120:40 -> 120:43]** It's transfer learning from a three-train model.

**[120:43 -> 120:47]** That is, I mean, a variant, a different condition,

**[120:47 -> 120:49]** with respect to learning from scratch,

**[120:49 -> 120:51]** that requires a way to evaluate.

**[120:51 -> 120:54]** So it's a different way to initialize the way.

**[120:54 -> 120:58]** Now, not a new model, but from the knowledge

**[120:58 -> 121:01]** that someone else passed you in terms of parameters

**[121:01 -> 121:02]** of a three-train model.

**[121:02 -> 121:14]** And trust to learn is also the solution somehow to the issue that for a long time,

**[121:14 -> 121:20]** create problems to research, that would be the idea that to train a big network,

**[121:20 -> 121:23]** a lot of earlier, you need a lot of data.

**[121:23 -> 121:26]** So this means there is a big number.

**[121:26 -> 121:35]** It's not true, it's not true, that to train a deep nerve network, you need wheels or beams of it.

**[121:35 -> 121:40]** Of course, if you have them, then you're lucky, but you might not have it.

**[121:40 -> 121:44]** And so you might inherit knowledge from a different training.

**[121:44 -> 121:49]** And so you will create training about it.

**[121:49 -> 121:55]** Now, to tell you about this, to tell you more about trans-learning,

**[121:55 -> 122:05]** Let me quote on the side, I mean this email that I think I mentioned it for a immovable

**[122:05 -> 122:06]** mind.

**[122:06 -> 122:13]** So this email sent database was the one that actually was used for the international challenge

**[122:13 -> 122:22]** in 2012 that led to practical and behavioural demonstration that they meant learning modern

**[122:22 -> 122:23]** work.

**[122:23 -> 122:32]** was having these big pathways that contained originally 20, so overall, contained something

**[122:32 -> 122:43]** like 21,000 causes, but all of them just 1,000 were used for the image of that challenge.

**[122:43 -> 122:47]** And it's a sort of visual book outlet.

**[122:47 -> 122:51]** So for every word that you can find in a vocabulary, so they were using more of the

**[122:51 -> 122:54]** with a hierarchy of eulaeontology,

**[122:54 -> 122:57]** which of the term you can have in the local gallery,

**[122:57 -> 122:59]** they were searching for images,

**[122:59 -> 123:03]** and they were collecting them in this visual vocabulary.

**[123:03 -> 123:08]** And so they were covering more than 21,000 boxes.

**[123:08 -> 123:15]** And out of these 1,000, 1,000 of them were used to start this challenge,

**[123:15 -> 123:19]** international challenge of being researched to build the model

**[123:19 -> 123:24]** So I believe that the E-men's land website

**[123:24 -> 123:27]** doesn't want to exist anymore in this term, right?

**[123:27 -> 123:28]** It was like this.

**[123:28 -> 123:32]** We had an image and website where you could navigate

**[123:32 -> 123:36]** the object and in the name and visualize different examples

**[123:36 -> 123:39]** of that object class.

**[123:39 -> 123:42]** Yeah, it doesn't exist anymore for several reasons

**[123:42 -> 123:46]** because then we discovered that the way inappropriate images

**[123:46 -> 123:51]** inside the other base, they started caving, they were biased.

**[123:51 -> 123:57]** And now I think that just last month, I mean this month,

**[123:57 -> 124:01]** it has been accepted to paper, I believe, at the narrow information

**[124:01 -> 124:06]** post-system conference of narratives, one of the most famous one,

**[124:06 -> 124:11]** that says that this data has to be read, both completely.

**[124:11 -> 124:15]** So even after so many years, this data has not really, I mean,

**[124:15 -> 124:21]** more in the center of the public of the research. Still people are too focused on the Bible.

**[124:21 -> 124:27]** It was not perfect. Agree, it is not perfect, but still it was really the reason why people

**[124:27 -> 124:34]** explored their views of these models. So, these are the ways for certain periods of time,

**[124:34 -> 124:40]** people started to really get mad about being able to solve the laws. And it was not just

**[124:40 -> 124:44]** the matter of winning the challenge, because there was not that many mornings behind winning

**[124:44 -> 124:49]** the challenge and it was not the matter of like the challenge of mathematics.

**[124:49 -> 124:54]** We were providing money. It was just a research task.

**[124:54 -> 125:06]** But the reason why people were really interested in that is because once the new model came out and demonstrated to be able to be used as a classifier,

**[125:06 -> 125:15]** classifier, the grid classifier, a 1000 pound on the imagination, then the rest of the world

**[125:15 -> 125:21]** was just inherited with and transferring knowledge for their own private task.

**[125:21 -> 125:26]** So I'd say we have a model that has been trained to classify 1000 classes.

**[125:26 -> 125:33]** These were mainly animals and natural objects and things, and that kind of fungi and other

**[125:33 -> 125:40]** stuff, right? The mushrooms and vegetables, animals, there were all the some vehicles, right?

**[125:40 -> 125:48]** So once the model has been trained like this, then I don't know a company that needed to

**[125:48 -> 125:55]** create its own model to classify fashion and a different kind of peaceful reward group, right?

**[125:55 -> 126:02]** Then they were inheriting the weight of things by training women's life and they were just

**[126:02 -> 126:05]** take those weights for their own goal,

**[126:05 -> 126:08]** partial classification or something else.

**[126:08 -> 126:12]** So people were really just waiting for these models

**[126:12 -> 126:15]** to come out, because there was a lot of knowledge inside

**[126:15 -> 126:18]** those weights that could be inherited for something else.

**[126:18 -> 126:22]** So think about a simple Alex Napul

**[126:22 -> 126:25]** going in depth into how the architecture

**[126:25 -> 126:27]** was done in the next lecture.

**[126:27 -> 126:30]** But for the moment, we know that we

**[126:30 -> 126:34]** have some like our input, then a set of convolutional layer,

**[126:34 -> 126:37]** max coding layers, and then at the end,

**[126:37 -> 126:40]** we have our thermodynamic layer, right?

**[126:40 -> 126:45]** So now we train this thing on ImageNet.

**[126:45 -> 126:51]** And then we know that the very last output layer

**[126:51 -> 126:56]** produces 1,000 pages because that was the goal of the challenge,

**[126:56 -> 126:56]** right?

**[126:56 -> 126:59]** So being able to classify 1,000 classes,

**[126:59 -> 127:01]** So we have 1,000 millions.

**[127:01 -> 127:04]** For every image, we look at these values

**[127:04 -> 127:06]** and we expect that the highest values correspond

**[127:06 -> 127:08]** to the probability of cost, cost, cost, right?

**[127:08 -> 127:10]** And all the other should be zero.

**[127:10 -> 127:11]** And our probability of cost,

**[127:11 -> 127:12]** and all the other should be zero.

**[127:12 -> 127:16]** So 1,000 billion, each of them represent

**[127:16 -> 127:18]** the probability for seven class

**[127:18 -> 127:20]** to let them actually be able to predict, okay,

**[127:20 -> 127:22]** over this class.

**[127:22 -> 127:23]** Perfect.

**[127:23 -> 127:26]** So if this has been trained, what it can do

**[127:26 -> 127:29]** to pose a path now a new data set

**[127:29 -> 127:36]** will have more amount of sample is that they can keep this network completely frozen. I

**[127:36 -> 127:44]** don't change anything, so I freeze the weights of the network and I only change the last

**[127:44 -> 127:51]** layer. So I really show all the weights of only this part and I train the model, but actually

**[127:51 -> 127:56]** what I'm training at this point is not the whole network. Nothing changes in terms of

**[127:56 -> 128:01]** of this part, I will ask the model to change only the parameters of the last layer.

**[128:01 -> 128:02]** Okay?

**[128:02 -> 128:07]** And in this way, I'm practically reusing all the knowledge that I've been captured by

**[128:07 -> 128:11]** the model before.

**[128:11 -> 128:18]** Now, this has been used, I mean, it's a typical thing that you will train on, or image that

**[128:18 -> 128:24]** and then you want to use another data set and you see that you get an increased performance

**[128:24 -> 128:29]** And the more data you have, the better the best.

**[128:29 -> 128:38]** But the point is that if you train with this exploiting

**[128:38 -> 128:41]** this part of an effort, your performance

**[128:41 -> 128:46]** is much better with respect to what you have.

**[128:46 -> 128:50]** You could just start from scratch.

**[128:50 -> 128:51]** And this was just showing that.

**[128:51 -> 128:58]** So this was the performance that you get by using the decaf feature.

**[128:58 -> 129:09]** So the first implementation of Alex Nann was called Capen.

**[129:09 -> 129:14]** And then the new version was decaf, you know, the search is playing the names.

**[129:14 -> 129:19]** And what this model was doing was just inheriting all the weights,

**[129:19 -> 129:26]** And just changing the last layer to produce this classification of 100 boxes.

**[129:26 -> 129:28]** Now, what are we doing here?

**[129:28 -> 129:34]** So you remember that the very first layer of the network are really extracting factors

**[129:34 -> 129:35]** out of the image, right?

**[129:35 -> 129:38]** And then combine them to become more more semantic.

**[129:38 -> 129:46]** Now if we keep the initial layer, so this is just, we are reusing the ability of the network

**[129:46 -> 129:50]** to extract a lot of global colors, edges.

**[129:50 -> 129:52]** This kind of part of the image will be there,

**[129:52 -> 129:54]** even if you change the path, right?

**[129:54 -> 129:57]** If you're passing from the landing cars to the landing fashion,

**[129:57 -> 129:59]** and you leave lots and controls and stuff,

**[129:59 -> 130:00]** they will be there.

**[130:00 -> 130:05]** It's really the composing elements of your natural image.

**[130:05 -> 130:08]** Of course, the more you go inside,

**[130:08 -> 130:11]** the more you go into the semantic of the specific task

**[130:11 -> 130:14]** you are solving for these 1000 causes.

**[130:14 -> 130:19]** And so these will become very specific features.

**[130:19 -> 130:22]** So these might not be perfect for your task.

**[130:22 -> 130:29]** And so in the case of which you have a little bit more samples,

**[130:29 -> 130:32]** maybe rather than changing only the last layer,

**[130:32 -> 130:36]** you might decide to start providing the net growth

**[130:36 -> 130:41]** to also change a little bit, I mean, a larger part of the net.

**[130:41 -> 130:44]** So not updating all the weight of the last layer,

**[130:44 -> 130:48]** but the other way of the more later.

**[130:51 -> 130:56]** And another thing that we can do is rather than keeping

**[130:56 -> 130:59]** this part of the network completely frozen,

**[130:59 -> 131:03]** you can still decide to let it change,

**[131:03 -> 131:06]** but it was more amount.

**[131:06 -> 131:12]** So we don't completely let it move from the original point

**[131:12 -> 131:16]** of the solution that these naps are fine, which we set away.

**[131:16 -> 131:20]** But we use more learning rate, like one term with respect

**[131:20 -> 131:24]** to the learning rate that we'll use in the reading on training.

**[131:24 -> 131:29]** And the effect of this is that we still keep the knowledge,

**[131:29 -> 131:35]** we inherit the knowledge that we had from the previous century,

**[131:35 -> 131:38]** and we just adjusted the bits.

**[131:38 -> 131:43]** So what we're doing is that we are fine tuning the network

**[131:44 -> 131:46]** for our new task.

**[131:46 -> 131:48]** Of course, this would be completely

**[131:48 -> 131:50]** that they started from scratch, new layer.

**[131:50 -> 131:55]** While this part, we can start deciding to let change,

**[131:55 -> 131:57]** not completely but with a smaller array.

**[131:58 -> 132:03]** Now, if I tell you, what does it mean to freeze this network?

**[132:04 -> 132:07]** So now you know that fine tuning means

**[132:07 -> 132:11]** changing the little bit of learning, right?

**[132:11 -> 132:13]** Freezing, what does it mean?

**[132:14 -> 132:16]** So how do you freeze that?

**[132:19 -> 132:20]** Yeah, that is our problem.

**[132:20 -> 132:23]** We don't want the parameters to change,

**[132:23 -> 132:25]** the value to change.

**[132:25 -> 132:28]** And what is the rule that we use to change the parameter?

**[132:32 -> 132:35]** Yes, the calculation is practically realizing

**[132:35 -> 132:36]** it's rather the same, right?

**[132:36 -> 132:42]** So the new W is equal to the old W minus alpha that there is a lot, right?

**[132:42 -> 132:50]** So how do we considering this formula, how do we impose that the new W is equal to the

**[132:50 -> 132:51]** old W?

**[132:51 -> 132:52]** Okay.

**[132:52 -> 132:54]** You are using the learning way to put the new.

**[132:54 -> 133:01]** So if I impose that the learning way is equal to 0, I am freezing up this data.

**[133:01 -> 133:07]** So I'm saying, whatever is your derivative of the law, I don't care.

**[133:07 -> 133:12]** I want the new data to be equal to whatever.

**[133:12 -> 133:15]** So and this really became pervasive.

**[133:15 -> 133:21]** I mean, people, when this logic of being able to inherit knowledge started to be understood,

**[133:21 -> 133:28]** then people started using having for new tasks or for verification, or I mean other tasks,

**[133:28 -> 133:30]** flowers, seeing objects, whatever.

**[133:30 -> 133:34]** So it just scenario what imagines the knowledge

**[133:34 -> 133:36]** from image that they're just abusing it.

**[133:36 -> 133:39]** And it's not using it for not only classification,

**[133:39 -> 133:41]** but maybe you've been used for detection.

**[133:41 -> 133:44]** So a completely different task, right?

**[133:44 -> 133:47]** Because still the backbone, so the feature part,

**[133:47 -> 133:49]** the extracted the top of the image,

**[133:49 -> 133:51]** the part of the conclusion, is still relevant,

**[133:51 -> 133:54]** even if your task is likely different.

**[133:54 -> 133:57]** So not only it has a part of the image,

**[133:57 -> 133:59]** but maybe looking, searching for a part of the image.

**[133:59 -> 134:03]** So where is the person defining a bounding box

**[134:03 -> 134:06]** along the object, searching for the object?

**[134:06 -> 134:09]** So even object detection can be applied.

**[134:09 -> 134:14]** In heriting, can be used or executed by an area

**[134:14 -> 134:19]** known from what even that classifier was.

**[134:19 -> 134:21]** And you see here, what's the image retrieval?

**[134:21 -> 134:22]** So what does it mean?

**[134:22 -> 134:26]** It means that any way that, again, the features

**[134:26 -> 134:29]** that are describing your data aren't good enough,

**[134:29 -> 134:32]** even to run nearest neighbors.

**[134:32 -> 134:35]** So think about what's happening here.

**[134:35 -> 134:39]** So let's say they cut my networks here, right?

**[134:39 -> 134:43]** So if I cut my networks here, what I have is that

**[134:43 -> 134:48]** every time I provide an image to my data, I get here,

**[134:49 -> 134:51]** and I get that any function,

**[134:51 -> 134:54]** the difference is producing a vector of the machine ID

**[134:54 -> 134:56]** 4096 for it.

**[134:56 -> 135:00]** OK, so for every sample, I just put it to the network.

**[135:00 -> 135:04]** It produces a vector of the measure of 4096.

**[135:04 -> 135:05]** Perfect.

**[135:05 -> 135:06]** So this will be my descriptor.

**[135:06 -> 135:10]** So any new image will be defined by this vector.

**[135:10 -> 135:12]** So I start putting all my data with this,

**[135:12 -> 135:15]** I'm using this 4096 dimensional space.

**[135:15 -> 135:18]** And at this time, I take in a sample,

**[135:18 -> 135:21]** that were directly there, and it's for its neighbors.

**[135:21 -> 135:23]** And just doing the illegal investigation

**[135:23 -> 135:27]** in a space that is really rich, because it extracted

**[135:27 -> 135:31]** a lot of knowledge already from the image that's dying.

**[135:31 -> 135:34]** And so these have been used for years,

**[135:34 -> 135:35]** just as a feature vector, and they

**[135:35 -> 135:38]** had a script throughout your data.

**[135:38 -> 135:41]** There were people that didn't actually anything

**[135:41 -> 135:43]** about how this network was trained,

**[135:43 -> 135:46]** and were just using these representation

**[135:46 -> 135:50]** the way to describe the data and really apply the labor.

**[135:50 -> 135:53]** Because this is a very powerful representation,

**[135:53 -> 135:55]** very powerful feature factor.

**[135:58 -> 136:00]** And again, that's the reason why people

**[136:00 -> 136:02]** are really getting mad.

**[136:02 -> 136:04]** There have been a challenge in 2012

**[136:04 -> 136:07]** where the big narrow level of one,

**[136:07 -> 136:09]** so these were the error rates.

**[136:09 -> 136:12]** So three years or producing very high error rates,

**[136:12 -> 136:16]** then the challenge in 2012 rose to these very significant

**[136:16 -> 136:19]** because of the reduction in error,

**[136:19 -> 136:21]** and it was the introduction of the first victim

**[136:21 -> 136:23]** and effort working well, then older,

**[136:23 -> 136:26]** the year after, this challenge went on,

**[136:26 -> 136:28]** and then there were just people waiting

**[136:28 -> 136:31]** for the winner of the challenge

**[136:31 -> 136:34]** that be able to inherit their weight for their own work,

**[136:35 -> 136:37]** okay, in transfer the knowledge.

**[136:37 -> 136:41]** So, yeah, and after this work application

**[136:41 -> 136:44]** for classification and the logic of authentication,

**[136:44 -> 136:46]** but you can use this logical over detection.

**[136:46 -> 136:50]** This is an object detection on a database

**[136:50 -> 136:53]** which is called common object in context.

**[136:53 -> 136:55]** And you see different architecture

**[136:55 -> 136:57]** just an area in a way

**[136:57 -> 136:59]** and see what happens in general performance.

**[137:00 -> 137:05]** Now, overall, we need to define,

**[137:05 -> 137:09]** it's said to find some general rule of thumb

**[137:09 -> 137:12]** about how to use this logical transfer.

**[137:12 -> 137:18]** Because we said that this avoids the issue of not being able

**[137:18 -> 137:23]** to use deep models when you have a limited amount of samples.

**[137:23 -> 137:24]** Actually, there are two things you

**[137:24 -> 137:27]** have to pay attention to.

**[137:27 -> 137:31]** The amount of samples of your new sets of data

**[137:31 -> 137:35]** for your new problem is that e-mails natural images

**[137:35 -> 137:38]** and then no fashion classification or something else.

**[137:38 -> 137:41]** So the second data set, your own

**[137:41 -> 137:45]** the one in which you are interested in solving and in a task on it,

**[137:45 -> 137:49]** then the amount of samples that you have for it is relevant, of course.

**[137:49 -> 137:52]** And then you also have to think about how different is the new

**[137:52 -> 137:56]** that was in respect to the one in which your original model was turned on.

**[137:56 -> 138:02]** Because if you have a model that may train an image then,

**[138:02 -> 138:07]** and then your goal is that all of classifying inksray images,

**[138:07 -> 138:10]** maybe it doesn't work well.

**[138:10 -> 138:12]** OK, this is just to instill the doubt,

**[138:12 -> 138:16]** because it looks like that it may show that it still works well.

**[138:16 -> 138:19]** But it's just to tell you that the difference in terms

**[138:19 -> 138:24]** of semantics of what was to go and the kind of data

**[138:24 -> 138:27]** you used in the pre-training with respect

**[138:27 -> 138:29]** to what you want to use and the task,

**[138:29 -> 138:33]** to have a deployment time for the transferring,

**[138:33 -> 138:34]** then of course, it is an asset that you're

**[138:34 -> 138:36]** taking to the association.

**[138:36 -> 138:38]** So dimensionality, the new deficit,

**[138:38 -> 138:42]** and difference in coherence between the original goal

**[138:42 -> 138:45]** and the natural data in the pre-training

**[138:45 -> 138:47]** and in the downstream task.

**[138:47 -> 138:52]** So usually the names that you pre-training,

**[138:52 -> 138:54]** which is more than been trained before,

**[138:54 -> 138:56]** and downstream task.

**[138:56 -> 139:00]** So the task which are interested in later on.

**[139:00 -> 139:02]** Okay, so if you have

**[139:02 -> 139:09]** There's more data sets in your downstream task.

**[139:09 -> 139:14]** Then one thing that you can choose to do is just keeping

**[139:14 -> 139:20]** really all your, so if your data set is very similar,

**[139:20 -> 139:22]** and you have a limited amount of samples,

**[139:22 -> 139:27]** or the data set between the pre-training and the downstream

**[139:27 -> 139:29]** manner, similar, and you only have a very limited amount

**[139:29 -> 139:39]** samples, then what is convenient is to just keep those networks and change only the very

**[139:39 -> 139:46]** last layer. So this in practice, since the very last layer is only a fully connected layer,

**[139:48 -> 139:54]** its role in practice is just about a linear classifier. It's like applying an SVM at the

**[139:54 -> 139:56]** the end of your network.

**[139:56 -> 139:59]** It's like a find a linear classifier.

**[139:59 -> 140:03]** And this indeed is also called a linear probe.

**[140:03 -> 140:05]** And the other name is just linear probing.

**[140:05 -> 140:11]** If you keep everything frozen and you just change the last row.

**[140:11 -> 140:15]** Well, if you have a little bit more data,

**[140:15 -> 140:17]** and again, your data set is pretty,

**[140:17 -> 140:22]** now then you can decide to unlock some of the layers before,

**[140:22 -> 140:26]** because then you want to let your model absorb a little bit more

**[140:26 -> 140:29]** of the knowledge of your properties, of your immune properties.

**[140:29 -> 140:33]** And so rather than just applying linear probing,

**[140:33 -> 140:39]** you unlock some of the other layers and you find two.

**[140:39 -> 140:41]** If you notice it is very different,

**[140:41 -> 140:44]** and you have a limited amount of samples for these two

**[140:44 -> 140:46]** and four of them.

**[140:46 -> 140:50]** You can try to linear probe to just change the last layer,

**[140:50 -> 140:54]** But it might not work well with the space of significant

**[140:54 -> 140:57]** incoherence within the data basis.

**[140:57 -> 141:00]** And in that sense, maybe the best thing

**[141:00 -> 141:03]** is that you go out and try to collect it with a new data.

**[141:03 -> 141:07]** Or you have a new task of the downstream task.

**[141:07 -> 141:10]** If you have a little more data, that means that you can start

**[141:10 -> 141:14]** and find to make the model of this.

**[141:14 -> 141:20]** So these are the two axes that you have to look at.

**[141:20 -> 141:24]** And again, nowadays, transfer learning

**[141:24 -> 141:26]** is more than normal in the exception.

**[141:26 -> 141:27]** So it's really the sum.

**[141:27 -> 141:31]** So in every paper, and most of the paper you will read,

**[141:31 -> 141:36]** there is a small line that says that your model is starting

**[141:36 -> 141:41]** from this other model X pre-trained model.

**[141:41 -> 141:43]** And pay attention to that.

**[141:43 -> 141:45]** Because, yeah, this is one of the kind of questions

**[141:45 -> 141:48]** I ask during the paper presentation.

**[141:48 -> 141:52]** So this, the order just changed from scratch

**[141:52 -> 141:56]** or inherited some, or using some plans

**[141:56 -> 141:58]** to learn from the green from the model.

**[141:59 -> 142:02]** So it's so much the norm, I mean, the standard that this is

**[142:02 -> 142:06]** as you said is applied not only for classification,

**[142:06 -> 142:10]** but also for detection, because the core of the model,

**[142:10 -> 142:12]** the backbone is still narrated.

**[142:12 -> 142:14]** So it can be narrated from an image

**[142:14 -> 142:16]** and it could be created by it.

**[142:16 -> 142:19]** Although the acting part of the network changes

**[142:19 -> 142:21]** because the goal is different,

**[142:21 -> 142:23]** now you want to detect the objects

**[142:23 -> 142:26]** and find the bound box around the specific objects.

**[142:26 -> 142:28]** So the task is different,

**[142:28 -> 142:31]** but the backbones of most of the architecture

**[142:31 -> 142:33]** is practically the same

**[142:33 -> 142:34]** that the one that you will do,

**[142:34 -> 142:37]** you will do it used for constipation.

**[142:37 -> 142:39]** So you just tend to inherit it.

**[142:39 -> 142:41]** You can use it for image captioning

**[142:41 -> 142:44]** where you have a part of the network

**[142:44 -> 142:49]** best to extract feature from an image and then a part of an actor that has to

**[142:49 -> 142:54]** out-regrestively produce words that describe what is in there in the image

**[142:54 -> 143:00]** then still the part related to the image, let's say feature instruction, you just

**[143:00 -> 143:08]** use a pre-grained model from the one image here. So these parts, you can inherit them.

**[143:08 -> 143:12]** well these other parts would be inherited from something else.

**[143:12 -> 143:16]** So that's the visual part, is the name from a pre-trained woman's name.

**[143:16 -> 143:20]** The foreign language would not start from scratch in the way.

**[143:20 -> 143:24]** It would start with something else that would be pre-trained and applied after this.

**[143:24 -> 143:28]** And of course there's a little part.

**[143:28 -> 143:32]** Yeah, I mean really, even if you want to do, not polycaptioning, but also

**[143:32 -> 143:36]** question answering another kind of talk, the language model.

**[143:36 -> 143:38]** There is this logical problem there.

**[143:41 -> 143:44]** And what is the effect, as you said,

**[143:44 -> 143:50]** is that we have a model that is able to predict better

**[143:50 -> 143:51]** and faster.

**[143:51 -> 143:53]** So we can ask the problem.

**[143:53 -> 143:58]** So if when I train prospects, I have these kind of curves.

**[143:58 -> 144:01]** Then when I train wisdom from counselor,

**[144:01 -> 144:04]** So, inherently knowledge from a freedom ball,

**[144:04 -> 144:07]** then also if you can really have a little amount of samples,

**[144:07 -> 144:08]** it starts from a higher point.

**[144:10 -> 144:12]** And also, I mean, maybe my growth in the curve

**[144:12 -> 144:16]** of getting to a high value is like that.

**[144:17 -> 144:19]** So, yeah, to dream to scratch,

**[144:19 -> 144:21]** maybe you have to train three times as long

**[144:21 -> 144:24]** in respect to not having the, not not transferring position.

**[144:26 -> 144:29]** So now, if you look at the figure,

**[144:29 -> 144:31]** which I have this performance right,

**[144:31 -> 144:34]** so this accuracy for a specific dark

**[144:34 -> 144:36]** and this case of infection.

**[144:36 -> 144:39]** And you have these jumps.

**[144:39 -> 144:41]** Let me start with him here.

**[144:41 -> 144:43]** What do you think they are?

**[144:48 -> 144:49]** Oh, it's like they're not something

**[144:49 -> 144:52]** right in the natural field.

**[144:52 -> 145:06]** So, what the author who are trying to do is very fine what happens either by training

**[145:06 -> 145:10]** a model with a circular relate and let it go, okay.

**[145:10 -> 145:16]** Or from time to time, we are stopping the training, keeping the, saving the model and

**[145:16 -> 145:20]** then letting the model go on with a different learning way.

**[145:20 -> 145:25]** And so you see all these extra branches of the model, right?

**[145:25 -> 145:28]** Because they go with trying to verify or compare.

**[145:28 -> 145:34]** Not only the model of trying to scratch with the one that is using transfer learning,

**[145:34 -> 145:39]** but also what happens when you change the learning when you move the procedure to verify

**[145:39 -> 145:43]** that you get the same result somehow.

**[145:43 -> 145:47]** And so they have to do overall observation of the performance.

**[145:47 -> 145:52]** In general, what we can expect is that if you have a lot of data,

**[145:52 -> 145:56]** well transfer learning or those don't have a big effect.

**[145:56 -> 145:59]** But if your data is known and you want to divide it

**[145:59 -> 146:04]** in terms of performance and better to exploit some knowledge transfer.

**[146:04 -> 146:08]** So you can see it's cold in the paper, transfer learning or knowledge transfer,

**[146:08 -> 146:10]** which is another name you can use.

**[146:10 -> 146:20]** So what I would do here is just a bit of pre-training and then fine-tuning that makes

**[146:20 -> 146:23]** you freely faster and so it's practically useful.

**[146:23 -> 146:28]** Training from scratch works well if you have enough data.

**[146:28 -> 146:35]** And there's, I mean, as I said, it's how the standard right to use is trust-learning

**[146:35 -> 146:36]** and more transingologic.

**[146:36 -> 146:39]** And that's not the way in which you can do that.

**[146:42 -> 146:46]** So, yeah.

**[146:46 -> 146:49]** So this was just going a little bit more in depth

**[146:49 -> 146:54]** about just deciding to define tune,

**[146:54 -> 146:57]** which means updating all the parameter of an effort,

**[146:57 -> 147:02]** maybe with a smaller way, or just what I call linear probing.

**[147:02 -> 147:04]** In linear probing, this part of an effort

**[147:04 -> 147:11]** of the initial part is frozen and I update only the very last layer, which is practically

**[147:11 -> 147:13]** the same as the motion.

**[147:13 -> 147:15]** Now which method does better?

**[147:15 -> 147:20]** Well it depends as we discussed about the amount of samples that you have and the relation

**[147:20 -> 147:27]** between the training there and the training dataset and your deployment task or the same

**[147:27 -> 147:28]** downstream task.

**[147:28 -> 147:33]** And indeed, usually fine tuning works well.

**[147:33 -> 147:38]** And it works better with respect to linear probing.

**[147:38 -> 147:48]** If your, I'd say, the deployment task is similar to the original task.

**[147:48 -> 147:56]** And also if your database is somehow well-behaved.

**[147:56 -> 148:01]** Because if it happens that there is some out of distribution

**[148:01 -> 148:05]** that samples, they have your sample, the one into some categories,

**[148:05 -> 148:09]** and then you have something strange that is really by way

**[148:09 -> 148:15]** with respect to what the pre-training has seen,

**[148:15 -> 148:20]** then it might be better just to train the last layer,

**[148:20 -> 148:23]** like not the whole map, not fine tuning,

**[148:23 -> 148:27]** but just linear tooling.

**[148:27 -> 148:30]** So fine tuning can be words when you

**[148:30 -> 148:32]** are in a condition of output distribution.

**[148:32 -> 148:37]** So when your goal is better of identifying outliers,

**[148:37 -> 148:41]** for instance, in your new cell data.

**[148:41 -> 148:44]** And this is a relevant task because you

**[148:44 -> 148:48]** might be interested in anomaly detection

**[148:48 -> 148:51]** in out of distribution data.

**[148:51 -> 148:52]** So really, I'll identify something

**[148:52 -> 148:57]** that is analogous with respect to the rest of the database.

**[148:57 -> 149:02]** Defects industrial production or strange object on the street

**[149:02 -> 149:05]** for your autonomous driving car.

**[149:05 -> 149:11]** So again, the choice of what you do in terms of training

**[149:11 -> 149:14]** and trying to lead them and trans-learning

**[149:14 -> 149:17]** is also related to the kind of task location.

**[149:17 -> 149:22]** And this is because when you have fine tuning in practice,

**[149:22 -> 149:26]** you are changing both the feature, the representation

**[149:26 -> 149:30]** of the data and the classifier at the end of the model,

**[149:30 -> 149:34]** while instead, so you are practically updating both, right?

**[149:34 -> 149:37]** So how you represent the data and the classifier with them.

**[149:37 -> 149:41]** While when you do linear probing,

**[149:41 -> 149:44]** you are practically keeping the feature frozen,

**[149:44 -> 149:47]** And you're just changing the production by.

**[149:47 -> 149:50]** And this gets enough better in the future

**[149:50 -> 149:53]** and I'll have an institution.

**[149:53 -> 149:56]** Now here I was just mentioning some research work

**[149:56 -> 150:00]** that was trying to properly combine two things.

**[150:00 -> 150:02]** So linear proving and then contuning.

**[150:02 -> 150:05]** And then it was showing the better results

**[150:05 -> 150:07]** for our institution.

**[150:07 -> 150:09]** So our institution is always an interesting part.

**[150:09 -> 150:13]** That is a interactive, a third form real world application.

**[150:13 -> 150:15]** So it's interesting for other people.

**[150:18 -> 150:19]** Okay.

**[150:20 -> 150:21]** Yeah.

**[150:21 -> 150:22]** Let's see the first option.

**[150:22 -> 150:25]** And then next time, we go back to a little bit.

**[150:25 -> 150:29]** We summarize the knowledge of sustainability and we also discuss about the business.

