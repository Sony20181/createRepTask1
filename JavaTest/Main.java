//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class PrimeNumberTest {

    @Test
    void testIsPrime() {
        assertTrue(Main.isPrime(5));
        assertFalse(Main.isPrime(18));
        assertFalse(Main.isPrime(-1));
        assertFalse(Main.isPrime(1));
    }

}
public class Main {
    public static boolean isPrime(int number) {
        if (number < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}


