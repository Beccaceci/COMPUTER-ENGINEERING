# Lecture Transcription

- **Source**: `temp_audio_89001.wav`
- **Model**: `small.en`
- **Device**: `mps`

---

**[00:00 -> 00:12]** Thank you.

**[00:30 -> 00:31]** Okay.

**[00:31 -> 00:37]** This is what it looks like.

**[00:37 -> 00:42]** What is that?

**[00:42 -> 00:45]** Okay.

**[00:45 -> 00:57]** So I'm going back to the deck of slides.

**[00:57 -> 01:06]** to the deck of slides we were looking at last time, just to remember that now we are passing from

**[01:06 -> 01:14]** what can be a neural network just for both of fully connected layers, so where every neuron

**[01:14 -> 01:21]** depends on all the neurons in the previous layer, to something which can incorporate prior knowledge

**[01:21 -> 01:25]** on the existence of a structure on the data.

**[01:25 -> 01:29]** And so we have a network where the first layers

**[01:29 -> 01:32]** are actually convolutional layers, right?

**[01:32 -> 01:35]** And these convolutional layers practically extract

**[01:36 -> 01:40]** the features out of the data, out of images.

**[01:40 -> 01:41]** In this particular case,

**[01:41 -> 01:45]** we are a reference example of structured data.

**[01:45 -> 01:47]** And then after the initial phase

**[01:47 -> 01:48]** where we have convolutional layers,

**[01:48 -> 01:50]** then at the end of the network,

**[01:50 -> 01:53]** we have fully connected layers.

**[01:53 -> 01:56]** And as we said, the choices that we are making

**[01:56 -> 01:58]** in using convolution and the shape of the convolution,

**[01:58 -> 02:01]** the way in which it is say defined,

**[02:01 -> 02:05]** reflect and incorporates inside the architecture,

**[02:05 -> 02:06]** inside the backbone of the network,

**[02:06 -> 02:09]** all these characteristics that somehow

**[02:09 -> 02:12]** are typical of the data themselves.

**[02:12 -> 02:16]** Okay, so we're looking at how the layers work

**[02:16 -> 02:18]** and this was just a simple fully connected layer.

**[02:18 -> 02:23]** we know that everything has to be transformed into a vector

**[02:23 -> 02:25]** because fully connected layers only elaborate

**[02:25 -> 02:27]** on this kind of information.

**[02:27 -> 02:30]** And then, so this vector X is multiplied,

**[02:30 -> 02:33]** this is the linear part with a matrix W

**[02:33 -> 02:34]** to obtain the output.

**[02:34 -> 02:37]** And depending on the number of rows of our W,

**[02:37 -> 02:41]** we have as many elements in the output vector.

**[02:41 -> 02:45]** Okay, so one number for every row of the W matrix.

**[02:45 -> 02:49]** But then we saw how the convolutional layer worked,

**[02:49 -> 02:52]** which instead is able to take into consideration

**[02:52 -> 02:55]** spatial extension of the image.

**[02:55 -> 02:58]** So it looks at region inside the image

**[02:58 -> 03:02]** and convolve the image itself with filters.

**[03:03 -> 03:05]** So now we're talking about images,

**[03:05 -> 03:07]** but this is what happens at every layer.

**[03:07 -> 03:10]** So at the input layer, we have that image

**[03:10 -> 03:12]** and we convolve with filters.

**[03:12 -> 03:14]** Then we create the feature map.

**[03:14 -> 03:18]** And this feature must become the input to the next layer.

**[03:18 -> 03:21]** So let's say that this here,

**[03:21 -> 03:24]** it can be indicated as an image like in the first layer,

**[03:24 -> 03:26]** but then later on, what we produce as output

**[03:26 -> 03:28]** becomes the input of the next layer.

**[03:28 -> 03:31]** And the reasoning is analogous.

**[03:31 -> 03:33]** What we have is always a filter

**[03:33 -> 03:36]** that is convolved over the input.

**[03:36 -> 03:38]** What does it mean to convolve?

**[03:38 -> 03:41]** It means that in practice,

**[03:41 -> 03:44]** the window that describe our filter,

**[03:44 -> 03:49]** that corresponds to our filter is applied over the input.

**[03:49 -> 03:52]** And we take for every element, the product

**[03:52 -> 03:54]** between each element of the filter

**[03:54 -> 03:56]** and each element of the input.

**[03:56 -> 03:59]** And then we sum all the, let's say,

**[03:59 -> 04:01]** results of the product that we got.

**[04:01 -> 04:04]** And we have just one single number.

**[04:04 -> 04:07]** And this is the linear part of our model, right?

**[04:07 -> 04:11]** So just multiplication and sum,

**[04:11 -> 04:14]** this is per se, it's just a dot product, right?

**[04:14 -> 04:19]** And this is what we are doing inside the convolutional layer.

**[04:19 -> 04:24]** So here, for instance, we had an image of special extension,

**[04:24 -> 04:30]** 32 by 32, depth 3, because we have RGB, D.

**[04:30 -> 04:33]** So D, if you will, so either the depth would be 4.

**[04:33 -> 04:37]** So RGB is just the three colors.

**[04:37 -> 04:42]** And our filter should have the same depth of the input.

**[04:42 -> 04:44]** So we can select the dimension line

**[04:44 -> 04:46]** in terms of spatial extension five by five,

**[04:46 -> 04:49]** but three has to be the same of the inputs, okay?

**[04:49 -> 04:50]** So same guess.

**[04:50 -> 04:53]** And so then we can perform the product

**[04:53 -> 04:54]** and obtain an offer,

**[04:54 -> 04:59]** which then will compose the output of this convolution.

**[05:01 -> 05:04]** And we might have as many filters as we want.

**[05:04 -> 05:08]** Again, this depends on the design of our network.

**[05:08 -> 05:10]** So we started with one filter,

**[05:10 -> 05:15]** and we run another use another filter and so on and so forth.

**[05:15 -> 05:18]** Here, for instance, we had six filters.

**[05:18 -> 05:23]** And so you see the depending on how many filter we apply,

**[05:23 -> 05:25]** we have this number.

**[05:25 -> 05:30]** So six filter will define the depth of the output, right?

**[05:32 -> 05:34]** So here we have that six.

**[05:34 -> 05:39]** So this object here is not anymore an image,

**[05:39 -> 05:41]** is a feature map, is something that we obtain

**[05:41 -> 05:44]** out of the evolution.

**[05:45 -> 05:48]** It has a special extension 28 by 28,

**[05:48 -> 05:52]** which depends on the choices that we made

**[05:52 -> 05:54]** in terms of the dimension of the filters

**[05:54 -> 05:57]** and its depth depends on how many filters

**[05:57 -> 05:59]** we decided to use, okay?

**[05:59 -> 06:01]** So it's not really an image,

**[06:01 -> 06:05]** but we can consider it as the new input of the next layer.

**[06:06 -> 06:07]** So it's a different shape,

**[06:07 -> 06:14]** but more or less it can be, it's still a tensor that we can feed to the next layer.

**[06:15 -> 06:21]** For every filter we usually also have a bias. So we have the W right, but also the B.

**[06:22 -> 06:28]** So here we had five by five by three, the dimension of each filter, we had six of them,

**[06:28 -> 06:33]** and for each of them we also add the bias, so the B. So each of them we can call it the W,

**[06:33 -> 06:36]** and for each W we have the corresponding B, which is just a coefficient.

**[06:37 -> 06:42]** So I'm going fast because it's something that we saw with LASA.

**[06:42 -> 06:49]** Now the convolutional part is the linear part of our model, just applying the, let's say,

**[06:49 -> 06:51]** linear function.

**[06:51 -> 06:54]** And then we need to introduce some non-linearity.

**[06:54 -> 07:01]** And so what we do is that we can use the ReLU, Rectified Linear Unit, which is, again, in

**[07:01 -> 07:06]** our standard kind of activation function that we use to introduce non-linearity.

**[07:06 -> 07:08]** and then we get our output.

**[07:08 -> 07:13]** And so we repeat then this logic for multiple stages.

**[07:14 -> 07:17]** As you see the again, number of filters

**[07:17 -> 07:20]** define the depth of the output.

**[07:20 -> 07:22]** Then in this second step,

**[07:22 -> 07:24]** here we decide to still keep the dimensionality

**[07:24 -> 07:26]** of the filter five by five,

**[07:26 -> 07:28]** but of course you can adapt the depth.

**[07:28 -> 07:32]** So now the filter at this stage should be of that six.

**[07:32 -> 07:35]** And if we decide to have 10 of these filters,

**[07:35 -> 07:38]** than the depth of the output would be 10.

**[07:41 -> 07:44]** So yeah, so this is what's happening.

**[07:44 -> 07:46]** And as we said, once the model is trained

**[07:47 -> 07:51]** or a specific task like classification of 1000 classes,

**[07:51 -> 07:54]** we can go back and look inside of these filters.

**[07:54 -> 07:57]** So what is the content of these filters?

**[07:57 -> 08:01]** They are the parameters that the model should learn, right?

**[08:01 -> 08:04]** So you remember we are doing this pass through the network

**[08:04 -> 08:08]** and then back propagation of data,

**[08:08 -> 08:09]** the parameters of the network, right?

**[08:09 -> 08:11]** So this is the training phase.

**[08:11 -> 08:13]** And what we are doing in this training phase

**[08:13 -> 08:17]** is that we are filling in the content of this filter.

**[08:17 -> 08:21]** So the value of this W and this B is what we learn.

**[08:21 -> 08:23]** At the beginning, they are initialized randomly.

**[08:23 -> 08:26]** Let's say, let's suppose they're initialized randomly.

**[08:26 -> 08:28]** And then progressively with the training of the model

**[08:28 -> 08:31]** and minimizing the loss function,

**[08:31 -> 08:33]** the content of these filters will be filled in

**[08:33 -> 08:37]** with new numbers, they will be progressively adopted.

**[08:37 -> 08:39]** And then what we can do at the end of the training

**[08:39 -> 08:43]** is then look back at what is the content of this filter

**[08:43 -> 08:45]** and we can visualize them, especially at the beginning

**[08:45 -> 08:47]** because they are really, I mean, they are images

**[08:47 -> 08:49]** that we can visualize at the RGB

**[08:49 -> 08:51]** because they live in the same, let's say,

**[08:51 -> 08:53]** they have the same depth of the input.

**[08:53 -> 08:56]** So we can look at them and we see that this is the kind

**[08:56 -> 08:58]** of thing that the network has learned.

**[08:58 -> 09:00]** And so this is what we started from.

**[09:00 -> 09:08]** Okay, so whenever we decide this kind of layer, we design this layer, what do we have to choose?

**[09:08 -> 09:11]** We have to choose the dimensionality of the filter, right?

**[09:11 -> 09:15]** So in this case, for instance, three by three.

**[09:15 -> 09:19]** But besides the dimensionality, we also have to decide the stride, right?

**[09:19 -> 09:25]** So the kind of the way in which we move the filter and the stride in this case is just

**[09:25 -> 09:26]** one.

**[09:26 -> 09:27]** So one pixel at a time.

**[09:27 -> 09:29]** We move it one pixel at a time.

**[09:29 -> 09:31]** And it's the size of the dimensionality of the output.

**[09:31 -> 09:35]** So in this case, we start from 7 by 7.

**[09:35 -> 09:37]** We use a kernel 3 by 3.

**[09:37 -> 09:44]** And since we have five steps with stride 1, then we repeat this logic both horizontally

**[09:44 -> 09:45]** and vertically.

**[09:45 -> 09:47]** And we have output 5 by 5.

**[09:47 -> 09:52]** There is a general formula to get to the output, let's say, spatial extension.

**[09:52 -> 09:55]** N is the dimensionality of the input.

**[09:55 -> 09:59]** F is the dimensionality of the kernel divided by the stride.

**[09:59 -> 10:02]** So in this case, one and everything plus one,

**[10:02 -> 10:04]** and this provides us with the dimensionality

**[10:04 -> 10:05]** of the output.

**[10:06 -> 10:09]** So what we have is that per se,

**[10:09 -> 10:13]** this procedure allows to reduce the dimensionality, right?

**[10:13 -> 10:15]** Progressively, if we started as in the case

**[10:15 -> 10:18]** we were looking at before, so seven by seven,

**[10:18 -> 10:22]** it will become a five by five and so on and so forth.

**[10:22 -> 10:24]** The basis of our choice of the stride

**[10:24 -> 10:26]** and of the dimensionality of the kernel,

**[10:26 -> 10:28]** what we have is that the feature map

**[10:28 -> 10:37]** to have usually a smaller dimensionality in terms of spatial extension, so from 7 to 7 to 5 by 5,

**[10:37 -> 10:42]** but usually what happens is that the depth increases and you remember the depth depends

**[10:42 -> 10:49]** on how many filters we used. So, spatially it shrinks, the depth usually instead increases.

**[10:50 -> 10:56]** If we have stride 2, we see that we get to a 3 by 3 output, but there are some cases in which

**[10:56 -> 11:02]** Of course, the choice is not a good one. So for instance, stride 3, well, we cannot move this

**[11:02 -> 11:10]** window 3x3 of step 3 times, I mean, of 3 pixels, because, okay, we can do it once, but then the

**[11:10 -> 11:16]** second time we do it, the windows get out from the original input, so it doesn't fit. We cannot apply

**[11:16 -> 11:23]** a 3x3 filter on this kind of output, on this kind of input. Indeed, I mean, this number is not an

**[11:23 -> 11:29]** an integer anymore. And so what we can do is that, of course, we can change, I mean,

**[11:29 -> 11:36]** choose properly the stride to avoid these kind of cases, or we can decide to add what

**[11:36 -> 11:42]** is called zero padding, so a frame around the input, which is usually filled in with

**[11:42 -> 11:52]** zeros. And these allow me to also keep the original dimensionality. So by playing with

**[11:52 -> 11:53]** the dimensionality of the kernel,

**[11:53 -> 11:55]** the dimensionality of the input,

**[11:55 -> 11:57]** the stride and the padding,

**[11:57 -> 11:59]** I might be able to keep the dimensionality

**[11:59 -> 12:01]** of the feature map in terms of

**[12:01 -> 12:03]** partial extension equal to the input.

**[12:03 -> 12:05]** So if I had seven by seven,

**[12:05 -> 12:07]** by playing a bit with these parameters,

**[12:07 -> 12:09]** specifically they are not parameters,

**[12:09 -> 12:12]** they are hyper parameters, okay?

**[12:12 -> 12:14]** I can decide to have an output,

**[12:14 -> 12:18]** I will be able to have an output still a seven by seven,

**[12:18 -> 12:20]** let's say dimensionality in terms of

**[12:20 -> 12:22]** feature map, spatial extension.

**[12:22 -> 12:27]** So let me be clear on this point.

**[12:27 -> 12:31]** What the network is learning is the content of the filter.

**[12:31 -> 12:35]** So what will be inside of the kernel?

**[12:35 -> 12:37]** So the W values and the B,

**[12:37 -> 12:42]** while instead the dimensionality of the kernel,

**[12:42 -> 12:46]** the stride and the dimensionality of the padding

**[12:46 -> 12:48]** are hyperparameters.

**[12:48 -> 12:51]** So are things that I choose by hand,

**[12:51 -> 12:53]** I can of course change them,

**[12:53 -> 12:54]** but it's not something that I let,

**[12:54 -> 12:57]** I'm letting the network to optimize.

**[12:57 -> 13:00]** It's not the network optimizes this information,

**[13:00 -> 13:03]** it's me that I'm the designer of the network

**[13:03 -> 13:07]** that I'm deciding on stride,

**[13:07 -> 13:10]** padding and the mesh variety of the person.

**[13:11 -> 13:12]** Okay?

**[13:12 -> 13:13]** So in this case,

**[13:13 -> 13:16]** if I start from a mesh variety of the input,

**[13:16 -> 13:19]** which was seven by seven, and I use a three by three filter

**[13:19 -> 13:23]** with stride one and pad one, okay,

**[13:23 -> 13:25]** pad in one and zero pad in one,

**[13:25 -> 13:27]** then I have a seven by seven output.

**[13:30 -> 13:32]** Okay, so I have a question in the chat.

**[13:32 -> 13:33]** Yes, I mean, the question is about the fact

**[13:33 -> 13:38]** that we are dealing with squared inputs, right?

**[13:38 -> 13:40]** It's always a square, it's always n by n

**[13:40 -> 13:43]** or I mean, seven by seven, five by five.

**[13:43 -> 13:45]** And the answer is yes, I mean,

**[13:45 -> 13:51]** it's a convention, the network are able to manage squared input.

**[13:52 -> 13:58]** So generally what happens is that you take sub crops of your image, of your larger image,

**[13:58 -> 14:07]** or you say deform a bit the image properly to stay in a square. But this is this was, let's say,

**[14:07 -> 14:14]** somehow the historical strategy, how the backbone have been developed with this squared kind of

**[14:14 -> 14:19]** input, then I mean there are also version of network that are able to manage, I mean not

**[14:20 -> 14:25]** input with different dimensionality, but we will keep the standard so we'll manage

**[14:26 -> 14:31]** squared inputs. So I should be able, I should have answered the question.

**[14:33 -> 14:37]** Yeah, of course. Yeah, so we can apply some preprocessing technique to obtain

**[14:38 -> 14:43]** a squared input, right? So you can also decide if you have a large image just crop

**[14:43 -> 14:54]** in subparts which are squared. Okay, you can work the image, you can deform it a bit to stay in

**[14:55 -> 15:02]** squared shape. So usually there are some, let's say, standard choices in terms of the,

**[15:03 -> 15:10]** these hyper parameters that we described. So we can have, for instance, three by three kernels

**[15:10 -> 15:16]** with zero padding of one or five by five with zero padding of two or seven by seven with zero padding

**[15:16 -> 15:25]** three. Now remember that when I say zero padding one now okay so I'm referring to the fact that

**[15:25 -> 15:34]** I have a frame which is just one set of zeros but the truth is that you are adding two columns

**[15:34 -> 15:41]** and two rows, right, it's doubled. So it's called a padding of one, but when you look

**[15:41 -> 15:46]** at the matrix what's happening here is that we are adding two columns and two rows.

**[15:48 -> 15:54]** Okay, it's possible that I updated a bit, I mean I added some slides with respect to what you have,

**[15:54 -> 16:01]** but I will update also the PDF, sorry I did it yesterday quite late, just to,

**[16:01 -> 16:08]** to, it's only a few more figures to explain better some of the concepts that were already

**[16:08 -> 16:18]** there. So receptive field, what is a receptive field? So when we look at the multilayer perceptrons,

**[16:18 -> 16:26]** so a neural network, not a convolutional network, just composed of fully connected layers, what

**[16:26 -> 16:30]** we have is that every element, I mean, the hidden layers that

**[16:30 -> 16:34]** depends on the input actually depends on all the, right, so we

**[16:34 -> 16:37]** have this full connections. So every one of these points

**[16:37 -> 16:42]** depends on all of them. And then have a realism linearity and

**[16:42 -> 16:48]** then have a next layer. But then again, so there's this full

**[16:48 -> 16:54]** dependence on the previous layer in the linear part. And in this

**[16:54 -> 16:58]** case, I mean, what is the receptive field? So in general, the receptive field of a neuron

**[16:58 -> 17:05]** refers to the portion of the input seen by that neuron. So this neuron here depends on all the

**[17:06 -> 17:11]** points you had, all the neurons you had in the input. So that's the definition of the receptive field.

**[17:12 -> 17:17]** And when we deal instead with the convolutional network, as already we discussed, I mean, in the

**[17:17 -> 17:26]** nature of this using the filters and the logic of the convolution itself, every element in a hidden

**[17:26 -> 17:32]** layer actually does not depend on all the elements in the previous layer on the input layer, right?

**[17:32 -> 17:36]** It depends only on a subset, which is exactly the region that the filter is looking at.

**[17:37 -> 17:44]** So in this case it will depend on a sub portion, so not the raw input but just the sub part. So

**[17:44 -> 17:53]** So in CNN, in convolutional network, anyone only sees a portion of the previous layer.

**[17:53 -> 17:59]** And of course, the deeper you go, the larger is the region of the input that you have seen.

**[17:59 -> 18:04]** And you remember that I mentioned that the more you go in depth into the network, the

**[18:04 -> 18:06]** more it's like you are zooming out.

**[18:06 -> 18:08]** So at the beginning, you look at a very small region.

**[18:08 -> 18:14]** The filter looks at only, I mean, three by three, for instance, region with a filter.

**[18:14 -> 18:18]** But then the end, and this output here depends only on three elements.

**[18:18 -> 18:22]** Then you have reloop, but then when you pass through the next layer, in practice, every

**[18:22 -> 18:28]** of these single elements, if you go back to the inputs, it has seen a larger region, right?

**[18:28 -> 18:33]** Because it's combining information from more elements in this layer here.

**[18:33 -> 18:37]** But these were, these three, let's say, were already summarizing information coming from

**[18:37 -> 18:40]** five of the elements of the input.

**[18:40 -> 18:44]** So the receptive field, you can consider it, I mean, from one layer to the other layer

**[18:44 -> 18:45]** is just the dimensionality of the kernel.

**[18:45 -> 18:51]** So the region that the kernel itself was looking at, but the more you go inside the network,

**[18:51 -> 18:55]** the larger is actually, I mean, the receptive field of this ending layer with respect to

**[18:55 -> 18:59]** the input is a larger region.

**[18:59 -> 19:01]** It should be quite clear.

**[19:01 -> 19:07]** And then we can look at it in this, let's say, figure where we have also the spatial

**[19:07 -> 19:15]** dimensionality exactly with the filters we were referring to. So yeah, here it is called kernel

**[19:15 -> 19:20]** and we have seen that also in some of the previous slides I was using the word kernel,

**[19:20 -> 19:25]** but it's not a name with respect to filters, but it's referring to the same thing.

**[19:28 -> 19:37]** And yeah, so this element of the output depends on a 3x3 region. So the receptive field of this

**[19:37 -> 19:40]** is the region, the portion of the input,

**[19:40 -> 19:44]** from which that output depends.

**[19:45 -> 19:50]** So now when you consider the whole stack of layers,

**[19:50 -> 19:54]** you see that this output here is actually looking

**[19:54 -> 19:57]** at the whole seven by seven input.

**[19:57 -> 19:59]** That's summarizing information coming

**[19:59 -> 20:01]** from all the seven by seven input.

**[20:02 -> 20:06]** So at each successive, I mean, successive convolution,

**[20:06 -> 20:11]** we are adding the K minus one to the receptive field size.

**[20:11 -> 20:14]** So the region that we're looking is growing.

**[20:14 -> 20:16]** And so the overall at the end, if we have L layers,

**[20:16 -> 20:20]** it will be the region that this one have looked at

**[20:20 -> 20:23]** is one plus the number of layers multiplied by K minus one

**[20:23 -> 20:27]** where K is the dimensional ideal of the kernel.

**[20:29 -> 20:31]** Now question.

**[20:33 -> 20:36]** So you see here, you have the input.

**[20:36 -> 20:39]** And then the output is producing a value,

**[20:39 -> 20:43]** but I mean, we are touching the border of the input.

**[20:43 -> 20:46]** And then the output of these gets here.

**[20:46 -> 20:48]** Why it does not get here?

**[20:50 -> 20:51]** So look at this figure, right?

**[20:51 -> 20:54]** So we have taken, you're taking the input,

**[20:54 -> 20:56]** we are convolving,

**[20:56 -> 21:00]** and this appears to be the very first step you will do,

**[21:00 -> 21:00]** right?

**[21:00 -> 21:03]** So you take the filters, you put it at the top left,

**[21:03 -> 21:05]** but then the output gets here.

**[21:05 -> 21:07]** why it doesn't get here.

**[21:07 -> 21:08]** Yes.

**[21:08 -> 21:09]** We don't have found.

**[21:09 -> 21:10]** Yeah, we are not visualizing it,

**[21:10 -> 21:13]** but the hypothesis is that there is a padding there.

**[21:13 -> 21:16]** So the real first step is a little bit more

**[21:16 -> 21:19]** on the top left part, right?

**[21:19 -> 21:22]** So the very first step of this positioning

**[21:22 -> 21:24]** of this orange square, the orange filter

**[21:24 -> 21:27]** is a little bit more on the upper,

**[21:27 -> 21:29]** let's say external side,

**[21:29 -> 21:31]** which means that that was the very first step.

**[21:31 -> 21:33]** And now when you use the padding,

**[21:33 -> 21:35]** the very first output would be there.

**[21:35 -> 21:37]** So here I'm just taking, let's say a partial part

**[21:37 -> 21:39]** of the whole visualization.

**[21:39 -> 21:41]** So I'm not visualizing the padding

**[21:41 -> 21:42]** that we are actually using.

**[21:44 -> 21:48]** Okay, then of course, I mean, you can refer

**[21:48 -> 21:51]** to receptive field just the previous layers

**[21:51 -> 21:54]** or what inner neuron is looking at with respect

**[21:54 -> 21:56]** to this layer or you can have the receptive field

**[21:56 -> 21:57]** of the whole stack.

**[21:57 -> 22:00]** And then yeah, so depending on the context,

**[22:00 -> 22:02]** usually when you read the paper, you understand

**[22:02 -> 22:04]** what it is referring to.

**[22:07 -> 22:12]** Now, as you see here, considering this rule,

**[22:14 -> 22:19]** we might need a lot of layers to be able to have an output

**[22:19 -> 22:21]** that an element in the output that is really looking

**[22:21 -> 22:24]** at the whole input that we provided.

**[22:25 -> 22:30]** So actually what we did was introducing the padding

**[22:30 -> 22:35]** the bad thing to avoid that the information

**[22:35 -> 22:38]** inside the network shrinks too fast.

**[22:38 -> 22:43]** But at the same time, yeah, so we might need a lot of layers

**[22:43 -> 22:46]** then to be able to elaborate over all the semantic

**[22:46 -> 22:50]** information, all the content of the input itself.

**[22:50 -> 22:53]** So we might, we need to find the right trade off.

**[22:54 -> 22:57]** And so make sure that we also have some downsampling

**[22:57 -> 22:58]** inside the network.

**[22:58 -> 23:03]** And so there are different ways to do that.

**[23:03 -> 23:07]** And we said that we can have a pulley.

**[23:07 -> 23:09]** You already mentioned about the pulley.

**[23:11 -> 23:14]** So yeah, so this is just to say that, of course,

**[23:14 -> 23:16]** you want to keep the dimensionality in some cases,

**[23:16 -> 23:18]** but you don't want your net,

**[23:18 -> 23:20]** and you don't want your net to shrink too fast,

**[23:20 -> 23:21]** but at the same time,

**[23:21 -> 23:23]** you don't want to keep the dimensionality of the input

**[23:23 -> 23:25]** for too long.

**[23:25 -> 23:27]** Otherwise, we are not able to summarize the information

**[23:27 -> 23:37]** the full image towards the end of the network. Now filters, still now we have seen filters

**[23:37 -> 23:42]** always are dimensional, three by three, five by five, so they have a reasonable extension

**[23:42 -> 23:48]** in terms of pixels, let's call it like them, like these, right? But we can also have a

**[23:48 -> 23:54]** filter of dimensional IT one by one. So just let's say in respect to the input covering

**[23:54 -> 24:02]** one pixel. What does it mean? It seems strange, right, because we have said that we want to look

**[24:02 -> 24:07]** at the region, but now we are restricting especially the region at one single pixel with respect to the

**[24:07 -> 24:15]** input. But these kind of convolutional filters, they still make sense. They have a specific reason

**[24:15 -> 24:21]** to be used. And what is the reason? Well, when I have this kind of input like this, so we are

**[24:21 -> 24:29]** in the middle of the network, right? And at a certain point, my feature map ends up to this

**[24:29 -> 24:37]** size. So it's a tensor of dimensions of 56 by 56 with depth 64. So now I can use a convolutional

**[24:37 -> 24:43]** filter, which is just one by one. So let's say that it's look at just one single pixel in terms of

**[24:43 -> 24:50]** dimension with respect to the 56 by 56, we looked at just one. But we will have, I mean, as we said

**[24:50 -> 24:58]** before, the convolutional filter has the same depth of the input. So it will be 1 by 1 by 64.

**[25:01 -> 25:07]** And this will produce one value when you apply it on the input. Now, depending on the number

**[25:07 -> 25:15]** of filters of this kind that I use, I know that this will guide the depth of the output. So if

**[25:15 -> 25:18]** if I use one by one by 64 filter

**[25:18 -> 25:21]** and I decide to use 32 of them,

**[25:21 -> 25:23]** this will be the output that I get.

**[25:23 -> 25:27]** So in particular, the depth would be 32 by 32.

**[25:27 -> 25:29]** The spatial dimensionality in this case,

**[25:29 -> 25:31]** in terms of spatial extension, so the 56,

**[25:31 -> 25:33]** where the 56 remains the same.

**[25:33 -> 25:36]** So why I would use this?

**[25:36 -> 25:39]** Well, because it's indeed it's reducing the depth.

**[25:39 -> 25:42]** So I might need in some cases,

**[25:42 -> 25:48]** might want to shrink a bit the depth of the network, I mean, of that particular feature

**[25:48 -> 25:53]** map, then I don't know, make an operation that otherwise would be very costly, and then

**[25:53 -> 25:59]** possibly I can get back to the original dimension. So I can use this one by one convolution of

**[25:59 -> 26:05]** 32 filters, and then I do my, let's say, costly operation, and then I will have another stage

**[26:05 -> 26:12]** of one by one convolutional filters of dimension, maybe 32 words, or in this case, I have to

**[26:12 -> 26:13]** to the dimension that they have,

**[26:13 -> 26:17]** and for which I decide to have 64 of them.

**[26:17 -> 26:21]** And so I bring back the dimensionality to that 64.

**[26:22 -> 26:25]** So it might seem strange,

**[26:25 -> 26:28]** but the use of convolutional filters

**[26:28 -> 26:30]** of spatial dimension one by one,

**[26:30 -> 26:32]** they are relevant.

**[26:33 -> 26:36]** And the trick is just on the basis of

**[26:36 -> 26:38]** how many of them you use,

**[26:38 -> 26:41]** because this will guide the depth of your output.

**[26:44 -> 26:48]** Okay, so this is just again,

**[26:48 -> 26:51]** a little bit of application of the formulas, let's say.

**[26:51 -> 26:56]** So I have an input dimension, which is 32 by 32 by three.

**[26:56 -> 27:00]** I decide to apply filters of dimensionality five by five,

**[27:00 -> 27:05]** 10 of them with stride one and padding two.

**[27:05 -> 27:09]** So what will be the output of the volume?

**[27:14 -> 27:17]** Okay, sorry, I'm just reading one of the question,

**[27:17 -> 27:20]** which is okay, yeah, the candles filter

**[27:20 -> 27:22]** can be used to come back to the regional depth.

**[27:22 -> 27:24]** Yes, is exactly what I said before, right?

**[27:24 -> 27:28]** So you can have one step where you reduce

**[27:28 -> 27:30]** the dimensionality in terms of depth,

**[27:30 -> 27:32]** and then you can have another time.

**[27:32 -> 27:37]** So you apply your possibly complex operation

**[27:39 -> 27:41]** that you don't want to spend too much,

**[27:41 -> 27:43]** let's say might cost too much.

**[27:43 -> 27:47]** So you run it on this lower dimensionality, okay.

**[27:47 -> 27:50]** And then you can reuse the one by one convolution

**[27:50 -> 27:53]** to bring back to the original 64 depth.

**[27:53 -> 27:57]** So I think I answered the question.

**[27:57 -> 27:59]** So sorry about jumping back,

**[27:59 -> 28:02]** but there was a question on this.

**[28:03 -> 28:06]** Okay, so we were looking at this

**[28:06 -> 28:11]** and we were just applying the formula, right?

**[28:11 -> 28:14]** So I'm using the formula, so 32 by 32,

**[28:14 -> 28:17]** which is the regional dimensionality.

**[28:17 -> 28:21]** So now, as we said, we're using padding two, right?

**[28:22 -> 28:26]** And so padding two means that we are actually adding

**[28:26 -> 28:31]** four columns and four rows.

**[28:31 -> 28:36]** So you are taking these two and you are doubling it.

**[28:36 -> 28:42]** And these 32 plus four will be the new dimensionality of your input,

**[28:42 -> 28:45]** because you are using the pattern.

**[28:45 -> 28:50]** And then since you are applying your filter, which is 5 by 5, so minus 5,

**[28:50 -> 28:55]** divided by the stride, which is 1 plus 1, and so we have that specially we keep

**[28:55 -> 28:59]** the original dimension ID 32 by 32.

**[28:59 -> 29:02]** And since we have 10 filters, then we have 10 of them.

**[29:02 -> 29:03]** The depth will be 10.

**[29:08 -> 29:09]** Right?

**[29:09 -> 29:12]** So how many parameters do we have for this layer?

**[29:13 -> 29:17]** Well, each filter is five by five by three plus one.

**[29:17 -> 29:20]** What is this plus one is the bias, right?

**[29:20 -> 29:24]** So each filter contains the W value, right?

**[29:24 -> 29:26]** So which are the one that you are trying to learn, right?

**[29:26 -> 29:28]** So there are really the parameters

**[29:28 -> 29:29]** that you're trying to optimize.

**[29:29 -> 29:33]** So inside these filters, there are five by five

**[29:33 -> 29:36]** by three values plus you have to consider also the B,

**[29:36 -> 29:37]** so the bias.

**[29:37 -> 29:40]** So overall you have 76 parameters.

**[29:40 -> 29:44]** And since you have 10 filters, then it is 76 by 10.

**[29:44 -> 29:48]** So 760, right?

**[29:48 -> 29:58]** Now, how many operations I'm performing? And this will be relevant because one way to measure,

**[29:58 -> 30:05]** let's say, the cost of your network is considering the floating point operation. We will see

**[30:05 -> 30:11]** it later on. They're called FLOPS, floating point operation, which in practice, as you

**[30:11 -> 30:17]** see, I mean, in this, most of the operation happens in the linear part, right? And what

**[30:17 -> 30:24]** are doing are multiplication sums, nothing more than that. So now how do we count the operations?

**[30:24 -> 30:31]** Well, let's look at the output in this particular case. So we produce something which is, as we said,

**[30:33 -> 30:42]** 32 by 32 by 10, right? So we said it in this previous thing here. So we said that we used

**[30:42 -> 30:50]** as output. So the output will be a tensor or dimension 32 by 32 by 10. So this is our output.

**[30:50 -> 30:59]** Okay, so globally this is the number of values that we have in the output and each of them

**[31:00 -> 31:11]** was obtained by an inner product of the filter with the input. So each of them, each values of

**[31:11 -> 31:14]** of the output are obtained by these operations,

**[31:14 -> 31:19]** which practically are five by five by three multiplication

**[31:21 -> 31:23]** plus a sum of everything.

**[31:23 -> 31:27]** So every one of the values that we get as the output

**[31:27 -> 31:31]** costed 75 multiplication in practice.

**[31:31 -> 31:36]** So the addition does not really cost that much, let's say.

**[31:36 -> 31:39]** So overall, this is the number of operation

**[31:39 -> 31:44]** that we are considering, which is 700k.

**[31:47 -> 31:49]** Okay, so here there is a sort of summary

**[31:49 -> 31:51]** about all the formulas that we mentioned.

**[31:51 -> 31:55]** Look that here the padding is always doubled, right?

**[31:55 -> 31:57]** Twice the padding.

**[31:57 -> 31:59]** Yeah, so here is the find the dimensionality,

**[31:59 -> 32:02]** the kernels, partial extent of the filter,

**[32:02 -> 32:04]** the number of filters in this case k,

**[32:04 -> 32:06]** the stride is s and so on and so forth.

**[32:06 -> 32:11]** And so it's just a summary of the formulas that we saw.

**[32:11 -> 32:15]** And as we said, there are some standard choices

**[32:15 -> 32:17]** in these parameters in terms of the dimensionality

**[32:17 -> 32:18]** of the kernel, the side-departing,

**[32:18 -> 32:21]** these are just conventional kind of choices

**[32:21 -> 32:22]** that one can take.

**[32:26 -> 32:30]** Now, as we said, we also want to make sure

**[32:30 -> 32:34]** that we have a tool or strategy to reduce the dimensionality

**[32:34 -> 32:37]** of the feature map inside the network

**[32:37 -> 32:39]** to avoid that our network explodes

**[32:39 -> 32:42]** in terms of number of parameters that it has to image.

**[32:44 -> 32:47]** So one thing that we can do is apply pooling,

**[32:48 -> 32:50]** which is indeed exactly a sort of downsampling

**[32:50 -> 32:55]** of the information that we had on the previous input.

**[32:57 -> 32:59]** How does it work pooling?

**[32:59 -> 33:01]** So even in the case of pooling,

**[33:01 -> 33:04]** you have some hyper parameters that you have to choose,

**[33:04 -> 33:07]** like the dimension of the window that I have to look at,

**[33:07 -> 33:10]** which I still can call it kernel size, okay?

**[33:10 -> 33:12]** The size of the kernel, the window, the stride,

**[33:12 -> 33:14]** so how I move this window,

**[33:14 -> 33:15]** and then the pooling function

**[33:15 -> 33:19]** that I execute inside of this window.

**[33:19 -> 33:23]** It can be max pooling, it can be average pooling, or others.

**[33:25 -> 33:28]** Usually these two are the most common one.

**[33:28 -> 33:29]** And what we are doing here,

**[33:29 -> 33:31]** so the pooling is actually already introducing

**[33:31 -> 33:33]** a little bit of nonlinearity.

**[33:34 -> 33:40]** So it's somehow a nonlinear function which is applied on the local window.

**[33:40 -> 33:45]** So in the case of max folding, just look at what was happening.

**[33:45 -> 33:49]** As we said, in this case, we are choosing a filter of dimension two by two,

**[33:49 -> 33:53]** and we decide to apply it with stride two, right?

**[33:53 -> 33:59]** So we have these windows, and we take the maximum out of it.

**[33:59 -> 34:01]** So like six here.

**[34:01 -> 34:07]** And for this other figure, for this other part of the image, we take the eight and so on and so forth.

**[34:07 -> 34:16]** So this strategy, besides squeezing the dimensional idea of the input, it also introduces a bit of invariance.

**[34:16 -> 34:23]** Because you can imagine that if you take a photo, right, of natural scene, let's say,

**[34:23 -> 34:28]** and you take it also once on the left or once on the right or top or bottom,

**[34:28 -> 34:31]** I mean, when you go to take the average of more or less,

**[34:31 -> 34:33]** that region does not change that much, right?

**[34:33 -> 34:37]** So it's also introducing invariance in terms of shift,

**[34:37 -> 34:40]** spatial shift with respect to what we are looking at.

**[34:42 -> 34:47]** Now, despite the logic of functioning of these pooling

**[34:48 -> 34:53]** in terms of using the kernel and the stride,

**[34:53 -> 35:02]** So not usually, pooling by definition does not have any learnable parameters.

**[35:02 -> 35:10]** So when we apply the filter, the kernel that we are looking at for the convolutional layer,

**[35:10 -> 35:16]** what we are searching for is the contents, so the w inside the filter, which then has

**[35:16 -> 35:19]** to be multiplied with the input.

**[35:19 -> 35:22]** for the pooling, we don't have learnable parameters.

**[35:22 -> 35:26]** We're just taking a region and just applying an operation,

**[35:26 -> 35:29]** which tells us just take the maximum.

**[35:29 -> 35:32]** There are no learnable parameters here.

**[35:32 -> 35:34]** There are hyper parameters, although,

**[35:34 -> 35:37]** which are these choices.

**[35:37 -> 35:39]** The hyper parameters in this case

**[35:39 -> 35:41]** are still choices you have to make, right?

**[35:41 -> 35:44]** But no learnable parameters.

**[35:46 -> 35:47]** Okay.

**[35:47 -> 35:48]** Now there are different ways

**[35:48 -> 35:59]** which you can apply the pooling. This is what we were looking at. So for every channel of your,

**[35:59 -> 36:04]** I mean, for every element in the depth of your tensor, you look at the, let's say,

**[36:06 -> 36:11]** region of your filter, and then you take maximum or average, right? So this would be what we have

**[36:11 -> 36:18]** seen till now. But there are also other kind of strategies where rather than pooling, let's

**[36:18 -> 36:24]** say, a non-spatial region, you can also pool at the channel level. So you just look along

**[36:24 -> 36:31]** the channel and you sub-sample, let's say, the radio rather than doing it in a spatial way.

**[36:32 -> 36:37]** So there are different ways in which you can apply pooling depending on what, let's say,

**[36:37 -> 36:41]** what is the condition that you really want to, the dimension that you really want to shrink.

**[36:41 -> 36:45]** And this depends on which kind of operation you are going to apply next.

**[36:45 -> 36:53]** So depending on the architecture that you're building, there are different kinds of coding you can decide to use.

**[36:53 -> 37:06]** Yeah, and these, of course, introduce a little bit of, say, again, a sort of invariance, but in this case, it's an invariance with respect to what each filter was performing.

**[37:06 -> 37:13]** Right, so you remember each filter, when you look back after the training of the old network,

**[37:13 -> 37:19]** each filter had a specific role, right? You remember either highlighting some, I don't know,

**[37:19 -> 37:25]** 45 degree edge or blob of colors, such that when those filters are applied on the image,

**[37:25 -> 37:32]** they tend to highlight exactly those kind of pattern in the input, from the input. And so,

**[37:32 -> 37:39]** So when you use, I don't know, in this case, three, six, eight filters, you expect that

**[37:39 -> 37:44]** and you obtain a depth of dimension eight, you expected that each filter was highlighting

**[37:44 -> 37:48]** one particular characteristic out of the origin input, right?

**[37:48 -> 37:55]** And then if you pull like this, you are saying that you are somehow summarizing information

**[37:55 -> 37:56]** over the filters.

**[37:56 -> 38:01]** So you tend to be a little bit more invariant with respect to, for instance, if you had

**[38:01 -> 38:06]** filters that were looking at different orientational badges, then you end up with something that is

**[38:06 -> 38:12]** summarizing on all the orientation. So it's a different kind of way of summarizing information,

**[38:12 -> 38:18]** right? So either especially or in terms of what each filter was performing over the input,

**[38:19 -> 38:23]** right? So this is what this sentence is telling you here.

**[38:25 -> 38:31]** And there is also another kind of pooling, which is just global average pooling or global

**[38:31 -> 38:35]** of max pooling, where this can be very helpful

**[38:35 -> 38:37]** when you really want to summarize information

**[38:37 -> 38:40]** and a lot of information of one single step.

**[38:40 -> 38:41]** So you take everything

**[38:41 -> 38:43]** and just take the maximum or the average.

**[38:43 -> 38:46]** And we will see later on that this is a strategy

**[38:46 -> 38:49]** that you can use towards the end of the network

**[38:49 -> 38:52]** where sometimes you want to reduce the number

**[38:52 -> 38:55]** of fully connected layers that you apply.

**[38:55 -> 38:59]** Because as we said, the network usually what you see

**[38:59 -> 39:03]** is that you have some convolutional layers

**[39:03 -> 39:05]** at the beginning to extract the features

**[39:05 -> 39:08]** and then fully connected layers at the end.

**[39:08 -> 39:12]** And usually you have more than one fully connected layer

**[39:12 -> 39:14]** which elaborate on the classification

**[39:14 -> 39:16]** or the regression tasks you want to do.

**[39:16 -> 39:19]** But sometimes you want to reduce this number of filters.

**[39:19 -> 39:21]** You want to use just one fully connected layer.

**[39:21 -> 39:25]** And so you need somehow to speed up the squeezing

**[39:25 -> 39:27]** of the information from the convolutional layer

**[39:27 -> 39:28]** then provides you with a tensor,

**[39:28 -> 39:31]** which is usually quite rich of information.

**[39:31 -> 39:34]** So it's quite big, especially quite deep, let's say.

**[39:34 -> 39:36]** So it's a lot of channels.

**[39:36 -> 39:38]** To something that can be elaborated

**[39:38 -> 39:40]** by a fully connected layer.

**[39:40 -> 39:43]** Fully connected layer only take as input vectors, right?

**[39:43 -> 39:45]** So you have to squeeze the information

**[39:45 -> 39:46]** somehow in a long vector,

**[39:46 -> 39:48]** flutter the information and provide it

**[39:48 -> 39:50]** to a fully connected layer.

**[39:50 -> 39:52]** So sometimes rather than passing through multiple

**[39:52 -> 39:54]** fully connected layer, you decide to apply

**[39:54 -> 39:59]** just a global pooling over each channel, for instance,

**[39:59 -> 40:02]** such that the information is then quickly squeezed

**[40:02 -> 40:04]** into a long vector, which can be elaborated

**[40:04 -> 40:05]** by philanthropy.

**[40:05 -> 40:08]** So you can just have a global pooling,

**[40:08 -> 40:11]** which can be global max or global average.

**[40:12 -> 40:14]** Okay, so even in this case,

**[40:14 -> 40:17]** you can have some common setting

**[40:17 -> 40:19]** in terms of dimensionality of the kernel,

**[40:19 -> 40:22]** which is the window in this case that you're looking at

**[40:22 -> 40:24]** to take the maximum or the average.

**[40:24 -> 40:26]** and also the stride.

**[40:26 -> 40:28]** Zero padding is not super, let's say used,

**[40:28 -> 40:32]** but still you can think about adding also a zero padding

**[40:32 -> 40:33]** when you apply the pooling papers.

**[40:36 -> 40:38]** And this is the kind of output,

**[40:38 -> 40:40]** I mean the kind of architecture you would expect, right?

**[40:40 -> 40:43]** So convolution, which is the, let's say linear part,

**[40:43 -> 40:45]** nonlinearity of the convolution,

**[40:45 -> 40:48]** and from time to time you also introduce some pooling.

**[40:48 -> 40:50]** As we said, you need to somehow have a trade off

**[40:50 -> 40:53]** between the fact that you don't want to keep

**[40:53 -> 40:57]** higher dimensional, you want to squeeze somehow

**[40:57 -> 40:59]** the information inside the network,

**[40:59 -> 41:01]** but at the same time you don't want to do it too fast.

**[41:01 -> 41:05]** So yeah, of course you have specific choices

**[41:05 -> 41:08]** in terms of the kernel size of the convolutional layer

**[41:08 -> 41:10]** to do it properly.

**[41:10 -> 41:12]** And then you have your nonlinearity.

**[41:12 -> 41:15]** And at the end you have one or more fully connected layers

**[41:15 -> 41:19]** that will produce an output with SOAP, right?

**[41:19 -> 41:23]** So SOAP marks that tells me, provide me with a value,

**[41:23 -> 41:25]** each of them will represent,

**[41:25 -> 41:28]** they will try to mimic the behavior of a probability

**[41:28 -> 41:29]** for a certain class.

**[41:29 -> 41:30]** In the case of classification,

**[41:30 -> 41:34]** you would have what is called cross entropy loss,

**[41:34 -> 41:37]** your number, we saw it in previous lecture.

**[41:37 -> 41:39]** And the cross entropy loss in practice with softmax

**[41:39 -> 41:42]** is providing you a sort of a score

**[41:42 -> 41:45]** which tells you the probability of each class

**[41:45 -> 41:45]** that you have as output,

**[41:45 -> 41:48]** and you will have as many elements in the output,

**[41:48 -> 41:50]** as many classes you want to predict.

**[41:50 -> 41:53]** And so I just signed with the corresponding probability.

**[41:55 -> 41:59]** Okay, so this ends this part of this deck of slides.

**[41:59 -> 42:00]** So we'll pass to the next.

**[42:01 -> 42:03]** And in the meanwhile, if you have question,

**[42:03 -> 42:04]** just raise your hand.

**[42:20 -> 42:22]** you

**[42:50 -> 43:05]** Okay. No hands, no question in the chat. So let me see. Let's see. Go ahead. Okay. So

**[43:05 -> 43:16]** I don't know if you've already seen this. This is a video of Jan Lekan 1989 showing

**[43:16 -> 43:21]** how the first neural network was working

**[43:21 -> 43:24]** to recognize digits, handwritten digits.

**[43:24 -> 43:26]** Okay, so again, based on images.

**[43:26 -> 43:28]** So Yang-Lagand is this guy here.

**[43:28 -> 43:30]** Was probably, this is today,

**[43:30 -> 43:32]** and you saw it at the beginning of the video.

**[43:32 -> 43:35]** It was much younger back then.

**[43:35 -> 43:38]** And it was one of the strong believers in the fact

**[43:38 -> 43:40]** that neural network could work even better

**[43:40 -> 43:42]** with respect to support vector machine

**[43:42 -> 43:44]** and the shallow machine learning model.

**[43:44 -> 43:46]** And indeed at the end, it was right.

**[43:46 -> 43:49]** but it took 20 years to make it work.

**[43:50 -> 43:53]** So Chappeau to the persistence.

**[43:54 -> 43:57]** And indeed, I mean, everything is based on images, right?

**[43:57 -> 44:00]** So different handwritten digit ability to,

**[44:00 -> 44:04]** yeah, this guy here is him with his PhD

**[44:04 -> 44:07]** and post-it colleagues.

**[44:07 -> 44:10]** But yeah, I mean, this network was called,

**[44:10 -> 44:13]** I mean, that network was called the LENF1.

**[44:13 -> 44:18]** So a very, let's say, the modest way decided to call it

**[44:18 -> 44:22]** with his own name, Lecan, so it's a LeNet-1.

**[44:22 -> 44:24]** And then, I mean, what we're looking at here instead

**[44:24 -> 44:27]** is LeNet-5 that indeed is composed

**[44:27 -> 44:31]** of multiple convolutional layers.

**[44:31 -> 44:34]** And then at the end, you have the fully connected part.

**[44:34 -> 44:36]** And you see here that when passing

**[44:36 -> 44:39]** from the convolutional layer to the linear parts

**[44:39 -> 44:41]** or the fully connected part, what you do is

**[44:41 -> 44:45]** that you take your tensor here,

**[44:45 -> 44:47]** you have to flatten it into a vector

**[44:47 -> 44:50]** and then provide it as input to the fully connected layer,

**[44:50 -> 44:52]** which is what I was mentioning before, right?

**[44:52 -> 44:54]** So when passing from the convolutional part

**[44:54 -> 44:55]** to the fully connected part,

**[44:55 -> 44:59]** you have to translate this tensor into a vector.

**[45:02 -> 45:07]** And so yeah, usually what happens is that you see shrinks

**[45:07 -> 45:12]** in the spatial extension, the feature map shrinks,

**[45:13 -> 45:15]** but then it extends in terms of depth.

**[45:15 -> 45:17]** And so more or less you keep the volume.

**[45:17 -> 45:22]** So LENet5 because it has five convolutional layers

**[45:22 -> 45:24]** and here, I think I'm gonna report.

**[45:24 -> 45:28]** So five layers, not five convolutional, five layers in total.

**[45:28 -> 45:30]** And moreover here, you see that this network

**[45:30 -> 45:32]** is mentioned in RALUM.

**[45:32 -> 45:35]** So the activation function, non-linearity,

**[45:35 -> 45:38]** we have seen in the previous lecture.

**[45:38 -> 45:42]** But the truth is that the first LENET,

**[45:42 -> 45:45]** and also LENET, I mean, this you see,

**[45:45 -> 45:47]** this is already 10 years after, right?

**[45:47 -> 45:49]** With respect to what you saw before.

**[45:49 -> 45:52]** And so being able to combine multiple layers

**[45:53 -> 45:55]** already took quite some time.

**[45:55 -> 45:57]** And also the introduction of the RELO,

**[45:57 -> 45:59]** because at the beginning that was not

**[45:59 -> 46:01]** the activation function usually used.

**[46:01 -> 46:05]** It was a ton H, so a different activation function.

**[46:05 -> 46:07]** And indeed, to compose this network,

**[46:07 -> 46:09]** we need multiple ingredients.

**[46:09 -> 46:11]** It's not just the shape of, let's say,

**[46:11 -> 46:13]** the architecture of every single layer,

**[46:13 -> 46:15]** but also the choice in terms of

**[46:15 -> 46:18]** which activation function to use.

**[46:18 -> 46:19]** And there is also another ingredient.

**[46:19 -> 46:21]** I mean, we have seen fully connected layers,

**[46:21 -> 46:24]** we have seen convolutional layer, boolean layers,

**[46:24 -> 46:27]** but we would like to go a little bit in depth

**[46:27 -> 46:29]** with respect to these other two ingredients

**[46:29 -> 46:30]** that we didn't mention,

**[46:30 -> 46:33]** but we actually are quite relevant.

**[46:33 -> 46:35]** And moreover, if you look here,

**[46:35 -> 46:37]** here there's synonormalization.

**[46:37 -> 46:42]** Okay, so these ingredients here was not present back then.

**[46:42 -> 46:45]** And it is a more recent sort of choice

**[46:45 -> 46:49]** or it's a invention that has been introduced later on.

**[46:50 -> 46:52]** So let's start from the activation function

**[46:52 -> 46:55]** because I mean, we said, we mentioned sigmoid,

**[46:55 -> 47:00]** we mentioned relu, but actually,

**[47:00 -> 47:04]** I mean, there is a family of possible nonlinear function

**[47:04 -> 47:06]** that we can adopt.

**[47:06 -> 47:10]** So here you see the functioning of every single sort

**[47:10 -> 47:13]** of neurons somehow that takes the inputs,

**[47:13 -> 47:15]** elaborates the information linearly,

**[47:15 -> 47:17]** and then you have the nonlinearity, right?

**[47:17 -> 47:21]** So mimicking the functioning of the neuron cell,

**[47:22 -> 47:25]** where we pass the nonlinear function, right?

**[47:25 -> 47:28]** So the activation function.

**[47:28 -> 47:30]** But then, as we said, we have a plethora.

**[47:30 -> 47:32]** I mean, we can have many of them.

**[47:32 -> 47:33]** It's not just one.

**[47:34 -> 47:38]** The sigmoid was the first that we met,

**[47:38 -> 47:40]** and then we discussed about the relu.

**[47:40 -> 47:45]** But what Lekan was using at the beginning was the tanh,

**[47:45 -> 47:47]** because the sigmoid has some limitation.

**[47:47 -> 47:49]** We will discuss now.

**[47:49 -> 47:51]** And then besides the relu,

**[47:51 -> 47:54]** you can have many other kinds of variants

**[47:54 -> 47:59]** that tend to avoid the presence of this discontinuity here

**[47:59 -> 48:03]** or the fact that here we have a constant, a plateau

**[48:03 -> 48:07]** and so the gradient is zero and this is an issue.

**[48:07 -> 48:08]** So let's see.

**[48:08 -> 48:11]** The first activation function that we mentioned

**[48:11 -> 48:13]** was the sigmoid, right?

**[48:13 -> 48:14]** So what does it do?

**[48:14 -> 48:17]** It takes every input we provide

**[48:17 -> 48:18]** and it squashes it between zero and one.

**[48:18 -> 48:22]** So the output will be always available between zero and one.

**[48:22 -> 48:25]** It was initially popular because it resembled

**[48:25 -> 48:27]** the step function, right?

**[48:27 -> 48:31]** That is what it's on or off with respect to the,

**[48:32 -> 48:35]** let's say what a real neuron does.

**[48:37 -> 48:40]** But you have an issue here,

**[48:40 -> 48:43]** which is the fact that the activation function

**[48:43 -> 48:46]** then plateaus both at very high values

**[48:46 -> 48:49]** and at very low values, okay?

**[48:49 -> 48:51]** So in this case, what happens?

**[48:51 -> 48:57]** the gradient of a constant is zero. So when you take the gradient, which is all the, let's say,

**[48:57 -> 49:02]** the source of your model because you have updated parameters and the cent is based on gradients,

**[49:02 -> 49:09]** right? So when you take gradient of these, that kind of thing, you get zero. So this saturation

**[49:09 -> 49:16]** behavior kills the gradient. And if the gradient is killed, your network is not able anymore to

**[49:16 -> 49:17]** to update the parameters.

**[49:17 -> 49:21]** And so we don't know exactly how to go on training.

**[49:21 -> 49:24]** So this is an issue, right?

**[49:24 -> 49:27]** So you remember we have the gradient that comes

**[49:27 -> 49:28]** from the end of the network.

**[49:28 -> 49:32]** So the reality of the loss with respect to the sigma here.

**[49:32 -> 49:34]** And then you have to multiply it with the other elements,

**[49:34 -> 49:35]** right?

**[49:35 -> 49:37]** So in the back propagation,

**[49:37 -> 49:40]** but if X is very small,

**[49:40 -> 49:42]** so the input is very small or very big,

**[49:43 -> 49:45]** then the gradient is zero, right?

**[49:45 -> 49:48]** And so in this region here, you don't have information

**[49:48 -> 49:50]** about how to do the update.

**[49:50 -> 49:53]** Now around zero, yes, I mean the gradient is the slope

**[49:53 -> 49:56]** of your let's say linear behavior of the model.

**[49:56 -> 49:58]** So still you have a signal that can pass,

**[49:58 -> 50:02]** but when instead we are in the saturation region,

**[50:02 -> 50:05]** then we don't have information anymore.

**[50:09 -> 50:12]** And moreover, there is also another issue,

**[50:12 -> 50:17]** which is the fact that all the outputs are positive.

**[50:17 -> 50:18]** Right?

**[50:18 -> 50:21]** So if the output is in this case is between zero and one.

**[50:21 -> 50:23]** So we are putting a positive value,

**[50:24 -> 50:25]** it's not zero center.

**[50:25 -> 50:27]** So there's no equal probability

**[50:27 -> 50:30]** of having negative and positive values, right?

**[50:30 -> 50:32]** It's only, the output will be only the pose

**[50:32 -> 50:35]** of positive values for these activation function.

**[50:35 -> 50:39]** So the sigmoid is not zero centered, it's always positive.

**[50:39 -> 50:40]** And this is an issue.

**[50:40 -> 50:51]** So now think about this, which is just the linear part of a layer, but think of the case in which we are in the middle of the network.

**[50:51 -> 51:01]** So your X is not the image, is the feature map, so we are in the middle of the network.

**[51:01 -> 51:07]** So now the reality of this function with respect to w, which is what you are searching for,

**[51:07 -> 51:14]** is indeed what you provide as input. But what is this x? This is what is coming from the

**[51:14 -> 51:19]** previous layer. And in the previous layer, you applied the convolution and you applied

**[51:19 -> 51:27]** the activation function. So you have a conv, then you have the sigmoid. And as we said,

**[51:27 -> 51:29]** Is there something you want to share with us too,

**[51:29 -> 51:33]** such that we can laugh together or discuss it together?

**[51:36 -> 51:37]** Okay.

**[51:39 -> 51:40]** So this is not an easy concept.

**[51:40 -> 51:44]** This takes a little bit of focusing to understand it.

**[51:44 -> 51:46]** We are in the middle of the network.

**[51:46 -> 51:47]** Okay.

**[51:47 -> 51:52]** So this, I'm executing a linear step

**[51:53 -> 51:56]** and the derivative of this is just the X.

**[51:56 -> 51:59]** X is what has been provided by the previous layer,

**[51:59 -> 52:01]** which means something that pass through a linear,

**[52:01 -> 52:03]** it's a operation and through a nonlinearity.

**[52:03 -> 52:06]** So it's the output of our activation function.

**[52:06 -> 52:08]** It means that it's the output of the sigmoid

**[52:08 -> 52:10]** if we decided to use the sigmoid.

**[52:10 -> 52:12]** And then it's always a positive value.

**[52:13 -> 52:17]** Okay, so this thing here comes from the previous layer

**[52:17 -> 52:18]** and it's positive.

**[52:19 -> 52:20]** Now this has to be multiplied

**[52:20 -> 52:22]** with the other part of the gradient, right?

**[52:22 -> 52:23]** So we are doing the back propagation.

**[52:23 -> 52:27]** So it has to multiply all the other pieces.

**[52:27 -> 52:30]** And so you have something which is always positive

**[52:30 -> 52:32]** multiplied with the derivative of the loss,

**[52:32 -> 52:34]** I mean, the end with respect to f.

**[52:34 -> 52:37]** So this means that all the components

**[52:37 -> 52:41]** of this derivative here will have,

**[52:41 -> 52:43]** will need to have the same sign of this.

**[52:43 -> 52:47]** So this will guide the sign of this element here, right?

**[52:47 -> 52:49]** In all the directions,

**[52:49 -> 52:54]** which means that the new gradient can leave,

**[52:54 -> 52:55]** so think about the gradient

**[52:55 -> 52:58]** as living in a two dimensional space.

**[52:58 -> 53:01]** If all its components have the same sign,

**[53:01 -> 53:03]** it means that the direction of your vector

**[53:03 -> 53:05]** either live in this quadrant, let's say,

**[53:05 -> 53:06]** or in this quadrant,

**[53:06 -> 53:09]** or the two components have the same sign,

**[53:09 -> 53:12]** because this is guided by what you obtained

**[53:12 -> 53:14]** from the previous step,

**[53:14 -> 53:16]** which means that the update that you can get,

**[53:16 -> 53:19]** so the direction for the future update,

**[53:19 -> 53:22]** will can be only composed by this kind of vector here.

**[53:22 -> 53:24]** So vectors that leave in this quadrant,

**[53:24 -> 53:27]** so this direction or in this direction, so here.

**[53:27 -> 53:28]** They have to have the same sign.

**[53:28 -> 53:31]** So ideally your network would like to move

**[53:31 -> 53:34]** towards a minimum and you would like to have a direction

**[53:34 -> 53:36]** that points you towards the minimum,

**[53:36 -> 53:40]** but you can do it only by taking steps

**[53:40 -> 53:42]** which are zigzagging around it.

**[53:42 -> 53:44]** So this will take more time.

**[53:44 -> 53:48]** So the fact that the sigmoid outputs values

**[53:48 -> 53:51]** which are only positive and so are guiding,

**[53:51 -> 53:55]** I mean, the choice of the sign of the next,

**[53:55 -> 53:59]** I mean, direction of your gradient is an issue.

**[53:59 -> 54:02]** Now, of course, since you are not looking

**[54:02 -> 54:06]** at one sample at a time, you are averaging over batches.

**[54:06 -> 54:07]** This is a little bit, let's say,

**[54:09 -> 54:11]** the issue is not so heavy,

**[54:11 -> 54:16]** somehow it's not so really causing big issues,

**[54:16 -> 54:23]** the issues but still is there. So it's something we don't want. And how should we avoid it? Well,

**[54:23 -> 54:31]** exactly we should avoid to have always positive output. We should have something which is

**[54:31 -> 54:39]** zero-centered. So this is an issue. The third issue, although it's less problematic, is the

**[54:39 -> 54:46]** fact that the function contained an exponent. And exponential function back then were needed

**[54:46 -> 54:52]** a little bit of computation for computer to be calculated. So it was a little bit expensive

**[54:52 -> 54:58]** in terms of computing. So now this is not an issue anymore. But I mean, at the beginning

**[54:58 -> 55:03]** when the network was developed, choosing the sigmoid was not really a good choice indeed.

**[55:03 -> 55:11]** So that's the reason why Lecan was using Tundh. So Tundh, so the hyperbolic tangent, has the

**[55:11 -> 55:17]** same shape or similar shape with respect to the sigmoid, but it is zero centered.

**[55:17 -> 55:23]** Right? So it can have, let's say, you can have values which are equally either positive

**[55:23 -> 55:30]** or negative, right? So the equally distributed. It goes from minus one to one. But of course,

**[55:30 -> 55:36]** you still have the issue that it kills gradient in the very positive or very negative regions.

**[55:36 -> 55:38]** So it can still cause saturation,

**[55:38 -> 55:41]** but still is better with respect to the sigma.

**[55:42 -> 55:43]** Okay.

**[55:44 -> 55:48]** And then people started to realize that

**[55:48 -> 55:50]** maybe they can also change the function

**[55:50 -> 55:53]** to something which looks like the value

**[55:53 -> 55:57]** because the value at least saturates only one side.

**[55:57 -> 56:02]** So for negative values, it puts everything to zero.

**[56:02 -> 56:05]** While for positive values, I mean as input,

**[56:05 -> 56:07]** we get Y equal X.

**[56:07 -> 56:10]** So I mean the output will be equal to the input.

**[56:10 -> 56:13]** So at least in this part, it does not saturate.

**[56:16 -> 56:17]** So it's very computationally efficient

**[56:17 -> 56:19]** because practical is not doing anything.

**[56:19 -> 56:24]** No exponential, no other things, hyperbolic function.

**[56:24 -> 56:25]** No, nothing of that.

**[56:25 -> 56:27]** It's just taking exactly the input

**[56:27 -> 56:29]** or bringing a negative values to zero.

**[56:31 -> 56:33]** It's much, I mean allows to guide the training

**[56:33 -> 56:37]** of the network and so better.

**[56:37 -> 56:40]** So it gets better and allow it to get much faster,

**[56:40 -> 56:43]** let's say convergence of the network.

**[56:43 -> 56:46]** So the loss gets out down much faster.

**[56:47 -> 56:52]** So in the original paper that in 2012 presented

**[56:54 -> 56:58]** the very first convolutional network working

**[56:58 -> 57:03]** for a classification task on the ImageNet challenge.

**[57:03 -> 57:10]** This was the value that they reported. So the fact that choosing ReLU allowed to speed up

**[57:10 -> 57:16]** the convergence by six times with respect to using sigmoid or tanh. Then yes, I mean,

**[57:16 -> 57:23]** it's also biologically plausible, but this is, yeah, I mean, just let's leave this kind of stuff to

**[57:23 -> 57:33]** biologists. We are computer scientists. Okay, still is not zero-centered. And we still have

**[57:33 -> 57:38]** the issue that here everything goes to zero. So at this point it's not only the gradients. So before

**[57:38 -> 57:44]** you remember there was the fact that when I have the function that time h was plateauing so indeed

**[57:44 -> 57:50]** there's no slope and the derivative is zero but at least the value of the function was not zero.

**[57:50 -> 57:55]** So here it was either plus one or minus one. Here not only the derivative is zero, it's also the

**[57:55 -> 58:02]** function itself is zero. So that is I mean this region here is not certainly not ideal. And this

**[58:02 -> 58:10]** This indeed can cause a problem because you can find yourself in a condition in which

**[58:10 -> 58:14]** many of your neurons do not answer anymore.

**[58:14 -> 58:20]** Your data, depending on the gradient flow of the neuron, if it happens to be in a region

**[58:20 -> 58:27]** where the gradient is very high and the input, what you get out of the activation function

**[58:27 -> 58:29]** is always something in this region,

**[58:29 -> 58:33]** then you have what is called that relu.

**[58:33 -> 58:36]** So your data in practice is not communicating anymore.

**[58:36 -> 58:38]** It's not providing any more information,

**[58:38 -> 58:40]** because any way the relu does not react.

**[58:41 -> 58:44]** And so the parameters are never updated.

**[58:44 -> 58:45]** And this is an issue.

**[58:46 -> 58:49]** Part of your network is not able anymore

**[58:49 -> 58:52]** to understand how to change the weights.

**[58:52 -> 58:54]** So I'm not able to learn.

**[58:54 -> 58:58]** So these, of course, is something we would like to avoid.

**[58:58 -> 59:00]** And how can we do that?

**[59:00 -> 59:05]** Well, we can eventually add some positive bias

**[59:05 -> 59:09]** in the function, so in the relu.

**[59:09 -> 59:11]** So rather than having it flat, we

**[59:11 -> 59:15]** can add the smallest loop and avoiding this.

**[59:15 -> 59:16]** I see that there is a question.

**[59:16 -> 59:33]** Okay, it's a little bit longer. We'll answer later on. So let me, let me go ahead. Okay,

**[59:33 -> 59:42]** so yeah, so this will allow to avoid these dead neurons, right? Still, we have a discontinuity

**[59:42 -> 59:47]** here. And we remember, right, that we would like to have something which is differentiable,

**[59:47 -> 59:53]** so we don't want to have this kind of discontinuities. And moreover, here in practice, what we are

**[59:53 -> 60:01]** doing is that we're introducing a hyperparameter. So we are introducing by hand a value that decides

**[60:01 -> 60:08]** the slope of this part of the nonlinearity. There is another thing you can do. So rather than putting

**[60:08 -> 60:15]** it by hand, you can introduce a parameter here. So now it's really a parameter. It's something

**[60:15 -> 60:22]** that you might try to optimize. This, of course, makes your model much more complex. Because

**[60:22 -> 60:30]** remember, at the beginning, what we said is that the parameters of the network are only in the

**[60:30 -> 60:40]** linear part wx plus b which is executed by the conclusion. So in the ReLU, in the sigmoid,

**[60:40 -> 60:47]** in the tanh, so in the activation function, there are no parameters and not even hyperparameters.

**[60:48 -> 60:55]** Now what we're doing here is just changing this and saying well in theory you can either add a

**[60:55 -> 61:01]** hyperparameter, something by hand, or we can also introduce a learnable parameter inside the

**[61:01 -> 61:05]** activation function, which means that when you take the derivatives, you don't have to take into

**[61:05 -> 61:10]** consideration only the parameters in the linear part, you also have to consider the fact that you

**[61:10 -> 61:15]** have a learnable parameters in the nonlinearity part, which of course makes things much more complex.

**[61:18 -> 61:24]** You might not like the discontinuity, which is in the origin, and so maybe you can decide also

**[61:24 -> 61:35]** to change the ReLU is something that is smooth, but then this choice reintroduces back an

**[61:35 -> 61:41]** exponential function. Okay, not too bad, as we said, it's not too much computational cost,

**[61:41 -> 61:49]** but still we are changing the function. And there's also other kind of this function like

**[61:49 -> 61:56]** Jell-U, and you might see that there are many other of these activation functions. It might

**[61:57 -> 62:06]** happen that you read about them in papers. Okay, now you see here, this is an experiment again

**[62:06 -> 62:15]** coming from a paper showing back then what was the effect of changing the activation function.

**[62:15 -> 62:24]** Now overall, we know that the sigmoid function is not a good choice, so it's not even represented

**[62:24 -> 62:34]** here. And what we are looking at are the results on Cypher 10, which is a data set of natural images

**[62:34 -> 62:40]** containing 10 categories. And the goal is to classify these 10 categories. So it's a network

**[62:40 -> 62:46]** which is trained for this goal, actually is more than one network. There's one network which is

**[62:46 -> 62:51]** called ResNet, another network which is called YResNet, another dense ResNet. And then they were

**[62:51 -> 62:57]** looking at this different kind of architecture and seeing what happens when you change the

**[62:57 -> 63:04]** activation function. Now, yes, changing the activation function might lead to a small

**[63:04 -> 63:12]** improvements or there are some variation, but the truth is that it's not the thing that really

**[63:13 -> 63:20]** provides you a significant change in the performance. So, yeah, of course, if your

**[63:20 -> 63:25]** choice is really bad, and sometimes you can see that there is a big jump, but more or less,

**[63:25 -> 63:32]** I mean, the best choices, you see that the variance of this value is not that big. What does it mean?

**[63:32 -> 63:37]** Again, it means that when you are designing your network,

**[63:37 -> 63:42]** I mean, you will not think about changing the activation

**[63:42 -> 63:45]** function as the first thing.

**[63:45 -> 63:48]** If you really want to improve the performance of your network,

**[63:48 -> 63:50]** well, this will not be the first thing

**[63:50 -> 63:51]** you would decide to change.

**[63:51 -> 63:58]** Because this provides you with a small, possibly a small key.

**[63:58 -> 64:00]** And moreover, again, another thing,

**[64:00 -> 64:03]** If your network is not converging at all,

**[64:03 -> 64:07]** and I mean, if you're trying to train a resonant

**[64:07 -> 64:09]** and the network is not converging,

**[64:09 -> 64:14]** it's not because the network is using a relo or a jello

**[64:14 -> 64:15]** or something else.

**[64:15 -> 64:16]** It's not that one.

**[64:16 -> 64:17]** That's for sure something else

**[64:17 -> 64:20]** that is creating the issue for you.

**[64:20 -> 64:24]** So the culprit is not the choice of activation function.

**[64:24 -> 64:25]** Of course, it's a relevant choice,

**[64:25 -> 64:28]** but it's not the thing that makes your network work or not.

**[64:28 -> 64:37]** Okay. So in general, I would say that, yeah, I mean, by changing the activation function,

**[64:37 -> 64:42]** you can squeeze out the performance of your network to your 1% of accuracy, maybe a little

**[64:42 -> 64:46]** bit more, but you don't expect to completely change the performance of your model by changing

**[64:46 -> 64:55]** the activation function. And there's a, let's say, general choice, avoid sigmoid and tonnage,

**[64:55 -> 64:58]** because they're not good ones. Nowadays, ReLU is the standard.

**[65:00 -> 65:07]** Okay, so this is about the activation function, but as we said there are other ingredients

**[65:07 -> 65:10]** inside the network and one of them is normalization.

**[65:13 -> 65:17]** Okay, so we'll go ahead if there are no questions about the activation function.

**[65:18 -> 65:22]** I will get back to the question at the end of the lecture, the one that is on the chat.

**[65:22 -> 65:31]** Now, what is normalization? We said that, so as you see from the formula in practice, it means that

**[65:31 -> 65:36]** we take something, we want to subtract the mean and divide by the standard deviation. And there

**[65:36 -> 65:44]** is some epsilon here, which is something that we add by hand just to avoid that the fraction gets

**[65:44 -> 65:50]** to infinity because if this is zero, then this value can explode. So why are we introducing

**[65:50 -> 65:57]** this normalization. Well, indeed, I mean, what we are doing is just having values which are,

**[65:57 -> 66:04]** by subtracting the mean and dividing by the sum of radiation, we want values that behave according to

**[66:04 -> 66:11]** a Gaussian somehow. So we have values that have zero mean and unit variance, so very standard Gaussian.

**[66:12 -> 66:18]** And why are we doing that? Well, think about what's happening inside an network, right? So every layer

**[66:18 -> 66:25]** has to use some Ws, so the values inside your kernel, that are multiplied by the input and

**[66:25 -> 66:32]** produce some output. And the values inside the kernel, so the W, change continuously.

**[66:32 -> 66:36]** So while you are updating, you are training your network, the content of the filters,

**[66:36 -> 66:42]** or the value of the W, are probabiliously updated, which means that the output of every

**[66:42 -> 66:45]** the values of the output change, right?

**[66:46 -> 66:49]** And so this thing will become the input of the next layer

**[66:49 -> 66:50]** that is again,

**[66:50 -> 66:52]** again, collaborated with other values of the filter

**[66:52 -> 66:53]** and so on.

**[66:53 -> 66:55]** So it's a moving target.

**[66:55 -> 66:57]** So you would like to find the feature

**[66:57 -> 67:02]** that then becomes the next entry for the next layer,

**[67:02 -> 67:04]** but all these failures are changing

**[67:04 -> 67:05]** and we don't have,

**[67:05 -> 67:07]** so during the training of the process,

**[67:07 -> 67:09]** we don't have, let's say,

**[67:09 -> 67:14]** any constraint on the range that these values can take.

**[67:16 -> 67:18]** And this is bad because it means that you can have

**[67:18 -> 67:22]** a very, very high value, very, very small values.

**[67:22 -> 67:24]** And this again, create the condition of moving target

**[67:24 -> 67:25]** inside the network.

**[67:25 -> 67:29]** So at the end, all these values that are changing a lot

**[67:29 -> 67:34]** makes the convergence of the network very complex.

**[67:34 -> 67:36]** So we want to make sure to have somehow to govern

**[67:36 -> 67:38]** this process.

**[67:38 -> 67:41]** And so that's the reason why we apply some normalization.

**[67:41 -> 67:45]** So we want that every time we get the output of a layer,

**[67:45 -> 67:49]** the values, these numbers that we get behave nicely

**[67:49 -> 67:51]** such that they are all around zero

**[67:51 -> 67:54]** and we have a unit variance.

**[67:54 -> 67:56]** So if we want our values to behave like this,

**[67:56 -> 67:58]** we just impose them to do it.

**[67:58 -> 68:00]** So we just do it by hand.

**[68:00 -> 68:02]** So once we obtain the output, then we say,

**[68:02 -> 68:04]** okay, let's look at the average of these values.

**[68:04 -> 68:06]** We subtract the average and we divide by the variance

**[68:06 -> 68:08]** such that they behave nicely.

**[68:08 -> 68:10]** and we control the range.

**[68:11 -> 68:14]** This moving target effect that I was mentioning before

**[68:14 -> 68:17]** is what is called internal covariate shift.

**[68:17 -> 68:21]** So it's this changing of these values inside the network,

**[68:21 -> 68:22]** which make things complicated.

**[68:23 -> 68:25]** So we are just normalizing, right?

**[68:25 -> 68:27]** So this is what we are doing.

**[68:27 -> 68:31]** And usually we do it over a batch of data.

**[68:31 -> 68:34]** So that's the reason why in particular,

**[68:34 -> 68:37]** this takes the name of batch normalization.

**[68:37 -> 68:41]** So why are we taking the average and the standard deviation

**[68:41 -> 68:42]** or over a set of data?

**[68:42 -> 68:46]** So the batch, we said that when we discuss about

**[68:46 -> 68:48]** grabbing the send and Stochastic getting the send,

**[68:48 -> 68:51]** we said that Stochastic getting the send is called like this

**[68:51 -> 68:52]** because we are taking batches, right?

**[68:52 -> 68:57]** So our network elaborates data in subgroups of samples.

**[68:57 -> 69:00]** So we're taking the average of the values produced

**[69:00 -> 69:01]** by the output of the layer,

**[69:01 -> 69:02]** average of on what?

**[69:02 -> 69:05]** Over the data, over the elements

**[69:05 -> 69:07]** which are inside that batch,

**[69:07 -> 69:10]** which means that we are not treating anymore

**[69:10 -> 69:12]** every sample separately,

**[69:12 -> 69:14]** but we are treating them as part of this group.

**[69:16 -> 69:17]** Okay.

**[69:17 -> 69:21]** Now, so this is why it's called batch normalization.

**[69:21 -> 69:25]** And what we are doing here is just subtracting the division.

**[69:25 -> 69:27]** They are very simple operation.

**[69:28 -> 69:31]** It's very simple to derivate over them.

**[69:31 -> 69:32]** So they don't create any problem.

**[69:32 -> 69:35]** Indeed, we can sort of define a layer,

**[69:35 -> 69:37]** which is called batch normalization layer,

**[69:37 -> 69:40]** that operates this and for which we can easily take

**[69:40 -> 69:43]** the reality when we have the back propagation.

**[69:44 -> 69:49]** So think about applying batch normalization

**[69:49 -> 69:52]** on a fully connected layer.

**[69:52 -> 69:53]** What do we have in a fully connected layer?

**[69:53 -> 69:58]** We said that fully connected layer manage only vectors.

**[69:59 -> 70:02]** So we have vectors of dimension D.

**[70:02 -> 70:05]** So maybe we passed already through all the convolutional

**[70:05 -> 70:06]** part of the network.

**[70:06 -> 70:08]** Now we're entering the fully connected layers.

**[70:08 -> 70:11]** So we need to flatten the information.

**[70:11 -> 70:13]** Okay, our tensor becomes a long vector,

**[70:13 -> 70:15]** vector of dimension D.

**[70:15 -> 70:18]** And we're looking at the batch of data,

**[70:18 -> 70:21]** just composed of N of these samples.

**[70:21 -> 70:24]** So we have, let's say a matrix composed of N data,

**[70:24 -> 70:27]** each of them of dimension D.

**[70:27 -> 70:29]** So what are we doing here?

**[70:29 -> 70:32]** we are taking the average over the dimension.

**[70:32 -> 70:35]** So for each dimension, we take the average,

**[70:36 -> 70:38]** running over what, over all the samples.

**[70:38 -> 70:40]** So we are taking the average over all the samples

**[70:40 -> 70:43]** that we observed for each of the dimensionality

**[70:43 -> 70:44]** of the vectors.

**[70:45 -> 70:48]** And so this is the normalization that we are applying.

**[70:50 -> 70:52]** Just compute the empirical mean and the variance

**[70:52 -> 70:54]** independently for each dimension.

**[70:54 -> 71:01]** Now, ideally, we would like the network to learn by itself, right?

**[71:01 -> 71:08]** But here we are intervening somehow by hand to imposing a condition, because there's no

**[71:08 -> 71:09]** again learnable parameter.

**[71:09 -> 71:14]** It's something that this part here is something that we are just imposing by hand.

**[71:14 -> 71:18]** You have to behave in this way, so we subtract the mean and we divide by the standard dimension.

**[71:18 -> 71:22]** But maybe this operation that we are doing is too strong.

**[71:22 -> 71:28]** So we would like to leave the network a little bit of freedom to maintain the data that it

**[71:28 -> 71:32]** would have been produced by itself without this operation.

**[71:32 -> 71:33]** So what do we do?

**[71:33 -> 71:37]** Well, we reintroduce some learnable primary.

**[71:37 -> 71:43]** So we say, yes, we operate the batch normalization, we do it, right?

**[71:43 -> 71:47]** So the normalization per se, we do it, right?

**[71:47 -> 71:53]** But then we introduce a gamma and a beta, which are learnable parameters.

**[71:53 -> 71:58]** And the output of the batch visualization will be not only this step, but what we obtain

**[71:58 -> 71:59]** out of this.

**[71:59 -> 72:05]** So we will ask the network also to learn these two components, these two values.

**[72:05 -> 72:12]** And if the network decide by itself, doing this, optimizing these values, that this value

**[72:12 -> 72:19]** should be exactly equal to the square root of the variance and the average of the data,

**[72:19 -> 72:24]** then it's like as if we didn't apply the best realization. Of course this doesn't happen,

**[72:24 -> 72:29]** so it's not just a one by one. So this equality is exactly the one it is. It's rarely to happen,

**[72:29 -> 72:36]** right? But we are still providing the network a little bit of freedom to decide to revert

**[72:36 -> 72:42]** the decision that we did by hand by subtracting the mean and dividing by the

**[72:42 -> 72:52]** sum of the relation. Okay so it can record in theory. Okay so this is just the

**[72:52 -> 72:59]** let's say sort of a sales algorithm of what we are doing and this helps a lot

**[72:59 -> 73:03]** to improve the gradient flow through the network because again these

**[73:03 -> 73:05]** these values are not changing a lot,

**[73:05 -> 73:09]** we are keeping them in controlled ranges.

**[73:09 -> 73:12]** Allows also to use higher learning rates.

**[73:12 -> 73:15]** You remember we said that the learning rate

**[73:15 -> 73:17]** is that videos that you put in front of the gradient

**[73:17 -> 73:19]** in gradient descent,

**[73:19 -> 73:21]** and that regulates how big is the step

**[73:21 -> 73:23]** that you are taking towards the minimum.

**[73:23 -> 73:26]** So if the learning rate is small,

**[73:26 -> 73:29]** you're taking very small steps towards the minimum,

**[73:29 -> 73:31]** if the learning rate is big,

**[73:31 -> 73:34]** then you're taking big steps towards them, okay?

**[73:34 -> 73:39]** So taking big steps, as we mentioned, it might be risky

**[73:39 -> 73:42]** because then if you take big step around the minimum,

**[73:42 -> 73:44]** you might end jumping here and there,

**[73:44 -> 73:47]** but never reaching the minimum of your,

**[73:47 -> 73:49]** you'd say, lost landscape, right?

**[73:49 -> 73:52]** You might end up jumping from the border.

**[73:52 -> 73:56]** While instead, since we are now normalizing

**[73:56 -> 73:59]** and the overall loss behave better, the overall network,

**[73:59 -> 74:07]** you have a better flow of the gradient, you can afford to also take higher learning rates,

**[74:08 -> 74:15]** okay, to take larger steps because, yeah, I mean, you still are able to get to the minimum

**[74:15 -> 74:21]** properly with a good speed, so, and avoiding to jump in here or there because the flow, I mean,

**[74:22 -> 74:28]** the loss function behaves better thanks to the fact, so it has a more, it's a smooth kind of

**[74:28 -> 74:33]** behaviour, thanks to the fact that you have this normalisation. And a bit acts as a form of

**[74:33 -> 74:41]** regularisation. So you remember, what is regularisation is a strategy that we apply

**[74:42 -> 74:50]** to avoid our network to overfit. What does it mean overfitting? It means memorising the training

**[74:50 -> 74:58]** samples and not being able to generalize. So why I'm saying that batch normalization somehow

**[74:59 -> 75:03]** act as a form of regularization exactly for the reason why we're calling it batch.

**[75:04 -> 75:09]** It's actually for the same reason why we said that also stochastic gradient descent

**[75:09 -> 75:14]** introduces a bit of regularization. Because rather than looking at one sample at a time,

**[75:14 -> 75:21]** we are somehow averaging over a set of samples, right? So this makes memorizing every single

**[75:21 -> 75:29]** sample, the nature of a single sample, much more complex, right? So this is why it introduces a bit

**[75:29 -> 75:40]** of memorization. So note that since here we have, we are learning some parameters,

**[75:40 -> 75:45]** Okay, so the gamma and the beta.

**[75:45 -> 75:47]** At this time, what does it happen?

**[75:47 -> 75:56]** So at this time, I should not recalculate the mean and the standard deviation of a batch

**[75:56 -> 75:57]** of test data.

**[75:57 -> 76:01]** No, because I will want a prediction percentage.

**[76:01 -> 76:05]** So at this time, I want to make a prediction on every single instance that I see.

**[76:05 -> 76:09]** I don't want to wait for a batch of test samples, take the average and make the prediction.

**[76:09 -> 76:12]** No, I need to have a prediction per sample.

**[76:12 -> 76:17]** So what I will do, certainly, is that I will not recalculate

**[76:17 -> 76:19]** average and standard deviation.

**[76:19 -> 76:22]** At this time, I will use the average and the standard deviation

**[76:22 -> 76:25]** I had during the training.

**[76:25 -> 76:30]** And of course, I will also apply the gamma and the beta.

**[76:30 -> 76:40]** So this might be, let's say, a sort of source of bugs.

**[76:40 -> 76:43]** So pay attention that the test time, batch normalization

**[76:43 -> 76:45]** works differently with respect to what

**[76:45 -> 76:46]** you have at training time.

**[76:46 -> 76:49]** Anyway, I mean, you can simply operate

**[76:49 -> 76:52]** this in a linear operator because the operation

**[76:52 -> 76:53]** that you have are very simple.

**[76:53 -> 76:56]** You can simply derive it.

**[76:56 -> 76:58]** And where do you put it?

**[76:58 -> 77:00]** Well, usually in the convolutional part,

**[77:00 -> 77:02]** you have the fully connected layer.

**[77:02 -> 77:04]** Then you apply best formalization,

**[77:04 -> 77:07]** and you have your non-linearity.

**[77:07 -> 77:09]** Now here it's done age, but as we said,

**[77:09 -> 77:10]** it would be better to avoid it.

**[77:10 -> 77:16]** I was just taking the original Lynette idea.

**[77:16 -> 77:18]** But yeah, usually you can see it's positioned

**[77:18 -> 77:20]** after the fully connected layer.

**[77:20 -> 77:24]** There are some papers where you can read that they test

**[77:24 -> 77:28]** how to put visualization even after the nonlinearity.

**[77:28 -> 77:30]** It can be used for some specific reason.

**[77:30 -> 77:33]** So eventually, you can also move it afterwards.

**[77:33 -> 77:35]** The point is anyway that you want

**[77:35 -> 77:39]** to have under control what every single, let's say, layer

**[77:39 -> 77:40]** produce.

**[77:40 -> 77:43]** And when I say layer, I think about the combination

**[77:43 -> 77:46]** of fully connected, so linear part, fully connected part,

**[77:46 -> 77:47]** and nonlinearity.

**[77:47 -> 77:51]** So also the tanh or sigmoid or a relu.

**[77:54 -> 77:57]** There are different ways in which you can apply normalization.

**[77:57 -> 77:59]** We saw the batch normalization,

**[77:59 -> 78:02]** so that removes somehow the end dimensional in terms of the data,

**[78:02 -> 78:05]** and is in the fully connected layer.

**[78:05 -> 78:08]** When you can also apply it on the convolutional layer,

**[78:08 -> 78:13]** and in that case, you are averaging over not only the end samples,

**[78:13 -> 78:17]** but also you're squeezing the information in the region of your filter.

**[78:17 -> 78:20]** It's just taking the average and

**[78:20 -> 78:23]** the percent deviation or all the dimensional idea of the filter.

**[78:23 -> 78:25]** The only thing that you keep is the depth.

**[78:25 -> 78:30]** Okay, so you will have one value per depth channel of your,

**[78:31 -> 78:35]** let's say, in your feature map before going to the next area.

**[78:35 -> 78:40]** And there are different other ways in which you can use normalization.

**[78:40 -> 78:41]** I'll just quickly go here.

**[78:41 -> 78:45]** So you can have layer normalization, you can have instance normalization.

**[78:45 -> 78:48]** But yeah, and you can have also a subgroup.

**[78:48 -> 78:52]** So group normal, you can see just sub parts of the channels.

**[78:52 -> 78:54]** and take the average over them.

**[78:54 -> 78:56]** So depending on the task again,

**[78:56 -> 78:58]** and the design of the network,

**[78:58 -> 78:59]** you can make different choices.

**[79:01 -> 79:03]** So I would say that I stop here

**[79:03 -> 79:06]** and we'll get back to the next lecture

**[79:06 -> 79:07]** for this kind of stuff.

**[79:08 -> 79:12]** So the plan is that the next lecture,

**[79:12 -> 79:13]** there will be still theory,

**[79:13 -> 79:16]** but then on Friday, you will start,

**[79:16 -> 79:19]** I mean, putting your hand in a bit of code.

**[79:19 -> 79:21]** So we'll have an exercise session Friday.

**[79:21 -> 79:31]** Thank you.

**[79:51 -> 79:53]** you

**[80:21 -> 80:23]** you

**[80:51 -> 80:53]** you

**[81:21 -> 81:23]** you

**[81:51 -> 81:53]** you

**[82:21 -> 82:23]** you

**[82:51 -> 82:53]** you

**[83:21 -> 83:23]** You

