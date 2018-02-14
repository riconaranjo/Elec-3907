# Reflection 1

## JeeNode

Due to various reasons – I was in Vancouver – everyone on our team missed the Monday lab section, and thus we were behind from the beginning. We did not let that deter us and on Wednesday the TAs explained to us how to solder components onto a PCB. They explained to us how it was important to heat up the board, as well the component leads so that the solder would stick to both and provide support; if this was not done properly then the solder would not create a good contact, or worse the component might fall out.

We spent a fair amount of time practicing on a an old board and using spare resistors, ensuring that all the members on the team got a turn. This is important because we need multiple people that can do every task; if we rely on only one person for each task (e.g. soldering) we may be blocked if that person is sick or drops the course. It was also important to practice because we did not want to waste time removing improperly soldering components onto the provided JeeNode. 

After we felt reasonably competent at soldering we started working on the JeeNode. We opened the provided documents that explained which components to solder where, and in which order. The order is important because larger/taller components can get in the way of smaller components so it is best to start with the ones with the lowest clearance. We again took turns soldering the components in place. Jake and I had the most experience soldering prior to this course so we soldered the processor and RF chip pins since we wanted to catch up to the other groups. The biggest challenge was holding the board down since we did not have a clamp. We used teamwork and had one person hold the board while another soldered, making sure not burn the other person's hand.

Now that we had soldered all the components, we had to test the board to make sure it worked. Peter lead the building of the circuits with the LED, LDR (Light Dependent Resistor), and resistors and I worked on getting the software working. At first we had issues getting things working, but after reading the documentation more closely, we realized the pins in Port 1 and 2 were opposite to what we had initially understood. This taught us to be more careful while connecting the pins. If the circuit had been more complex we might have spent much longer thinking the circuit was wrong and wasted time checking all the connections there.

After the initial tests getting the JeeNode to light and blink up a single LED we moved on to having the LED blink at a frequency that was dependent on how much light hit the LDR. I thought this was really interesting. At this point we wanted to move onto the last tutorial which required two JeeNodes to transmit and recieve data. While trying to find another group to do this with, we realized we were the first team to get to this stage. We assisted the teams around us since it was good practice and would get us quicker to transmitting. We spent the remainder of the period and we were able to receive the data from the other JeeNode, but our LED would not light even though we measured a voltage drop of 1.7 V. We could not figure it out.

The next period, we continued with the other team and they were able to receive the data from us, and their LED would light accordingly. After stumping the TA, I went through the other team's code and realized where we had Port.mode2(OUTPUT);, they had Port.mode(OUTPUT);. This small difference set the output of the port to an analog signal, as opposed to a digital signal, which is what an LED needs to turn on. We had gone through all the code and even wondered out loud what the difference between the two modes was, even to the TA. None of us actually bothered to check and if we had we probably would have figured out the issue much sooner. We need to be more proactive about clearing up what we don't understand because this just ensures that our understanding is shaky and will lead to unexpected behaviour in whatever we design.

We learned a lot in these first two weeks, including how to solder and code for a mircocontroller using Arduino IDE. We learned how to work together to build something, and how to solve problems as a team. I am excited to work with my team this semester.

## Meeting with Professor Manuel Baez

We met with the professor to talk about how we can work with him. He suggested we work to expand the <a href="https://carleton.ca/our-stories/story/gather-ring/">Gather-Ring</a> the he worked with students last year. We also talked about other ways of expanding it incvolving more hardware components

### LED Strip and Patterns Expansion

This project would involve mostly programming more patterns and more intricate patterns into the LED strips that are over top the beams in the Gathering Ring. They are currently a small length of the beam but the professor would like to expand these to be the full length so that they could illuminate a brighter and more complex lightshow. These patterns would be based of important dates and would show a pattern representing that day(i.e. red and white for Canada Day).

### LED Grid

This project could be much more complicated since it would require doing something new, as opposed to expanding on the existing patterns. This would include installing LEDs to go with the glass shapes hanging on the top chains, and these would be lit up to show patterns much like the LED strip. This could – with significant programming – be used to display images such as a maple leaf as well as patterns.