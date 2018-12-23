## Using LD_PRELOAD to get flag

### Compile
以下のコマンドを実行する.
```bash
make
```

### challenge.c
`challenge.c` は, `rand()` の戻り値を `key` として設定する. 標準入力に `key` と同じ値を入力すると, flagが出力される.


`challenge.c` をコンパイルした `challenge` でどのようにプログラムが実行されているかを以下のようなコマンドで調べると, 



### challenge
#### ltrace
`challenge.c` をコンパイルした `challenge` に対して, 以下のコマンドで実行時のライブラリ呼び出しのトレースを取得する.

```bash
ltrace ./challenge
```

```txt
time(0)                                                                                                                        = 1545575934
srand(0x5c1f9dfe, 0x7ffc789bfdd8, 0x7ffc789bfde8, 0x564b3ccea8a0)                                                              = 0
rand(0x7f295a6e81d0, 0x7f295a6e8740, 0x7f295a6e81c4, 0x7f295a6e81d0)                                                           = 0x336aabdb
printf("Input Password > ")                                                                                                    = 17
__isoc99_scanf(0x564b3ccea936, 0x7ffc789bfce0, 0, 0Input Password > dead
)                                                                           = 0
printf("Wrong, Key is %d\n", 862628827Wrong, Key is 862628827
)                                                                                        = 24
+++ exited (status 0) +++
```

以上の出力より, `time(0)` を呼び出して, その戻り値を引数として `srand()` を実行している.
`srand` の引数を同じにできれば, `key` の値は同じになる.

#### ldd
以下のコマンドで, `challenge` が使う共有ライブラリを調べる.

```bash
ldd ./challenge
```
```txt
	linux-vdso.so.1 (0x00007ffe8dfe4000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fc0307ea000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fc030ddd000)
```


### time.c
glibcの `time_t time (time_t *t)` を真似て実際の時間+3[sec]の時間を返す関数を実装.

### libtime.so
`time.c` から作った共有ライブラリ.

### solve.py
`challenge` から flag を取得するために, `LD_PRELOAD` を使って `time()` 関数を取り替えたものを実行して, 3秒後の `key` を取得し, それを利用してflagを取得するスクリプト.


### Reference
https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/
https://qiita.com/koara-local/items/d5205f94decade3ffbf1
http://matsu911.github.io/Testing/2012/02/27/testing-with-ld_preload/
https://siguniang.wordpress.com/2015/05/15/override-functions-with-ld_preload/