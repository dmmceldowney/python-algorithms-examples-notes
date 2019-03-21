from queue import Queue

def hotPotato(namelist, num): # the list of kids and the number of turns before they're removed
    # build the queue
    sim_queue = Queue()
    for name in namelist:
        sim_queue.enqueue(name)

    # play hot potato
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))