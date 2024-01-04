writeln("Hello World!").

parent(tom, john).
parent(john, tim).
parent(mary, tim).
male(john).
male(tom).
male(tim).
female(mary).

father(X, Y) :- parent(X, Y), male(X).


