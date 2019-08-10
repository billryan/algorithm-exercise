package basic;

import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Deque;

/**
 * @author billryan
 * @date 10/8/2019 10:59
 */
public class DataStructureTest {

    private static final Logger log = LoggerFactory.getLogger(DataStructureTest.class);

    @Test
    public void testStack() {
        DataStructure<Integer> ds = new DataStructure<>();
        Deque<Integer> stack = ds.getStack();
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
