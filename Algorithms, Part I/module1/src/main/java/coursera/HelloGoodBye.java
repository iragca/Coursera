package coursera;

public class HelloGoodBye {

    public static void main(String[] args) {

        // Prints "Hello, World" in the terminal window.
        if (args.length != 2) {
            System.out.println("Please enter two names.");
            System.out.println("Usage: java HellGoodBye <name1> <name2>");
        } else {
            System.out.println("Hello, " + args[0] + " and " + args[1]);
            System.out.println("Goodbye, " + args[1] + " and " + args[0]);
        }

    }
}