# Lecture Transcription

- **Source**: `temp_audio.wav`
- **Model**: `base.en`
- **Device**: `mps`

---

**[01:00 -> 01:29]** Turn on the microphone, yes, such that the video connection should be fine. So people from home who are connected should be able to see the screen and hear my voice. Okay, if you have any issues, just, yeah, let me know via chat, perfect. It seems to work. Perfect. Good. Okay. So, I'm going to go ahead and see if I can get a little bit more information.

**[01:29 -> 01:31]** Okay, so I think I'm in the right room, right?

**[01:31 -> 01:35]** So we are going to teach advanced machine learning.

**[01:35 -> 01:37]** I'm in the right room, perfect.

**[01:38 -> 01:43]** Okay, so welcome to the first lecture of the course.

**[01:43 -> 01:45]** I'm Tatiana Tomasi.

**[01:45 -> 01:48]** I'm a full professor here at Puyidakuni of Turin.

**[01:49 -> 01:53]** And what we will do today will be just mainly

**[01:53 -> 01:56]** introduce myself, introduce the team

**[01:56 -> 02:01]** that will lead the course and the activities

**[02:03 -> 02:05]** for the project and for the exam.

**[02:05 -> 02:09]** And then we will start also discussing

**[02:09 -> 02:11]** about a little bit of definition of what is,

**[02:11 -> 02:15]** machine learning, why are we talking today about AI,

**[02:15 -> 02:17]** what is that, what is the philosophy behind it,

**[02:17 -> 02:20]** and how we will formalize this concept

**[02:20 -> 02:22]** for the rest of the course.

**[02:22 -> 02:26]** So as I told you, I'm a professor here at BoiTech,

**[02:26 -> 02:30]** and you got to have been traveling around a bit in Europe,

**[02:30 -> 02:32]** but also in US.

**[02:32 -> 02:36]** So you can see the area of research work

**[02:36 -> 02:39]** I'm working on in the Google Scholar.

**[02:39 -> 02:41]** You have my email here.

**[02:41 -> 02:46]** Actually, the course will be mainly a lead by me,

**[02:46 -> 02:49]** but you will see during the lecture,

**[02:49 -> 02:53]** a group of PhD students that will serve as teaching assistant.

**[02:53 -> 02:58]** So we'll have Stephanie, David Lissandrin, Silvio.

**[02:58 -> 03:03]** And it is possible that there will be maybe some guest lecture

**[03:03 -> 03:07]** or video, even from other colleagues in my team,

**[03:07 -> 03:10]** from Professor Caputo, Averda Masone, Camariano, and Viscilla.

**[03:10 -> 03:14]** So we are part of our research group, which

**[03:14 -> 03:18]** is called Bandal, Visual and Multimodal Applied Learning

**[03:18 -> 03:20]** Lab.

**[03:20 -> 03:23]** So you will see that we'll talk about artificial intelligence

**[03:23 -> 03:28]** mainly with practical application in the area of computer vision,

**[03:28 -> 03:32]** multimodal learning, so combination of vision and language,

**[03:32 -> 03:38]** which is practically today one of the most active area for AI.

**[03:38 -> 03:45]** So you see here that beside the bundle name and name of the group,

**[03:45 -> 03:48]** you see also this big logo of Alice.

**[03:48 -> 03:53]** Alice is the European laboratory for learning an intelligent system.

**[03:53 -> 04:01]** is an effort of excellence in Europe that connects a top research center around Europe.

**[04:01 -> 04:09]** So you see on the left, it may be a bit small, but there are 47 places in Europe

**[04:09 -> 04:16]** where there is critical mass of people working on machine learning and AI and publishing at top level.

**[04:16 -> 04:21]** I mean, there are places like Paris, Oxford, Cambridge,

**[04:21 -> 04:25]** Berlin, Munich, and Zurich.

**[04:25 -> 04:31]** So together with these very well-known research centers,

**[04:31 -> 04:32]** there's also Turin.

**[04:32 -> 04:37]** So we have a unit of the LS network here in Turin,

**[04:37 -> 04:38]** which I'm directing.

**[04:38 -> 04:41]** And you see the people on the right

**[04:41 -> 04:43]** that are part of this team.

**[04:43 -> 04:46]** So we are connecting, protecting of Turing,

**[04:46 -> 04:49]** University of Turing, the links foundation,

**[04:49 -> 04:53]** the easy foundation, and we are going also to extend

**[04:53 -> 04:56]** to other entities here in the, let's say,

**[04:56 -> 04:58]** the local area of Turing,

**[04:58 -> 05:00]** because there's a lot of activity related to AI.

**[05:01 -> 05:04]** So what is ELIS, just to provide you a, let's say,

**[05:04 -> 05:08]** an overview and why, I mean, also providing an indication

**[05:08 -> 05:10]** of why I'm mentioning it here.

**[05:10 -> 05:17]** It is relevant because it's, I mean, AI now is a buzzword, right?

**[05:17 -> 05:20]** Everybody is talking about AI.

**[05:20 -> 05:24]** But the point is that most of it is, let me say it in Italian,

**[05:24 -> 05:25]** it's Fufa, right?

**[05:25 -> 05:31]** It's just selling wind, nothing really grounded.

**[05:31 -> 05:36]** What we are doing in this excellence network is really producing results which

**[05:36 -> 05:41]** are verified by peers, technically so very solid.

**[05:41 -> 05:45]** And in practice, this network offers support also

**[05:45 -> 05:50]** for traveling among these places to do research.

**[05:50 -> 05:57]** And there is a very nice and very well supported PhD path.

**[05:57 -> 05:59]** So if you're interested in doing research,

**[05:59 -> 06:01]** you can having a look at these kind of activities

**[06:01 -> 06:03]** because it's a very solid.

**[06:03 -> 06:08]** And now it's almost six years that this PhD program

**[06:08 -> 06:11]** is established with very, very great success.

**[06:11 -> 06:13]** And good connection with industries,

**[06:13 -> 06:15]** like I mean Google, Apple, and so on.

**[06:15 -> 06:18]** So there's also a lot of money, of course,

**[06:18 -> 06:21]** as you know, behind machine learning at the moment.

**[06:23 -> 06:27]** Okay, so just let me go ahead.

**[06:27 -> 06:29]** In practice, what are we going to do in this course?

**[06:29 -> 06:33]** Well, first of all, here there's the basic information

**[06:33 -> 06:41]** about the course. So the course covers six credits. Well, I start immediately by saying it,

**[06:42 -> 06:50]** generally a student complained because six credit is not exactly correctly evaluating the amount

**[06:50 -> 06:56]** of work that we are going to do. I know. Okay, so but unfortunately this is how it is. We are

**[06:56 -> 07:03]** within a path where AI is of course the main direction and here I mean this course is the

**[07:03 -> 07:07]** the richest one in terms of concepts

**[07:07 -> 07:08]** and then practical applications.

**[07:08 -> 07:11]** So it will need a little bit of effort,

**[07:11 -> 07:14]** but you will see that this effort will pay off, right?

**[07:14 -> 07:17]** So really you will be able to write in your CV,

**[07:17 -> 07:18]** I attended this course,

**[07:18 -> 07:20]** I know how to put my hand inside the models,

**[07:20 -> 07:22]** I know how to design a new model,

**[07:22 -> 07:24]** I know what does it mean,

**[07:24 -> 07:25]** I know how to read the results,

**[07:25 -> 07:28]** I know how to improve a model,

**[07:28 -> 07:31]** how to make it more efficient and so on, right?

**[07:31 -> 07:34]** So you will learn a lot in this sense.

**[07:34 -> 07:36]** We have this when and where.

**[07:36 -> 07:39]** So today is Friday, but of course, for next week,

**[07:39 -> 07:43]** we will start back with the three hours on Tuesday.

**[07:43 -> 07:46]** Most of the lecture will be in presence.

**[07:46 -> 07:50]** There will be only maybe a small fraction online, rare

**[07:50 -> 07:52]** free recorded video mainly, I mean,

**[07:52 -> 07:54]** none of them, I believe.

**[07:54 -> 07:55]** There will be a lot of discussion session,

**[07:55 -> 07:59]** because besides the exercises that, of course,

**[07:59 -> 08:05]** be in presence, the teaching assistants from a certain period on will be available online

**[08:05 -> 08:12]** to support you with the project and with the work you will be able to do, also for the exam.

**[08:12 -> 08:19]** So in practice you will have also extra availability from the tutors to support you with your work

**[08:19 -> 08:27]** and to discuss about what you are going to work on. Everything will be recorded, so starting from

**[08:27 -> 08:29]** on today, all the lectures are recorded.

**[08:29 -> 08:31]** You will find them online on the portal

**[08:31 -> 08:33]** after the lecture itself.

**[08:33 -> 08:37]** We will not record exercise session because it's really,

**[08:37 -> 08:40]** I mean, if you are putting your hand inside the code,

**[08:40 -> 08:43]** there's not really anything to record.

**[08:43 -> 08:45]** There will be just a short presentation

**[08:45 -> 08:48]** in the exercise lecture, short presentation of the problem,

**[08:48 -> 08:50]** short presentation of the tasks that you have to solve

**[08:50 -> 08:55]** and some basic indication, then you are left to do it.

**[08:55 -> 08:58]** So again, teaching a assistant will be around,

**[08:58 -> 08:59]** we will support you during the exercise,

**[08:59 -> 09:03]** but there's nothing practically to be recorded

**[09:03 -> 09:05]** on those kind of sessions.

**[09:06 -> 09:08]** And we have a Discord channel.

**[09:08 -> 09:12]** So I've seen already that some of you started entering,

**[09:12 -> 09:13]** very well, fine.

**[09:13 -> 09:16]** So it's, say at the moment,

**[09:16 -> 09:18]** there's just a general space.

**[09:19 -> 09:21]** Now consider that all the announcement

**[09:21 -> 09:24]** will go through the portal, right?

**[09:24 -> 09:29]** So the Discord at the moment is just an extra channel.

**[09:29 -> 09:33]** Maybe I will try to duplicate some of the messages,

**[09:33 -> 09:36]** but mainly the main channel is the portal.

**[09:36 -> 09:41]** What Discord will be very helpful for is what will happen

**[09:41 -> 09:44]** for your exercises and project section.

**[09:44 -> 09:49]** Okay, so once the projects and see in the next slides,

**[09:49 -> 09:51]** once the project topic will be presented,

**[09:51 -> 09:55]** Then we will have one sub-channel in Discord

**[09:55 -> 09:56]** for each of the project.

**[09:56 -> 09:58]** And there you can ask question,

**[09:58 -> 10:01]** interact with the teaching assistant and so on and so forth.

**[10:01 -> 10:04]** Of course, you can always reach me through the,

**[10:04 -> 10:06]** I mean the general channel if you need me

**[10:06 -> 10:07]** for some specific reason.

**[10:09 -> 10:12]** But yeah, usually if there are specific cases

**[10:12 -> 10:14]** for, I mean, personal reason for some specific student,

**[10:14 -> 10:17]** you can also, and it's also better to send me an email.

**[10:17 -> 10:22]** Okay, so the Discord channel is there.

**[10:22 -> 10:27]** You can use it already, although at the moment is not very active,

**[10:27 -> 10:32]** at least from the, let's say, teaching team side.

**[10:32 -> 10:37]** Okay, so let's start entering in some of the topics.

**[10:37 -> 10:43]** So what I expect is to have at the moment just a very high level of view of your expertise,

**[10:43 -> 10:48]** means I know that in the path, in your study path,

**[10:48 -> 10:51]** you already should have, I mean, covered some of the topics,

**[10:51 -> 10:54]** this is just a survey to double check it,

**[10:54 -> 10:56]** but yeah, let's see together.

**[10:56 -> 10:58]** So I will ask you to raise your hand

**[10:59 -> 11:02]** to verify I'm answering some of these questions.

**[11:02 -> 11:07]** So do you know what is principal component analysis?

**[11:07 -> 11:17]** Okay, I would expect even a higher fraction, but okay, maybe there's someone online and

**[11:17 -> 11:24]** this sense fine. Well, actually we have 40 participants online. Okay, good. Do you know

**[11:24 -> 11:32]** what is super vector machines? Have you ever trained a super vector machine classifier

**[11:32 -> 11:37]** Do you know what is cross validation?

**[11:37 -> 11:40]** Okay, that's the basic, right?

**[11:40 -> 11:44]** Do you have experience with Python coding?

**[11:44 -> 11:47]** Okay, very well.

**[11:47 -> 11:52]** Have you ever trained a neural network model specifically a

**[11:52 -> 11:55]** convolutional neural network model for classification?

**[11:55 -> 11:57]** Okay, good.

**[11:57 -> 12:02]** Okay, in this case, the last question of course will be the focus, I mean part of the focus

**[12:02 -> 12:10]** of this course. So I was expecting that this is something new for many of you, but it's

**[12:10 -> 12:16]** good that some already had this kind of experience. But yeah, I mean the statistics that I'm

**[12:16 -> 12:22]** collecting from this survey is something very close to what I was expecting.

**[12:22 -> 12:24]** Now let's go to the next question.

**[12:24 -> 12:27]** Do you know what the acronym GPT stands for?

**[12:30 -> 12:35]** Okay, I'm very, very delusional answer, right?

**[12:35 -> 12:37]** Because I know that you know what is charge GPT.

**[12:37 -> 12:39]** I mean, I put my hand on the fire

**[12:39 -> 12:40]** that you know what is that.

**[12:40 -> 12:42]** But the fact that you don't know what does it mean,

**[12:42 -> 12:46]** this acronym means that you're using a tool,

**[12:46 -> 12:49]** but you don't have any idea what is behind that tool.

**[12:49 -> 12:52]** which okay, I mean, I know that this is standard nowadays,

**[12:52 -> 12:55]** but the reason why you are attending this course

**[12:55 -> 12:57]** is that you will know, after this course,

**[12:57 -> 13:02]** what this acronym stands for, why it is called like this,

**[13:02 -> 13:05]** and what is this method?

**[13:05 -> 13:10]** So GPT stands for generative pre-trained transformer.

**[13:10 -> 13:12]** Okay, so a method that can generate,

**[13:12 -> 13:16]** a method that is pre-trained on something,

**[13:16 -> 13:20]** and a method that uses as architecture a transformer.

**[13:20 -> 13:23]** So the course will bring you to understand

**[13:23 -> 13:25]** what a transformer is,

**[13:25 -> 13:27]** what is the structure behind the architecture,

**[13:27 -> 13:30]** why it works and the way it works,

**[13:30 -> 13:31]** and what does this mean to have a method

**[13:31 -> 13:34]** that can generate something like.

**[13:34 -> 13:37]** So here we're talking about melee method

**[13:37 -> 13:38]** that generates text, at least originally.

**[13:38 -> 13:43]** Now it can generate also visual output, so images,

**[13:43 -> 13:48]** and it's practically a multi-model genetic approach.

**[13:49 -> 13:51]** And what we will see is, I mean,

**[13:51 -> 13:56]** what is behind each of these pieces of the snake, right?

**[13:58 -> 14:03]** So we'll dig in in this kind of methods.

**[14:04 -> 14:06]** Now, useful material.

**[14:08 -> 14:10]** You will have the slides, of course,

**[14:10 -> 14:15]** But there are a lot of good books that you can consider as reference,

**[14:15 -> 14:19]** even because my slides are actually inspired by the content of those books.

**[14:19 -> 14:21]** It's inevitable.

**[14:21 -> 14:25]** Some of these books are freely available online.

**[14:25 -> 14:28]** The little book of deep learning is really lovely.

**[14:28 -> 14:31]** So it's very small and it's very compact,

**[14:31 -> 14:34]** but all the concepts are there.

**[14:34 -> 14:41]** And there are also other books, which are very well known.

**[14:41 -> 14:48]** I cannot put the link, of course, because they're not really public, but I'm sure you can find them a lot.

**[14:48 -> 14:56]** But the point is, now, let me clarify something.

**[14:56 -> 14:59]** I'm providing you references, right?

**[14:59 -> 15:03]** So you have those slides, my slides, you have these links.

**[15:03 -> 15:05]** Most of my slides will have also further links

**[15:05 -> 15:09]** that you can click and check the content and read.

**[15:10 -> 15:13]** Please, don't come at the exam telling me,

**[15:13 -> 15:16]** oh, I'm sorry, I had to study through charge FITI

**[15:16 -> 15:18]** because I didn't have a reference.

**[15:19 -> 15:21]** I will use a very strong word, I will kill you.

**[15:21 -> 15:24]** It's not that you don't class the exam,

**[15:24 -> 15:25]** that's the minimum, okay.

**[15:26 -> 15:30]** You don't exit a lie from the room after this kind of answer.

**[15:30 -> 15:31]** Okay?

**[15:31 -> 15:32]** Please, no.

**[15:32 -> 15:34]** You have the tools.

**[15:34 -> 15:36]** Books is something that you can still read.

**[15:36 -> 15:37]** Okay?

**[15:37 -> 15:39]** It's not something that does not exist.

**[15:39 -> 15:40]** It exists.

**[15:40 -> 15:43]** They are there and they contain a lot of knowledge.

**[15:43 -> 15:47]** You can access this kind of knowledge to enrich yourself.

**[15:47 -> 15:49]** Now,

**[15:49 -> 15:59]** Of course, books have specific years of addition and maybe they are not really updated.

**[15:59 -> 16:03]** And AI is done really by its alive.

**[16:03 -> 16:07]** It's something that produces new results every day.

**[16:07 -> 16:15]** So maybe the books have the, let's say, the very clean concept and the most static and

**[16:15 -> 16:20]** and established knowledge, but the new part is mainly

**[16:20 -> 16:23]** on conference paper, technical reports

**[16:23 -> 16:26]** that are published at top conferences,

**[16:26 -> 16:28]** like the ones I'm citing here.

**[16:28 -> 16:31]** So like NERIPs, the NERO Information

**[16:31 -> 16:32]** and Processing System conferences,

**[16:32 -> 16:34]** which is one of the oldest one,

**[16:34 -> 16:37]** CBPR, Computer Vision and Pattern recognition.

**[16:37 -> 16:41]** Then you have ICLR, which is International Conference

**[16:41 -> 16:43]** of Learning and Representation.

**[16:43 -> 16:44]** You have all the conferences related

**[16:44 -> 16:49]** computer vision, so the European conference, the international conference and so on.

**[16:49 -> 16:54]** So these are the kind of support we will use practically to extract knowledge from

**[16:56 -> 17:04]** and be able to provide you the most new concept. And the point is that it might be

**[17:04 -> 17:09]** scaring to be able to extract information from these papers, these technical records, because

**[17:09 -> 17:13]** It's a kind of format maybe you are not used to.

**[17:13 -> 17:17]** So what we will try to do is help you to read the paper

**[17:17 -> 17:19]** to understand how to distill knowledge out of them,

**[17:19 -> 17:23]** how to organize knowledge from this kind of technical record,

**[17:23 -> 17:25]** how to understand what is the part of the information

**[17:25 -> 17:28]** that you really need for your project, for your thesis,

**[17:28 -> 17:31]** for your next job in the future, and so on and so forth.

**[17:31 -> 17:36]** So this is a very important educational part of the course

**[17:36 -> 17:42]** Because in practice, it's impossible to say that whatever you will learn here, it's everything.

**[17:42 -> 17:45]** It's impossible, right?

**[17:45 -> 17:52]** So as I told you, AI is evolving very fast and you have to become, let's say, a self-learner.

**[17:52 -> 17:55]** So you have to understand how to learn.

**[17:55 -> 18:00]** And that's the technique of how to learn, how to extract knowledge out from the publication

**[18:00 -> 18:05]** that makes you then really an expert in machine learning or AI.

**[18:06 -> 18:14]** Besides these references, you can find some very reliable online courses like the one

**[18:14 -> 18:19]** of Professor Feifei Lee in Stanford, like the one from Enjunga, which is one of the

**[18:19 -> 18:21]** founder of Coursera.

**[18:21 -> 18:25]** So certainly you can find good references.

**[18:25 -> 18:28]** Many of my lectures are also inspired from those courses.

**[18:28 -> 18:30]** There's no reason to hide it.

**[18:30 -> 18:33]** Of course, they are very good teachers.

**[18:33 -> 18:38]** So why not try to reuse this kind of, let's say, structure

**[18:38 -> 18:40]** and the presentation for the course.

**[18:40 -> 18:42]** And then there is also previous courses

**[18:42 -> 18:44]** that some of them I expect already.

**[18:44 -> 18:48]** I mean, went through and some others from other courses,

**[18:48 -> 18:52]** from other paths, maybe can be useful as reference.

**[18:52 -> 18:55]** And then in terms of Python, I mean, most of you

**[18:55 -> 18:58]** is expert as we saw.

**[18:58 -> 19:00]** But if you need to improve your knowledge,

**[19:00 -> 19:03]** There is some tutorial online.

**[19:03 -> 19:07]** PyTorch is slightly different with respect to Python.

**[19:07 -> 19:11]** So PyTorch provides you the tools to then be able to work with

**[19:11 -> 19:16]** deep learning models, which is the most modern AI architecture.

**[19:16 -> 19:18]** So you will actually,

**[19:18 -> 19:21]** PyTorch will be part of the knowledge objective,

**[19:21 -> 19:24]** let's say that you will learn through the course.

**[19:24 -> 19:26]** Besides the fact that even for

**[19:26 -> 19:29]** PyTorch you can find tutorial online.

**[19:29 -> 19:34]** So in practice, the topics of the course will be AI at high level,

**[19:34 -> 19:36]** machine learning, the basic definition by

**[19:36 -> 19:39]** expectant most of those already well known.

**[19:39 -> 19:43]** Probability fundamentals again is just a review of something that I expect you to know.

**[19:43 -> 19:46]** But then we will start entering into, let's say,

**[19:46 -> 19:53]** the most useful basics for deep learning models and for modern AI.

**[19:53 -> 19:57]** So like definition of the loss, the prediction rule,

**[19:57 -> 20:02]** and then deep learning with all the different architecture and task for supervised

**[20:02 -> 20:06]** and supervised different kind of current learning, generative approaches as we mentioned.

**[20:06 -> 20:09]** Right, so these are, let's say, the topics and objective.

**[20:09 -> 20:13]** And we will see applications in computer vision, right?

**[20:13 -> 20:18]** I mean, my personal expertise comes from these areas, so application in vision,

**[20:18 -> 20:22]** right, vision for machines, so robot, robotics,

**[20:22 -> 20:27]** The idea is that we want autonomous machines that are able to see the world,

**[20:27 -> 20:33]** understand what's going on, what is inside the scene, what are the objects, how the objects are

**[20:33 -> 20:40]** organized, eventually how I can navigate this space. So 2D information, 3D information, not only

**[20:40 -> 20:47]** images but videos, not only videos and visuals but language combined, semantics, so a combination

**[20:47 -> 20:55]** multiple kind of data, but yeah, mainly the goal of solving some tasks that is helpful for machines

**[20:55 -> 21:01]** and it's based on the ability to see the world. So in practice, just mimicking the ability of humans

**[21:01 -> 21:09]** for machines. Yeah, so to do 3D geometry, natural language processing, these are the kind of

**[21:10 -> 21:13]** topics we will refer to, we will mention during the course.

**[21:13 -> 21:19]** So, you will get to know the basics of machine learning and deep learning.

**[21:19 -> 21:23]** So, I mean, I expected the basics of shallow machine learning.

**[21:23 -> 21:30]** You already have them and that analysis because this was what I got from the answers you provided

**[21:30 -> 21:35]** me in the survey we did a few minutes ago.

**[21:35 -> 21:37]** But then we'll go to deep learning.

**[21:37 -> 21:42]** So you will learn how to read and understand the paper code included because most of the

**[21:42 -> 21:50]** technical reports, the paper at the conferences that will read, they come with a code. Of course,

**[21:50 -> 21:57]** you are engineer, you are in the computer engineering path, I expect you put your hands in the code.

**[21:58 -> 22:03]** I know that nowadays it's everything by coding. Someone else is coding this for me.

**[22:04 -> 22:11]** No. Okay, at the exam, we'll go through the code you produced and we'll ask questions

**[22:11 -> 22:16]** on the lines of the code because you should be able to tell us, I mean, the committee in the

**[22:16 -> 22:21]** sound, what that part of the code is doing, why it is formulated like that, what is the input of

**[22:21 -> 22:26]** this function, what is the output, what do, what are we doing with it, that part of the code, right?

**[22:26 -> 22:32]** So, understand the logic of the method, understand how to formalize it, understand how to code it.

**[22:34 -> 22:39]** You will learn how to design and implement your own machine learning model. So, a new algorithm,

**[22:39 -> 22:47]** eventually for a given problem and how to explain why you did it in that way. Because at the exam,

**[22:48 -> 22:53]** what you will be asked to do is a presentation of the project, right? So you have to do it and

**[22:53 -> 23:00]** you have to be able to communicate to others why you did that project in this way, why you decided

**[23:00 -> 23:07]** to solve this problem in that kind of approach. And this, I mean, we'll do also sort of exercise

**[23:07 -> 23:14]** during the course because we will have part of the course dedicated to paper presentation

**[23:15 -> 23:21]** and in practice it will be used for Santa papers. So you will have to read and to present to the

**[23:21 -> 23:26]** audience. So all of us, some of the technical papers, we will discuss them together.

**[23:28 -> 23:33]** Okay, so we will see how it will be structured. So we'll learn mainly for in-person lecture.

**[23:33 -> 23:37]** you will learn how to read and understand the paper,

**[23:37 -> 23:40]** mainly working in groups.

**[23:40 -> 23:43]** So both the project at the end of the course

**[23:43 -> 23:46]** and the paper presentation will be done in teams,

**[23:47 -> 23:50]** supported by me and the teaching assistant.

**[23:51 -> 23:53]** So you will learn again how to implement

**[23:53 -> 23:56]** in design, you method again, working in group

**[23:56 -> 23:58]** and you will have to present in front of the class

**[23:58 -> 23:59]** and at the exam.

**[23:59 -> 24:07]** Okay, so let's go through more specific details about the exam.

**[24:07 -> 24:13]** You see that the exam has three parts, paper presentation, project, and then you have really

**[24:13 -> 24:15]** the oral exam.

**[24:15 -> 24:19]** Okay, so paper presentation, what does it mean?

**[24:19 -> 24:25]** So I told you that the knowledge of machine learning, the most model part of machine learning

**[24:25 -> 24:29]** in AI is on this technical paper, published at conferences.

**[24:29 -> 24:36]** So what we will do is that more or less from half November on, maybe I mean, 10 of November,

**[24:36 -> 24:40]** something like that, we will start with a paper presentation.

**[24:40 -> 24:41]** What does it mean?

**[24:41 -> 24:47]** It means that you will be organizing groups, you will be assigned, you will have a paper

**[24:47 -> 24:53]** assigned, you will have approximately two weeks to read the paper and to present, I mean,

**[24:53 -> 24:57]** a short presentation of maximum 12 minutes, more or less.

**[24:57 -> 24:59]** You will work in group of four students,

**[24:59 -> 25:02]** so each group will have one paper to read.

**[25:03 -> 25:06]** And then, I mean, you will be asked to present

**[25:06 -> 25:08]** to the rest of the class, okay?

**[25:09 -> 25:12]** So it's a semi-op paper, I mean, related to some

**[25:12 -> 25:16]** of the sub-topics we will see during the, also the teaching

**[25:16 -> 25:17]** part, I mean the lecture part.

**[25:19 -> 25:22]** And that will be of interest for the project.

**[25:22 -> 25:26]** So I understand that this part of the course,

**[25:26 -> 25:33]** To some of you might be boring because, I mean, you say, okay, I have a paper to read.

**[25:33 -> 25:37]** So why I have to come to lecture and hear what other people are doing.

**[25:37 -> 25:40]** I don't care, I just study my own paper and that's fine.

**[25:40 -> 25:42]** I mean, you can do that.

**[25:42 -> 25:48]** But the point is that what we are going to present in the course, also from your colleagues,

**[25:48 -> 25:54]** is I mean, can provide you some ideas for the project afterwards, for the exam.

**[25:54 -> 25:57]** So it can be inspiring in the sense.

**[25:57 -> 25:58]** Besides the fact that, of course,

**[25:58 -> 26:01]** you will see that progressively the presentation,

**[26:01 -> 26:04]** I mean, maybe the first week will be a little bit tougher,

**[26:04 -> 26:05]** but then people will understand,

**[26:05 -> 26:07]** and you all understand what does it mean

**[26:07 -> 26:08]** to do the presentation.

**[26:08 -> 26:10]** Of course, there will be also a lecture.

**[26:10 -> 26:12]** So we'll guide you about how to compare it.

**[26:12 -> 26:16]** But anyway, I mean, having the experience of your colleague

**[26:16 -> 26:17]** will help you in general.

**[26:20 -> 26:23]** So papers will be assigned around the border.

**[26:23 -> 26:26]** you will have two weeks before the presentation.

**[26:26 -> 26:28]** We will have some time to adjust the calendar

**[26:28 -> 26:30]** because I understand that,

**[26:30 -> 26:31]** I mean, I start scheduling it,

**[26:31 -> 26:34]** there will be a spreadsheet with the assignment,

**[26:34 -> 26:36]** but I don't know for some reason,

**[26:36 -> 26:38]** some of you are not present in Turing,

**[26:38 -> 26:39]** but that specific day.

**[26:39 -> 26:41]** Okay, we can adjust it a bit.

**[26:41 -> 26:43]** So there will be a say buffer period

**[26:43 -> 26:46]** where we can adjust the calendar.

**[26:46 -> 26:47]** But then after that,

**[26:47 -> 26:50]** then we will freeze the schedule

**[26:50 -> 26:54]** and that will be kept for the rest of the course.

**[26:55 -> 26:57]** The presentation will be 12 minutes,

**[26:57 -> 26:59]** you will do it in group,

**[26:59 -> 27:01]** and you will be judged based on the comprehension

**[27:01 -> 27:03]** of the paper and the ability to explain it.

**[27:05 -> 27:09]** So let's put it in this way.

**[27:09 -> 27:12]** It's a gift of 10 points

**[27:12 -> 27:14]** because I'm not strict in this part.

**[27:14 -> 27:17]** I know that it is done during the course.

**[27:17 -> 27:19]** I know you are not experienced,

**[27:19 -> 27:23]** So you are learning, everybody in here is learning how to do it.

**[27:23 -> 27:29]** So it's just a matter of following some high level guidelines.

**[27:29 -> 27:32]** Be sure to not go over the 12 minutes.

**[27:32 -> 27:36]** Be sure to organize a slide in a certain way.

**[27:37 -> 27:40]** That's very basic kind of rules.

**[27:40 -> 27:42]** And then what will happen after the presentation

**[27:42 -> 27:44]** is that I will ask some questions.

**[27:44 -> 27:47]** And these will of course be part of the evaluation.

**[27:47 -> 27:50]** but they're very simple questions,

**[27:50 -> 27:52]** just to let the rest of the people in the room

**[27:52 -> 27:56]** be able to understand the content of that paper.

**[27:56 -> 27:59]** So again, it's an educational part of the course itself.

**[28:00 -> 28:04]** So I consider it, I mean, as an extra tool to judge you,

**[28:04 -> 28:06]** but it's a very mild, I mean,

**[28:06 -> 28:08]** it's really trying to help you in this way,

**[28:08 -> 28:10]** so you don't start from zero,

**[28:10 -> 28:11]** you start already from something,

**[28:11 -> 28:12]** which is different from zero,

**[28:12 -> 28:16]** because as I told you, I know that the course is very rich.

**[28:16 -> 28:20]** So in this part, I'm trying to be very gentle, let's say.

**[28:22 -> 28:27]** Yeah, so you see, as I told you,

**[28:27 -> 28:28]** you will be guided in a way.

**[28:28 -> 28:30]** So there will be a lecture, at least a video

**[28:30 -> 28:32]** dedicated to how to present a paper

**[28:34 -> 28:35]** and why we're doing it again,

**[28:35 -> 28:39]** because what I want to provide you is a tool

**[28:39 -> 28:41]** to become a lifelong learner.

**[28:41 -> 28:45]** This course will not exhaust all the information you need

**[28:45 -> 28:48]** to become a machine learner or to work tomorrow

**[28:48 -> 28:51]** in an area where AI is needed, okay?

**[28:51 -> 28:52]** Which means that you have to be able

**[28:52 -> 28:55]** to dig out of the information by yourself.

**[28:55 -> 28:57]** So the goal is teaching you how to do that,

**[28:57 -> 29:00]** how to become a lifelong learner in AI.

**[29:03 -> 29:08]** Now, you are a lot, more than 290 students.

**[29:09 -> 29:12]** I see that there is a media question in the chat.

**[29:15 -> 29:18]** Is the paper assigned to the group?

**[29:18 -> 29:21]** Does it mean we need to present only a part

**[29:21 -> 29:22]** of each component?

**[29:24 -> 29:27]** Okay, so you have to explain the entire paper.

**[29:27 -> 29:31]** You are four people, you organized among yourself

**[29:31 -> 29:33]** about who's going to present the task.

**[29:33 -> 29:35]** So let's say the introduction,

**[29:35 -> 29:38]** who's going to present the data set,

**[29:38 -> 29:39]** who's going to present the method,

**[29:39 -> 29:41]** who's going to present the results?

**[29:41 -> 29:46]** More or less, these are the four high level groups

**[29:46 -> 29:50]** of knowledge that you can extract from the paper.

**[29:51 -> 29:53]** So I'm not imposing it.

**[29:53 -> 29:56]** It's just up to you to decide who's doing what.

**[29:59 -> 30:03]** But we assured that if you're going to present

**[30:03 -> 30:07]** the introduction, I will ask you about the results.

**[30:07 -> 30:09]** Because each of you anyway has to read the little paper.

**[30:09 -> 30:11]** So it's not just that you divide the work

**[30:11 -> 30:14]** among the four of you, and then one reads only the introduction.

**[30:14 -> 30:16]** Let's use this.

**[30:16 -> 30:19]** So you have to read the whole paper.

**[30:19 -> 30:21]** And for the person who present the introduction,

**[30:21 -> 30:22]** you'll get a question about the results.

**[30:22 -> 30:24]** The person who will present the results

**[30:24 -> 30:29]** will get a question about the data set, and so on.

**[30:29 -> 30:33]** So the group for the paper presentation

**[30:33 -> 30:35]** will be assigned by me.

**[30:35 -> 30:37]** It's random.

**[30:37 -> 30:40]** And if you have some issue, we can try to adjust again.

**[30:40 -> 30:44]** So it's initially it's random, okay?

**[30:44 -> 30:47]** So we can do some fine adjustment.

**[30:47 -> 30:50]** That is for the paper presentation.

**[30:50 -> 30:53]** For the project, so for the exam,

**[30:53 -> 30:55]** the oral part of the exam,

**[30:55 -> 30:58]** the technical part of the exam, it's up to you.

**[30:58 -> 31:00]** You decide who's in your group.

**[31:00 -> 31:03]** So I believe that the random, let's say,

**[31:03 -> 31:07]** assignment at the beginning is helpful in some sense,

**[31:07 -> 31:10]** because maybe not all of you know each other.

**[31:10 -> 31:13]** So what I saw in the past is that some of the group

**[31:13 -> 31:15]** that is formed during the paper presentation

**[31:15 -> 31:17]** then is kept afterwards for the project.

**[31:17 -> 31:18]** But then, I mean, it's up to you.

**[31:18 -> 31:21]** The project presentation and the project for the exam

**[31:21 -> 31:23]** is up to you to decide your team.

**[31:24 -> 31:26]** So I hope I answered also the question

**[31:26 -> 31:27]** that we're in the chat.

**[31:29 -> 31:33]** Anyway, for the paper presentation, as you are a lot,

**[31:33 -> 31:46]** So I cannot really impose you to present the paper and it's also difficult to schedule all of you during the course itself.

**[31:46 -> 31:58]** So you can decide to not present a paper, which means that you don't start with this extra, I'd say maximum 10 point, you can get out of it.

**[31:58 -> 32:03]** And what will happen is that you will get more questions during the exam.

**[32:03 -> 32:07]** That's it. I mean, it's just to balance the fact that you didn't present.

**[32:07 -> 32:11]** But I mean, I understand because during the period of course,

**[32:11 -> 32:15]** maybe some of you is working, guys, not, I mean, that the timing does not match

**[32:15 -> 32:19]** to be present in the class. So I can understand it.

**[32:19 -> 32:21]** It might be difficult in this sense.

**[32:21 -> 32:25]** Okay. So let's go ahead.

**[32:25 -> 32:38]** Regarding the project, so again, together with the beginning of the presentation, we will also present the project topics.

**[32:38 -> 32:44]** I think there will be three or four proposals in terms of direction.

**[32:44 -> 32:49]** And each of the proposals, I mean, each of the projects

**[32:49 -> 32:52]** will contain something mandatory that we ask you to do

**[32:52 -> 32:55]** and some possible extension that you can try.

**[32:55 -> 32:58]** Usually what I see is that the students

**[32:58 -> 33:00]** like to do, I mean, one extension,

**[33:00 -> 33:02]** but of course it's appreciated.

**[33:02 -> 33:04]** If you propose three or four extensions,

**[33:04 -> 33:05]** you want to do all of them.

**[33:05 -> 33:07]** Well, of course it's appreciated, right?

**[33:07 -> 33:09]** But let's say there is a mandatory part

**[33:09 -> 33:11]** and an extension part.

**[33:11 -> 33:14]** You will work in team of four people.

**[33:14 -> 33:21]** There will be another sheet on the spreadsheet where you will indicate the members of the

**[33:21 -> 33:29]** group, the topic you want to work on such that before Christmas, the framework is very

**[33:29 -> 33:30]** clear.

**[33:30 -> 33:37]** And we will ask you to submit before the oral exam a technical report of your work, of the

**[33:37 -> 33:40]** project.

**[33:40 -> 33:42]** It will be in PDF form.

**[33:42 -> 33:45]** Of course, you will have also to upload the code

**[33:45 -> 33:46]** that you developed.

**[33:46 -> 33:48]** Melee and GITA blink, it's fine.

**[33:48 -> 33:50]** I want to use the zip.

**[33:50 -> 33:52]** I mean, upload it online, it's fine.

**[33:52 -> 33:54]** Everything will happen through the portal.

**[33:56 -> 34:00]** But in practice, I mean, differently from the previous years

**[34:00 -> 34:05]** where I was trying to teach students also how to formalize

**[34:05 -> 34:09]** or to structure research paper of the kinds of papers

**[34:09 -> 34:12]** that you have been reading during the course,

**[34:12 -> 34:16]** because this is the format in which scientists produce

**[34:16 -> 34:19]** and evaluate them in an end public result.

**[34:21 -> 34:26]** This educational goal with the large language model

**[34:26 -> 34:28]** becomes completely backwards,

**[34:28 -> 34:33]** because every one of you will just put some ideas online

**[34:35 -> 34:37]** to code, to charge a pt to Gemini

**[34:37 -> 34:41]** and ask this tool to write the full paper.

**[34:41 -> 34:42]** So it's completely useless.

**[34:42 -> 34:43]** Let's just be clear on that.

**[34:45 -> 34:46]** So these kind of tools,

**[34:46 -> 34:50]** I mean, let's just not hide behind a finger.

**[34:50 -> 34:53]** I mean, this is something you will use anyway, I know.

**[34:54 -> 34:58]** But then, I mean, what I ask you to produce as a report

**[34:58 -> 35:02]** will be just some specific answer in a form.

**[35:02 -> 35:04]** So I will ask you, there will be some specific question.

**[35:04 -> 35:06]** I will ask you to provide,

**[35:06 -> 35:08]** I mean, the report that you will provide

**[35:08 -> 35:11]** will be answering this specific question,

**[35:11 -> 35:13]** showing the results and discussing the results.

**[35:13 -> 35:15]** I mean, of course, you will be still able

**[35:15 -> 35:17]** to use large language models,

**[35:17 -> 35:20]** but at least it's, I mean, you don't have to waste your time

**[35:20 -> 35:23]** to write the introduction of the paper,

**[35:23 -> 35:24]** you don't have to waste your time

**[35:24 -> 35:27]** to organize a related work section,

**[35:27 -> 35:31]** which means that you know what people before you did

**[35:31 -> 35:33]** on that topic.

**[35:33 -> 35:36]** I believe that this kind of things that we are missing,

**[35:36 -> 35:38]** it's a pity that you don't learn how to do it,

**[35:38 -> 35:42]** but it's, I mean, it's how the world goes.

**[35:42 -> 35:44]** Anyway, I mean, then if you're interested

**[35:44 -> 35:46]** about how to do that,

**[35:46 -> 35:48]** it will be something that you will learn afterwards.

**[35:50 -> 35:55]** So you will be asked to upload this, your report

**[35:55 -> 35:57]** and your code 10 days before the oral exam,

**[35:57 -> 35:59]** then you come to the oral exam.

**[35:59 -> 36:08]** The project topics will be of course the same till the beginning of the next year course,

**[36:08 -> 36:10]** so the next edition of the course.

**[36:10 -> 36:17]** So there will be different exam dates where you can come and present one of the project

**[36:17 -> 36:21]** that you have selected among the three or four proposals.

**[36:21 -> 36:24]** But then next year the proposal will change.

**[36:24 -> 36:27]** So if you expect to do the exam after next September,

**[36:27 -> 36:31]** then of course, you will have to realign

**[36:31 -> 36:34]** with the new proposals that will appear

**[36:34 -> 36:36]** for the next edition of course.

**[36:36 -> 36:39]** And again, you have minimum six score maximum 10.

**[36:40 -> 36:42]** And the score even in this case is applied

**[36:42 -> 36:47]** to what you produce, what you upload on the board,

**[36:47 -> 36:50]** also the technical report and of the code,

**[36:50 -> 36:53]** of course, will be double check also during the exam.

**[36:53 -> 36:58]** So the oral exam consists in theoretical questions

**[36:59 -> 37:02]** about the lectures, because I'm here,

**[37:02 -> 37:06]** I mean, wasting my, let's say voice,

**[37:06 -> 37:08]** to tell you something, and the goal is that,

**[37:08 -> 37:11]** or what I hope is that what I'm telling you

**[37:11 -> 37:13]** is something that stays with you, right?

**[37:13 -> 37:15]** That you really want to learn.

**[37:15 -> 37:18]** So the content of our theoretical lecture

**[37:18 -> 37:21]** will be the main objective of the first question.

**[37:21 -> 37:24]** I will ask you during the oral exam.

**[37:24 -> 37:28]** And if you don't answer this basic course knowledge question,

**[37:28 -> 37:29]** you're feeling the exam.

**[37:29 -> 37:31]** Even if you spent six months,

**[37:31 -> 37:33]** or I don't know how many months working

**[37:33 -> 37:34]** on the project, I don't care.

**[37:34 -> 37:36]** You failed exam, you don't know the basics.

**[37:36 -> 37:40]** I mean, if you don't know how grad in the cent work,

**[37:40 -> 37:43]** which is the basic mathematical tool

**[37:43 -> 37:46]** to update the parameters in your deep network,

**[37:46 -> 37:49]** I mean, why should you do this course,

**[37:49 -> 37:50]** and why should you pass it?

**[37:50 -> 37:53]** means that you didn't get the basic information, right?

**[37:53 -> 37:56]** Or some other kind of, I'd say, subject

**[37:56 -> 37:57]** that we will see during the course.

**[37:57 -> 38:01]** So basic course knowledge is super important.

**[38:01 -> 38:05]** So it's relevant to fail or pass the exam.

**[38:06 -> 38:10]** And this is the kind of question you will get more.

**[38:10 -> 38:13]** I mean, you will get more of this kind of question

**[38:13 -> 38:16]** during your exam if you don't present the paper, okay?

**[38:16 -> 38:18]** So you will get more question on the theory part.

**[38:20 -> 38:24]** Then besides the basic course question, of course,

**[38:24 -> 38:28]** the objective of the oral is to let you present

**[38:28 -> 38:31]** the content of the project you've been working on.

**[38:31 -> 38:33]** Again, you are in group,

**[38:33 -> 38:35]** you will have something like 15 minutes to present

**[38:35 -> 38:38]** the results of your project,

**[38:38 -> 38:40]** and you will get question from the teaching assistant,

**[38:40 -> 38:41]** again, going through the code,

**[38:41 -> 38:43]** open the code, what is that?

**[38:43 -> 38:45]** Why is this doing it like this?

**[38:45 -> 38:47]** But also question like, okay,

**[38:47 -> 38:49]** you have been working on this project.

**[38:49 -> 38:53]** This project was based on a paper published two years ago.

**[38:53 -> 38:55]** Did you read the paper?

**[38:55 -> 38:57]** Yes, no. What is the content of the paper?

**[38:57 -> 39:01]** Why the authors of that paper decided to do this thing in this way?

**[39:01 -> 39:03]** Why are we asking this?

**[39:03 -> 39:07]** Because of course, the project build on something that has been published,

**[39:07 -> 39:10]** the author made some decision that you are just

**[39:10 -> 39:16]** inheriting for your project and you have to be aware of why this was done in that way.

**[39:16 -> 39:19]** It's not just again using the tool.

**[39:19 -> 39:22]** You're not here to use, to learn how to use tools.

**[39:22 -> 39:26]** You can do it every way, I mean, in your daily life.

**[39:26 -> 39:30]** There are millions of AI-based tools online, you can just use it,

**[39:30 -> 39:32]** exercise it, have fun.

**[39:32 -> 39:35]** The goal of this course is to let you understand what is behind.

**[39:35 -> 39:37]** The widest is done that way.

**[39:37 -> 39:44]** So if you didn't learn that, again, it's clear that you didn't get the main information from the course.

**[39:44 -> 39:51]** You see here some disclaimer, this is not a trial and error exam.

**[39:51 -> 39:57]** What I mean is that please, please, don't come at the exam just to try it out.

**[39:57 -> 40:00]** You will waste your time.

**[40:00 -> 40:06]** So try to get prepared, of course, I mean level of preparation depends, it's a personal

**[40:06 -> 40:13]** kind of thing, but it does not come to see that the oral exam just to try it out.

**[40:13 -> 40:15]** You can decide to postpone the oral.

**[40:15 -> 40:17]** I mean, don't do it the first date.

**[40:17 -> 40:19]** Come at the first date to see

**[40:19 -> 40:21]** which kind of question are asked to your colleagues,

**[40:21 -> 40:23]** okay, such that you are informed.

**[40:23 -> 40:25]** And then you decide to do it on the second date.

**[40:25 -> 40:29]** But don't just come at the exam to try it out.

**[40:29 -> 40:32]** It's, yeah, we are all wasting our time.

**[40:33 -> 40:35]** The code of the project will be checked,

**[40:36 -> 40:38]** don't cheat, which means,

**[40:38 -> 40:43]** I mean, don't let the code write the whole code for you.

**[40:43 -> 40:48]** or at least, I mean you can do it but then read it, okay? So try to understand why I

**[40:48 -> 40:53]** close the decide to write it in that way. So this is what I'm expecting that you at least

**[40:53 -> 40:59]** understand why something else, I mean an object, an AI based object did that thing for you in that way.

**[41:00 -> 41:06]** Okay, so for the present paper presentation, can I choose the paper? No, as I told you, it will

**[41:06 -> 41:12]** be assigned to you. I cannot make the presentation of mine assigned date because blah, blah, blah,

**[41:12 -> 41:16]** No problem, we'll try to adjust the calendar.

**[41:16 -> 41:21]** Will I get guidance with a very independent presentation? Yes, there will be one lecture that we get

**[41:21 -> 41:25]** to do that, or I'll do about how to do this.

**[41:25 -> 41:30]** Regarding the project, can I propose my own project? So I mean, some of you already trained

**[41:30 -> 41:35]** evolution and our natural maybe have some experience or some deep curiosity on solving

**[41:35 -> 41:39]** some specific task and they're really passionate and sometimes I get this question,

**[41:39 -> 41:42]** Can I solve this task for my project?

**[41:42 -> 41:45]** Well, it's very interesting, but unfortunately we can't,

**[41:45 -> 41:50]** because then it becomes a hell to correct.

**[41:50 -> 41:52]** So we cannot multiply the project.

**[41:52 -> 41:54]** So you have to stick to the three, four,

**[41:54 -> 41:56]** copies we're going to present.

**[41:57 -> 41:59]** Can I do the project alone or in two?

**[41:59 -> 42:00]** Again, no.

**[42:02 -> 42:09]** This kind of scenario can happen in the very last possible dates

**[42:09 -> 42:16]** before the next course or edition will start because at the end maybe some of you didn't

**[42:16 -> 42:21]** pass exam have to do it again the group already passed over I mean it's doing something else

**[42:21 -> 42:27]** passed over it's not there it's just that they are doing something else and so maybe you end up

**[42:27 -> 42:34]** being a group of two or three and or even you're just alone we can discuss about it but not

**[42:34 -> 42:37]** I mean as a standard thing, okay.

**[42:38 -> 42:41]** What computer facility I can use for the project Google Callup?

**[42:41 -> 42:44]** Google Callup offer GPU,

**[42:44 -> 42:49]** computation, so in practice we will set the projects

**[42:50 -> 42:52]** as that you can use those tools.

**[42:53 -> 42:57]** And of course this implies, let's say,

**[42:57 -> 43:00]** making a small version of the project itself,

**[43:00 -> 43:03]** but we'll try to use the tools which are freely available.

**[43:04 -> 43:09]** And how to choose a project will be up to you,

**[43:10 -> 43:11]** we'll present the topic.

**[43:11 -> 43:14]** I'm not proficient in Python, well, okay,

**[43:14 -> 43:16]** it's not the case, I would say.

**[43:17 -> 43:19]** Will I get guidance how to work on the project?

**[43:19 -> 43:21]** Yes, as we said.

**[43:23 -> 43:25]** Can I make the exam in a different session

**[43:25 -> 43:27]** that the rest, so see that the oral exam

**[43:27 -> 43:28]** in different session of the rest of my group?

**[43:28 -> 43:31]** No, the group is a group, you are sitting together.

**[43:31 -> 43:34]** Is your exam in English? Of course.

**[43:34 -> 43:38]** What will be asked during the exam? I think I clarified it.

**[43:38 -> 43:43]** So you will have theory question, you will have question on the algorithm using the project, in the code,

**[43:43 -> 43:50]** about the code, and there will be this question on the topic explained during the lectures.

**[43:50 -> 43:54]** Why are we doing this project? Well, this is what I will ask you.

**[43:54 -> 43:58]** So what was the task you are trying to solve in this project?

**[43:58 -> 44:11]** So of course we know, I mean, it's something that we are providing you, but that's part of the educational goal of this course and something again that you can spend in your city.

**[44:11 -> 44:18]** Having this GitHub project on your GitHub page and doing it well of course can be relevant.

**[44:18 -> 44:24]** Can I reject the final vote? Yes, I mean, for the next example session.

**[44:24 -> 44:29]** So what happens is that if you pass the, I mean,

**[44:29 -> 44:31]** if you pass the theory question

**[44:31 -> 44:33]** and you are going to present the project,

**[44:33 -> 44:37]** so after my, let's say initial assessment,

**[44:39 -> 44:41]** but then overall you don't have the project.

**[44:41 -> 44:43]** I mean, you don't have the exam,

**[44:43 -> 44:47]** I mean, you don't get the minimum 18 score, 18 score,

**[44:47 -> 44:49]** then for the next exam session,

**[44:49 -> 44:51]** you will have to change the project topic.

**[44:51 -> 44:55]** So you have four project topics, maybe you chose a project one.

**[44:55 -> 44:57]** Well, next time you have to choose among one of the other three.

**[44:57 -> 44:59]** Okay, you have to start from scratch.

**[44:59 -> 45:02]** Okay, so this is the reason why I'm telling you,

**[45:02 -> 45:03]** this is not a trial and error exam.

**[45:03 -> 45:06]** So it's, yeah, really it doesn't make any sense.

**[45:09 -> 45:11]** Okay, so why are you attending this course?

**[45:11 -> 45:14]** Again, the knowledge you are gaining here

**[45:14 -> 45:17]** is something you can spend for your thesis,

**[45:17 -> 45:19]** if you want to do research in the future, yes, thanks.

**[45:19 -> 45:25]** Yeah, four versus. Okay. Yes.

**[45:25 -> 45:35]** The human movement is the threshold to pass for the points or you can get also four points.

**[45:35 -> 45:45]** You can get four points by the representation. Although I mean, I have to say, I mean, even

**[45:45 -> 45:51]** if you get is you're not sufficient for the representation you are still allowed to come with your exam

**[45:51 -> 45:54]** okay so that's these things in good experiments.

**[45:54 -> 45:58]** Points are not the... I don't see that also if they are point to point.

**[45:58 -> 46:00]** Yeah yeah they are considered. They are considered.

**[46:00 -> 46:02]** Really is not the real need.

**[46:02 -> 46:06]** No exactly so this is the reason why I'm telling you I'm doing it's a gift.

**[46:06 -> 46:08]** It's a really gentle need that.

**[46:08 -> 46:12]** And for our watch time, these points,

**[46:12 -> 46:15]** like for example, we look at presentation, right?

**[46:15 -> 46:16]** Yes.

**[46:16 -> 46:20]** And the XNS, we are taking projects for.

**[46:20 -> 46:27]** Well, I mean, if you are sitting at the oral exam

**[46:27 -> 46:31]** before next September, so before the beginning

**[46:31 -> 46:34]** of an expedition of the course, the project are those ones.

**[46:34 -> 46:35]** Yes, project.

**[46:35 -> 46:37]** Yes.

**[46:37 -> 46:40]** The paper presentation, it's valid, it's kept, yes.

**[46:42 -> 46:47]** Then, is we decided to talk through the paper presentation?

**[46:48 -> 46:51]** Or are the examples on your points?

**[46:51 -> 46:52]** Yeah, of course.

**[46:52 -> 46:54]** So I have to sum what you missed.

**[46:54 -> 46:58]** So you have 10 extra points related to the extra question

**[46:58 -> 46:59]** that they've asked, yes.

**[47:01 -> 47:02]** Thank you.

**[47:02 -> 47:09]** I think it's in some way just to get the load.

**[47:09 -> 47:18]** To get the load, to get the owner, you have to surprise me.

**[47:18 -> 47:19]** Okay.

**[47:19 -> 47:24]** So have to come to the oral exam and really surprise me.

**[47:24 -> 47:27]** like I did, you asked to do, I mean,

**[47:27 -> 47:31]** mandatory part of the project and one of the possible extension,

**[47:31 -> 47:34]** but actually the four extension I did,

**[47:34 -> 47:36]** all of them because I had fun.

**[47:36 -> 47:39]** And moreover, Professor, I've read the paper,

**[47:39 -> 47:42]** and I think we can use that idea for this project.

**[47:42 -> 47:45]** So I try to implement it and I got this result.

**[47:45 -> 47:47]** The result is not really good.

**[47:47 -> 47:49]** I'm not sure, I mean,

**[47:49 -> 47:52]** exactly why I still have to work a little bit on it,

**[47:52 -> 47:54]** But I was so curious that I wanted to test it out.

**[47:56 -> 48:05]** Honor. Okay. So is this kind of passion that makes you get to the 30 plus points?

**[48:08 -> 48:13]** For those who skip the presentation is the early zone worth 20 points. Well, of course,

**[48:13 -> 48:17]** again, you see that you're like some since you will get extra pressure, you will also get the

**[48:17 -> 48:21]** possibility to get to the extract 10 points so you anyway have the

**[48:21 -> 48:28]** possibility to get to 30 so this should it's just repeating yeah

**[48:34 -> 48:43]** so we can they are not threshold but you understand that exactly what is the

**[48:43 -> 48:52]** real, real, real threshold for me is being able to answer the theory question. So that

**[48:52 -> 48:56]** is the signature question. If you don't answer to that, immediately you fill the sum, independently

**[48:56 -> 49:03]** of the fact that you did the presentation, 10 points, and so on. Okay, so I hope this

**[49:03 -> 49:09]** clarifies and thank you for having rise your hand. So I know that maybe when I present

**[49:09 -> 49:17]** I go fast or when I talk I go fast. So just feel free to raise your hand and ask question. Let's

**[49:17 -> 49:24]** keep it interactive. And even if it's just professor please go slower, it's fine. I understand that

**[49:24 -> 49:29]** I have the tendency. Since it's something that I mean it's I'm working in this area. I've been

**[49:29 -> 49:37]** working the last 15, 17 years. So to me it's like I'm telling you a story, me is passion, right?

**[49:37 -> 49:45]** but maybe sometimes it's too fast to be technical for you. So just ask to slow down, it's fine.

**[49:47 -> 49:55]** Okay, so why are you attending this course? The idea is that you can spend this knowledge

**[49:56 -> 50:04]** for your thesis, for your PhD in the future, for your startup, if you want to found a startup,

**[50:04 -> 50:07]** If you want to make money and go to War for Wall Street,

**[50:07 -> 50:11]** well, most of the financial model nowadays are based on AI.

**[50:11 -> 50:13]** You can go to War from Google,

**[50:13 -> 50:17]** Metah, Amazon, Media, some of the students that came out from

**[50:17 -> 50:21]** my team are actually sitting at Metah today at Amazon.

**[50:21 -> 50:24]** Some of them were Google and then move to Metah,

**[50:24 -> 50:25]** I mean, they're having fun.

**[50:25 -> 50:30]** Also Huawei, IBM, Siemens, Microsoft, Apple, and so on.

**[50:30 -> 50:33]** Of course, there are a lot of more practical,

**[50:33 -> 50:36]** or practical maybe application in terms of automatic,

**[50:36 -> 50:39]** like what you see in the last line.

**[50:39 -> 50:41]** And some of the project will be related to the topic

**[50:41 -> 50:45]** that you can really spend in these kind of companies.

**[50:46 -> 50:50]** And actually, if you look at the overview of companies

**[50:50 -> 50:53]** or startups that are working in this area

**[50:53 -> 50:56]** related to machine intelligence and AI,

**[50:56 -> 50:59]** well, this is just an overview of a few years ago.

**[50:59 -> 51:04]** I think, well, actually not few, is 10 years ago, 26th sin.

**[51:05 -> 51:10]** But if you go to 2024, then the overview becomes like this.

**[51:10 -> 51:12]** It's not even readable.

**[51:12 -> 51:15]** I mean, you have the PDF, and so maybe you can enlarge it

**[51:15 -> 51:18]** and read, but it's really huge.

**[51:18 -> 51:22]** I mean, the kind of, to start up and companies

**[51:22 -> 51:24]** that are working on the basis of AI.

**[51:24 -> 51:28]** So, and this is growing, it's a growing trend.

**[51:28 -> 51:31]** So it's something that you really can spend for your job

**[51:31 -> 51:32]** in the future.

**[51:34 -> 51:37]** And okay, let me see where is the mouse.

**[51:38 -> 51:42]** And again, here you're not sitting to use deep learning

**[51:42 -> 51:45]** as a black box, you're sitting here

**[51:45 -> 51:47]** to understand the model and architecture.

**[51:47 -> 51:48]** So what we do in my research group

**[51:48 -> 51:52]** is that we design new model, new algorithm for new tasks.

**[51:52 -> 51:54]** So from scratch, or of course, I mean,

**[51:54 -> 51:57]** from scratch nowadays means you take a paper

**[51:57 -> 52:00]** from a recent publication, trying to understand architecture,

**[52:00 -> 52:03]** and maybe understanding that half of it is completely useless

**[52:03 -> 52:06]** because people were just adding layers in the model

**[52:06 -> 52:08]** just to make it richer.

**[52:08 -> 52:10]** But then you understand the connection, the residual things,

**[52:10 -> 52:12]** maybe this piece can be removed.

**[52:12 -> 52:15]** This part is doing something that is completely useless

**[52:15 -> 52:17]** for the task, and then you redesign it

**[52:17 -> 52:19]** practically from scratch.

**[52:19 -> 52:22]** So you are building on something that exists,

**[52:22 -> 52:24]** but you are thinking about how to make it better,

**[52:24 -> 52:25]** how to make it more efficient,

**[52:25 -> 52:27]** how to make it more understandable,

**[52:27 -> 52:29]** how to make it more explainable,

**[52:29 -> 52:31]** depending on the task on the, let's say,

**[52:31 -> 52:34]** kind of objective that you have.

**[52:34 -> 52:36]** And yeah, I don't repeat it again,

**[52:36 -> 52:39]** but you can read it in the misline that I'm not doing.

**[52:41 -> 52:43]** And yeah, because everything can be spent

**[52:43 -> 52:44]** in your future job, right?

**[52:44 -> 52:46]** So these are what you see here

**[52:46 -> 52:49]** is something related to the application,

**[52:49 -> 52:51]** the job area and the money you can gain

**[52:51 -> 52:53]** out of these kind of experience.

**[52:53 -> 52:54]** But it's quite old,

**[52:54 -> 52:57]** is maybe from two or three years ago.

**[52:57 -> 53:00]** If you go to the links that you see here,

**[53:00 -> 53:04]** which are most recent AI index report from Stanford,

**[53:04 -> 53:06]** then you will see that practically the statistics

**[53:06 -> 53:08]** is confirmed or even better.

**[53:11 -> 53:16]** Okay, so now let's start to dig in some of the concepts.

**[53:17 -> 53:22]** So I'm sure that's, I mean, AI you've heard about it.

**[53:22 -> 53:25]** There are movies nowadays based on AI.

**[53:25 -> 53:29]** There is blog posts based on AI.

**[53:29 -> 53:31]** So maybe you already know the history,

**[53:31 -> 53:33]** but let me just go quickly over it.

**[53:33 -> 53:36]** So first of all, this name, artificial intelligence

**[53:36 -> 53:38]** is quite misplaced.

**[53:39 -> 53:41]** I mean, it's artificial,

**[53:41 -> 53:43]** but the moment is not really intelligent,

**[53:43 -> 53:47]** or at least the idea was to be able to mimic

**[53:47 -> 53:52]** the ability of the intelligence of a human into machines.

**[53:52 -> 53:55]** And it's a term that was born in the 1950s.

**[53:55 -> 53:59]** But the truth is that, yeah, since the beginning,

**[53:59 -> 54:02]** the idea was to be able to mimic, let's say,

**[54:02 -> 54:04]** the output of intelligence,

**[54:04 -> 54:06]** so the ability to solve specific tasks,

**[54:06 -> 54:08]** but not necessarily all the inherent

**[54:08 -> 54:12]** and internal wiring that intelligence need.

**[54:12 -> 54:16]** So all the reasoning level is something that is coming

**[54:16 -> 54:20]** more recently into the table of researcher

**[54:20 -> 54:24]** and people working on AI.

**[54:24 -> 54:25]** At the beginning, the goal was mainly

**[54:25 -> 54:29]** try to reproduce some abilities that apparently were based

**[54:29 -> 54:31]** on intelligence from human.

**[54:31 -> 54:38]** And indeed, the idea was to having some high-level rules,

**[54:39 -> 54:44]** logic rules, think about it as a set of if and then close,

**[54:44 -> 54:51]** and then close, which then are applied and executed by a computer, right?

**[54:51 -> 54:59]** There has to follow this structure of rules. And so the typical reference is a chess or checkers,

**[54:59 -> 55:07]** so games that has to be solved by one of these methods. But yeah, I mean, everything is predefined,

**[55:07 -> 55:11]** And so the logic, the definition of the method,

**[55:11 -> 55:15]** was just, let's say, handmade,

**[55:15 -> 55:18]** and then the computer is executing it.

**[55:18 -> 55:20]** And of course, there was research

**[55:20 -> 55:23]** about how to do it effectively.

**[55:23 -> 55:27]** But, towards these years from 1950s,

**[55:27 -> 55:30]** which is also the period where Alan Turing

**[55:30 -> 55:34]** will think about his Turing test, and the 1980s,

**[55:34 -> 55:37]** There were some, let's say, winter period of AI

**[55:37 -> 55:40]** because at the beginning, I mean, the idea was cool

**[55:40 -> 55:44]** but nothing seemed to practically work.

**[55:44 -> 55:47]** And then going towards the 1980s,

**[55:47 -> 55:52]** statistical learning started to enter the scene.

**[55:52 -> 55:54]** And of course, we start talking about

**[55:54 -> 55:56]** super vector machine and that kind of approaches

**[55:56 -> 55:58]** that you have started already.

**[55:58 -> 56:02]** So that part of statistical learning started to work.

**[56:02 -> 56:04]** And we have machine learning.

**[56:04 -> 56:08]** So we really see the flourishing, I mean,

**[56:08 -> 56:11]** the core of AI in machine learning part

**[56:11 -> 56:13]** and start us to produce results.

**[56:13 -> 56:17]** And you see that the kind of application

**[56:17 -> 56:21]** for machine learning, it's a symbolic reference

**[56:21 -> 56:26]** is recognizing a spam or legitimate email.

**[56:26 -> 56:29]** This was one of the tasks that was originally solved

**[56:29 -> 56:33]** by method based on machine learning, statistical learning,

**[56:33 -> 56:37]** Because of course, I mean, in an email,

**[56:37 -> 56:41]** it cannot really define a standard rule

**[56:41 -> 56:44]** to define what is spam and what is ham, legitimate email.

**[56:44 -> 56:46]** So something that is spam for you

**[56:46 -> 56:48]** cannot be spam for another person.

**[56:48 -> 56:50]** So it has to be based on the statistics

**[56:50 -> 56:51]** to be able to do that.

**[56:51 -> 56:56]** But actually, this kind of method

**[56:56 -> 57:01]** are work and have been working in your email account

**[57:01 -> 57:04]** account since the 1990s.

**[57:04 -> 57:07]** Of course, maybe you were not even born.

**[57:07 -> 57:12]** So from then on, it's something really, really standard.

**[57:12 -> 57:14]** And you see machine learning is a sub-part

**[57:14 -> 57:16]** of artificial intelligence.

**[57:16 -> 57:19]** Artificial intelligence is much bigger umbrella.

**[57:19 -> 57:22]** It contains a heuristic method.

**[57:22 -> 57:27]** It contains, as we said, some logic-based approaches.

**[57:27 -> 57:30]** So it's much bigger with respect to just machine learning,

**[57:30 -> 57:32]** which is a sub-part of artificial intelligence,

**[57:32 -> 57:35]** and it is based on statistical learning.

**[57:36 -> 57:38]** And then from the 2010 on,

**[57:38 -> 57:42]** we have deep learning methods, okay?

**[57:42 -> 57:45]** And you see here that the reference approach

**[57:45 -> 57:48]** is related to images, recognizing cats,

**[57:48 -> 57:52]** which is a very basic kind of task researchers love to do,

**[57:53 -> 57:56]** because exactly, I mean, the first demonstration

**[57:56 -> 58:01]** that deep learning model could work properly was on images.

**[58:02 -> 58:05]** So the interesting thing here is that,

**[58:05 -> 58:07]** I mean, you see the history,

**[58:07 -> 58:09]** one of the first stars that was solved

**[58:09 -> 58:11]** was related to language, right?

**[58:11 -> 58:14]** So email reading and trying to discriminate.

**[58:14 -> 58:15]** And then we passed three images

**[58:15 -> 58:17]** which were considered more complex.

**[58:17 -> 58:19]** Nowadays we are going back.

**[58:19 -> 58:23]** So there have been a new wave mostly focusing on language

**[58:23 -> 58:27]** And then multimodality came afterwards.

**[58:27 -> 58:30]** So it goes like a different kind of interest.

**[58:30 -> 58:34]** But anyway, AI is not only language.

**[58:34 -> 58:35]** It's not only charge-up-t.

**[58:35 -> 58:40]** There is a world of other method, AI-based.

**[58:40 -> 58:44]** It's not only generating images and making you more beautiful

**[58:44 -> 58:46]** in your picture.

**[58:46 -> 58:49]** There's a lot of other things and a lot of methods

**[58:49 -> 58:52]** that are based on AI approaches, and we'll try to dig in.

**[58:52 -> 58:56]** Okay, so I think that the oral history, it's clear.

**[58:56 -> 58:59]** And you also see that deep learning

**[58:59 -> 59:02]** is a sub-part of machine learning.

**[59:02 -> 59:05]** So please don't say, well, machine learning is a thing.

**[59:05 -> 59:06]** Deep learning is another.

**[59:06 -> 59:11]** No, deep learning is just one particular kind

**[59:11 -> 59:15]** of machine learning approaches, which is a larger group,

**[59:15 -> 59:18]** which is within artificial intelligence,

**[59:18 -> 59:21]** which is even a larger group.

**[59:21 -> 59:25]** Okay, so I think this figure made it very, very clear.

**[59:25 -> 59:35]** And of course, I mean in 2010, there has been a sort of perfect storm because there was

**[59:35 -> 59:45]** started to be computational resources that became cheaper, the ability to use GPUs, digital

**[59:45 -> 59:51]** data that are becoming available, massively available through the web.

**[59:51 -> 59:57]** And then I mean the logical evolution of narrow network that became deep narrow network.

**[59:57 -> 60:02]** So all this component provided us the ability to define

**[60:02 -> 60:07]** normal deep learning model and the new wave for AI solution.

**[60:07 -> 60:14]** Now artificial intelligence as we said, the name per se, it's really a buzzword.

**[60:14 -> 60:17]** but let's try to understand how to formalize it.

**[60:18 -> 60:20]** When we see artificial intelligence,

**[60:20 -> 60:25]** we can think about thinking like a human

**[60:25 -> 60:30]** because we said originally it was defined as a way

**[60:30 -> 60:35]** to mimic the ability of humans like the human intelligence.

**[60:35 -> 60:38]** So but then practically how do we formalize it?

**[60:38 -> 60:40]** Is it thinking humanly?

**[60:40 -> 60:42]** Is it thinking rationally?

**[60:42 -> 60:45]** So being sure that everything is super structured

**[60:45 -> 60:48]** and rational or acting like a human,

**[60:48 -> 60:52]** so trying to make the behavior or acting rationally.

**[60:52 -> 60:55]** So acting but following specific structured rule.

**[60:56 -> 60:59]** Let's try to understand each of these definitions.

**[60:59 -> 61:03]** So thinking humanly, what does it mean?

**[61:03 -> 61:07]** At the moment, we don't know exactly how human think.

**[61:07 -> 61:09]** I mean, there are a lot of studies,

**[61:09 -> 61:12]** They are starting to put probes also directly

**[61:12 -> 61:14]** in the brain of humans.

**[61:15 -> 61:19]** And so we know, we started collecting information

**[61:19 -> 61:22]** about how a human think,

**[61:22 -> 61:25]** but we don't have conclusive results at the moment.

**[61:25 -> 61:28]** And there's also a lot of research in neuroscience.

**[61:28 -> 61:31]** There's lots of research in psychology

**[61:31 -> 61:34]** and specifically cognitive science,

**[61:34 -> 61:38]** not to understand how an adult learn

**[61:38 -> 61:40]** are how a kid learn.

**[61:40 -> 61:43]** Because in the future, if we want autonomous agent

**[61:43 -> 61:46]** able to learn by themselves, I want

**[61:46 -> 61:49]** them to be able to learn like a kid, not like an adult.

**[61:49 -> 61:51]** Kid learns much faster.

**[61:51 -> 61:53]** They interact with the world differently

**[61:53 -> 61:54]** with respect to the nodal.

**[61:54 -> 61:56]** And it's a slope.

**[61:56 -> 62:00]** I'd say that how fast the learning core

**[62:00 -> 62:04]** grows, which makes an autonomous agent being

**[62:04 -> 62:08]** able to adapt to new situation in the world.

**[62:08 -> 62:12]** So there's a lot of studies really fascinating in this area,

**[62:12 -> 62:16]** but at the moment, we don't know exactly how to formalize them

**[62:16 -> 62:20]** and how to make them something that can be translated into code

**[62:20 -> 62:25]** and can be provided to a machine to execute what human thinking needs.

**[62:25 -> 62:26]** Right?

**[62:26 -> 62:30]** OK, so this definition is not the one we want to adopt.

**[62:30 -> 62:31]** Acting humanly.

**[62:31 -> 62:35]** Well, I mentioned the Turing test, right?

**[62:35 -> 62:38]** and I believe you all have heard about it.

**[62:38 -> 62:43]** So Turing stated that we should check the ability

**[62:43 -> 62:48]** of a machine on the basis of what a human can evaluate.

**[62:48 -> 62:52]** So we have a human that is interacting with something else,

**[62:52 -> 62:56]** which can be either another human or an eye-based system.

**[62:56 -> 62:59]** And if the human interrogator is, I mean,

**[62:59 -> 63:03]** not able to distinguish if he or she is interacting

**[63:03 -> 63:06]** with another human being or with a machine,

**[63:06 -> 63:09]** then the Turing test is passed.

**[63:09 -> 63:14]** And AI is, I mean, practically solved.

**[63:14 -> 63:16]** Well, nowadays we see that AI system

**[63:16 -> 63:18]** are able to answer our question.

**[63:18 -> 63:20]** Do we consider them human?

**[63:20 -> 63:23]** Not really.

**[63:23 -> 63:26]** Even because, I mean, natural language processing

**[63:26 -> 63:28]** and ability to communicate is only a part

**[63:28 -> 63:32]** of what we expect from an AI system.

**[63:32 -> 63:42]** Of course, internally it has to represent knowledge, store knowledge, have a knowledge graph to be able to retrieve the information it needs, depending on the task.

**[63:42 -> 63:50]** I mean, in the kind of question we are asking should be able to do automated reasoning as a tool do we are going in that direction, but this still not solved.

**[63:50 -> 63:59]** There are many tasks in which even foundation model or large models are not able to find a good solution.

**[63:59 -> 64:05]** Moreover, okay, now methods, I mean machines can understand vision,

**[64:05 -> 64:10]** the revision and preceding object is something which is already part of foundation models,

**[64:10 -> 64:13]** but robotics is far.

**[64:13 -> 64:18]** I mean, robotics mean having a really robotic agent doing something.

**[64:18 -> 64:22]** So these two in tests should not be applied to just language.

**[64:22 -> 64:26]** It should be applied to a machine that does thing

**[64:26 -> 64:30]** in the way in which a human behaves as a human,

**[64:30 -> 64:32]** like acting humanly, right?

**[64:32 -> 64:33]** So if you want to go in that direction,

**[64:33 -> 64:37]** at least we have to get to this kind of robotics application,

**[64:37 -> 64:40]** manipulating object, which is still not there.

**[64:40 -> 64:45]** So the first of all, the AI doing tests is not passed yet,

**[64:45 -> 64:48]** but besides this, I will really sure we want to go

**[64:48 -> 64:57]** that direction. Is this what we defined for AI? I doubt it. And the reason why I doubt

**[64:57 -> 65:04]** it is that if we follow this direction, it means that computer science for AI is like

**[65:04 -> 65:09]** thinking about aeronautical engineering and say the goal of the field is making machines

**[65:09 -> 65:16]** that fly soil exactly like pigeons that other pigeons are fooled by this. So we have a logic

**[65:16 -> 65:22]** based on deception. So we say we want to fool a human, right? This doesn't make any sense. And I

**[65:22 -> 65:29]** mean, this is the parallel with birds, right? So our analytical engineer started to develop when

**[65:29 -> 65:37]** we thought about wind tunnels, when we think about physics and the loads of flying, right?

**[65:37 -> 65:43]** So it's a completely different way to face the problem from an engineering point of view,

**[65:43 -> 65:48]** and to formalize it with respect to just saying we need to fool humans. This is

**[65:48 -> 65:53]** not enough. Okay, we want quantitative measure even because we can deceive

**[65:53 -> 65:57]** humans in different ways, right? And even depends on which kind of interrogator

**[65:57 -> 66:01]** you're interacting with. So this does not work. We need something more

**[66:01 -> 66:08]** practical and quantitative to define AI. So there has been a lot of evolution of

**[66:08 -> 66:15]** these two in test, new ways to define it. There are lots of perception tests that comes out to

**[66:15 -> 66:21]** evaluate how good is a foundation model. I'm sure you have seen, I mean, there has been the news

**[66:22 -> 66:27]** from time to time, oh, the new model from, you know, anthropic, you see, you have this table,

**[66:27 -> 66:32]** well, it passed all the exam of this university, it passed the mathematical test, it passed this,

**[66:32 -> 66:38]** it passed that these are all the kind of tests we are trying to propose like intelligence tests

**[66:38 -> 66:44]** to this foundation model. They are interesting. They are a new version of let's say the Turing

**[66:44 -> 66:49]** test, although they are not really fully satisfying to understand what the model is doing, what's

**[66:49 -> 66:53]** the reasoning behind it and if we are really getting to what we need.

**[66:53 -> 67:03]** Thinking rationally, so what does it mean? Well, this goes more into the direction of

**[67:04 -> 67:13]** philosophers. So trying to idealize what thinking means, how it should be done in a logic and

**[67:13 -> 67:25]** cows away, right? But doing this means that we need to formalize this logic concept in

**[67:25 -> 67:33]** something again that can be consumed by a computer. And this is not easy, okay? First

**[67:33 -> 67:40]** of all, it's not easy. And second of all, it extract, I mean, it abstract knowledge with

**[67:40 -> 67:42]** with respect to the real world.

**[67:42 -> 67:45]** You know, philosopher, live in a world without friction, right?

**[67:45 -> 67:48]** But we are engineers, friction is there.

**[67:48 -> 67:52]** You have to interact with the real world, uncertainty is there.

**[67:52 -> 67:56]** So, obstructing this knowledge is partially interesting,

**[67:56 -> 67:59]** but I mean, first of all, it's difficult to formalize

**[67:59 -> 68:00]** and second of all,

**[68:00 -> 68:03]** does not really ring us in the right direction.

**[68:04 -> 68:05]** Okay.

**[68:05 -> 68:12]** Then, thinking rationally is not exactly the direction we want.

**[68:12 -> 68:18]** Acting rationally, well, here we start in going in the right direction.

**[68:18 -> 68:22]** Irrational agent asks to achieve the best outcome, right?

**[68:22 -> 68:27]** So it defines the task and the target.

**[68:27 -> 68:32]** You have to go from A to B and you want to find a model that is able to do that.

**[68:32 -> 68:38]** So you define, let's say, target, you have the data to extract information to be able

**[68:38 -> 68:45]** to go from A to B. Of course, the data are noisy, so there is a certain level of uncertainty.

**[68:45 -> 68:47]** But the goal is very clear.

**[68:47 -> 68:51]** We can measure how close we get to the goal, right?

**[68:51 -> 68:55]** So the goal is very well, can be very well defined.

**[68:55 -> 68:57]** We can measure how good we are.

**[68:57 -> 69:02]** So quantitatively, if you are getting closer to the goal or not,

**[69:02 -> 69:05]** and then certainty is there due to the noise of the data,

**[69:05 -> 69:06]** and this is the information in a way

**[69:06 -> 69:09]** that we have to use to get to the goal.

**[69:09 -> 69:12]** So racial agents, so acting racially

**[69:12 -> 69:18]** is what we use to formalize AI nowadays.

**[69:18 -> 69:23]** And so in practice, this is the overall figure

**[69:23 -> 69:25]** you can think about.

**[69:25 -> 69:28]** you want to get information from the environment,

**[69:28 -> 69:32]** which is your data, you know that you need to solve a task,

**[69:32 -> 69:33]** right?

**[69:33 -> 69:36]** And you want to understand how cool you get to this task.

**[69:36 -> 69:38]** And eventually, I mean, in very specific kind

**[69:38 -> 69:40]** of learning procedure, you can also

**[69:40 -> 69:44]** decide to adjust the procedure you get to the target.

**[69:44 -> 69:49]** So like, kind of reinforcement learning kind of loop, right?

**[69:49 -> 69:53]** But I think racially is exactly what we want to do,

**[69:53 -> 69:54]** is to formalize the problem.

**[69:54 -> 69:55]** Now, what does it mean?

**[69:55 -> 69:57]** It means that everything we are doing

**[69:57 -> 70:00]** is optimizing a utility function.

**[70:00 -> 70:01]** So we know where we want to go

**[70:01 -> 70:03]** and we let the machine do it.

**[70:03 -> 70:08]** So now, let's bring this concept into today's words.

**[70:09 -> 70:11]** You have heard from the news, certainly.

**[70:11 -> 70:16]** Oh, on Tropic or OpenAI decided to do that experiment

**[70:16 -> 70:18]** and they asked the model to do X.

**[70:18 -> 70:21]** And look, that model decided to go on internet

**[70:21 -> 70:22]** and find the solution.

**[70:22 -> 70:24]** Well, it's natural.

**[70:24 -> 70:27]** You're not putting guardrails to the model, right?

**[70:27 -> 70:30]** You're just saying you have to go there.

**[70:30 -> 70:31]** Okay, you have to go from A to B.

**[70:31 -> 70:33]** That's the target.

**[70:33 -> 70:38]** You can be sure, and it's guaranteed

**[70:38 -> 70:42]** that if the model find a shortcut to get to the target,

**[70:42 -> 70:44]** it will use it.

**[70:44 -> 70:45]** Why to be surprised about it?

**[70:45 -> 70:48]** It's natural, it's the utility function.

**[70:48 -> 70:50]** We are optimizing the model

**[70:50 -> 70:54]** to be able to get to the target in the most efficient

**[70:54 -> 70:56]** and effective possible way.

**[70:56 -> 71:00]** So if it escapes and find its own solution,

**[71:00 -> 71:03]** well, it's exactly what we are asking to the model.

**[71:03 -> 71:06]** If you don't put guardrails, it will do it.

**[71:07 -> 71:10]** So this is just to, I mean, make it clear

**[71:10 -> 71:14]** that all AI model have this kind of logic

**[71:14 -> 71:16]** and follow this idea of acting rationally.

**[71:16 -> 71:21]** So we want and we need to reach a target.

**[71:21 -> 71:25]** I provide you with data where the information are

**[71:25 -> 71:28]** and you have to extract information out of that data

**[71:28 -> 71:32]** to be able to get to the target, do it by yourself.

**[71:32 -> 71:34]** You're free to find a way to do it.

**[71:34 -> 71:37]** Well, then if there is a bias in the data,

**[71:37 -> 71:40]** if there is one particular kind of feature

**[71:40 -> 71:42]** that is a spurious feature,

**[71:42 -> 71:45]** because I mean, for some reason appear frequently

**[71:45 -> 71:51]** some historical reason and in theory we would not like the model to use it. It's there. I mean,

**[71:51 -> 71:57]** if you don't explicitly put constraints, it will use it. It is its own job, maximizing the utility.

**[71:57 -> 72:05]** It will do it. Okay. Now, acting racially uses practically the same kind of knowledge that we

**[72:05 -> 72:10]** were listing before for the Turing test, knowledge representation, automatic reasoning, combination

**[72:10 -> 72:13]** natural language processing, computer vision,

**[72:13 -> 72:15]** they're trying to reach the color of robotics,

**[72:15 -> 72:17]** but it's just formalizing a different way.

**[72:17 -> 72:20]** So all you have to focus on is the fact that you are defined

**[72:20 -> 72:24]** as utility function, you want to obtain a specific objective,

**[72:24 -> 72:26]** and you measure how far you are with respect to the objective

**[72:26 -> 72:27]** you are getting through.

**[72:27 -> 72:30]** That's the logic, but the tools in the middle

**[72:30 -> 72:33]** it's practically the same to solve the AI Turing test.

**[72:36 -> 72:39]** Well, we'll focus, of course, mainly in the machine learning

**[72:39 -> 72:43]** in terms of theory or a division of the algorithm.

**[72:43 -> 72:46]** And then we'll see application in computer vision

**[72:46 -> 72:48]** and robotics, but also combination

**[72:48 -> 72:50]** with semantics and natural language processing.

**[72:50 -> 72:53]** But then machine learning, right?

**[72:53 -> 72:56]** So learning, we need to measure, right?

**[72:56 -> 72:58]** Again, we are engineer, we measure.

**[72:58 -> 73:01]** Don't go by coding.

**[73:01 -> 73:03]** Something else, do something for me.

**[73:03 -> 73:05]** And I'm satisfied because with a lot of words

**[73:05 -> 73:08]** is convincing that it did the right thing.

**[73:08 -> 73:09]** No, I want numbers.

**[73:09 -> 73:14]** I want tables. I want to quantification. I'm an engineer. If I don't see the table, I don't trust you.

**[73:15 -> 73:19]** Okay. So how do we quantify this? What does it mean? Machine learning.

**[73:20 -> 73:27]** Okay. So to define learning for a machine, we need experience. We need a task. We need a performance measure.

**[73:27 -> 73:39]** And what we expect is that an agent learns when its performance at a task T measured by the performance measure P improves with experience.

**[73:39 -> 73:46]** Okay, so what we expect is this kind of curve the more data you provide to your model the better is the performance of course

**[73:46 -> 73:50]** a certain point with billions of data you expect to see a plateau

**[73:50 -> 73:54]** Especially if you start creating synthetic data, which is what we see nowadays

**[73:55 -> 74:00]** There's no more human data. We start creating synthetic ones and the plateau states there

**[74:00 -> 74:05]** But as I told you the most interesting part is not really let's say the plateau part

**[74:05 -> 74:07]** is this part of the court?

**[74:07 -> 74:12]** If I have a limited amount of samples from a new task,

**[74:12 -> 74:14]** how do I make this curve?

**[74:14 -> 74:17]** I mean, the slope of this curve go higher, right?

**[74:17 -> 74:19]** So make it faster learning.

**[74:19 -> 74:20]** That's the core.

**[74:20 -> 74:23]** I mean, the part where there's still a lot of research.

**[74:23 -> 74:26]** So we need a computer to do well at a task

**[74:26 -> 74:29]** without manually building its competence.

**[74:29 -> 74:31]** So the computer has to extract information

**[74:31 -> 74:33]** directly from the data.

**[74:33 -> 74:35]** I'm passing to it the data.

**[74:35 -> 74:40]** I'm not passing it logical rules if then close, no.

**[74:40 -> 74:42]** I'm not providing a structure in this sense.

**[74:42 -> 74:45]** I just want the model to extract information

**[74:45 -> 74:46]** directly from data.

**[74:48 -> 74:50]** Now, of course, I mean,

**[74:50 -> 74:52]** I mean, this is what I want for the most modern AI,

**[74:52 -> 74:55]** but going through the history of machine learning,

**[74:55 -> 74:58]** the kind of task I've been also formalized originally,

**[74:58 -> 75:01]** like just based on some specific rules.

**[75:01 -> 75:04]** So these are just some examples of what we meaning

**[75:04 -> 75:06]** will experience, what we mean with task,

**[75:06 -> 75:08]** what we mean with the performance

**[75:08 -> 75:10]** in different kind of scenario,

**[75:10 -> 75:13]** like recognizing handwritten words,

**[75:13 -> 75:15]** of course, is not, I mean,

**[75:15 -> 75:17]** we cannot recognize handwritten words

**[75:17 -> 75:20]** or handwritten digits with specific rules.

**[75:20 -> 75:22]** So think about someone that tells you,

**[75:22 -> 75:23]** you have to read my letter.

**[75:23 -> 75:25]** I mean, I'm a handwriting something, my notes,

**[75:25 -> 75:27]** and there are some numbers,

**[75:27 -> 75:30]** and I want an automatic system to read my numbers.

**[75:30 -> 75:34]** Now, I do the two or the zero in a certain way,

**[75:34 -> 75:37]** and there's no logic rule that says

**[75:37 -> 75:39]** how that number has to be done.

**[75:39 -> 75:43]** So for instance, I mean, I do the zero with a pen stroke,

**[75:43 -> 75:45]** but I don't close it, so it's a circle,

**[75:45 -> 75:48]** but I mean, it does not close really the zero.

**[75:48 -> 75:51]** Some others does some ribbon.

**[75:51 -> 75:55]** So there's no specific rule, or if then close,

**[75:55 -> 75:57]** I can define a number, right?

**[75:57 -> 76:00]** So it's something that has to be extracted from the data.

**[76:01 -> 76:05]** So what changes in the logic with respect to,

**[76:05 -> 76:07]** let's say, all statistical learning

**[76:07 -> 76:09]** and the new machine learning model.

**[76:09 -> 76:10]** And here I'm talking about something

**[76:10 -> 76:12]** that happened in the 80s, right?

**[76:12 -> 76:16]** So we are still in the very first AI, let's say revolution,

**[76:16 -> 76:19]** I mean, the very first kind of formalization of the problem.

**[76:19 -> 76:22]** Now originally it was, I gave you the data,

**[76:22 -> 76:25]** I gave you the program, so I gave you the rules.

**[76:25 -> 76:28]** And then I asked the computer to produce the output, right?

**[76:28 -> 76:31]** So this is programming with data

**[76:31 -> 76:35]** and a original logic of what AI was thought about.

**[76:35 -> 76:39]** So I just want the computer to execute something I ask.

**[76:39 -> 76:42]** But this kind of logic, it's difficult for programmers,

**[76:42 -> 76:44]** it's brittle because you have to anyway,

**[76:44 -> 76:46]** anytime you have a corner case,

**[76:46 -> 76:50]** you have to reformize the program itself

**[76:50 -> 76:51]** and doesn't work well.

**[76:51 -> 76:54]** So what's, and this is the example of recognizing

**[76:54 -> 76:55]** digit numbers, right?

**[76:55 -> 76:57]** So what is that?

**[76:57 -> 77:00]** Whoa, which is a two, which is a seven.

**[77:00 -> 77:02]** I mean, there's no logic rule I can use to define them.

**[77:02 -> 77:04]** I have to learn it from the data.

**[77:05 -> 77:06]** How to spam.

**[77:07 -> 77:10]** Maybe we can say all the emails

**[77:10 -> 77:12]** that contain the words Viagra will okay.

**[77:12 -> 77:16]** It goes to a spam, fine, but that's just one rule.

**[77:16 -> 77:18]** We cannot do it for all the possible words.

**[77:18 -> 77:20]** And that depends on the user, right?

**[77:20 -> 77:23]** So there's no logic rule for that.

**[77:23 -> 77:26]** And just provide you another example.

**[77:26 -> 77:32]** So Netflix, before being the two-ton kind of thing

**[77:32 -> 77:35]** on our days, it's a very old company.

**[77:35 -> 77:37]** There was a lot of people working there

**[77:37 -> 77:43]** and developing AI models to solve their own tasks,

**[77:43 -> 77:46]** the tasks that they need to sell their product.

**[77:46 -> 77:49]** So this kind of programming with data logic

**[77:49 -> 77:52]** would never work for their solution, for their task.

**[77:52 -> 77:57]** So in 2009, so we're talking about lots of years ago,

**[77:59 -> 78:03]** Netflix defined a challenge where they asked

**[78:03 -> 78:07]** are international students, people working in AI,

**[78:07 -> 78:10]** to develop, I mean, help them to develop a model

**[78:10 -> 78:13]** that could be able to improve the suggestion

**[78:13 -> 78:17]** that they provide to their users, right?

**[78:17 -> 78:20]** when you have watched a certain amount of movies,

**[78:20 -> 78:23]** then they want to advise you to the next movie

**[78:23 -> 78:25]** to watch, right?

**[78:25 -> 78:27]** This is practically an AI problem.

**[78:27 -> 78:29]** You have Matrix completion problem.

**[78:29 -> 78:34]** You have your users, you have, I mean, the movies,

**[78:34 -> 78:36]** and then some of them like,

**[78:36 -> 78:38]** so you see that in the middle of this table,

**[78:38 -> 78:40]** there are some greener places and red places,

**[78:40 -> 78:42]** some places where the user liked the movie

**[78:42 -> 78:44]** and some other know,

**[78:44 -> 78:48]** but it's mostly empty, it's a sparse matrix, right?

**[78:48 -> 78:50]** How do we fill in the rest of the places

**[78:50 -> 78:52]** where we don't have information?

**[78:52 -> 78:56]** So this recommendation system, which is based on the model,

**[78:56 -> 78:58]** which is matrix completion,

**[78:58 -> 79:01]** they were asking people to help them to improve

**[79:01 -> 79:05]** these results, and if they were able to get something like,

**[79:05 -> 79:10]** I mean, a 10% improvement in the prediction

**[79:10 -> 79:16]** of which correct movie to propose to a user, you would have get $1 million.

**[79:17 -> 79:23]** And we were talking about lots of years ago. So you understand how much money are behind this kind of

**[79:24 -> 79:31]** tasks and how AI can make the difference now. But this kind of logic would never work for the

**[79:31 -> 79:38]** problem, right? So we cannot formalize some ETH then else close to be able to solve the task.

**[79:38 -> 79:41]** We need to change the logic.

**[79:41 -> 79:43]** So what is the changing in the logic?

**[79:43 -> 79:45]** We have the data.

**[79:45 -> 79:48]** We know what we want as the output.

**[79:48 -> 79:51]** We ask the computer to define the problem.

**[79:51 -> 79:54]** It's exactly in line with the utility function

**[79:54 -> 79:57]** that we're talking about, so acting racially.

**[79:57 -> 79:58]** I know where you start from.

**[79:58 -> 80:00]** I know where you want to get.

**[80:00 -> 80:03]** And that's, we provide this information to the computer.

**[80:03 -> 80:05]** It has to find the function.

**[80:05 -> 80:13]** function. So if x is the data and y is the output, I want to find the function f of x that produces

**[80:13 -> 80:20]** the correct y. So that brings me to the correct output. Okay, this is what we want to do. And this

**[80:20 -> 80:27]** is the logic. Now, of course, once you have this overview of the method of the framework,

**[80:27 -> 80:35]** then you start thinking about family of tasks. You can have supervised learning models, where

**[80:35 -> 80:42]** actually the data, your X, come together with a corresponding label. Okay, so you have fears

**[80:42 -> 80:48]** and your goal is just to, for instance, to classify, here is a very simple binary classification task.

**[80:49 -> 80:55]** So data plus label, supervised learning, I'm sure you know it. I'm just doing a binary classification

**[80:55 -> 81:03]** that's based on one specific feature. So it's very simple. It can become a classification on a higher

**[81:03 -> 81:09]** dimensional space when the feature becomes richer and for instance you have two descriptors.

**[81:09 -> 81:15]** It can become a much difficult problem where you have images and every single pixel is

**[81:15 -> 81:18]** a value in your X vector.

**[81:18 -> 81:23]** So the X vector is containing more features and you have to classify not only two classes

**[81:23 -> 81:27]** but maybe three, four, five depending on what's your goal.

**[81:27 -> 81:30]** So now the classification becomes multi-class.

**[81:30 -> 81:34]** You're going to have regression where the task, again,

**[81:34 -> 81:37]** you'll have a y assigned to each x.

**[81:37 -> 81:39]** But the y is not anymore a label.

**[81:39 -> 81:42]** It is a continuous value.

**[81:42 -> 81:44]** And so your goal is to predict the trend.

**[81:44 -> 81:47]** So you're predicting something like a curve,

**[81:47 -> 81:49]** not really just the label of that specific x.

**[81:49 -> 81:52]** You're predicting a continuous value, right?

**[81:52 -> 81:55]** So you have the regression task.

**[81:55 -> 81:58]** you can have unsupervised learning,

**[81:58 -> 82:02]** where the data comes without their labels.

**[82:02 -> 82:03]** And that's an interesting kind of setup

**[82:03 -> 82:06]** because then the only thing you can do

**[82:06 -> 82:08]** is to organize the data itself.

**[82:08 -> 82:13]** And then you create groups, for instance, so clustering.

**[82:13 -> 82:15]** That's another kind of setting.

**[82:15 -> 82:17]** Unsupervised learning is super helpful

**[82:17 -> 82:19]** in a lot of practical application.

**[82:19 -> 82:22]** And if you have just two, for logistics,

**[82:22 -> 82:24]** if you have to organize your own server,

**[82:24 -> 82:25]** how to put the computers.

**[82:25 -> 82:26]** That's important.

**[82:26 -> 82:28]** I mean, and you can group things,

**[82:28 -> 82:29]** you can group information.

**[82:29 -> 82:32]** You see it's applied in a lot of tasks.

**[82:32 -> 82:35]** And nowadays, which is the logic

**[82:35 -> 82:38]** of unsupervised learning is super popular.

**[82:38 -> 82:40]** Many of the approaches you use,

**[82:41 -> 82:44]** I mean, code, the GPT,

**[82:44 -> 82:47]** Dino, you will talk about Dino later on.

**[82:47 -> 82:49]** Very famous foundation model

**[82:49 -> 82:53]** are learned in a self-supervised way.

**[82:53 -> 82:54]** No labels, okay?

**[82:54 -> 82:57]** Even segment anything model, SAM model.

**[82:57 -> 82:58]** It's a very famous one.

**[82:58 -> 83:01]** It helps you to segment much better with respect

**[83:01 -> 83:04]** to your law or other methods that maybe you have heard about.

**[83:04 -> 83:09]** Well, SAM is not trained with labels, okay?

**[83:10 -> 83:12]** So it has particular label,

**[83:12 -> 83:15]** but it's partly semi-supervised.

**[83:15 -> 83:18]** So you will see what do I mean?

**[83:18 -> 83:19]** We'll go into the details of this,

**[83:19 -> 83:21]** but this is a very popular kind of approach.

**[83:21 -> 83:23]** There is reinforcement learning.

**[83:23 -> 83:27]** There is a dedicated course completely to that.

**[83:27 -> 83:29]** If you're interested in reinforcement learning,

**[83:29 -> 83:31]** robot learning and so on.

**[83:31 -> 83:36]** So this is how to train a model to adapt to a new condition.

**[83:37 -> 83:40]** And this is practically the logic used for robotics.

**[83:40 -> 83:42]** And it's practically the logic used

**[83:44 -> 83:47]** for the AlphaGo model that in 2015,

**[83:47 -> 83:52]** I think one against the champion of the goal game.

**[83:53 -> 83:57]** So yeah, the person here was quite desperate

**[83:57 -> 84:00]** when the computer system won the game,

**[84:00 -> 84:02]** it's a very complex one, but actually it can be done.

**[84:02 -> 84:04]** So you see, there's a very long list

**[84:04 -> 84:05]** of kind of learning approaches,

**[84:05 -> 84:08]** but the logic we are trying to follow

**[84:08 -> 84:11]** and the framework is exactly what it told you.

**[84:11 -> 84:15]** So we provide the data, we describe what we want

**[84:15 -> 84:19]** as an output and then we let the model find the function

**[84:19 -> 84:20]** to solve the task.

**[84:20 -> 84:23]** This is the utility function we'll try to optimize.

**[84:23 -> 84:26]** And these will guide us to define what is a loss,

**[84:26 -> 84:29]** how do I update the parameters of my model to do that,

**[84:29 -> 84:32]** what does it mean to make it more efficient,

**[84:32 -> 84:33]** and so on and so forth.

**[84:34 -> 84:35]** Who is a machine learner?

**[84:35 -> 84:38]** Well, you see the comics here.

**[84:39 -> 84:42]** This is not what I expect you to do.

**[84:42 -> 84:45]** Just tear the data and see what happens.

**[84:45 -> 84:49]** Again, we want to understand how these models are.

**[84:49 -> 84:59]** Yeah, so this is the high-level logic of a machine learning in general and what a machine

**[84:59 -> 85:01]** learner does.

**[85:01 -> 85:06]** Understand the domain, understand the prior knowledge, so which kind of knowledge can

**[85:06 -> 85:11]** be used to define the model, the goal of the task, understand the data, open the directory

**[85:11 -> 85:15]** the data, the fact that someone else provided the data is not enough.

**[85:15 -> 85:17]** You have to see them.

**[85:17 -> 85:20]** Define the model, train the model, interpret the results,

**[85:20 -> 85:22]** consolidate and restart from scratch.

**[85:22 -> 85:28]** Usually that's the procedure until you get the kind of accuracy you want for your model.

**[85:28 -> 85:36]** Okay, so I would say that for today we stop here and then we go ahead in the next section.

