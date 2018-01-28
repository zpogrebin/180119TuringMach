UTM Program:
______________________
|Turing Machine Format\___________________________
>Ln  Description     Example
 L1: Initial State : q1
 L2: Declare Break : #
 L3: Init tape w/  : 0
 L4: State inst fn : q1,0,q1,#,R 
 L5: State inst fn : same
 L6: State inst fn : same
 Ln: State inst fn : same
_______________
|inst fn format\__________________________________
 
>State inst function format
 q[state number],[digit on tape],q[go to state],[digit to write],[move direction]
        1               2              3              4               5
 
>Allowed inputs
 1, 3: any integer
 2, 4: 1, 0, or the character declared in line 2
 5.  : L, R, or any other character to indicate a halt

>Handling of inproper inputs
 1, 3: the program will fail
 2, 4: Will convert to the character declared in line 2
 5.  : Will not move the tape
