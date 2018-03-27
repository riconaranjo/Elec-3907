# Reflection 2

`What is 'good design' in a product?`

## Good Design

Good design – although a simple statement – is a very complex idea. Good design means that a product useful and perfoms its desired objectives. These objectives usuallly fall within these criteria: performance [being the fastest or most efficient at completing a task], accessibility, and usability.

A well designed product can be a product that performs better than any other such as a fighter jet that costs billions but cannot be shot down, or a formula-1 car that is able to break records. But these are only good designs in a given contect. A fighter jet is a poor choice for a commercial airline, and a formula-1 car would not do well in off-road scenarios. When you design a product you must take into account the context in which it wil be used. For example a well designed power-tool is only useful to someone that knows how to use it; it was designed for a professional in mind. Much like professional software is covered in options and setting which a professional will find indispensable, a regular user would be overwhelmed and find the product completely unusable. A product must be designed to accomplish its task effectively without negatively affecting the user experience.

Good design can be when an existing product is refined in order to make it more accessible. For example, <a href="https://www.theatlantic.com/science/archive/2015/09/one-dollar-origami-microscope-foldscope/403156/">Manu Prakash</a> created a microscope that costs $1, comes as a single sheet of paper, and is easily assembled. His invention, although not the best microsope, has good design because it was carefully designed to be accessible by making it easy to manufacture and distrubute, while still performing the core functionality of what a microscope should be.

Good design is when a product is designed to be robust. A product that needs to be replaced every week, may not be as well designed as a similar product that lasts 10 years. This is particularly prevelant in fields such as the military, emergency response, or simply when part failure has significant consequences. The product may be robust because no parts will breakdown for a long period, but also can mean that any broken parts in the product can be replaced, for example tank threads.

Good design also takes into account both time and money costs. Spending billions and decades to develop a product may create the best pen of all time, but this may mean that the product is now obsolete, or that the cost to research and/or manufacture the components is so high that there is no way that enough units will be sold to recoup the costs. Certain companies will develop technolgies that will not immediately recoup their development costs because they know that they can improve on this technolgy and make it mass-market. An example of this is the techology used by car companies in their Formula-1 vehicles. These cars costs millions to develop and produce, and they are not  for commercial sale. Instead the technolgy used to make these cars go faster, operate longer, and run more efficiently is refined and improved on, and eventually is seen in the mass-market cars.

Good design is not a clearly defined idea, but instead is a measure of how well a product is created such that it fulfills its requirements including (but not limited to) performance, usablility, robustness, and economics.

## Miscommunication

When we initially met with professor Manuel Báez, he gave some ideas about what he initially wanted the Gather-Ring to look like. He wanted LED strips to be added the crossbeams with more patterns, so that on certain days they would like up in recognition of some event or holiday. We told him we had the idea to install LED lights across the chains spanning over the centre of the ring, and then create patterns on that. Unfortunately when he met with another group, he mistakenly told them that they should work on LEDs across the chains. Next time we should have been more clear on what we were planning on doing because we made it sound like we were undecided. If we had sent him an email with a clear outline of our plans this may have been avoided.

During the project proposal presentations, we found out that the other group was attempting what we had set out to do. I brought this up with team and we had a long discussion about whether we wanted to compete against them, or pivot and find a way to work together. If we competed, we would have the possibility of having or project proposal rejected and have to pivot anyways, and we decided it would be more interesting to work together, and create an even better project. If we create a worthy project, we would then be able to propose it to the city and it would be installed on the art installation.

This outcome although is not what we had intended, seems to be a better result since we took a more challenging project, which also interests the team more. This means we are able to push ourselves to learn more, so that we can have a successful project, while enjoying the process more. It is always easier to finish a team project if the team is motivated.

## Pivoting

Initially, we wanted to install the LED lights and then if we have time add sensors to track the visitors to the Gather-Ring. Now that the other group was working on LED lights we decided to implement the tracking system. We first considered using infrared sensors. These sensors are very accurate at tracking object and their distances, but require a lot of processing power, and complicated software. The other option we considered was ultrasonic sensors. These are much cheaper and integrate with the Arduino we were already planning on using with the LED lights.

Considering these two options, we had to deside how accurate the tracking should be. The IR sensors would be able to track multiple users with very high resolution, but at a higher price and more challenging integration. The ultrasound sensors could be arranged together side-by-side to triangulate the location of one user, but being much cheaper and easier to integrate. Since we did not need very high tracking resolution, our skill level, and our limited budget we decided it would be best to use an array of ultrasonic sensors.

Having the team work together to come up with our own idea has helped us, because the team members are more motivated to work on a project they see as their own. It was important to let everyone in the team contribute; if I had lead the conversation and only allowed my ideas to be discussed then we would undoubtably be worse of. Nelson Mandela once said that leaders should always speak last, that way everyone's ideas would be heard.

## Presentation

Now that we had an idea of the final project, we were motivated and excited at what our final project would look like. We put our order in for parts, and we prepared for the project propsal presentation.

We had to present to our peers what we intended to do, and explain how it was different from the other group working on the same project. We had to explain why it was significant, why we were devoting our time to improve some benches with lights, and convey that we had a plan on how to accomplish our goal.

Every member of my team does not like presenting, including myself. This presented a challenge, to motivate my team members to present when even myself I did not want to present. Presenting skills are very important in any field, particularly engineering because you have to be able to communicate your work to others. In order to motivate those on my team to present I decided to lead by example: I said I would present and asked who would join me. Peter and Jake volunteered reluctantly and we created a rough outline for the presentation using Google Slides.

We store all our files on Google Drive, a cloud storage service, so that the entire team can work on the same files and no have to worry about some team members having older versions or losing files because someone's computer died. This has allowed us to work on the same files from home or at school, or in the case with the presentation slides, at the same time from different locations.

We practiced for the presentation a few days before by meeting up after class and going through the slides. We talked about what we wanted to say with the slides, what information we should add or remove, and practiced our lines. Practice is important for any presentation, because how you present to an audience will decide how much they will understand and what they will remember.

The presentation went well, especially considering it had been 1-2 years since we last presented. In hindsight I spoke too fast, which I will work on by practicing my lines out loud. My team members, Peter and Jake did very well explaining the overall design considertions and how we planned on tracking the visitors.

## Collaboration

Throughout the last two weeks, both our team and the other team working on the Gather-Ring have been trying to arrange a meeting with the professor, but it was challenging with everyone's busy schedules. We finally managed to meet up with the professor and he was very excited with what we we planning. This was also the first time both teams talked about how we would work together.

Talking to the other team raised some key points we had not considered; they told us that they only had one controller for the lights and that would make it difficult to convert the x,y coordinates to a location along one of their LED light strips. Since we are using both a microcontroller for the sensors and a Raspberry Pi for the computation, we can do this conversion more easily than they could. We also opened up a channel of communication so we collaborate more closely. This is important if we are to integrate both projects rather than create two independent projects.

## Getting Stuff Done

In the preceeding week after the design pivot, we had no direction. We knew what we wanted, but had no idea how to actually get there. We had order few parts, simply to make sure that the ulrasound sensors could detect an object's location. I knew as group leader it was my responsibility to organize my team, and ensure the project was completed on time.

The biggest challenge I have always faced when leading people to accomplish something, is motivating them to actually care about the project. It can be hard to see what the benefit of putting effort into something is. I motivate my team by reminding them how cool it would be to see our project realized and actually installed on te Gather-Ring; I also remind them that this is practice for our fourth year project. The next biggest challenge is organizing tasks so that eveyone knows what their tasks are. If you assign tasks that are too generic [software, hardware]then the group members don't know how to proceed. I saw this initially in my team when we assigned 4 members to software and 2 members to hardware. The remedy to this is assign small tasks that are immediately actionable and simple; this allows the team to move forward and focus on one small component at a time.

I wrote up a document describing the current roles and responsibilities. It describes what everyone should be working on, such as writing software that triangulates visitors from sensor data. This ensures everyone is aware of what they are responsible for, and gets them thinking about what parts they need during the work sessions. I have also set a tentative deadline for a working prototype that as a team we all agreed on. This gives a sense of urgency and will allow us to react if something fatally wrong is discovered in the design. I then sent this to the group chat and asked if everyone agreed with it, or had any questions.