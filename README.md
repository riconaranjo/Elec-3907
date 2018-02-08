# ELEC 3907
## Third year engineering project

This is a term long project where we work in groups of 4-6 to design and build a finished product. This allows us to use the technical knowledge from school work, coop experience, and our interests to design something from start to finish.

## Light and Art

My team and I decided to work with Professor Manuel Baez to create something that intersects technology and art. We will be working with him to expand on the <a href="https://carleton.ca/our-stories/story/gather-ring/">Gathering Ring</a> that was designed by three architecture students last year with his help.

We are designing a system that is able to track visitors to the Gather-Ring, and then use their location to create a unique pattern that updates as they move around. We hope this adds a whole new level of interactivity for the community with this existing installation. We will be using an array of ultrasonic sensors installed underneath the benches pointing inwards to track the visitors.

## Team Roles and Responsibilities

### Team Members

- Federico Naranjo
- Huzaifah Sulaiman
- Ibrahim Bishtawi
- Jake Godin
- Peter Freundorfer
- Yusuf Adam

### Responsibilities

These are the current responsibities of each team member. They will be updated as project develops.

#### Federico Naranjo [Group Leader]

- Ensuring project is on schedule and within budget
- Inter-team communication with other team working on Gather-Ring
- Software for Arduino to read from Sensors
  - Noise Reduction from sensor data
- Communication link between Arduino and Raspberry Pi
- Software that transforms Cartesian coordinates to a format that corresponds to LED strips
  - Other team's LED light strips are organized in spiral layout

#### Huzaifah Sulaiman + Yusuf Adam

- Raspberry Pi software integration
  - making sure raspberry pi runs software on launch [when power is connected]
- Software to light up LED light strips
  - Given cartesian locations, update the lights to track persons

#### Ibrahim Bishtawi + Peter Freundorfer

- Designing and building Prototype model
- Create circuit designs and design schematics
  - To help us build it and debug
  - For presentations and reports

#### Jake Godin

- Software to take averaged sensor data and coordinate location of visitors
  - Three sensor values to triangulate position
  - Most likely to be run on Raspberry PI