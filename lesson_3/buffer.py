'''Alyssa was asked to write an implementation of a rolling buffer.
You can add and remove elements from a rolling buffer.
However, once the buffer becomes full, any new
elements will displace the oldest elements in the buffer.
She wrote two implementations of the code for adding
elements to the buffer: Is there a difference between
these implementations, other than the way she is
adding an element to the buffer?'''
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    print(buffer)
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    print(buffer)
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

print(add_to_rolling_buffer1([1, 2, 3, 4], 4, 'frog'))
print(add_to_rolling_buffer2([1, 2, 3, 4], 4, 'frog'))

print(add_to_rolling_buffer1([1, 2, 3, 4], 2, ['f', 'fi']))
print(add_to_rolling_buffer2([1, 2, 3, 4], 2, ['f', 'fi']))

print(add_to_rolling_buffer1([1, 2, 3, 4], 3, ['f', 'fi']))
print(add_to_rolling_buffer1([1, 2, 3, 4], 3, ['f', 'fi']))

'''yes there is a diference: 
with append we just add the element to the end of the original list
vs with + we create a new list and concatenate the 2 elements 
important difference between them bc one(+) modifies original buffer 
and you might want to keep original buffer '''
