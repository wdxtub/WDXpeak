# 18645 final preparation


## SIMD Short Answer

    float array[256] = {...}; // initialize with some value
    __m128 v0 = _mm_load_ps((__m128*)array);

绝大部分 SSE 指令都要求位址是 16 的倍数，如果不是的话，就会导致 exception。而浮点数只会对齐在 4 bytes 或 8 bytes 的边上(根据 compiler 设定而不同)

这题里面就不符合对齐的要求。

可以用 `_mm_loadu_ps` 来读取非 16 对齐的。
