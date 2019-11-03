package basic;

import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * @author billryan
 * @date 10/8/2019 12:04
 */
public class StackTest {

    private static final Logger log = LoggerFactory.getLogger(StackTest.class);

    @Test
    public void testStack() {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        int peek = 3;
        while (!stack.isEmpty()) {
            int stackPeek = stack.pop();
            log.info("stack peek: {}", stackPeek);
            assert peek == stackPeek;
            peek--;
        }
    }
}
