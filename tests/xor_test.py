import cocotb
from cocotb.triggers import Timer, RisingEdge


@cocotb.test()
async def xor_test(xor_gate):
    
    a = (0, 0, 1, 1);
    b = (0, 1, 0, 1);
    y = (0, 1, 1, 0);
    
    for i in range(4):
       xor_gate.a.value = a[i]
       xor_gate.b.value = b[i]
       await Timer(1, 'ns')
       assert xor_gate.y.value == y[i], f"Error at iteration"
