# Reliable UDP

出处

If you are designing a reliable UDP, what should you do?

## Solution 

通常，所谓的reliable都是指接收端能够将收到的数据情况反馈给发送端。由于我们已经知道一种可靠的传输协议，TCP，故reliable UDP的设计完全可以参考TCP的设计方式，引入ACK，flow control，congestion control等模块。模块的实现可以直接模仿TCP，也可以通过和面试官的沟通进一步确定需求。Reliable UDP的核心在于反馈机制，这里给出几个可能的实现方式。

由于reliable要求在接收端能够恢复数据包的顺序，故发送端每个数据包都需要有sequence number。现在着重讨论反馈机制：

1. 最朴素的ACK方式：发送端每发送一个数据包，都需要接收端返回ACK，一旦超时，发送端重新发送数据包，直到该数据包被接收端ACK。该方法效率不高，因为之后的所有数据包都被当前数据包block，并且每次返回ACK增加了overhead。
2. Block/bit map ACK：发送端发送一批数据包，例如32个，编号0～31。接收端发回的ACK中用32bits(4bytes)的bit map表示收到了哪些数据包，发送端再一次性重发所有未被收到的数据包。该方法能够更加充分地利用带宽，在发送端一次性传输更多的数据。但缺点是在发送端接收端都需要更深的buffer，暂存正在传输的所有数据。
3. ACK last packet：发送端可以在发送最后一个数据包时要求接收端反馈ACK，并重发丢失的数据包。这样做的好处可以减少由ACK造成的data overhead，但需要通过buffer暂存数据。

事实上，可以结合方法2和方法3，在每一批数据包的最后一个置位request ACK flag，要求接收端返回bit map ACK。更进一步地，可以根据丢包率及延迟，估计网络状况，动态地调整bit map的大小：在网络状况好的情况下，用更大的bit map，即同时发送更多数据。否则，减小发送数据量。事实上，这种对于网络状况的自适应也相当于实现了congestion control。

