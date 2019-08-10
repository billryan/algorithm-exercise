package basic;

import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.LinkedList;
import java.util.Queue;

/**
 * @author billryan
 * @date 10/8/2019 12:05
 */
public class QueueTest {

    private static final Logger log = LoggerFactory.getLogger(QueueTest.class);

    @Test
    public void testQueue() {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);

        int peek = 1;
        while (!queue.isEmpty()) {
            int queuePeek = queue.poll();
            log.info("queue peek: {}", queuePeek);
            assert peek == queuePeek;
            peek++;
        }
    }
}
