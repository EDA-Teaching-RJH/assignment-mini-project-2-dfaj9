# Reflection:

In this project, i managed to create a python login system in which clients can sign up to the app then their details will be saved into a text file, in which the validation process starts for when they want to log in.

The first requirement that i managed to do was implement object-oriented programming to my program by creating a User class and a Client class, in which the Client class inherits from the User class. This is called inheritance and is useful because it allows me to reuse the same code, which helped keep my coding clean and tidy making it much easier to mantain.

The second requirement that i managed to implement was regular expressins to my program, which was used to validate emails and passwords. For example, in my code the email validation governs the fact that only emails that end with ac.uk are passed through and for passwords it makes sures that the length of the password is 12 characters long, contains uppercase, lowercase, special characters and numbers. Overall, this makes sure that user input mistakes are prevented and that security of their account is secure by encouraging them to have strong passwords. 

The third requirement that i managed to implement was file I/O, which was done to store user details in a text file in the registration process, in which they can easily retrieve for when they just log in. This was an efficient way of allowing user detail to be managed.

The last requirement was testing, in which i managed to do in my program using pytest. All my validation functions were tested and contained both valid and invalid scenarios in order to make sure that my code is performing correctly. This is very useful because it helps by spotting errors, which can help me get rid of them before publishing. 

Libraries was implemented in my program, with the built in library "re", which helped with implementing regular expressions for the validation of email addresses and passwords that users entered. This is useful beccause it has very high pattern matching and is very efficient.

During my programming process, i faced an obstacle in which i was stuck on for days and this was that originally made an infinite loop by calling the sign up function inside itself and also the login function inside itself, at first i did not see an issue with this until i removed them and used only the main loop, which resolved my issue. However, overall i managed to create a very good python login app, which can easily be expanded on to be a great high security app.

