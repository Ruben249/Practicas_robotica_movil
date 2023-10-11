# Mobile_Robotics_Practices

##Index

-[Start](#start)

-[Development](#development)
### Practice 2
#### Start
At the beginning I was testing how to use the commands provided in the robot API.
Thanks to the advice provided by the teachers, we discovered that we should start by obtaining the image of the robot, converting all the reds to a single red, while the rest of the colors should be converted to black. In the following image we see an example of obtaining the photo.

Then I decided to add a small blue dot in the middle of what the robot saw. To do this I simply had to divide the width and length of the image by 2. 
#### Development
I continued developing the code, and managed to make it move randomly a few times, but I ran into the problem that it got stuck in the corner, as seen in this photo ![Foto 2](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/f8d04b4a-32e3-41e9-8d9b-d2ca34269ef1)
I perfected it a little, making it turn more to one side than the other and making it so that if it collided in the center it would turn randomly to one side or the other, as seen in this photo ![Foto 3](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/ee905959-6861-40f6-9f34-05bb06b9a556)
In the next photo we see how the robot has greater self-sufficiency to get out of small holes and places where it was previously trapped
![Foto 4](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/0730b7de-f180-458c-863a-4523695ecb29)
Finally, I thought that in order to get out of corners, the robot would have to make random turns, so I decided that every time it turned it would do it differently, and this is the result: 
![Foto 5](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/e7d6d708-e3a8-446f-94de-f01458674561)

Here is a sped-up X3 video where we briefly see how the robot behaves.
https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/ba953b52-4f57-4145-97a5-65e79850400a
