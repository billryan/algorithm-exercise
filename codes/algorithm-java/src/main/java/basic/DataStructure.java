package basic;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Basic data structure including queue, stack, graph...
 *
 * @author billryan
 * @date 2019-06-22
 */
@Data
@NoArgsConstructor
public class DataStructure<T> {
    private Queue<T> queue = new LinkedList<>();
    private Deque<T> stack = new ArrayDeque<>();
}
